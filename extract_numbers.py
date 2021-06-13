#! /usr/bin/env python
"""
Extracts the numbers from HTML files and writes them to a csv file.

This will parse all sub-directories in the passed in directory, and process all files within using the
extract_numbers_lib. It then will merge all of the results into a csvfile.

"""
import argparse
import csv
import os

import extract_numbers_lib


def parse_filename(path):
    """Returns the cik and year for a file"""
    path_array = path.split('/')  #
    cik = path_array[-1].split('-')[0]  # Get the first element before the -
    year = path_array[-2]
    return [cik, year]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-r', '--root',
                        metavar='root',
                        default='html',
                        help='Path to read the file from')

    args = parser.parse_args()
    input_file = 'html/2007/51644-R20100226-C20091231-F04-0.htm'
    output = []
    folders = (args.root + '/' + f for f in os.listdir(args.root))
    for folder in folders:
        files = (folder + '/' + f for f in os.listdir(folder))
        for file in files:
            with open(input_file) as f:
                row = parse_filename(input_file)
                row.extend(extract_numbers_lib.parse_file(f))
                output.append(row)

    with open('output.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(output)


if __name__ == "__main__":
    main()
