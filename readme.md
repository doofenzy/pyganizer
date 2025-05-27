
# 📂 Pyganizer

This Python script automatically organizes files in your Downloads folder by file type. It creates categorized folders (like Images, Documents, Videos, etc.) and moves files into them based on their extensions.




## 🚀 Features

- Automatically organizes your messy Downloads folder

- Categorizes files into:

   - 📷 Images: .jpg, .jpeg, .png, .gif

    - 📄 Documents: .pdf, .docx, .txt

    - 🎬 Videos: .mp4, .mov, .avi

    - 🎼 Music: .mp3, .wav

    - 📦 Archives: .zip, .rar, .7z, .tar

    - ⚙️ Executables: .exe, .bat, .sh

- Creates missing folders if they don’t exist

- Ignores subfolders and only organizes files

## 🖥️ How It Works

- Detects your username automatically using getpass.getuser()

- Targets the current user's Downloads folder

- Iterates over each file and moves it to the corresponding folder based on its extension


## 📦 Installation
### Requirements 
- Python 3.x

- Runs on Windows (uses a Windows-style path: C:\Users\{user}\Downloads)

No external packages are required — just uses built-in Python libraries:
```
os, shutil, pathlib, getpass
```

✅ Step 1: Copy or clone the script
```
git clone https://github.com/yourusername/download-folder-organizer.git
cd download-folder-organizer
```

### 💻 Usage
✅ Step 2: Run the script
```
python main.py
```

You will see output like this
```
Folder Images does not exist. Creating...
Folder Documents exists.
...
Done Organizing
```

📁 Example Folder Structure (after running)
```
Downloads/
├── Images/
├── Documents/
├── Videos/
├── Music/
├── Archives/
├── Executables/
```

## ✏️ Customization
You can easily add or modify extensions:
```
folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z', 'tar'],
    'Executables': ['.exe', '.bat', '.sh'],
}
```

## 🛡️ Safety Notes
- Files are moved (not copied) — they will no longer be in the root Downloads folder

- The script does not recursively go into subfolders

## Authors

- [@JeromeInfante](https://www.github.com/doofenzy)

