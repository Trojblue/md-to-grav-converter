from typing import List

def Main():
    read_file("test.md")



def read_file(file)->List[str]:
    """
    reads markdown file into a list of lines, removing \n at the end of each line
    :param file: path of markdown file, *.md
    :return:
    """
    lines = []
    with open("test.md", "r") as t:
        lines = t.readlines()
        # print(lines)

    for line in lines:
        pass

    return lines

if __name__ == '__main__':
    Main()
