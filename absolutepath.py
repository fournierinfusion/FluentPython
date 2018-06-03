import os


def argswalk(*args):
    a = [




if __name__ == '__main__':

    directory = '/Users/alex.fournier/downloads/data'
    print(os.path.abspath(directory))
    print(os.listdir(directory))
    a = [t for t in (os.walk(directory))]
    print(a)