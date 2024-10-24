def open_file(file_path):
    """
    Opens the log file in common log format.

    :param file_path: Path to the log file (.txt)
    """
    try:
        with open(file_path, 'r') as file:
            # Read and print content for demonstration (can be modified as needed)
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
