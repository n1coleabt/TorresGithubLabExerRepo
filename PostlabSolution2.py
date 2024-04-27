def read_file(filename):
    """
    Read the lines of text from a file and return them as a list.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list of str: List of lines from the file, or None if the file is not found.
    """

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def main():
    print("Welcome to the File Navigator!")

    while True:
        filename = input("Enter the filename (or '0' to quit): ")

        if filename == '0':
            print("Goodbye!")
            break

        lines = read_file(filename)

        if lines is not None:
            line_count = len(lines)

            while True:
                print(f"\nNumber of lines in the file: {line_count}")
                line_number_str = input("Enter a line number (1 to {line_count}, or 0 to quit): ")

                try:
                    line_number = int(line_number_str)

                    if line_number == 0:
                        break

                    if 1 <= line_number <= line_count:
                        print(f"Line {line_number}: {lines[line_number - 1]}")  
                    else:
                        print(f"Invalid line number. Please enter a number between 1 and {line_count}.")
                except ValueError:
                    print("Invalid input. Please enter a valid line number.")

if __name__ == "__main__":
    main()
