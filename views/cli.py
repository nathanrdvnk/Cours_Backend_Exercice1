class CLI:
    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("\nAucune tâche.")
        else:
            print("\nListe des tâches :")
            for t in tasks:
                print("-", t)

    @staticmethod
    def task_added(task):
        print(f"\nTâche ajoutée : {task.title}")
