    """
    Writes the key-value pairs to a YAML file, representing every pair on a new line.

    :param data: Dictionary of status codes and their occurrences
    :param output_file: Path to the output YAML file
    """
    try:
        # Write the status codes and their occurrences to a YAML file
        with open(output_file, 'w') as file:
            # Start the YAML file with '---'
            file.write("---\n")
            # Using collections to write the data in YAML format
            for key, value in sorted(data.items()):
                file.write(f"{key}: {value}\n")
        print(f"Results have been written to {output_file}")
    except Exception as e:
        # Handle any other exception that may occur during file writing
        print(f"An error occurred while writing to the YAML file: {e}")
        sys.exit(1)
