# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def register_user(username, password, re_password):
    print("register user : " + username + " " + password + " " + re_password)


def login(username, password):
    print("login : " + username + " " + password)


def logout():
    print("logout")


def create_type(type_name, tokens):
    print("create_type : " + type_name)
    print(tokens)


def delete_type(type_name):
    print("delete_type : " + type_name)


def inherit_type(target_type_name, source_type_name, tokens):
    print("inherit_types : " + target_type_name + " " + source_type_name)
    print(tokens)


def list_type():
    print("list type")


def print_hi(name):
    with open('Halo/input.txt') as f:
        lines = f.readlines()

    for line in lines:
        tokens = line.split()
        if tokens[0] == "logout":
            logout()
        elif tokens[0] == "login":
            login(tokens[1], tokens[2])
        elif tokens[0] + tokens[1] == "registeruser":
            register_user(tokens[2], tokens[3], tokens[4])
        elif tokens[0] + tokens[1] == "createtype":
            del tokens[0:2]
            type_name = tokens.pop(0)
            tokens.pop(0)
            create_type(type_name, tokens)
        elif tokens[0] + tokens[1] == "deletetype":
            delete_type(tokens[2])
        elif tokens[0] + tokens[1] == "inherittype":
            del tokens[0:2]
            target_type_name = tokens.pop(0)
            source_type_name = tokens.pop(0)
            inherit_type(target_type_name, source_type_name, tokens)
        elif tokens[0] + tokens[1] == "listtype":
            list_type()
        elif tokens[0] + tokens[1] == "createrecord":
            print("createrecord")
        elif tokens[0] + tokens[1] == "deleterecord":
            print("deleterecord")
        elif tokens[0] + tokens[1] == "updaterecord":
            print("updaterecord")
        elif tokens[0] + tokens[1] == "searchrecord":
            print("searchrecord")
        elif tokens[0] + tokens[1] == "listrecord":
            print("listrecord")
        elif tokens[0] + tokens[1] == "filterrecord":
            print("filterrecord")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
