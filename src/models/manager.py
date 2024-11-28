from models.task import Task


class TaskManager:
    tasks: list[Task] = []

    @classmethod
    def add_task(cls, task: Task):
        cls.tasks.append(task)

    @classmethod
    def get_all(cls) -> list[Task]:
        return cls.tasks

    @classmethod
    def get_by_id(cls, task_id: int) -> Task | None:
        for task in cls.tasks:
            if task.id == task_id:
                return task

    @classmethod
    def get_by_params(cls, **kwargs) -> list[Task]:
        found_tasks = []
        for task in cls.tasks:
            task_dict = task.__dict__
            for key, value in kwargs.items():
                if task_dict[key] == value:
                    found_tasks.append(task)
                    break
        return found_tasks

    @classmethod
    def get_by_keyword(cls, word: str):
        found_tasks = []
        for task in cls.tasks:
            if word in task.title or word in task.description:
                found_tasks.append(task)
        return found_tasks

    @classmethod
    def update_task(cls, task: Task, update_task_data: dict) -> Task:
        for key, value in update_task_data.items():
            setattr(task, key, value)
        return task

    @classmethod
    def delete_task(cls, task: Task):
        cls.tasks.remove(task)
