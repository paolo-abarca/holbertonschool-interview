#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import sys


if __name__ == "__main__":
    dict_status = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
    total_sizes = [0]
    count_line = 1

    def print_stats():
        """
        Prints file size and stats for every 10 loops
        """
        print('File size: {}'.format(total_sizes[0]))
        for code in sorted(dict_status.keys()):
            if dict_status[code] != 0:
                print('{}: {}'.format(code, dict_status[code]))

    def parse_stdin(line):
        '''
        Checks the stdin for matches
        '''
        try:
            line = line[:-1]
            word = line.split(' ')
            total_sizes[0] += int(word[-1])
            status_code = int(word[-2])
            if status_code in dict_status:
                dict_status[status_code] += 1
        except BaseException:
            pass

    try:
        for line in sys.stdin:
            parse_stdin(line)
            if count_line % 10 == 0:
                print_stats()
            count_line += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
