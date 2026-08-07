#internal
import argparse
import subprocess
import os

#external
import psutil

#local
from parameters import ParamInfo

def byte_to_gig(byte):
    return byte / 1024 ** 3

def main():
    parser = argparse.ArgumentParser(prog="coremon")
    sub = parser.add_subparsers(dest="subarg", required=True)

    sub.add_parser("core")
    sub.add_parser("mem")
    sub.add_parser("cwd")
    sub.add_parser("version")

    args = parser.parse_args()
    match args.subarg:
        case "core": 
            cpuinf_path = os.path.join(os.path.dirname(__file__), "exec", "cpuinf.exe")
            subprocess.run([cpuinf_path], shell=True)
            for core_num, percentage in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
                print(f"Core {core_num}: {percentage}%")
            frequency = psutil.cpu_freq(percpu=False)
            print(f"Estimate frequency: {frequency.current} MHz")
        case "mem":
            memory = psutil.virtual_memory()
            print(f"Total memory: {byte_to_gig(memory.total):2f} GiB")
            print(f"Memory used: {byte_to_gig(memory.used):2f} GiB")
        case "version":
            print(f"Current version: ({ParamInfo.version})")
        case _:
            parser.print_help()

if __name__ == '__main__':
    main()