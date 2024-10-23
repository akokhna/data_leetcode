def add_binary(a: str, b: str) -> str:
	"""
    Принимает два двоичных числа в виде строк и возвращает их сумму в виде двоичной строки.

    :param a: Первое двоичное число в виде строки.
    :param b: Второе двоичное число в виде строки.
    :return: Сумма двух двоичных чисел в виде строки.
    """
	max_length = max(len(a), len(b))
	
	# Выравниваем длины строк, добавляя ведущие нули
	a = a.zfill(max_length)
	b = b.zfill(max_length)
	
	carry = 0
	result = []
	
	# Выполняем сложение побитно справа налево
	for i in range(max_length - 1, -1, -1):
		bit_sum = carry
		bit_sum += 1 if a[i] == '1' else 0
		bit_sum += 1 if b[i] == '1' else 0
		
		# Результирующий бит
		result.append('1' if bit_sum % 2 == 1 else '0')
		
		# Перенос на следующий разряд
		carry = 0 if bit_sum < 2 else 1
	
	# Если остался перенос на старший разряд
	if carry != 0:
		result.append('1')
	
	# Объединяем и реверсируем результат
	result.reverse()
	return ''.join(result)


# Пример использования
a = "1010"
b = "1101"
result = add_binary(a, b)
print(result)  # ожидаемый результат: "10111"
