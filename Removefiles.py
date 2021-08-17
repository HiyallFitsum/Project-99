import time
import os
import shutil

def main():
    deletedFolderCount = 0
    deletedFileCount = 0
    path = input("Enter the path of the folder you want to sort: ")
    days = int(input("Enter how many days old the: "))
    seconds = time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFolderCount += 1
                break
            else:
                for folder in folders: 
                    filePath = os.path.join(filePath, folder)
                    if seconds >= get_file_or_folder_age(filePath):
                        remove_file(filePath)
                        deletedFileCount += 1
                        break
    print("These are the number of folder deleted", deletedFolderCount)
    print("These are the number of files deleted", deletedFileCount)

    

def main()