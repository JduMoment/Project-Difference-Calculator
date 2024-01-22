import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', help='set format of output',
                        type=str, default='stylish')
    args = parser.parse_args()
    return args
