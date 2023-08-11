import argparse, shutil, os
from pathlib import Path
parser = argparse.ArgumentParser()

parser.add_argument('-s','--src', help='Path to source folder', required=True)
parser.add_argument('-d','--dst', help='Path to replica folder',required=True)
parser.add_argument('-l','--log', help='Path to log file',required=True)
parser.add_argument('-t','--sync_time', type=int, help='Interval of time for synchronization (sec)', default=10000,required=True)

args = parser.parse_args()

src_path = Path(args.src)
dst_path = Path(args.dst)
log_path = args.log
sync_time = args.sync_time

def sync_files(src_folder, dst_folder, log_path):
    #checks if replica folder exists, if not it creates it
    if not Path.exists(dst_folder):
        Path.mkdir(dst_folder)
    if not Path('log_file.txt').exists():
        Path.touch('log_file.txt')
    for dirpath, dirname, files in os.walk(src_folder):
        for file in files:
            if file not in dst_folder.iterdir():
                shutil.copy2(Path(dirpath) / file ,dst_folder)
                print(f"{file} was copied")
                # Path("log_file.txt").write_text("\n".join(f"{file} was copied"), encoding="utf-8")
                with open("log_file.txt",'a') as log_file:
                    log_file.write(f"{file} was copied\n")


if __name__ == "__main__":
    sync_files(src_path, dst_path, log_path)