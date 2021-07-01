# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def asf():
    print("asf")


def print_hi(name):
    with open('src/input.txt') as f:
        lines = f.readlines()

    for operator in lines:
        if operator == "asf\n":
            asf()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
