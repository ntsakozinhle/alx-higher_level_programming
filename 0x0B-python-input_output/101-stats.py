#!/usr/bin/python3
import sys

def compute_metrics():
    total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            ip, _, _, status_code, file_size = line.strip().split()[0], line.strip().split()[8], line.strip().split()[10], line.strip().split()[11], line.strip().split()[12]
            total_file_size += int(file_size)
            status_code_counts[int(status_code)] += 1

            if line_count % 10 == 0:
                print_metrics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_counts)

def print_metrics(total_file_size, status_code_counts):
    print("File size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] != 0:
            print("{}: {}".format(code, status_code_counts[code]))

if __name__ == "__main__":
    compute_metrics()
