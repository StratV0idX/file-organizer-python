# File Organizer Script
# Copyright (c) 2026 Roshan Jeffrin
# Licensed under the MIT License
import os
import shutil

# Folder you want to organize
source_folder = input('''Enter Valid Folder Path 
(E.g  C:/User/HP/Downloads)
''')
if not os.path.exists(source_folder):
    print("Invalid path! Please check and try again.")
    exit()
os.chdir(source_folder)

# File type categories
Images = (".jpg", ".jpeg", ".png", ".gif", ".jfif")
Documents = (".pdf", ".docx", ".txt")
Videos = (".mp4", ".mkv", ".avi")
Audios = (".mp3", ".wav", ".aiff", ".flac", ".alac", ".ape", ".aac", ".ogg", ".wma")
Archives = (".zip", ".rar")

#Here it creates folders
folders = ["Images", "Videos", "Audios", "Documents", "Archives", "Unknown_Files"]
base = "File_Organiser"

if not os.path.exists(base):
    os.mkdir(base)

for folder in folders:
    path = os.path.join(base, folder)
    if not os.path.exists(path):
        os.mkdir(path)

# Go through each file
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    name, ext = os.path.splitext(file)
    ext = ext.lower()

    #Skip folders
    if os.path.isdir(file_path):
        continue

    #Checks for images
    elif ext in Images:
        path = os.path.join("File_Organiser/Images", file)
        if os.path.exists(path):
            shutil.move(file, os.path.join("File_Organiser/Images", name+"_Copy"+ext))
        else:
            shutil.move(file, os.path.join("File_Organiser/Images", file))

    #Checks for Audios
    elif ext in Audios:
        path = os.path.join("File_Organiser/Audios", file)
        if os.path.exists(path):
            shutil.move(file, os.path.join("File_Organiser/Audios", name + "_Copy" + ext))
        else:
            shutil.move(file, os.path.join("File_Organiser/Audios", file))

    #Checks for Videos
    elif ext in Videos:
        path = os.path.join("File_Organiser/Videos", file)
        if os.path.exists(path):
            shutil.move(file, os.path.join("File_Organiser/Videos", name + "_Copy" + ext))
        else:
            shutil.move(file, os.path.join("File_Organiser/Videos", file))

    #Checks for Documents
    elif ext in Documents:
        path = os.path.join("File_Organiser/Documents", file)
        if os.path.exists(path):
            shutil.move(file, os.path.join("File_Organiser/Documents", name + "_Copy" + ext))
        else:
            shutil.move(file, os.path.join("File_Organiser/Documents", file))

    #Checks for Archives
    elif ext in Archives:
        path = os.path.join("File_Organiser/Archives", file)
        if os.path.exists(path):
            shutil.move(file, os.path.join("File_Organiser/Archives", name + "_Copy" + ext))
        else:
            shutil.move(file, os.path.join("File_Organiser/Archives", file))

    #For files except the above format
    else:
        path = os.path.join("File_Organiser/Unknown_Files", file)
        if os.path.exists(path):
            shutil.move(file, os.path.join("File_Organiser/Unknown_Files", name + "_Copy" + ext))
        else:
            shutil.move(file, os.path.join("File_Organiser/Unknown_Files", file))

#Final_Output
print("Files organized successfully!")