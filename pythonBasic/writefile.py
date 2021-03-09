# file = open("text.txt")
#
# file.close()

# abr ele archivo y lo cierra cuando ya no le ocupa es mejor que el flo.eclose()

# read the file and store all the lines in list
# reverse the list
with open('text.txt', 'r') as reader:
    lines = reader.readlines()
    print(lines)
    # lines.reverse()
    # print(lines)
    with open('text.txt', 'w') as writer:
        # writer.writelines(lines)
        for line in reversed(lines):
            writer.write(line)
