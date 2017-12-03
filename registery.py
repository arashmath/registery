print(""" Hello! This program keeps a list of information about people (containing first name, last name, age and job).
The commands you may you use are:
add : To add a person to the list
del : To remove a person from the list
show : To view the information of every person in the list
edit : To edit any information about a person
quit : to exit from the program 
Special thanks to my instructor, Arian Rahimi. Github: @itsarianr""")

import csv

list_of_people = [] # List where all the information is stored

def length_of_file(file_name): # Returns the number of rows in list_of_people.csv
    file_to_list = list(file_name)
    return len(file_to_list)


def show():  # Shows the entire list of people when called
    i = 1
    if length_of_file("list_of_people.csv") == 0:
        print("The list is empty.")
    else:
        with open("list_of_people.csv", "r") as registery_file:
            reader = csv.DictReader(registery_file, delimiter=',')
            for row in reader:
                print(str(i) + ". Name: " + row["last_name"] + ", " + row["first_name"] + "  Age: " + row["age"] + "  Job: " + row["job"])
                i += 1
    registery_file.close()
             

def add(): # Adds a person to list_of_people.csv when called
    first_name = input(" First Name : ")
    last_name = input(" Last Name : ")
    age = input(" Age : ")
    job = input(" Job : ")
    with open("list_of_people.csv", "a") as registery_file:
        fieldnames = ["first_name", "last_name", "age", "job"]
        writer = csv.DictWriter(registery_file, fieldnames = fieldnames)
        writer.writerow({"first_name":first_name, "last_name":last_name, "age":age, "job":job})
    print(" Person added successfully !")
    registery_file.close()

#problems on lines:  46: why "r" / how does it cause data to be deleted?
def delete(): # Deletes a person from list_of_people when called
    to_be_deleted = []
    delete_by_first_name = input(" Enter the first name of the person you want to delete: ")
    with open("list_of_people.csv", "r") as registery_file:
        reader = csv.DictReader(registery_file)
        for row in reader:
            if row["first_name"] == delete_by_first_name:
                to_be_deleted.append(row)
    i = 1
    if len(to_be_deleted) == 0:
        print("Nobody existed with the first name " + delete_by_first_name)
    else:    
        print("The following people with " + delete_by_first_name + " as their first name are avaiable :")
        for person in to_be_deleted:
            print(str(i) + ". Name: " + person["last_name"] + ", " + person["first_name"] + "  Age: " + person["age"] + "  Job: " + person["job"])
            i += 1
    while(True):
        ans = input("Enter the number for person you want to delete. Enter 0 to finish : ")
        if int(ans) == 0:
            print("Exited from del function.")
            break
        elif int(ans) in range(1,i):
            with open("list_of_people.csv", "w"):
                field_names = ["first_name", "last_name", "age", "job"]
                writer = csv.DictWriter(registery_file, fieldnames = field_names)
                reader = csv.DictReader(registery_file)
                for row in reader:
                    if row == to_be_deleted[int(ans)-1]:
                        writer.writerow(row)
                        to_be_deleted.pop(int(ans)-1)
            #list_of_people.pop(list_of_people.index(to_be_deleted[int(ans)-1]))
            print(" Removal done successfully.")
            continue
        else:
            print("Invalid input. Re-enter your answer.")
            continue
# End of function delete()

def show_information(person): # Shows the information of a person when called by delete() function
    print(" First Name: " + person["first_name"])
    print(" Last Name: " + person["last_name"])
    print(" Age: " + str(person["age"]))
    print(" Job: " + person["job"])


def edit(): # Edits the informaton of a person when called
    while True:
        show()
        ans = input(" Enter the number for the person you want to edit (or 0 to quit): ")
        if int(ans) == 0:
            print("Function edit exited.")
            break
        elif int(ans) in range(1,len(list_of_people)+1):
            show_information(list_of_people[int(ans)-1])
            info_to_edit = input(" Enter the information you want to edit: first name, last name, age or job\n")
            person_to_edit = list_of_people[int(ans)-1]
            if info_to_edit == "first name":
                person_to_edit["first_name"] = input("Enter the first name: ")
            elif info_to_edit == "last name":
                person_to_edit["last_name"] = input("Enter the last name: ")
            elif info_to_edit == "age":
                person_to_edit["age"] = input("Enter the age: ")
            elif info_to_edit == "job":
                person_to_edit["job"] = input("Enter the job: ")
            else:
                print("Undefined information to edit. Please try again.")    
            continue
        else:
            print("Unspecified Command. Please check & re-enter your asnwer.")
            continue
# End of function edit()   

# Body of program
while(True):
    order = input(" Enter your command :")

    if order == "quit":
        print("Have a nice day !")
        break
    elif order == "show":
        show()
        continue
    elif order == "add":
        add()
        continue
    elif order == "del":
        delete()
        continue
    elif order == "edit":
        edit()
        continue
    else:
        print("Unspecified command. Review and then re-enter your answer.")
        continue