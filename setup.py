import os
#test2
def setup():
    requirements = open('requirements.txt', "r")
    modules = requirements.read()
    command = input('Please enter the command to install modules. For example "python -m pip install ". ')
    os.system(command + '-r requirements.txt')

def print_information():
    print('Please make sure to run setup.py before running this script.')
    print('Take a look on the information provided on the github page.')
    print('')

if __name__ == '__main__':
    setup()
