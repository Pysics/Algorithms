import math

def fermat_factorisation(number: int) -> int:
    _number = math.ceil(math.sqrt(number))
    __number = _number ** 2 - number
    while math.sqrt(__number) % 1 != 0:
        _number += 1
        __number = _number ** 2 - number
    square_root = int(_number - math.sqrt(__number))
    return square_root
