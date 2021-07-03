import csv
import time
import os
import shutil

f = open('Halo/haloLog.csv', 'a', newline='')
writer = csv.writer(f)


def register_user(username, password, re_password):
    print("register user : " + username + " " + password + " " + re_password)


def login(username, password):
    print("login : " + username + " " + password)


def logout():
    print("logout")


def create_type(instruction_line, type_name, tokens):
    a_file = open("Halo/type.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    for type_lines in lines:
        ts = type_lines.split()
        if ts[0] == type_name:
            log = ["admin", time.time(), instruction_line.strip(), "failure"]
            writer.writerow(log)
            return

    lines = []
    with open('Halo/type.txt', 'r') as file:
        for line in file:
            lines.append(line.strip())
    file.close()
    line = type_name
    for token in tokens:
        line += " " + token
    lines.append(line)
    lines.sort()
    with open('Halo/type.txt', 'w') as file:
        for line in lines:
            file.write(line + "\n")
    path = "Halo/" + type_name
    os.mkdir(path)
    os.mkdir(path + "/file1")
    with open(path + "/file1/page1.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_file.close()
    with open(path + "/type_header.txt", 'w', newline='') as file_header:
        file_header.write("1")
    file_header.close()
    with open(path + "/file1/header.txt", 'w', newline='') as file_header:
        file_header.write("1 0 0")
    file_header.close()
    with open(path + "/file1/header2.txt", 'w', newline='') as file_header:
        file_header.write("0 - 0 - 0 - 0 - 0 - 0 - 0 - 0")
    file_header.close()
    log = ["admin", time.time(), instruction_line.strip(), "success"]
    writer.writerow(log)

    print("create_type : " + type_name)
    print(tokens)


def delete_type(instruction_line, type_name):
    a_file = open("Halo/type.txt", "r")

    lines = a_file.readlines()
    a_file.close()

    ins_line = ""
    for ins in instruction_line:
        ins_line += " " + ins

    new_file = open("Halo/type.txt", "w")
    log = ""
    for line in lines:
        token = line.split(" ")
        if token[0] == type_name:
            log = ["admin", time.time(), ins_line.strip(), "success"]
        if token[0] != type_name:
            new_file.write(line)
    new_file.close()
    if log == "":
        log = ["admin", time.time(), ins_line.strip(), "failure"]
        writer.writerow(log)
        return

    path = "Halo/" + type_name
    shutil.rmtree(path)
    writer.writerow(log)
    print("delete_type : " + type_name)


def inherit_type(instruction_line, target_type_name, source_type_name, columns):
    a_file = open("Halo/type.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    for type_lines in lines:
        ts = type_lines.split()
        if ts[0] == target_type_name:
            log = ["admin", time.time(), instruction_line.strip(), "failure"]
            writer.writerow(log)
            return
    lines = []
    with open('Halo/type.txt', 'r') as file:
        for line in file:
            lines.append(line.strip())
    file.close()
    result = target_type_name
    a_file = open("Halo/type.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    for line in lines:
        tokens = line.split()
        if tokens[0] == source_type_name:
            for token in tokens:
                if token != source_type_name:
                    result += " " + token
    for column in columns:
        result += " " + column
    result += "\n"
    lines.append(result)
    lines.sort()

    with open('Halo/type.txt', 'w') as file:
        for line in lines:
            file.write(line)
    file.close()

    path = "Halo/" + target_type_name
    os.mkdir(path)
    os.mkdir(path + "/file1")
    with open(path + "/file1/page1.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_file.close()
    with open(path + "/type_header.txt", 'w', newline='') as file_header:
        file_header.write("1")
    file_header.close()
    with open(path + "/file1/header.txt", 'w', newline='') as file_header:
        file_header.write("1 0 0")
    file_header.close()
    with open(path + "/file1/header2.txt", 'w', newline='') as file_header:
        file_header.write("0 - 0 - 0 - 0 - 0 - 0 - 0 - 0")
    file_header.close()
    log = ["admin", time.time(), instruction_line.strip(), "success"]
    writer.writerow(log)
    print("inherit_types : " + target_type_name + " " + source_type_name)
    print(columns)


def list_type(instruction_line):
    file_object = open('Halo/output.txt', 'a')
    a_file = open("Halo/type.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    for line in lines:
        tokens = line.split()
        file_object.write(tokens[0] + "\n")
    ins_line = ""
    for ins in instruction_line:
        ins_line += " " + ins
    log_output = ["admin", time.time(), ins_line.strip(), "success"]
    writer.writerow(log_output)
    file_object.close()
    print("list type")


def create_record(instruction_line, type_name, id, tokens):
    control = False
    a_file = open("Halo/type.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    for type_lines in lines:
        ts = type_lines.split()
        if ts[0] == type_name:
            control = True
    if control == False:
        log = ["admin", time.time(), instruction_line.strip(), "failure"]
        writer.writerow(log)
        return

    path = "Halo/" + type_name
    a_file = open(path + "/type_header.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    file_number = 0
    for line in lines:
        spl = line.split()
        file_number = int(spl[0])
    page_number = 0;
    lowest = 0;
    highest = 0;
    for i in range(file_number):
        os_path = path + "/file" + str(i+1)
        a_file = open(os_path + "/header.txt", "r")
        lines = a_file.readlines()
        a_file.close()

        for line in lines:
            spl = line.split()
            page_number = int(spl[0])
            lowest = int(spl[1])
            highest = int(spl[2])






def print_hi():
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
            instruction = ""
            for tk in tokens:
                instruction += " " + tk
            del tokens[0:2]
            type_name = tokens.pop(0)
            tokens.pop(0)
            create_type(instruction.strip(), type_name, tokens)
        elif tokens[0] + tokens[1] == "deletetype":
            delete_type(tokens, tokens[2])
        elif tokens[0] + tokens[1] == "inherittype":
            instruction = ""
            for tk in tokens:
                instruction += " " + tk
            del tokens[0:2]
            target_type_name = tokens.pop(0)
            source_type_name = tokens.pop(0)
            inherit_type(instruction, target_type_name, source_type_name, tokens)
        elif tokens[0] + tokens[1] == "listtype":
            list_type(tokens)
        elif tokens[0] + tokens[1] == "createrecord":
            instruction = ""
            for tk in tokens:
                instruction += " " + tk
            del tokens[0:2]
            type_name = tokens.pop(0)
            id = tokens.pop(0)
            create_record(instruction.strip(), type_name, id, tokens)
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
    f.close()


if __name__ == '__main__':
    print_hi()

