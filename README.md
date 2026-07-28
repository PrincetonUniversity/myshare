# myshare

`myshare` wraps Slurm `sshare` to explain queue times to users in plain language.

## Requirements

- Python 3.7+
- treelib 1.7.1+
- blessed (optional)

Note: Do not use treelib 1.7.0 or you will encounter errors when trees are displayed.

## Installation

```
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip3 install treelib blessed
(.venv) $ git clone https://github.com/PrincetonUniversity/myshare
```

## Usage

```
$ myshare                  # quick explanation of your queue times
$ myshare -u <user>        # same as above but for a specific user
$ myshare -v               # full explanation
$ myshare -A <account>     # show top users under account
$ myshare -A <account> -g  # same as above but grouped by sub-account
```
