import random
from dictionary import verbs

def check_answers(verb_forms):
    attempts = 3
    for i, form in enumerate(['вторую форму', 'третью форму']):
        user_input = input(f"Введите {form} для глагола '{verb_forms[0]}': ").strip()
        if user_input.lower() == verb_forms[i + 1].lower():
            print("Верно!")
        else:#1
            attempts -= 1
            print(f"Неверно. Осталось попыток: {attempts}")
            if attempts == 0:
                print(f"Вы проиграли! Правильные формы: {verb_forms[:3]} ({verb_forms[3]})")
                return False
    print(f"Поздравляю! Вы правильно ввели все формы: {verb_forms[:3]} ({verb_forms[3]})")
    return True

def mode_1():
    print("Режим 1: Слова по порядку из словаря")
    for verb in verbs:
        print(f"Подсказка: перевод глагола - '{verb[3]}'.")
        if not check_answers(verb):
            break

def mode_2():
    print("Режим 2: Слова в случайном порядке")
    random_verbs = verbs.copy()
    random.shuffle(random_verbs)
    for verb in random_verbs:
        print(f"Подсказка: перевод глагола - '{verb[3]}'.")
        if not check_answers(verb):
            break

def mode_3():
    print("Режим 3: Перевод на русском, введите все 3 формы глагола")
    random_verbs = verbs.copy()
    random.shuffle(random_verbs)
    correct_count = 0
    incorrect_count = 0
    for verb in random_verbs:
        print(f"Слово: - '{verb[3]}'.")
        user_input = input("Введите три формы глагола через пробел: ").strip().split()
        if len(user_input) == 3 and all(user_input[i].lower() == verb[i].lower() for i in range(3)):
            print("+")
            correct_count += 1
        else:
            print(f"Неверно. Правильные формы: {verb[:3]} ({verb[3]})")
            incorrect_count += 1
    print(f"Конец. Верных ответов: {correct_count}, неверных ответов: {incorrect_count}.")

if __name__ == "__main__":
    while True:
        print("Выберите режим игры:")
        print("1 - Слова подряд из словаря")
        print("2 - Слова в случайном порядке")
        print("3 - Перевод на русском, введите три формы")
        try:
            mode = int(input("Введите номер режима: ").strip())
            if mode == 1:
                mode_1()
            elif mode == 2:
                mode_2()
            elif mode == 3:
                mode_3()
            else:
                print("Некорректный номер режима. Попробуйте ещё раз.")
                continue
        except ValueError:
            print("Пожалуйста, введите число.")
            continue

        play_again = input("Хотите сыграть ещё раз? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Спасибо за игру!")
            break
