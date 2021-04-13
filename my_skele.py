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


if __name__ == '__main__':
    main()