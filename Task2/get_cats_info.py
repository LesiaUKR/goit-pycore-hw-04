from pathlib import Path

path = Path("Task1/salaries.txt")


def get_cats_info(path: str) -> list[dict[str, str, str]]:
    '''Function to read cats info from file and return
       it as a list of dictionaries.
       path: str - path to the file with cats info'''
   #  create an empty list to store cats info
    cats_info = []

    try:
      #   open the file with cats info
        with open(path, "r", encoding="utf-8") as cats_file:
            # read the file line by line
            for line in cats_file:
               #  delete spaces, split the line by comma and unpack the values
                id, name, age = line.strip().split(",")
               #  add the cat info to the list as a dictionary
                cats_info.append({"id": id, "name": name, "age": age})

    except FileNotFoundError:
        print(f"File '{path}' not found.")

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return cats_info


print(get_cats_info("Task2\cats.txt"))
