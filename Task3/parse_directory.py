from pathlib import Path
from colorama import Fore


def parse_directory(directory_path, indent=0):
    '''Функція для візуалізації структури директорії '''

    # get Path object from directory_path
    directory = Path(directory_path)

    # check if the directory exists and is a directory
    if not directory.exists() or not directory.is_dir():
        print(
            Fore.RED + f"Directory '{directory_path}' does not exist or is not a directory.")
        return

    # output the name of the directory with the corresponding color
    print(Fore.BLUE + "📁" + directory.name)

    # get the list of items in the directory
    for item in directory.iterdir():
        if item.is_dir():
            # output the name of the subdirectory with the corresponding color and indent
            print(Fore.CYAN + "  " * indent + "┣ 📁" + item.name)
            # recursively call the function for the subdirectory if it is a directory
            parse_directory(item, indent + 1)
        else:
            # output the name of the file with the corresponding color and indent
            print(Fore.GREEN + "  " * indent + "┗ 📜" + item.name)
