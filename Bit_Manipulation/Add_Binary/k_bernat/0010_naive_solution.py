def add_binary(a: str, b: str) -> str:
    # Преобразуем бинарные строки в десятичные числа
    sum_decimal = int(a, 2) + int(b, 2)
    # Преобразуем сумму обратно в бинарную строку и удаляем префикс '0b'
    return bin(sum_decimal)[2:]

# Пример использования
a = "1010"
b = "1101"
result = add_binary(a, b)
print(result)