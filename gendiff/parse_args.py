import argparse

def parse_args():
    gendiff = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    gendiff.add_argument('first_file', help='')
    gendiff.add_argument('second_file', help='')
    gendiff.add_argument('-f', '--format', help ='set format of output')
    args = gendiff.parse_args()
    return args