import datetime

from utils.utils import Category, Priority, Status


class Task:
    id = 0

    def __init__(
            self,
            title: str,
            description: str,
            category: Category,
            due_date: datetime.date,
            priority: Priority
    ):
        self.increment_id()
        self.id = Task.id
        self.title = title
        self.description = description
        self.category = category.value
        self.due_date = due_date
        self.priority = priority.value
        self.status = Status.NOT_COMPLETED.value

    def __repr__(self):
        return (f'\n{{\n'
                f'\tid: {self.id}\n'
                f'\ttitle: {self.title}\n'
                f'\tdescription: {self.description}\n'
                f'\tcategory: {self.category}\n'
                f'\tdue_date: {self.due_date}\n'
                f'\tpriority: {self.priority}\n'
                f'\tstatus: {self.status}\n'
                f'}}\n')

    @classmethod
    def increment_id(cls):
        cls.id += 1
