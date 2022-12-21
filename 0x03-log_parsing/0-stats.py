#!/usr/bin/python3
"""
"""
import sys

status = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
sizes = 0
count_line = 0

try:
    for line in sys.stdin:
        count_line += 1
        parts = line.split()
        try:
            status_code = parts[7]
            file_size = parts[8]

            if status_code in status.keys():
                status[status_code] += 1

            sizes += int(file_size)

        except Exception:
            pass

        if count_line % 10 == 0:
            print('File size: {}'.format(sizes))
            for scode, size in sorted(status.items()):
                if size:
                    print('{}: {}'.format(scode, size))

    print('File size: {}'.format(sizes))
    for scode, size in sorted(status.items()):
        if size:
            print('{}: {}'.format(scode, size))

except KeyboardInterrupt:
    print('File size: {}'.format(sizes))
    for scode, size in sorted(status.items()):
        if size:
            print('{}: {}'.format(scode, size))
