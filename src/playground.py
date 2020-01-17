import os
import converter

SAMPLE_FILE = os.path.join(os.path.dirname(os.getcwd()), "bin", "test.md")


def try_read():
    with open("test.md", 'r') as t:
        lines = t.readlines()
        print(t, lines)
    pass

def try_read2():
    with open("test.md", "r") as t:
        lines = t.readlines()

def try_parent_dir():
    # print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print(os.path.abspath(os.path.dirname(os.getcwd())))
    # print(os.path.abspath(os.path.join(os.getcwd(), "..")))
    print(  os.path.join(os.path.dirname(os.getcwd()), "bin", "test.md")    )

def try_converter():
    c = converter.Converter("asd")
    c.read_md()

if __name__ == '__main__':
    try_converter()

