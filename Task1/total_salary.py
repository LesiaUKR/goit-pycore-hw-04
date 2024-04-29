from pathlib import Path

path = Path("Task1/salaries.txt")


def total_salary(path: str) -> str:
    '''Function to read salary data from file and return
     total and avarage salary.
     path: str - path to the file with salary data'''

   #  create variables to store total salary and count of salaries
    total_salary = 0
    count = 0

    try:
      #   open the file with salary data
        with open(path, "r", encoding='utf-8') as salary_file:
            # read the file line by line
            for line in salary_file:
                # split the line by comma and unpack the values
                _, salary = line.strip().split(",")
                total_salary += int(salary)
                count += 1

    except FileNotFoundError:
        return "File not found"

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    if count == 0:
        print("File is empty or has no salary data.")
        return None
    #  calculate avarage salary
    avarage_salary = int(total_salary / count)
    return f"Total salary: {total_salary}, Avarage salary: {avarage_salary}"


print(total_salary("Task1\salaries.txt"))
