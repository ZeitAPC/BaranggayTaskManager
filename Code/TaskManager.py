from Task import *

class TaskManager:
    def __init__(self):
        self.listOfTasks = []      # Where the task instance will be stored
        self.dictionary = {}       # Where the taskID and the task instance will be stored
        self.normalizedSet = set() # To check for duplication

    def suggest(self, suggestion):                                      # Time complexity: O(1)
        normalized = suggestion.strip().lower()
        if normalized in self.normalizedSet:                            # Loop over the list
            print(f"Duplicate suggestion ignored: '{suggestion}'\n")    # Return if normalized is found
            return
        # If not found
        entryNumber = len(self.dictionary) + 1                          # Calculate taskID
        newSuggestion = Task(entryNumber, suggestion)                   # Create new task instance
        self.listOfTasks.append(newSuggestion)                          # Add task object to list
        self.dictionary[entryNumber] = newSuggestion                    # Add task object with id to dictionary
        self.normalizedSet.add(normalized)                              # Add normalized task name to set

    def vote(self, taskNumber):                                             # Time complexity: O(1) on average
        if taskNumber not in self.dictionary:                               # Uses taskID to look up key in dictionary
            print("Invalid input: Task not found \n")
            return
        self.dictionary[taskNumber].votes +=1                                   # Increments vote of specified task
        print(f"Successfully voted for {self.dictionary[taskNumber].task} \n")

    def isEmpty(self):                                                  # Time complexity: O(1)
        return len(self.listOfTasks) == 0                               # Return False if something is on list

    def size(self):                                                     # Time complexity: O(1)
        return len(self.listOfTasks)                                    # Return the length of list

    def done(self):                                                     # Time complexity: O(N)
        finishedTask = self.listOfTasks.pop(0)                          # Removes top task and stores the output
        print(finishedTask.task, "is finished")                         # Displays task is done message
        self.dictionary.pop(finishedTask.taskID)                        # Updates the dictionary
        self.normalizedSet.remove(finishedTask.task.strip().lower())    # Updates the set

    def showList(self):
        if self.isEmpty():                                                      # Checks if list is empty
            print("There are no pending tasks")
            return None
        longest = 0                                                             # instantiate longest
        for i in self.listOfTasks:                                              # Loops over list
            checkLen = len(i.task)                                              # Checks the length of each task
            if checkLen > longest:                                              # If current task is longer
                longest = checkLen                                              # Assigns it as longest
        longest +=3                                                             # Readjusts it for padding
        print("ID".ljust(8), "Task".ljust(longest), "Votes".ljust(longest+5))   # Formats the title of the table
        for k in self.listOfTasks:                                              # Loops over the list for printing table
            print("{:<8} {:<{taskWidth}} {:<{voteWidth}}"                       # Formats each column of the table
                  .format(k.taskID, k.task, k.votes,                      # assigns attributes taskID, task, votes
                                                                                # to first, second and third columns
                          taskWidth=longest, voteWidth=longest+5))              # assigns the width to task and vote column
        print("")

    def finalize(self):
        self.listOfTasks.sort(key=lambda obj: obj.votes, reverse=True)          # sorts the list in descending order

    def peek(self):
        if self.size() != 0:                                                    # Checks if the list is not empty
            return self.listOfTasks[0].task                                     # Returns the first element
        return "No pending projects"

    # https://stackoverflow.com/questions/17330139/python-printing-a-dictionary-as-a-horizontal-table-with-headers
    # https://www.w3schools.com/python/ref_string_format.asp
