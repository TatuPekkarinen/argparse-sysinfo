#internal
import argparse
from parameters import ParamInfo

#external
import psutil

def byte_to_gig(n):
    return n / 1024 ** 3

def main():
    parser = argparse.ArgumentParser(prog="coremon")
    sub = parser.add_subparsers(dest="subarg", required=True)

    sub.add_parser("core")
    sub.add_parser("mem")
    sub.add_parser("version")

    args = parser.parse_args()
    match args.subarg:
        case "core": 
            print(f"Logical: [{psutil.cpu_count()} Threads]")
            print(f"Physical: [{psutil.cpu_count(logical=False) or '(Unknown)'} Cores]")
            for core_num, percentage in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
                print(f"Core {core_num}: {percentage}%")
            frequency = psutil.cpu_freq(percpu=False)
            freq_current = frequency.current
            print(f"Current Frequency: {freq_current} MHz")
        case "mem":
            memory = psutil.virtual_memory()
            print(f"Total memory: {int(byte_to_gig(memory.total)):2f} GB")
            print(f"Used: {int(byte_to_gig(memory.available)):2f} GB")
        case "version":
            print(f"Current version: ({ParamInfo.version})")
        case _:
            parser.print_help()

if __name__ == '__main__':
    main()