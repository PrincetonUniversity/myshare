#!/scratch/jdh4/envs/tree-env/bin/python3

"""Leading spaces in each line of the output of sshare are used to determine
   the level of the tree.

   Note that andlinger has users at level 5 in the tree.

   from sharetree import ShareTree
   mytree = ShareTree(); mytree.get_raw_data(); mytree.parse()
"""


import os
import sys
import argparse
import textwrap
import config as c
from sharetree import ShareTree
from sharetree import ShareTreeError
from single_job import SingleJobBreakdown
try:
    from blessed import Terminal
    blessed_is_available = True
except ModuleNotFoundError:
    blessed_is_available = False


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Explain to users what resources they should expect")
    parser.add_argument("-u", "--user", type=str, default=os.environ.get("USER"), help="Username of the user")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show more details")
    parser.add_argument("-A", "--account", type=str, default=None, help="Show usage of all users under an account")
    parser.add_argument("-g", "--group-by-account", action="store_true", help="Group by account (modifies the -A option)")
    parser.add_argument("-s", "--shares", action="store_true", help="Show accounts sorted by shares")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug info")
    args = parser.parse_args()
    if args.group_by_account and args.account is None:
        print("The -g flag can only be used when -A <account> is specified.")
        sys.exit(1)

    term = Terminal()
    mytree = ShareTree()
    mytree.get_raw_data()
    try:
        mytree.parse(args.user)
    except ShareTreeError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    if args.debug:
        print(mytree.analyze())
    if mytree.num_accounts == 0:
        print(f"INFO: User {args.user!r} not found in the sshare tree.")
        if args.account is None:
            sys.exit(1)

    print("─" * c.WIDTH)
    print("What is My Share of the Cluster?".center(c.WIDTH))
    print("─" * c.WIDTH)


    ###################
    ## A C C O U N T ##
    ###################
    if args.account:
        if args.verbose:
            print("INFO: The -v flag has no effect on -A <account>.")
        node_id = f"{args.account} (--)"
        if node_id in mytree.tree:
            #mytree.draw_subtree(node_id, ["root (--)"], args.account)
            table = mytree.get_descendants_table(node_id=node_id,
                                                 decimals=1,
                                                 sort_by="Usage",
                                                 user_to_color=args.user,
                                                 group_by_account=args.group_by_account,
                                                 args_account=args.account,
                                                 output_width=c.WIDTH)
            mytree.print_account_table(table, args.account, args.group_by_account)
        else:
            valid_accounts = mytree.get_valid_accounts(c.SKIP_ROOT_ACCOUNTS)
            msg = mytree.invalid_account_message(args.account,
                                                 valid_accounts,
                                                 group_by_account=args.group_by_account,
                                                 output_width=c.WIDTH)
            print(msg)
            sys.exit(1)
        sys.exit(0)


    #################
    ## S H A R E S ##
    #################
    if args.shares:
        for path in mytree.root_to_user_paths:
            if args.verbose:
                print("INFO: The -v flag has no effect on -s or --shares.")
            down = "\u2193"
            print(f"\nThe table below ({down}) shows the accounts sorted by Shares:\n")
            node_id_top_level = mytree.get_top_level_node_id(path, c.SKIP_ROOT_ACCOUNTS)
            accounts_to_color = tuple([p.split()[0] for p in path[:-1]])
            fields_shares = ("Account", "Shares", "ActiveUsers")
            # TODO does not work for PLI since mix of accounts and users
            print(mytree.get_descendants_table(node_id=node_id_top_level,
                                               decimals=1,
                                               sort_by="RawShares",
                                               accounts_to_color=accounts_to_color,
                                               output_width=c.WIDTH,
                                               fields=fields_shares))
        sys.exit(0)


    #############
    ## U S E R ##
    #############
    num_accounts_shown = 0
    for path in mytree.root_to_user_paths:
        node_id = path[-1]
        node_id_top_level = mytree.get_top_level_node_id(path, c.SKIP_ROOT_ACCOUNTS)
        mytree.draw_subtree(node_id_top_level, path, args.user)
        fs = mytree.tree[node_id].data.fair_share
        print(mytree.format_fairshare_line(fs))
        print("")
        print(mytree.explain(fs))
        top_level_shares = mytree.get_top_level_shares(node_id_top_level, path)
        print(f"Top-level shares: {top_level_shares}")
        print("")

        if not args.verbose:
            print("The table below shows the accounts sorted by LevelFS which is normalized")
            print("Shares divided by normalized Usage:\n")
            accounts_to_color = tuple([p.split()[0] for p in path[:-1]])
            fields_acc = ("Account", "Shares", "Usage", "LevelFS", "ActiveUsers")
            print(mytree.get_descendants_table(node_id=node_id_top_level,
                                               decimals=1,
                                               sort_by="LevelFS",
                                               user_to_color=args.user,
                                               accounts_to_color=accounts_to_color,
                                               output_width=c.WIDTH,
                                               fields=fields_acc))
        if args.verbose:
            for sr_account in c.SKIP_ROOT_ACCOUNTS:
                nid = f"{sr_account} (--)"
                if nid in path and mytree.tree.root in path:
                    path.remove(mytree.tree.root)
            accounts_to_color = tuple([p.split()[0] for p in path[:-1]])
            print("\nThe tables below show the accounts sorted by LevelFS which is normalized")
            print("Shares divided by normalized Usage. Slurm sorts accounts by LevelFS when")
            print("determining the fairshare values of the individual users. Higher")
            print("LevelFS is better for job priority.\n")
            for i, nid in enumerate(path[:-1]):
                level2 = f"{term.bold}{nid.split()[0]}{term.normal}"
                print(level2)
                print(mytree.get_descendants_table(node_id=nid,
                                                   decimals=1,
                                                   tabbing=i,
                                                   vertical_line=True,
                                                   accounts_to_color=accounts_to_color,
                                                   output_width=c.WIDTH,
                                                   user_to_color=args.user), end="")
                if i < len(path) - 2:
                    print(f"{' ' * 5 * (i - 0)}│")
                    print(f"{' ' * 5 * (i - 0)}└────", end="")
            print("\n")
            s = ("Accounts with LevelFS > 1 have been under-served by Slurm. User within "
                 "those accounts will receive a priority boost. Similarly, accounts with "
                 "LevelFS < 1 will receive a priority penalty since they have been over-served. "
                 "When all accounts are running the shares breakdown will "
                 "reflect where the resources are allocated. The shares column "
                 "reflects the limiting distribution or what to expect over long times. "
                 "The good news for users in a department with 1 share or a small number of "
                 "shares is that the contributing departments often run fewer jobs "
                 "for periods of time. Then the effective shares increases for everyone else.\n")
            print(textwrap.fill(s, width=c.WIDTH))
            print("More important than shares is your LevelFS Rank at level 2\n")
            j = SingleJobBreakdown(args.user, fs)
            j.get_job_data()
            j.parse()
            #if j.job_dict:
                #print(j.job_dict)
                #j.explain()
            j.explain()

        num_accounts_shown += 1
        if mytree.num_accounts > 1 and num_accounts_shown < mytree.num_accounts:
            print("\n\n")
            print("─" * c.WIDTH)
            next_acc = "  N E X T    A C C O U N T  ".center(c.WIDTH, "─")
            print(next_acc)
            print("─" * c.WIDTH)

    if not args.verbose:
        print("─" * c.WIDTH)
        print("For more details about your cluster share, run the following command:")
        print()
        print("    $ myshare -v | less")
    if args.verbose:
        print("\nFor more information about job priority, making a financial contribution\nto the cluster, additional GPUs at Princeton:")
        print(f"    {c.MORE_INFO_URL}")
        print("\nTo see the users with the highest Usage, run this command:\n\n    $ myshare -A <account>")
        print("\nTo see the groups with the highest Usage, run this command:\n\n    $ myshare -A <account> -g")
