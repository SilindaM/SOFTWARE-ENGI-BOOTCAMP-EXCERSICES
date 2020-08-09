import datetime

logged_in_user = " "

#method to register new user
def register():
    username = input("Please register a username: ")
    password = input("Please register a password: ")
    print("_____________________________________")
    file = open("user.txt", "a")
    file.write(username)
    file.write(", ")
    file.write(password)
    file.write("\n")
    file.close()
    print("You are now Registered...")
    print("__________________________________")

def login():
    login_status = False
    while login_status == False:
        #login == to false run
        username = input("Please login with your username")
        password = input("Please login with your password")
        for line in open("user.txt", "r").readlines():
            login_info =line.split(",")#where there is a split login info is an array
            if username == login_info[0].strip() and password == login_info[1].strip():#use strip to remove white lines
                print("correct login.")
                global logged_in_user # we are trying to assign a vakue to the global variable

                logged_in_user = username
                if(username.strip() == "admin"): # we need to check that the user is admin or not if not give them a normal menu if it is a admin we will give him the admin user
                    adminmenu()
                    view_my_tasks()
                    view_all_tasks()
                else: 
                    menu() 
                login_status = True# if login == to true goes to menu
                break
            else:
                
                login_status = False
                # if reurn false was here it was going to Login()
        if(login_status == False):
            print("Incorrect login.")
            # no need to check for true cause we will redirect to the menu if it is true.


def add_task():
 task_user = input("enter task's user:")
 task_title = input("write task's title")
 task_description = input("add the task's description:")
 date_assigned = datetime.datetime.now().strftime("%d %B %Y")
 due_date = input("what is the due date ")
 task_completed = ("NO")
 file = open("tasks.txt", "a")
 file.write("\n" + task_user + "," + task_title + "," + task_description + "," + date_assigned + "," + due_date + "," + task_completed)
 file.close()
 print("task added")



def view_my_tasks():
     for line in open("tasks.txt", "r").readlines():
            
            task_info =line.split(",")
            print(task_info[0].strip() + " " + logged_in_user.strip())# checkin what it is comparing
            
            if task_info[0].strip() == logged_in_user.strip():
                print("Task: "+ task_info[1] + "\nAssigned to: " + task_info[0] + "\nTask description: " + task_info[2]+ "\nDate assigned: " + task_info[3] + "\nDue date: " +task_info[4] + "\nTask Complete: " + task_info[5])  
            
def view_all_tasks():
    for line in open("tasks.txt", "r").readlines():
            
            task_info =line.split(",")
            print("Task: "+ task_info[1] + "\nAssigned to: " + task_info[0] + "\nTask description: " + task_info[2]+ "\nDate assigned: " + task_info[3] + "\nDue date: " +task_info[4] + "\nTask Complete: " + task_info[5])  
            

    print("view my tasks") 


def menu(): # this menu is for users that are not admin
    
    task = ""#defining the variable to use when asking the person what to so.

    while task != "e":#using the while loop to ask the person what they want to do, until they select to stop.
        task = input("""Please select one of the following options:\n
                     a - add task\n
                     va - view all tasks\n
                     vm - view my tasks\n
                     e - exit """)
        if(task == "a"):
            add_task()
        elif(task == "va"):
            view_all_tasks()
        elif(task == "vm"):
            view_my_tasks()

def adminmenu():

    task = ""#defining the variable to use when asking the person what to do.
            
    while task != "e":#using the while loop to ask the person what they want to do, until they select to stop.
        userCount = 0 #we need to count the number of users.
        taskCount = 0 #we need to count the number of task.
        for taskline in open("tasks.txt", "r").readlines():
             taskCount += 1; # this loop is to count how many lines are in the task file and we will have the number of tasks
        for userline in open("user.txt", "r").readlines():
             userCount += 1; # this loop is to count how many lines are in the user file and we will have the number of users
        task = input("Number of task: " + str(taskCount) + "\nNumber of users: " + str(userCount) +
                     """\nPlease select one of the following options:\n
                     r - register\n
                     a - add task\n
                     va - view all tasks\n
                     vm - view my tasks\n
                     e - exit\n """)
        if(task == "r"):
            register()
        elif(task == "a"):
            add_task()
        elif(task == "va"):
            view_all_tasks()
        elif(task == "vm"):
            view_my_tasks()
            

register()
login()
