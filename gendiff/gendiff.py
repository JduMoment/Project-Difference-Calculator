#!/usr/bin/env python3

from gendiff.parse_args import parse_args
from gendiff.file_to_dict import transform_to_dict
from gendiff.generate_diff import generate_diff


def main():
    args = parse_args()
    file1, file2 = transform_to_dict(args.first_file, args.second_file)
    print(file1, file2)


if __name__ == '__main__':
    main()
