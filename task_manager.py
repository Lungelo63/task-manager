#importing current date
from datetime import datetime

#opening user file

user_file = open("user.txt", "r+")

text = user_file.readlines()

login = False

#while login is false,

#if user enters correct credentials, login

#changes to True. Giving exccess

while login == False:

    username = input("Enter your username: ")

    password = input("Enter your password: ")

    for lines in text:

        valid_user, valid_password = map(str.strip, lines.split(", "))

        if valid_user == username and valid_password == password:

            login = True

            print("Logging in...")

            break

        else:

            print("Invalid login details")

    user_file.seek(0)

#user_file.close()

#choices for the user to choose from

choices = input('''Select option one below:

r - register username

a - add task

va - view all tasks

vm - view my tasks

e - exit

s - stats

''')

#if user selects admin selects "r" he can

#register a user to user_file

if choices == "r":

    if username == "admin":

        new_userLogin = False

        new_usersName = input("Enter username: ")

        while new_userLogin == False:

            new_userPass = input("Enter password: ")

            validate = input("Confirm password: ")

            if new_userPass == validate:

                new_userLogin = True

            if new_userPass != validate:

                print("password did not match. Try again")

            if new_userPass == validate:

                print("password matches. New user created")

                append_me = open("user.txt", "a")

                append_me.write("\n" + str(new_usersName) + ", " + str(validate))

                append_me.close()

    if username != "admin":

        print("Only admin can add a new user.")

#if user selects "a" he/she will have

#to enter input. input will be written one

#tasks_file

elif choices == "a":

    tasks = open("tasks.txt", "a")

    assignee = input("Enter the usersname of assignee: ")

    title = input("Enter the title of the task: ")

    description = input("Enter task description: ")

    due_date = input("Enter task due date YYYY-MM-DD: ")

    date = datetime.now()

    completed = "no"

    tasks.write(str(assignee) + ", " + str(title) + ", " + str(description) + ", " + str(due_date)

+ ", " + str(date) + ", " + str(completed) + "\n")

    tasks.close()

#if user selects "va" he will be given info

#of every file in an easy to read format

elif choices == "va":

    tasks_file = open("tasks.txt", "r+")

#loop to print out details in proper manner

    for line in tasks_file:

        assignee, title, description, due_date, date, completed = line.split(", ")

        print(f'''

        Name: {assignee}

        Title: {title}

        Description: {description}

        Due Date: {due_date}

        Date Assigned: {date}

        Task Complete: {completed}

        ''')

    tasks_file.close()

#if user selects "vm" program

#will desplay specific user task

if choices == "vm":

    view = open("tasks.txt", "r")

    for line in view:

        assignee, title, description, due_date, date, completed = line.split(", ")

    if username == assignee:

        print(f'''

        Name: {assignee}

        Title: {title}

        Description: {description}

        Due Date: {due_date}

        Date Assigned: {date}

        Task Complete: {completed}

        ''')

    view.close()

#if the user selects "e" program

#breaks

if choices == "e":

    print("closing program...")

    breakpoint

#if user selects "s". number of tasks and

#number of users are displayed

if choices == "s":

    stats_file = open("tasks.txt", "r+")

    other_stats = open("tasks.txt", "r+")

    if username == "admin":

        num_title = 0

        num_assignee = 0

    for line in stats_file:

        assignee, title, description, due_date, date, completed = line.split(", ")

        assignee

        num_assignee += 1

        print(f'''

        Total number of users: {num_assignee}

        ''')

    stats_file.close()

    for title in other_stats:

        assignee, title, description, due_date, date, completed = title.split(", ")

        title

        num_title += 1

        print(f'''

        Total number of tasks: {num_title}

        ''')

    other_stats.close()