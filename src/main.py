#internal
import argparse
from parameters import ParamInfo

#external
import psutil

def main():
    parser = argparse.ArgumentParser(prog="coremon")
    sub = parser.add_subparsers(dest="subarg", required=True)
    sub.add_parser("core")
    sub.add_parser("version")

    args = parser.parse_args()

    match args.subarg:
        case "core": 
            print(f"Logical / [{psutil.cpu_count()} Threads]")
            print(f"Physical / [{psutil.cpu_count(logical=False) or '(Unknown)'} Cores]")
            for core_num, percentage in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
                print(f"Core {core_num}: {percentage}%")
        case "version":
            print(f"Coremon / Current version ({ParamInfo.version})")
        case _:
            parser.print_help()

if __name__ == '__main__':
    main()