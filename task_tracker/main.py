import json
import os
from utils.actions import add_task, view_all_tasks, remove_task, show_actions


if __name__ == '__main__':

    while True:
        show_actions()
        command = input("Выберите доступное действие: ")
        print()
        os.system('clear')
        match command:
            case "1":
                add_task()
                input("Введите Enter, чтобы продолжить: ")
            case "2":
                view_all_tasks()
                input("Введите Enter, чтобы продолжить: ")
            case "3":
                remove_task()
                print("\nСписок задач обновлён\n    ~~~~~")
                view_all_tasks()
                input("\nВведите Enter, чтобы продолжить: ")
            case "0":
                break
            case _:
                print("Такого действия нет, выберите другое")
        print("\n")