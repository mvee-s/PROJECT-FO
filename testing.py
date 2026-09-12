import os
import shutil

user_folder = input("Enter the folder path to organize: ")
list_files = [os.listdir()]
list_subfolders = ["Images", "Documents", "Videos", "Others"]
images = 0
documents = 0
videos = 0
others = 0 


if os.path.exists(user_folder):

    for subfolder in list_subfolders:
        if os.path.exists(subfolder):
            print(subfolder)

    
        

    
else:
    print("The folder does not exist.")