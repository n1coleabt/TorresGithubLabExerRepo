enterfile = input("Enter the filename: ")
if not os.path.isfile(enterfile):
    print(f"File not found: {enterfile}")
    exit()

with open(enterfile, 'r') as file:
    lines = file.readlines()
    print(f"Total number of lines in the file: {len(lines)}")

    while True:
        num = int(input("Enter line number you want to view or press 0 to quit: "))
        if num > 0 and num <= len(lines):
            print(f"Line {num}: {lines[num - 1]}")
        elif num == 0:
            print("Thank you for using the program.")
            break
        else:
            print("Invalid line number.")
