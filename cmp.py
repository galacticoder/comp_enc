import lzma
import time
from tqdm import tqdm
import os
import pathlib

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} secs"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        seconds %= 60
        return f"{minutes} mins, {seconds:.2f} secs"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds %= 60
        if hours > 0:
            return f"{hours} hours, {minutes} mins, {seconds:.2f} secs"
        else:
            return f"{minutes} mins, {seconds:.2f} secs"

def compress_file(input_filename):
    try:
        fi = input_filename.find(".")
        sp = input_filename[fi:]
        start_time = time.time()
        output_filename = os.path.splitext(input_filename)[0] + '.cmp'
        with open(input_filename, 'rb') as f_in:
            with lzma.open(output_filename, 'wb', preset=9 | lzma.PRESET_EXTREME) as f_out:
                total_size = f_in.seek(0, 2)
                f_in.seek(0)
                with tqdm(total=total_size, unit='B', unit_scale=True, desc="Compressing") as pbar:
                    while True:
                        chunk = f_in.read(4096)
                        if not chunk:
                            break
                        f_out.write(chunk)
                        pbar.update(len(chunk))
        end_time = time.time()
        compression_time = end_time - start_time
        print("Compression time:", format_time(compression_time))
        os.remove(input_filename)
        print("File compressed.")
        print("Original file deleted.")
    except FileNotFoundError:
        print("File path not found")
        return
    except KeyboardInterrupt:
        print("Operation canceled by user")
        os.remove(output_filename)

def decompress_file(input_filename, compressed_filename):
    try:
        extension = pathlib.Path(input_filename).suffix
        if(extension.find('.')) != (-1):
            print("File extension found")
        else:
            print("File extension not found please use a valid input file with the extension")
            return
        output_filename = os.path.splitext(compressed_filename)[0]+str(extension)
        with lzma.open(compressed_filename, 'rb') as f_in:
            with open(output_filename, 'wb') as f_out:
                total_size = f_in.seek(0, 2)
                f_in.seek(0)
                with tqdm(total=total_size, unit='B', unit_scale=True, desc="Decompressing") as pbar:
                    while True:
                        chunk = f_in.read(4096)
                        if not chunk:
                            break
                        f_out.write(chunk)
                        pbar.update(len(chunk))
        print("Decompression complete.")
        os.remove(compressed_filename)
        print("Compressed file deleted.")
    except FileNotFoundError:
        print("File path not found")
    except KeyboardInterrupt:
        print("Operation canceled by user")
        os.remove(input_filename)

def get_files_in_directory(directory):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def compress_directory(directory):
    files = get_files_in_directory(directory)
    for file_path in files:
        compress_file(file_path)

def decompress_directory(directory):
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if file_path.endswith('.cmp'):  # Adjust the extension as needed
                decompress_file(filename, file_path)
                
choose = input("Do you want to compress or decompress a directory or file? (D/F): ").lower()

if choose == 'f':
    action = input("Do you want to 'c' or 'd' a file? (c/d): ").lower()
    if action == 'c':
        input_file = input("File path (exact path): ")
        compress_file(input_file)
    elif action == 'd':
        input_filename = input("Original file name (with file extension): ")
        compressed_file = input("Compressed file path (exact path): ")
        decompress_file(input_filename, compressed_file)
    else:
        print("Invalid action. Choose 'c' for compress or 'd' for decompress.")

elif choose == 'd':
    action = input("Do you want to 'c' or 'd' a directory? (c/d): ").lower()
    if action == 'c':
        input_dir = input("Directory path (exact path): ")
        compress_directory(input_dir)
    elif action == 'd':
        input_dir = input("Directory path (exact path): ")
        decompress_directory(input_dir)
    else:
        print("Invalid action. Choose 'c' for compress or 'd' for decompress.")
else:
    print("Invalid choice. Choose 'D' for directory or 'F' for file.")
