import sys
import os

def extract_logs(date, log_file_path):
    """
    Extracts log entries for a given date from a large log file (1TB).
    Efficiently processes the file line by line.
    """
    # Ensure the output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    output_file_path = os.path.join(output_dir, f"output_{date}.txt")

    try:
        # Open log file in read mode & output file in write mode
        with open(log_file_path, "r", encoding="utf-8") as log_file, open(output_file_path, "w", encoding="utf-8") as output_file:
            count = 0  # Count matching lines

            for line in log_file:
                if line.startswith(date + "T"):  # Ensure it matches YYYY-MM-DDT
# Check if the log entry matches the given date
                    output_file.write(line)
                    count += 1

            print(f"Logs extracted successfully! Total matching lines: {count}")
            print(f"Extracted logs saved to: {output_file_path}")


        # Handle case where no logs were found
        if count == 0:
            print(f"No logs found for {date}!")

    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found!")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <YYYY-MM-DD> <log_file_path>")
    else:
        extract_logs(sys.argv[1], sys.argv[2])
