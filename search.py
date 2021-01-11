import sys
import os

""" This is a script that iterates inside a directory through multiple directories or inside a single file
and try to find an email:password pair inside a .txt file for the email provided in the argument"""

"""
Features:
    - Search recursive in multiple directories from the root specified in the arguments;
    - Write on a file giving a location for the file output;
    - Search on a single file
    - You can choose two modes, choice and no choice, with choice after finding information will ask you questions to continue,
        without choice will go trought every file inside the directory without asking questions, both of them will write in the file
"""

if(len(sys.argv) != 5):
    print("Error: You need to specify the email and the path to the directory where you have the list")
    print("./searchEmail.py <email> <directory to search> <path to output file> <choice (yes/no)>")
    print(len(sys.argv))
    sys.exit(0)

email = sys.argv[1]
path = sys.argv[2]
output_path = sys.argv[3]
choice = sys.argv[4]

output_file = open(output_path + "\\" + email + ".txt", "w")

for arg in sys.argv:
    print("-->" + arg)

def iterate_folder_choice(path):
    for file in os.listdir(path):
        next_thing = path + "\\" + file
        if(os.path.isdir(next_thing)):
            iterate_folder_choice(next_thing)
        elif(os.path.isfile(next_thing)):
            if(file.endswith(".txt")):
                file_path = path + "\\" + file
                with open(file_path, 'r') as read_obj:
                    try:
                        for line in read_obj:

                            if email in line:
                                print("YOU FOUND INFORMATION!")
                                found_line = "Found in " + file_path + " : " + line + "\n"
                                output_file.write(found_line)
                                print("Target: " + email)
                                print("Found: " + found_line)
                                resp = ""

                                while((resp != "y" and resp != "yes") and (resp != "n" and resp != "no")):
                                    resp = input(
                                        "Do you want to continue to serch inside this file y(yes)/n(no)? ")

                                if resp == "n" or resp == "no":
                                    return
                    except:
                        Exception
        resp = input(
            "Do you want to continue to search inside other directories y(yes)/n(no)? ")
        if(resp == "n" or resp == "no"):
            return


def iterate_folder_no_choice(path):
    print(path)
    if(path.endswith(".txt")):
        file_ite(path, "")
        return
    

    for file in os.listdir(path):
        next_thing = path + "\\" + file
        if(os.path.isdir(next_thing)):
            iterate_folder_no_choice(next_thing)
        elif(os.path.isfile(next_thing)):
            if(file.endswith(".txt")):
                file_ite(path, file)


def file_ite(path, file):
    file_path = ""
    if(file == ""):
        file_path = path;
    else:
        file_path = path + "\\" + file
    

    with open(file_path, 'r') as read_obj:
        try:
            for line in read_obj:
                if email in line:
                    print("YOU FOUND INFORMATION!")
                    found_line = "Found in " + file_path + " : " + line + "\n"
                    output_file.write(found_line)
                    print("Target: " + email)
                    print("Found: " + found_line)

        except:
            Exception
                


if(choice == "yes"):
    iterate_folder_choice(path)
elif(choice == "no"):
    iterate_folder_no_choice(path)
