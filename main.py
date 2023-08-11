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

# src_folders, src_files = [], []
# dst_folders, dst_files = [], []

def write_args_to_file():
    with open('args_file.txt', 'w') as log_file:
        log_file.write(src_path)
        log_file.write("\n")
        log_file.write(dst_path)
        log_file.write("\n")
        log_file.write(log_path)
        log_file.write("\n")
        log_file.write(str(sync_time))


def sync_files(src_folder, dst_folder):
    if not Path.exists(dst_folder):
        Path.mkdir(dst_folder)

    for dirpath, dirnames , files in os.walk(src_folder):
        print(dirpath)
        relative_path = Path(dirpath) / src_folder
        print(relative_path)
        replica_root = Path(dst_folder) / relative_path
        print(replica_root)

        for file in files:
            source_file_path = Path(dirpath)/ file
            replica_file_path = Path(replica_root)/ file
            

def synchronize_folders(source_folder, replica_folder):
    # Create replica folder if it doesn't exist
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)

    for root, _, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        replica_root = os.path.join(replica_folder, relative_path)

        for file in files:
            source_file_path = os.path.join(root, file)
            replica_file_path = os.path.join(replica_root, file)

            if not os.path.exists(replica_file_path) or \
               os.path.getmtime(source_file_path) > os.path.getmtime(replica_file_path):
                # Copy the file from source to replica if it's missing or updated
                shutil.copy2(source_file_path, replica_file_path)
                print(f"Copied: {source_file_path} -> {replica_file_path}")

if __name__ == "__main__":

    # sync_files()
    # walk_src_dir(src_path)
    # walk_dst_dir(dst_path)
    # sync_files(src_path, dst_path)
    synchronize_folders(src_path, dst_path)
    # print(f'src: {src_folders}, {src_files}')
    # print(f'dst: {dst_folders}, {dst_files}')