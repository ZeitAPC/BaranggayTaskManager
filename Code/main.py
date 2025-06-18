from TaskManager import *

taskmanager = TaskManager() #Instantiates the Task Manager
print("-" * 6, "Suggestion period started", "-" * 6)
while True:
    suggestion = str(input("Enter suggestion (enter \"STOP\" to end suggestion period): ")).strip()     # Prompts user for suggestion
    if len(suggestion) == 0:                                                                            # Checks if input is empty
        print("Invalid input: No suggestion entered.")
        continue
    if suggestion.lower() == "stop" and taskmanager.isEmpty():                                          # Checks if user wants to stop without entering anything
        verify = str(input("Warning: List will be empty, proceed? (Y/N): "))                            # Prompts the user for confirmation
        if verify.upper() == "Y":                                                                       # If user wants to end suggestion period
            print("-" * 6, "Suggestion period concluded", "-" * 6)
            break
        elif verify.upper() == "N":                                                                     # If user doesn't to end suggestion period
            continue
    elif suggestion.lower() == "stop":                                                                  # If user wants to end suggestion period
        print("-" * 6, "Suggestion period concluded", "-" * 6)
        break
    taskmanager.suggest(suggestion)                                                                     # Adds suggestion to the task manager

if taskmanager.isEmpty():                                                   # Checks if task manager is empty
    print("Suggestion period concluded with no task being suggested. "      # Skips the voting and completion period if
          "Voting and completion period will be skipped.")                  # task manager is empty
else:
    print("-" * 6, "Voting period start", "-" * 6)
    while True:
        taskmanager.showList()                                                  # Displays the task manager contents
        voteATask = str(input("Enter task ID (enter 0 to end voting period): "))# Asks for taskID of the task to vote
        if voteATask == "0":                                                    # Checks if user wants to end voting
            print("-" * 6, "Voting period concluded", "-" * 6)
            break
        elif not voteATask.isdigit():                                           # Checks if input is not a number
            print("Invalid input: enter a number\n")
            continue
        taskmanager.vote(int(voteATask))                                        # Adds vote if input is a number

    taskmanager.finalize()                                                      # Sorts the task manager after the voting
    taskmanager.showList()                                                      # Shows the task manager content

    print("-" * 6, "Completion period start", "-" * 6)
    while not taskmanager.isEmpty():                                                        # Checks if there are tasks in task manager
        isDone = str(input(f"Is {taskmanager.peek()} finished? (Y/N): ")).strip().lower()   # Asks if top priority is finished
        if isDone == "y":                                                                   # Checks if yes
            taskmanager.done()
        elif isDone == "n":                                                                 # Checks if no
            print(f"Please focus on completing {taskmanager.peek()}")
        else:
            print("Invalid input, please enter \"Y\" for Yes and \"N\" for No")             # Error message if input is not valid
        taskmanager.showList()
