#!/usr/bin/env python3

from gendiff.parse_args import parse_args
from gendiff import generate_diff
from pprint import pprint

def main():
    args = parse_args()
    pprint(generate_diff(args.first_file, args.second_file, args.format), sort_dicts=False)


if __name__ == '__main__':
    main()
