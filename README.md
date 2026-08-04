# argparse-sysinfo

Command-line system information, built on [psutil](https://github.com/giampaolo/psutil) as a test of argparse library. Easily expandable.

## Install

```
git clone https://github.com/TatuPekkarinen/argparse-sysinfo
cd argparse-sysinfo
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
Current Frequency: 4700.0 MHz
```

```
$ coremon mem
Total memory: 31.000000 GB
Used: 16.000000 GB
```

## Requirements

Python 3.10+ and `psutil`.
