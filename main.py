#Folder paths, synchronization interval and log file path should be provided using the command line arguments;
import argparse

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


def write_args_to_file():
    with open('args_file.txt', 'w') as log_file:
        log_file.write(src_path)
        log_file.write("\n")
        log_file.write(dst_path)
        log_file.write("\n")
        log_file.write(log_path)
        log_file.write("\n")
        log_file.write(str(sync_time))