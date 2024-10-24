"""
  Pour d'autres formatations, modifier le regex (et ev. nom des variables)
"""

def is_clf(logs):
    """
    Checks if the log file is in Common Log Format (CLF).

    :param logs: file content
    :return: True if the file is in CLF format, kills the script otherwise
    """
    # Define the regular expression pattern for Common Log Format (CLF)
    clf_pattern = r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] ([\"])(\S+) (\S+)\s*(\S*)([\"]) (\d{3}) (\d+)([\n])'

    # Iterate over each line in the logs, with line numbers starting from 1
    for i, line in enumerate(logs, start=1):
        if re.match(clf_pattern, line) == "None":
            print(f"Error: Line {i} is not in Common Log Format (CLF).")
            return False
            sys.exit(1)
    # If all lines match the pattern, print a success message    
    print("The file is in Common Log Format (CLF). Proceeding...")
    return True
