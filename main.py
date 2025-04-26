import os
import shutil
import pathlib
import getpass

folder_dir = fr"C:\Users\{getpass.getuser()}\Downloads"

folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z', 'tar'],
    'Executables': ['.exe', '.bat', '.sh'],
}

# this loop will check for the folders inside the path
# and if the loop did not get the directory or missing dir it will create itself
for folder in folders:
    folder_path = os.path.join(folder_dir, folder)
    if not os.path.exists(folder_path):
        print(f'Folder {folder} does not exist. Creating...')
        os.makedirs(folder_path)
    else:
        print(f'Folder {folder} exists.')

for file in os.listdir(folder_dir):
    file_path = os.path.join(folder_dir, file)

    # ignore the folder
    if os.path.isdir(file_path):
        continue

    file_extension = os.path.splitext(file)[1].lower()
    for folder, extensions in folders.items():
        if file_extension in extensions:
            destination = os.path.join(folder_dir, folder, file)
            shutil.move(file_path, destination)

print("Done Organizing")