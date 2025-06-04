June 2, 2025
# BaranggayTaskManager
Dastruct Final project.
This application allows for submission of suggestions for baranggay projects. 
It also allows for voting which project should be prioritized first

Implements a list implementation of a priority queue or heap queue

--------------------------------------------------------------------------------

June 6, 2025
Created classes Task and Task Manager.

Task:
Attributes
taskName - the suggested task
votes    - number of votes (set to 0 by default)

TaskManager:
Attributes
listOfTasks(heap)     - heap to store the tasks in
dictionary(dict)      - dictionary for fast updates when vote()

Methods
suggest()             - add task to the list
vote()                - update the task.vote attribute
done()                - remove the task with most votes
showList()            - display the list in order of priority
_heapify()            - reorganizes the heap so the highest vote is the top
