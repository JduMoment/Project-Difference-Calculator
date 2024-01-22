### Hexlet tests and linter status:
[![Actions Status](https://github.com/JduMoment/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/JduMoment/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/400d66b15aa2310f7ceb/maintainability)](https://codeclimate.com/github/JduMoment/python-project-50/maintainability)
[![Python CI](https://github.com/JduMoment/python-project-50/actions/workflows/boilerplate.yml/badge.svg)](https://github.com/JduMoment/python-project-50/actions/workflows/boilerplate.yml)

The program works with files of the format **.json** and **.yml** any nesting.

It takes as arguments two files to compare and the format in which the result should be output.
By default, the result is output in **stylish** format, but you can also specify **plain** or **json**.
The name of the format should be specified after the `-f` switch.

For example, if you want output in plain format, you would enter the command:
`gendiff -f plain path_to_file path_to_file`

This asciinema demonstrates the generation of file differences in stylish format:
https://asciinema.org/a/jwND5N0rzuYSjQV4ctsqQzuvJ

Demonstrates the generation of file differences in plain format:
https://asciinema.org/a/ZOrXP49O22hlWEJnU7IRMPPGr

Demonstrates the generation of file differences in json format:
https://asciinema.org/a/nIibIo8eBiYXslA9JjcLFqppH <br>

For write to a file, just specify the path to the file: `gendiff -f json path_to_file
path_to_file > file_for_writing`. The output has already been converted to the json format.

