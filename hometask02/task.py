def to_hex(num):
    return hex(num)[2:] 

num = 255
hex_str = to_hex(num)
print(hex_str)  # 'ff'
print(hex(num))  # '0xff'

from fractions import Fraction

def add_and_multiply_fractions(fraction1, fraction2):
    # преобразуем строки с дробями в объекты Fraction
    numerator1, denominator1 = fraction1.split('/')
    numerator2, denominator2 = fraction2.split('/')
    fraction1 = Fraction(int(numerator1), int(denominator1))
    fraction2 = Fraction(int(numerator2), int(denominator2))
    
    # вычисляем сумму и произведение дробей
    sum_fraction = fraction1 + fraction2
    multiply_fraction = fraction1 * fraction2
    
    # возвращаем результаты в виде строк
    return str(sum_fraction), str(multiply_fraction)

# пример использования
fraction1 = '1/2'
fraction2 = '3/4'
sum_fraction, multiply_fraction = add_and_multiply_fractions(fraction1, fraction2)
print(sum_fraction)  # '5/4'
print(multiply_fraction)  # '3/8'