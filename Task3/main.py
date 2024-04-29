import sys
from colorama import init, Fore
from parse_directory import parse_directory

# colorama initialization
init(autoreset=True)


def main():
    '''main function for the reading command line argument
       and calling the parse_directory function'''

    # check if the number of arguments is correct
    if len(sys.argv) != 2:
        print(Fore.RED + "Please enter: python main.py <absolute directory_path>")
    else:
        directory_path = sys.argv[1]
        parse_directory(directory_path)


#  call the main function
if __name__ == "__main__":
    main()
