#!/usr/bin/python3

from sys import stdin

status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '402': 0,
    '403': 0,
    '404': 0,
    '500': 0,
}

total_size = i = 0


def log_printer():
    """this function printing informations"""
    print(f'File size: {total_size}')

    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


try:
    for line in stdin:
        spplited_line = line.split()
        if len(spplited_line) >= 2:
            status = spplited_line[-2]
            total_size += int(spplited_line[-1])
            if status in status_codes:
                status_codes[status] += 1
        i += 1

        if i % 10 == 0:
            log_printer()
        log_printer()
except KeyboardInterrupt as error:
    log_printer()
