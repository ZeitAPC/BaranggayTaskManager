from TaskManager import *
import time

class FilteredTaskManager:
    def __init__(self):
        self.task_manager = TaskManager()
        self.suggestions_set = set()

    def suggest(self, suggestion):
        normalized = suggestion.strip().lower()
        if normalized in self.suggestions_set:
            print(f"Duplicate suggestion ignored: '{suggestion}'")
        else:
            self.suggestions_set.add(normalized)
            self.task_manager.suggest(suggestion)

    def vote(self, task_id):
        self.task_manager.vote(task_id)

    def showList(self):
        self.task_manager.showList()

    def size(self):
        return self.task_manager.size()
    
pendingProjects = FilteredTaskManager()

def suggestionPeriod():
    suggestionPeriod = int(input("Continue voting period?: (1:Yes/2: No) "))
    while suggestionPeriod != 1 and suggestionPeriod !=2:
        print("Invalid input, please try again")
        suggestionPeriod = int(input("Continue voting period?: (1:Yes/2: No) "))
    if suggestionPeriod == 2:
        return False
    return True

def votingPeriod():
    votingPeriod = int(input("Continue voting? (1:Y/2:N): "))
    if votingPeriod == 2:
        return None

i = int(0)
print("Suggestion period, Please submit suggestions")
while True:
    suggestTask = str(input("Enter suggestion: "))
    if len(suggestTask.strip()) > 0:
        pendingProjects.suggest(suggestTask)
    else:
        print("Empty input, try again")
    pendingProjects.showList()
    i +=1
    if i == 5:
        if not suggestionPeriod():
            break
        i=0
print("--- Suggestion period over ---\n")

print("--- Voting period start ---")
i=0
while True:
    pendingProjects.showList()
    voteATask = int(input("Enter task ID: "))
    while voteATask <=0 or voteATask > pendingProjects.size():
        print("Task does not exist, try again")
        voteATask = int(input("Enter task ID: "))
        if voteATask <=pendingProjects.size() and voteATask != 0:
            break
    pendingProjects.vote(voteATask)
    i +=1
    if i == 5:
        if votingPeriod() is None:
            break
        i= 0
pendingProjects.showList()
