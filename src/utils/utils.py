from enum import Enum


class Category(Enum):
    WORK = "Работа"
    PERSONAL = "Личное"
    EDUCATION = "Обучение"


class Priority(Enum):
    HIGH = "Высокий"
    MEDIUM = "Средний"
    LOW = "Низкий"

class Status(Enum):
    COMPLETED = "Выполнена"
    NOT_COMPLETED = "Не выполнена"