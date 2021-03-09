# read a file
def read_file():
    file = open('text.txt')
    # read all content of file
    print(file.read())
    file.close()


def read_5_lines():
    file = open('text.txt')
    # read a n number of characteres by patameter
    print(file.read(5))
    print("***********")
    print(file.readline())
    print(file.readline())
    file.close()


def read_by_line():
    file = open('text.txt')
    line = file.readline()
    while line != "":
        print(line)
        line = file.readline()


read_file()
print("-----------------")
read_5_lines()
print("-----------------")
read_by_line()
