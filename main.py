from controllers.task_controller import TaskController

def main():
    controller = TaskController()

    while True:
        print("\nMenu")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Afficher les tâches")
        print("4. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            titre = input("\nEntrez le titre de la tâche : ")
            controller.add(titre)

        elif choix == "2":
            titre = input("\nEntrez le titre de la tâche à supprimer : ")
            controller.delete(titre)

        elif choix == "3":
            controller.display()

        elif choix == "4":
            print("A bientôt")
            break

        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
