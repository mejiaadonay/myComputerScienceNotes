import os

#   rename files
#   Author: Jose Escobar Mejia
#   Date:   1/18/2016

#` function rename_file definition/implementation
def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"/Users/adonay/desktop/prank")
    # print(file_list)
    saved_path = os.getcwd()
    
    print("Current Working Directory is " + saved_path)
    os.chdir(r"/Users/adonay/desktop/prank")

    # (2) for each file, rename filename
    for file_name in file_list:
       os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()


