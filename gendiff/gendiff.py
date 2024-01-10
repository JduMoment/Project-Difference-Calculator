#!/usr/bin/env python3

from gendiff.parse_args import parse_args
from gendiff.file_to_dict import transform_to_dict
from gendiff.construct_diff import construct_diff
from gendiff.generate_stylish_lines import generate_stylish_lines
from gendiff.generate_plain_lines import generate_plain_lines
from gendiff.generate_json_file import generate_json_file


def main():
    args = parse_args()
    file1, file2 = transform_to_dict(args.first_file, args.second_file)
    format = args.format
    diff = construct_diff(file1, file2)
    if format == 'stylish':
        print(generate_stylish_lines(diff))
    elif format == 'plain':
        print(generate_plain_lines(diff))
    elif format == 'json':
        print(generate_json_file(diff))


if __name__ == '__main__':
    main()
