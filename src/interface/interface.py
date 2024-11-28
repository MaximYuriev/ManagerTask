from datetime import datetime
import time

from models.manager import TaskManager
from models.task import Task
from utils.utils import Category, Priority, Status


class ConsoleInterface:
    run = True

    @classmethod
    def start(cls):
        print("-" * 100)
        time.sleep(1)
        print("Что Вы хотите сделать?\n"
              "1. Просмотреть задачи\n"
              "2. Добавить задачу\n"
              "3. Изменить задачу\n"
              "4. Удалить задачу\n"
              "5. Найти задачи\n"
              "6. Завершить работу программы")
        choice = input("Ваше действие: ")
        print("-" * 100)
        if choice == '1':
            cls.get_tasks()
        elif choice == '2':
            cls.add_task()
        elif choice == '3':
            cls.update_task()
        elif choice == '4':
            cls.delete_task()
        elif choice == '5':
            cls.find_task()
        elif choice == '6':
            print("Завершаю работу программы!")
            cls.run = False
        else:
            print(f"Ошибка! Некорректный ввод! Вы ввели {choice}, а ожидалась цифра от 1 до 6!")

    @classmethod
    def add_task(cls):
        try:
            category_enums = {
                '1': Category.WORK,
                '2': Category.PERSONAL,
                '3': Category.EDUCATION
            }
            priority_enums = {
                '1': Priority.HIGH,
                '2': Priority.MEDIUM,
                '3': Priority.LOW
            }
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            category_choice = input("Выберите категорию:\n"
                                    "1. Работа\n2. Личное\n3. Обучение\nВаш выбор: ")
            category = category_enums[category_choice]
            due_date_str = input("Введите дату (формат ввода даты Год-Месяц-День): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            priority_choice = input("Укажите приоритет задачи:\n"
                                    "1. Высокий\n2. Средний\n3. Низкий\nВаш выбор: ")
            priority = priority_enums[priority_choice]

            task = Task(
                title=title,
                description=description,
                category=category,
                due_date=due_date,
                priority=priority
            )
            TaskManager().add_task(task)
            print("Задача успешно добавлена")
        except KeyError:
            print("Ошибка! Ожидалась цифра от 1 до 3")
        except ValueError:
            print("Неверный формат даты!")

    @classmethod
    def get_tasks(cls):
        print("Выберите:\n"
              "1. Просмотр текущих задач\n"
              "2. Просмотр задач по категориям")
        choice_get_tasks = input("Ваш выбор: ")
        if choice_get_tasks == '1':
            print(TaskManager.get_all())
        elif choice_get_tasks == '2':
            category_enums = {
                '1': Category.WORK,
                '2': Category.PERSONAL,
                '3': Category.EDUCATION
            }
            category_choice = input("Выберите категорию:\n"
                                    "1. Работа\n2. Личное\n3. Обучение\nВаш выбор: ")
            try:
                category = category_enums[category_choice]
                print(TaskManager.get_by_params(category=category.value))
            except KeyError:
                print("Ошибка! Ожидалась цифра от 1 до 3")
        else:
            print(f"Ошибка! Некорректный ввод! Вы ввели {choice_get_tasks}, а ожидалась цифра от 1 до 2!")

    @classmethod
    def find_task_by_id(cls):
        try:
            input_id = input("Введите id задачи: ")
            task_id = int(input_id)
            return TaskManager.get_by_id(task_id)
        except ValueError:
            print(f'Ожидалось целочисленное значение! Вы ввели {input_id}')

    @classmethod
    def delete_task(cls):
        task = cls.find_task_by_id()
        if task is None:
            print("Задача не найдена!")
            return
        TaskManager.delete_task(task)
        print("Задача успешно удалена!")

    @classmethod
    def find_task(cls):
        print("Выберите критерии поиска:\n"
              "1. Поиск по ключевым словам\n"
              "2. Поиск по категории\n"
              "3. Поиск по статусу выполнения")
        choice_find_task = input("Ваш выбор: ")
        if choice_find_task == '1':
            word = input("Введите слово: ")
            print(TaskManager.get_by_keyword(word))
        elif choice_find_task == '2':
            category_enums = {
                '1': Category.WORK,
                '2': Category.PERSONAL,
                '3': Category.EDUCATION
            }
            category_choice = input("Выберите категорию:\n"
                                    "1. Работа\n2. Личное\n3. Обучение\nВаш выбор: ")
            try:
                category = category_enums[category_choice]
                print(TaskManager.get_by_params(category=category.value))
            except KeyError:
                print("Ошибка! Ожидалась цифра от 1 до 3")
        elif choice_find_task == '3':
            status_enums = {
                '1': Status.COMPLETED,
                '2': Status.NOT_COMPLETED,
            }
            status_choice = input("Укажите статус выполнения:\n"
                                  "1. Задача выполнена\n2. Задача не выполнена\nВаш выбор: ")
            try:
                status = status_enums[status_choice]
                print(TaskManager.get_by_params(status=status.value))
            except KeyError:
                print("Ошибка! Ожидалась цифра от 1 до 2")
        else:
            print(f"Ошибка! Некорректный ввод! Вы ввели {choice_find_task}, а ожидалась цифра от 1 до 3!")

    @classmethod
    def update_task(cls):
        task = cls.find_task_by_id()
        if task is None:
            print("Задача не найдена!")
            return
        update_data = {}
        print("Выберите, что вы хотите изменить:\n"
              "1. Название задачи\n"
              "2. Описание задачи\n"
              "3. Категорию задачи\n"
              "4. Дату задачи\n"
              "5. Приоритет задачи\n"
              "6. Статус задачи")
        choice_update_params = (
            input("Ваш выбор (в случае множественного выбора используйте пробел в качестве разделителя): ")
        )
        if not choice_update_params:
            print("Список параметров не может быть пустым!")
            return
        set_update_params = set(choice_update_params.split(" "))
        try:
            for param in set_update_params:
                if param == '1':
                    title = input("Введите название задачи: ")
                    update_data.update(title=title)
                elif param == '2':
                    description = input("Введите описание задачи: ")
                    update_data.update(description=description)
                elif param == '3':
                    category_enums = {
                        '1': Category.WORK,
                        '2': Category.PERSONAL,
                        '3': Category.EDUCATION
                    }
                    category_choice = input("Выберите категорию:\n"
                                            "1. Работа\n2. Личное\n3. Обучение\nВаш выбор: ")
                    category = category_enums[category_choice]
                    update_data.update(category=category.value)
                elif param == '4':
                    upd_due_date_str = input("Введите дату (формат ввода даты Год-Месяц-День): ")
                    due_date = datetime.strptime(upd_due_date_str, "%Y-%m-%d").date()
                    update_data.update(due_date=due_date)
                elif param == '5':
                    status_enums = {
                        '1': Status.COMPLETED,
                        '2': Status.NOT_COMPLETED,
                    }
                    status_choice = input("Укажите статус выполнения:\n"
                                          "1. Задача выполнена\n2. Задача не выполнена\nВаш выбор: ")
                    status = status_enums[status_choice]
                    update_data.update(status=status.value)
                elif param == '6':
                    priority_enums = {
                        '1': Priority.HIGH,
                        '2': Priority.MEDIUM,
                        '3': Priority.LOW
                    }
                    priority_choice = input("Укажите приоритет задачи:\n"
                                            "1. Высокий\n2. Средний\n3. Низкий\nВаш выбор: ")
                    priority = priority_enums[priority_choice]
                    update_data.update(priority=priority.value)
                else:
                    print("Ошибка! Ожидалась цифра от 1 до 6")
                    return
            TaskManager.update_task(task, update_data)
            print("Задача успешно изменена!")
        except KeyError:
            print("Ошибка! Ожидалась цифра от 1 до 3")
        except ValueError:
            print("Неверный формат даты!")
