#!/usr/bin/env python3

from gendiff.parse_args import parse_args
from gendiff import generate_diff


def main():
    args = parse_args()
    return generate_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
