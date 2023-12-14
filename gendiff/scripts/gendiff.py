#!/usr/bin/env python3

from gendiff.parse_args import parse_args
from gendiff.flat_file import generate_diff

def main():
    # args = parse_args()
    generate_diff(parse_args().first_file, parse_args().second_file)


if __name__ == '__main__':
    main()