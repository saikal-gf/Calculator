def calculator():
    print("Простой калькулятор")
    print("Доступные операции: +  -  *  /  **  %")

    while True:
        try:
            num1 = float(input("Введите первое число: "))
            op = input("Операция (+, -, *, /, **, %): ")
            num2 = float(input("Введите второе число: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            elif op == '**':
                result = num1 ** num2
            elif op == '%':
                result = num1 % num2
            else:
                print("Неверная операция.")
                continue

            print(f"Результат: {result}")

        except ZeroDivisionError:
            print("Ошибка: Деление на ноль.")
        except ValueError:
            print("Ошибка: Введите правильное число.")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

        again = input("Хотите продолжить? (да/нет): ").lower()
        if again != "да":
            print("Выход из калькулятора.")
            break

calculator()

