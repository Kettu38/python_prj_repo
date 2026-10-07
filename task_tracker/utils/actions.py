import json

def add_task() -> None:
    command = input("Введите задачу и приоритет через запятую:\n")
    title, priority = [item.strip() for item in command.split(",")]
    save_task(title, priority)

    print(f"Обновлённый список задач:")
    view_all_tasks()
    print("\n")


def save_task(title: str, priority: str) -> None:
    with open('tasks.json', 'r') as file:
        prev_version = json.load(file)

    prev_version.append({"title": title, "priority": priority})

    with open('tasks.json', 'w') as file:
        json.dump(prev_version, file, indent=4, ensure_ascii=False)


def view_all_tasks():
    list_tasks = load_tasks()
    for n, item in enumerate(list_tasks, 1):
        print(f"{n}. {item["title"]} [{item["priority"]}]")


def remove_task():
    print("Задачи, доступные для удаления:")
    view_all_tasks()
    list_tasks = load_tasks()
    what_to_remove = int(input("Укажите номер задачи для удааления: "))
    list_tasks.pop(what_to_remove - 1)

    with open('tasks.json', 'w') as file:
        json.dump(list_tasks, file, indent=4, ensure_ascii=False)


def load_tasks() -> list:
    # os.system('clear')
    # print("\n\n")
    with open("tasks.json", "r") as f:
        list_tasks = json.load(f)
        return (list_tasks)

def show_actions() -> None:
    print("""Доступные действия:
1. Добавить задачу
2. Показать задачи
3. Удалить задачу
0. Выйти""")