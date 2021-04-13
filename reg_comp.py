import skele


def main():
    root = input("root: ").capitalize()
    ext = int(input("jsx or tsx: type (1 or 2): "))
    extension = {1: ".jsx", 2: ".tsx"}
    skele.main(
        str(root), True, True, ['css'],
        [str(root) + extension[ext], '/css/' + str(root).lower() + '.css'])


if __name__ == '__main__':
    main()