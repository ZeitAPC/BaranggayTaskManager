from Task import *

class TaskManager:
    def __init__(self):
        self.listOfTasks = []  # Where the heap will be stored
        self.dictionary = {}  # Where the task name and the task object will be stored

    def _heapify(self):
        pass

    def suggest(self, suggestion):
        entryNumber = len(self.dictionary) + 1
        newSuggestion = Task(entryNumber, suggestion)
        self.listOfTasks.append(newSuggestion)
        self.dictionary[entryNumber] = newSuggestion
        self._heapify()

    def vote(self, taskNumber):
        self.dictionary[taskNumber].votes +=1
        self._heapify()

    def isEmpty(self):
        length = len(self.listOfTasks)
        if length == 0:
            return True
        return False

    def done(self):
        finishedTask = self.listOfTasks[0]
        print(finishedTask.task, "is finished")
        self.listOfTasks.remove(finishedTask)
        self.dictionary.pop(finishedTask.taskID)

    def showList(self):
        if self.isEmpty():
            print("There are no pending tasks")
            return None
        # for i in self.listOfTasks:
        #     print(f"{i.taskID}: {i.task} | Votes: {i.votes}")
        longest = 0
        for i in self.listOfTasks:
            checkLen = len(i.task)
            if checkLen > longest:
                longest = checkLen
        longest +=3
        print("ID".ljust(8), "Task".ljust(longest), "Votes".ljust(longest+5))
        for k in self.listOfTasks:
            print("{:<8} {:<{taskWidth}} {:<12}".format(k.taskID, k.task, k.votes, taskWidth=longest, voteWidth=longest+5))
        print(self.dictionary)
        # https://stackoverflow.com/questions/17330139/python-printing-a-dictionary-as-a-horizontal-table-with-headers
        # https://www.w3schools.com/python/ref_string_format.asp