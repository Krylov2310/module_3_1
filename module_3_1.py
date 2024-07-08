task = 'Домашняя работа по уроку "Пространство имён"'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
# Функция count_calls изменяет в ней значение переменной calls.
calls = 0


def count_calls():
    global calls
    calls +=1
    return


# Функция string_info с параметром string и реализует логику работы по описанию
def string_info(string):
    count_calls()
    #print(string)
    return len(string), string.upper(), string.lower()


# Вызвает соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    if string in list_to_search:
        #print(string,',', list_to_search)
        return True
    else:
        #print(string,',', list_to_search)
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
print()
print(thanks)