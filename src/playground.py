def try_read():
    with open("test.md", 'r') as t:
        lines = t.readlines()
        print(t, lines)
    pass

def try_read2():
    with open("test.md", "r") as t:
        lines = t.readlines()


if __name__ == '__main__':
    try_read2()

