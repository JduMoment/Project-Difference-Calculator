#!/usr/bin/env python3

from gendiff.parse_args import parse_args
from gendiff.file_to_dict import transform_to_dict
from gendiff.construct_diff import construct_diff
from gendiff.generate_stylish_lines import generate_stylish_lines


def main():
    args = parse_args()
    print(args)
    file1, file2 = transform_to_dict(args.first_file, args.second_file)
    diff = construct_diff(file1, file2)
    generate_stylish_lines(diff)


if __name__ == '__main__':
    main()
