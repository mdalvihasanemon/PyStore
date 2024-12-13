import os

def calculate_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file in filenames:
            total_size += os.path.getsize(os.path.join(dirpath, file))
    return total_size

folder_path = "./"
size_in_bytes = calculate_size(folder_path)
print(f"Total size: {size_in_bytes / (1024 * 1024):.2f} MB")
