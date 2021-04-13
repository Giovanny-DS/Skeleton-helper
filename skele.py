import os


def main(root_folder=False,
         sub_folders=False,
         files=False,
         sub_folders_names=[],
         file_names=[]):
    try:
        os.makedirs(root_folder)
        if sub_folders:
            for folder in sub_folders_names:
                os.makedirs(root_folder + '/' + folder)
        if files:
            for file in file_names:
                open(root_folder + '/' + str(file), "x")
    except FileExistsError:
        print("Directory already exists")


if __name__ == '__main__':
    main()
