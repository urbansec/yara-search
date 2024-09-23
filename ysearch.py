# imports
import yaramod
import argparse


def main():
    # parse command line arguments
    parser = argparse.ArgumentParser(
                    prog='yara-search',
                    description='Displays relevant info from yara rules file',
                    epilog='Walk in the light')
    parser.add_argument('filename', type=str, help='yara rules file to use')
    parser.add_argument('-n', '--name', dest='rule_name', type=str, help='name of the yara rule to search for')
    args = parser.parse_args()

    # instantiate yaramod
    ymod = yaramod.Yaramod()

    # read yara rules file
    if args.filename:
        yfile = ymod.parse_file(args.filename)

    # print the requested rule information
    for rule in yfile.rules:
        if rule.name == args.rule_name:
            print(f"""Yara rule name: {yfile.rules[0].name}""")
            print(f"""Yara rule source: {yfile.rules[0].location.file_path}""")
            print('Yara rule definition:')
            print(yfile.rules[0].text)


if __name__ == '__main__':
    main()