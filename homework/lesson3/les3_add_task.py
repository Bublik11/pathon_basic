def read_int(is_positive=False, is_negative=False, add_message="") -> int:
    """
    Позволяет вводить пользователю целое число. Есть проверка на ошибки.

    :param is_positive: bool: необходимо ввести не отрицательное число;
    :param is_negative: bool: необходимо ввести не положительное число;
    :param add_message: str: дополнительное сообщение пользователю.
    :return: int.
    """
    message = "Введите "
    if is_negative != is_positive:
        if is_positive:
            message += "не отрицательное "
        else:
            message += "не положительное "
    message += f"целое число ({add_message}):\n>>>"
    while True:
        result = input(message)
        try:
            result = int(result)
        except ValueError:
            print("Ошибка: введено не целое число")
        else:
            if is_negative != is_positive:
                if is_positive and result < 0:
                    print("Ошибка: введено отрицательное число")
                elif is_negative and result > 0:
                    print("Ошибка: введено положительное число")
                else:
                    break
            else:
                break
    return result


def read_float(is_positive=False, is_negative=False, add_message="") -> float:
    """
    Позволяет вводить пользователю дробное число. Есть проверка на ошибки.

    :param is_positive: bool: необходимо ввести не отрицательное число;
    :param is_negative: bool: необходимо ввести не положительное число;
    :param add_message: str: дополнительное сообщение пользователю.
    :return: float.
    """
    message = "Введите "
    if is_negative != is_positive:
        if is_positive:
            message += "не отрицательное "
        else:
            message += "не положительное "
    message += f"число ({add_message}):\n>>>"
    while True:
        result = input(message)
        try:
            result = float(result)
        except ValueError:
            print("Ошибка: введено не число")
        else:
            if is_negative != is_positive:
                if is_positive and result < 0:
                    print("Ошибка: введено отрицательное число")
                elif is_negative and result > 0:
                    print("Ошибка: введено положительное число")
                else:
                    break
            else:
                break
    return result


def my_map(funk, iter_obj):
    for item in iter_obj:
        yield funk(item)


def my_enumerate(*args, **kwargs):
    iter_obj = iter(*args) if args else iter(**kwargs)
    i = kwargs["start"] if kwargs.get("start") else 0
    while True:
        try:
            temp_tuple = (i, next(iter_obj))
            yield temp_tuple
        except StopIteration:
            break
        else:
            i += 1


def my_sum(*args, **kwargs):
    iter_obj = iter(*args) if args else iter(**kwargs)
    result = kwargs["start"] if kwargs.get("start") else 0
    while True:
        try:
            temp = next(iter_obj)
            result += temp
        except StopIteration:
            break
    return result


def my_min(*args, **kwargs):
    iter_obj = iter(*args) if args else iter(**kwargs)
    result = next(iter_obj)
    while True:
        try:
            temp = next(iter_obj)
            if temp < result:
                result = temp
        except StopIteration:
            break
    return result


def my_max(*args, **kwargs):
    iter_obj = iter(*args) if args else iter(**kwargs)
    result = next(iter_obj)
    while True:
        try:
            temp = next(iter_obj)
            if temp > result:
                result = temp
        except StopIteration:
            break
    return result


def my_len(*args, **kwargs):
    iter_obj = iter(*args) if args else iter(**kwargs)
    result = 0
    while True:
        try:
            next(iter_obj)
        except StopIteration:
            break
        else:
            result += 1
    return result


def my_reduce(function, iter_obj, initializer=None):
    if initializer is None:
        iter_obj = iter(iter_obj)
        temp = next(iter_obj)
        return my_reduce(function, iter_obj, function(temp, next(iter_obj)))
    else:
        try:
            temp = next(iter_obj)
            return my_reduce(function, iter_obj, function(temp, initializer))
        except StopIteration:
            return initializer


def my_filter(function, iterable):
    for i in iterable:
        if function(i):
            yield i


def my_zip(*args):
    if args:
        iter_obj = [iter(el) for el in args]
        while True:
            temp_list = []
            try:
                for i in iter_obj:
                    temp_list.append(next(i))
            except StopIteration:
                break
            else:
                yield tuple(temp_list)
