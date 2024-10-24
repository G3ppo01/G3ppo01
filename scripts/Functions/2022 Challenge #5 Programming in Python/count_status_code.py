"""
compter le nombre de status code http dans une liste de log
Utilise:
from collections import Counter 
import re
"""
def count_status_codes(logs):
    """
    Reads the log file and counts the occurrence of each status code.

    :param logs: file content as a list of lines
    :return: Ordered dictionary of status codes and their occurrences
    """
    try:
        # Define the regular expression pattern to extract status codes from CLF logs
        status_code_pattern = r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] \"(\S+) (\S+)\s*(\S*)\" (\d{3}) (\d+|-)$'
        
        # Initialize a Counter to keep track of status codes
        status_counter = Counter()
        
        # Iterate over each line to extract and count status codes
        for line in logs:
            match = re.match(status_code_pattern, line)
            if match:
                # Extract the status code (8th group in the pattern)
                status_code = match.group(8)
                status_counter[status_code] += 1
            else:
                # Handle the case where a line does not match the expected pattern
                print(f"Warning: A line did not match the expected format and was skipped.")
        
        # Return the ordered dictionary of status codes and their occurrences
        for code, count in sorted(status_counter.items()):
            print(f"Status Code {code}: {count} occurrences")
    except Exception as e:
        # Handle any other exception that may occur during processing
        print(f"An error occurred while counting status codes: {e}")
        sys.exit(1)
