import argparse
import shutil
import os
from pathlib import Path
parser = argparse.ArgumentParser()

parser.add_argument('-s', '--src', help='Path to source folder', required=True)
parser.add_argument(
    '-d', '--dst', help='Path to replica folder', required=True)
parser.add_argument('-l', '--log', help='Path to log file', required=True)
parser.add_argument('-t', '--sync_time', type=int,
                    help='Interval of time for synchronization (sec)', default=10000, required=True)

args = parser.parse_args()

src_path = Path(args.src)
dst_path = Path(args.dst)
log_path = args.log
sync_time = args.sync_time


def sync_files(src_folder, dst_folder, log_path):
    # checks if log file exists, if not it creates it
    if not Path('log_file.txt').exists():
        Path(log_path).touch('log_file.txt')
        print("Log file was created")
        with open("log_file.txt", 'a') as log_file:
            log_file.write("Log file was created\n")

    # checks if replica folder exists, if not it creates it
    if not Path.exists(dst_folder):
        Path.mkdir(dst_folder)
        print("Folder replica was created")
        with open("log_file.txt", 'a') as log_file:
            log_file.write("Folder replica was created\n")

    for src_file in src_folder.glob("*"):
        relative_path = src_file.relative_to(src_folder)
        dst_file = dst_folder / relative_path
        match dst_file.exists():
            case True:
                if src_file.stat().st_mtime > dst_file.stat().st_mtime:
                    shutil.copy2(src_file, dst_file)
                    print(f"{dst_file.name} was modified")
                    with open("log_file.txt", 'a') as log_file:
                        log_file.write(f"{dst_file.name} was modified\n")
                continue
            case False:
                shutil.copy2(src_file, dst_file)
                print(f"{dst_file.name} was copied")
                with open("log_file.txt", 'a') as log_file:
                    log_file.write(f"{dst_file.name} was copied\n")
                continue
            case _:
                pass

    for dst_file in dst_folder.glob('*'):
        if dst_file.is_file():
            re_path = dst_file.relative_to(dst_folder)
        for dirpath, dirname, files in os.walk(src_folder):
            if str(re_path) not in files:
                Path(dst_folder).joinpath(re_path).unlink(re_path)
                print(f"{re_path} was deleted")
                with open("log_file.txt", 'a') as log_file:
                    log_file.write(f"{re_path} was deleted\n")


if __name__ == "__main__":
    sync_files(src_path, dst_path, log_path)
