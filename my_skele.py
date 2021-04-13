import os


def main():
    try:
        root_folder = str(input("Folder name: "))
        sub_folders = bool(
            input("Sub folders? blank if not. anything else if yes"))
        os.makedirs(root_folder)
        if sub_folders:
            sub_folders_names = list(input("Sub folder names: ").split(','))
            for folder in sub_folders_names:
                os.makedirs(folder)

        files = bool(input('files? blank if not. anything else if yes'))
        if files:
            file_names = list(
                input(
                    'file names coma separated: (specify subfolders prefixing  with "your-sub-folder/" )'
                ).split(','))
            for file in file_names:
                open(root_folder + '/' + str(file), "x")
    except FileExistsError:
        print("Directory already exists")


#   print(str(root_dir))
# # Create directory
#   for i in range(0, len(main_dir)):
#   for j in range(0,len(main_dir[i])):
#     dirName = str(root_dir) + '/' + str(main_dir_names[i]) +'/' + str(main_dir[i][j])
#     try:
#         # Create target Directory
#         os.makedirs(dirName)
#         print("Directory " , dirName ,  " Created ")
#     except FileExistsError:
#         print("Directory " , dirName ,  " already exists")

#     # Create target Directory if don't exist
#     if not os.path.exists(dirName):
#         os.makedirs(dirName)
#         print("Directory " , dirName ,  " Created ")
#     else:
#         print("Directory " , dirName ,  " already exists")

if __name__ == '__main__':
    main()