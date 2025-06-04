from TaskManager import *

pendingProjects = TaskManager()
#
# pendingProjects.sendSuggestion("fix streetlights")
# pendingProjects.sendSuggestion("fix roads")
# pendingProjects.showList()
# pendingProjects.vote(2)
# print("")
# pendingProjects.done()
# pendingProjects.showList()

if __name__ == "__main__":
    # Create an instance of your TaskManager
    manager = TaskManager()

    # Test task data
    test_tasks = {
        1: ("fix streetlights", 0),  # Normal, zero votes
        2: ("fix roads", 2),  # Normal, multiple votes
        3: ("build park", 3),  # Highest votes to test priority
        4: ("clean river", 1),  # Single vote
        5: ("install CCTV", 0),  # Zero votes duplicate case
        6: ("build park", 2),  # Duplicate task name, different votes
        7: ("fix roads", 0),  # Duplicate name, zero votes
        8: ("remove graffiti", 5),  # Very high votes, test top priority
        9: ("", 1),  # Empty string task name edge case
        10: ("repair bench", -1),  # Negative votes edge case (if allowed)
    }

    # Suggest tasks
    for taskID, (taskName, _) in test_tasks.items():
        manager.suggest(taskName)  # This will auto-assign the ID in your actual implementation

        # Apply votes based on ID
    for taskID, (_, voteCount) in test_tasks.items():
        for _ in range(voteCount):
            manager.vote(taskID)  # Now using ID

    print("\n--- Task List After Voting ---")
    manager.showList()

    print("\n--- Mark Top Task as Done ---")
    manager.done()

    print("\n--- Task List After Removing Top Task ---")
    manager.showList()