import os

folder_path = r"/storage/emulated/0/DCIM/Camera"

files = sorted(os.listdir(folder_path))


temp_files = [ ]

for i, filename in enumerate(files, start=1):
    old_path = os.path.join(folder_path, filename)

    if not os.path.isfile(old_path):
        continue

    ext = os.path.splitext(filename)[1].lower()

    temp_name = f"tmp_{i:03d}{ext}"
    temp_path = os.path.join(folder_path, temp_name)

    os.rename(old_path, temp_path)

    temp_files.append(temp_name)


img_count = 1
vid_count = 1

for temp_name in sorted(temp_files):
    old_path = os.path.join(folder_path, temp_name)

    ext = os.path.splitext(temp_name)[1].lower()

    if ext in [".jpg", ".jpeg", ".png", ".webp"]:
        new_name = f"img{img_count:03d}{ext}"
        img_count += 1

    elif ext == ".mp4":
        new_name = f"vid{vid_count:03d}{ext}"
        vid_count += 1

    else:
        continue

    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print("Files renamed successfully!")
