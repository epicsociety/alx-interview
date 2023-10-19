#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics """

def print_stats(status_count, total_size):
    for code in sorted(status_count.keys()):
        if status_count[code]:
            print(f"{code}: {status_count[code]}")
    print(f"File size: {total_size}")

if __name__ == '__main__':
    import sys
    import re

    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    status_count = {code: 0 for code in status_codes}
    total_size = 0
    count = 0

    try:
        for line in sys.stdin:
            pattern = r'([\d.]+) - \[(.*?)\] "(.*?)" (\d+) (\d+)'
            match = re.match(pattern, line)

            if match:
                ip_address, date, request, status_code, file_size = match.groups()

                if int(status_code) in status_count:
                    status_count[int(status_code)] += 1

                total_size += int(file_size)
                count += 1

            if count % 10 == 0:
                print_stats(status_count, total_size)

    except (KeyboardInterrupt, SystemExit):
        print_stats(status_count, total_size)
        raise
