import argparse, shutil, pathlib, os

parser = argparse.ArgumentParser()

parser.add_argument('-s','--src', help='Path to source folder', required=True)
parser.add_argument('-d','--dst', help='Path to replica folder',required=True)
parser.add_argument('-l','--log', help='Path to log file',required=True)
parser.add_argument('-t','--sync_time', type=int, help='Interval of time for synchronization (sec)', default=10000,required=True)

args = parser.parse_args()

src_path = args.src
dst_path = args.dst
log_path = args.log
sync_time = args.sync_time

src_folders, src_files = [], []
dst_folders, dst_files = [], []

def write_args_to_file():
    with open('args_file.txt', 'w') as log_file:
        log_file.write(src_path)
        log_file.write("\n")
        log_file.write(dst_path)
        log_file.write("\n")
        log_file.write(log_path)
        log_file.write("\n")
        log_file.write(str(sync_time))

def sync_src_to_dst(dir1, dir2):
    """
    Function which deletes replica folder and copies 
    source folder completely
    di1 is source folder, dir2 is replica folder
    """
    try:
        shutil.copytree(dir1, dir2)
        print("Replica folder created")
    except:
        try:
            shutil.rmtree(dst_path)
            shutil.copytree(dir1, dir2)
        finally:
            print("Files synchronized!")

def walk_src_dir(path):
    entries = pathlib.Path(path)
    for entry in entries.iterdir():
        if entry.is_dir():
            # print(f'Folder: {entry.name}')
            src_folders.append(entry.name)
            walk_src_dir(entry)
        else: 
            src_files.append(entry.name)
            # print(entry.name)

def walk_dst_dir(path):
    entries = pathlib.Path(path)
    for entry in entries.iterdir():
        if entry.is_dir():
            # print(f'Folder: {entry.name}')
            dst_folders.append(entry.name)
            walk_dst_dir(entry)
        else: 
            dst_files.append(entry.name)
            # print(entry.name)

def sync_files(dir1, dir2):
    walk_src_dir(dir1)
    walk_dst_dir(dir2)
    for folder in src_folders:
        if folder not in dst_folders:
            shutil.copytree(os.path.join(src_path,folder),os.path.join(dst_path,folder))

if __name__ == "__main__":
    # sync_files()
    # walk_src_dir(src_path)
    # walk_dst_dir(dst_path)
    sync_files(src_path, dst_path)
    # print(f'src: {src_folders}, {src_files}')
    # print(f'dst: {dst_folders}, {dst_files}')