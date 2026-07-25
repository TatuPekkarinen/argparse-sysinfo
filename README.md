# coremon-sysinfo

Command-line system information, built on [psutil](https://github.com/giampaolo/psutil). CPU cores for now; memory and disk planned.

## Install

```
git clone https://github.com/TatuPekkarinen/coremon-sysinfo
cd coremon-sysinfo
pip install -e .
```

## Usage

```
coremon core      # core counts and per-core usage
coremon version   # version info
coremon --help    # available commands
```

```
$ coremon core
Logical / [16 Threads]
Physical / [8 Cores]
Core 0: 40.0%
Core 1: 23.1%
Core 2: 0.0%
...
```

## Requirements

Python 3.10+ and `psutil`.
