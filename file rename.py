import os

def rename_files(folder_path, prefix):
    for count, filename in enumerate(os.listdir(folder_path)):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{count + 1}{ext}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        print(f"Renamed: {filename} -> {new_name}")

folder_path = "./files"
prefix = "file"
rename_files(folder_path, prefix)
