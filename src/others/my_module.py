from datetime import datetime


def add(x, y):
    return x + y


def divide(x: int, y: int) -> int:
    return x // y


def return_now_datetime() -> datetime:
    return datetime.now()
