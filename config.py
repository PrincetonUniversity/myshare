# number of characters for output
WIDTH = 80

# number of digits of precision to show
FAIRSHARE_DIGITS = 3

USAGE_DIGITS = 0
SHARES_DIGITS = 0
SHARES_PREC = 0

# if this path is found for a given node then ignore root
# otherwise level 1 of the tree is considered where slurm does the most important stuff
# this is needed for computing department shares against a total
# if this path is found then ignore root and start at end of path
# is a pattern needed to differentiate different clusters?
# Use --skip=total,pli,ailab to override these config.py settings
# Use --skip="" to not skip any accounts
#SKIP_ROOT_ACCOUNTS = ("total", "pli", "ailab-c", "ailab-p")
#SKIP_ROOT_ACCOUNTS = ("total",)
SKIP_ROOT_ACCOUNTS = ()

# if set then will be displayed at bottom of verbose output
MORE_INFO_URL = "https://researchcomputing.princeton.edu/support/knowledge-base/job-priority"

# specify the factors instead of using auto-detect (options are ...)
FACTORS = ("SITE", "AGE", "FAIRSHARE", "JOBSIZE", "QOS")

# remove root user from tree if it has zero usage
REMOVE_ROOT_USER = False

# list of cluster names to ignore
IGNORE_CLUSTERS = ()

SHOW_ZERO_USAGE = False

# show or ignore the weights paragraph
JOB_PRIORITY_POST_AMBLE = True
