#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics """

import sys
import re

if __name__ == '__main__':

    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    status_count = {code: 0 for code in status_codes}
    total_size = 0
    count = 0

    def print_stats(status_count, total_size):
        print(f"File size: {total_size}")
        for code in sorted(status_count.keys()):
            if status_count[code]:
                print(f"{code}: {status_count[code]}")

    try:
        for line in sys.stdin:
            pattern = pattern = r'(.*?) - \[(.*?)\] "(.*?)" (.*?) (\S+)'
            match = re.match(pattern, line)

            if match:
                count += 1
                ip_address, date, request, status_code, file_size = match.groups()  # noqa: E501

                try:
                    if int(status_code) in status_count:
                        status_count[int(status_code)] += 1
                except BaseException:
                    pass

                try:
                    total_size += int(file_size)
                except BaseException:
                    pass

            if count % 10 == 0:
                print_stats(status_count, total_size)
        print_stats(status_count, total_size)

    except (KeyboardInterrupt, SystemExit):
        print_stats(status_count, total_size)
        raise
