import inspect


def strict(func):
    """
    Декоратор для проверки соответствия типов аргументов аннотациям функции.
    """
    def wrapper(*args, **kwargs):
        """Wrapper, проверяющий типы перед вызовом функции."""
        signature = inspect.signature(func)
        bound = signature.bind(*args, **kwargs)

        for name, value in bound.arguments.items():
            exp_type = signature.parameters[name].annotation
            if exp_type is inspect.Parameter.empty:
                continue

            if not isinstance(value, exp_type):
                raise TypeError(
                    f"Аргумент {name} должен соответствовать типу "
                    f"{exp_type.__name__}, получен некорректный аргумент "
                    f"{type(value).__name__}."
                )

        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    """Проверочная функция, возвращающая сумму двух чисел"""
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
