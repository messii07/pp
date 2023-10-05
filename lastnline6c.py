def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if n >= len(lines):
            return lines
        else:
            return lines[-n:]
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = 'r.txt'  # Replace with the path to your file
    n = 5  # Number of last lines to read

    last_n_lines = read_last_n_lines(file_path, n)

    if last_n_lines is not None:
        print(f"Last {n} lines of the file:")
        for line in last_n_lines:
            print(line.strip())
    else:
        print("File not found.")
