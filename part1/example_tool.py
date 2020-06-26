
import sys
import getopt

from cfn_flip import flip, to_yaml, to_json


def display_help():
    print('Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.')
    print('usage: -h --help               show help')
    print('usage: -p --palindrome "name"  tests if a project name is a palindrome')
    print('usage: -j --json "filename"    converts YAML files to JSON')
    print('usage: -n --new "project"      generates a new Django project at ./part2/')


def test_palindrome(arg):
    rev = ''
    size = len(arg)
    for i in range(size):
        rev += arg[size-i-1:size-i]
    if arg == rev:
        return True
    else:
        return False


def convert_yaml_to_json(arg):
    with open(arg) as f:
        jsonout = to_json(f.read())
    fout = open('tacocat_cf.json', 'w')
    fout.write(jsonout)
    fout.close()


def new_django_project(arg):
    print('dsadsa')


def main(argv):
    try:
       opts, args = getopt.getopt(
           argv,
           'hp:j:n:',
           ['help', 'palindrome=', 'json=', 'new='])
    except getopt.GetoptError:
        display_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            display_help()
            sys.exit()
        elif opt in ('-p', '--palindrome'):
            print(test_palindrome(arg))
        elif opt in ('-j', '--json'):
            convert_yaml_to_json(arg)
            print('file conversion completed')
        elif opt in ('-n', '--new'):
            new_django_project(arg)



if __name__ == "__main__":
    main(sys.argv[1:])
