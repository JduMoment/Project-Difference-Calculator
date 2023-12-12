import argparse

def parse_args():
    gendiff = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    gendiff.add_argument('first_file', type=str, help='')
    gendiff.add_argument('second_file', type=str, help='')
    args = gendiff.parse_args()
    return args