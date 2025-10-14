from model.task import Task
from views.cli import CLI

class TaskController:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        task = Task(title)
        self.tasks.append(task)
        CLI.task_added(task)
        return task

    def delete(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"\nTâche supprimée : {title}")
                return
        print("\nTâche pas trouvée.")

    def display(self):
        CLI.show_tasks(self.tasks)
