def greeting():
    print("Hello 'Выберите действие: 1 - калькуляторб 2 - ковертер'")
    select = int(input())
    return select

def get_math_example():
    primer = input('Введите выражение: ')
    return primer

def view_result(result):
    print("Результат = ", result)

def get_massa():
    massa = input('Введите массу в кг: ')
    return massa
