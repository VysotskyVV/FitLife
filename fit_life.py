# Проект FitLife - MVP версия 1.0
import sys

# Принудительно ставим UTF-8 для вывода в Windows, чтобы не падали тесты
# в этом помог ИИ
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

print('Приветствую! Меня зовут FitLife. Я Ваш фитнес помощник')
print()  # пустая строка
WATER_PER_KG = 30  # константа для расчётов нормы воды
ML_IN_LITER = 1000  # константа для перевода миллилитров в литры


user_name = input('Напишите Ваше имя: ')
user_name = user_name.title()  # делаем красивое имя с заглавной первой буквой

while True:  # цикл для проверки верного ввода возраста
    try:
        user_age = input('Напишите Ваш возраст: ')
        user_age = int(user_age)
        break
    except ValueError:
        print('Ошибка: нужно ввести целое число!')


while True:  # цикл проверки верного ввода массы
    try:
        user_weight = input('Напишите Ваш вес в кг: ')
        user_weight = float(user_weight)
        break
    except ValueError:
        print('Ошибка: нужно ввести вес в кг, используя точку: например 41.2')

while True:  # цикл для проверки верного ввода роста
    try:
        user_height = input('Напишите Ваш рост в метрах (например 1.75): ')
        user_height = float(user_height)
        break
    except ValueError:
        print('Ошибка: нужно ввести рост в метрах, используя точку:', end=' ')
        print('например 1.75')  # перенос, чтобы уложиться в длину строки


bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)


water_needed = user_weight * WATER_PER_KG / ML_IN_LITER


print()  # пустая строка
print(f'Привет, {user_name}!')
print(f'Ваш возраст: {user_age} г.')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed:.1f} л. в день')
print()  # пустая строка
print("Расчет окончен. Будьте здоровы!")
