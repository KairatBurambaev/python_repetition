total_cash = 0
transactions = []

def add(total_cash, transactions):
    add = int(input('Внесите сумму кратную 50: '))
    if add % 50 == 0:
        total_cash += add
        transactions.append(('внесенно', add))
    else:
        print('неверная сумма')
    return total_cash, transactions

def take(total_cash, transactions):
    take = int(input(f'Введите сумму кратную 50, но не превышающую {total_cash}): '))
    if take % 50 == 0:
        percent = take * 1.5 * 0.01
        if percent < 30:
            percent = 30
        elif percent > 600:
            percent = 600

        if total_cash < (take + percent):
            print('недостаточно средств')
        else:
            total_cash -= (take + percent)
            transactions.append(('снятие', take))
    else:
        print('неверная сумма')
    return total_cash, transactions

def exit_program():
    print('выход из программы')
    quit()

def process_operation(total_cash, transactions):
    while True:

        if total_cash > 5000000:
            total_cash *= 0.9
        print(f'Сумма на счету: {total_cash}')

        print('1 - внести')
        print('2 - снять')
        print('0 - выйти')

        action = input('Введите номер действия: ')

        if action == '1':
            total_cash, transactions = add(total_cash, transactions)
        elif action == '2':
            total_cash, transactions = take(total_cash, transactions)
        elif action == '0':
            exit_program()
        else:
            print('неверная команда')

        if len(transactions) % 3 == 0:
            total_cash *= 1.03

process_operation(total_cash, transactions)