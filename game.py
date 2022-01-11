print('Вітаю друже')
answer=input('Готовий пограти у вікторину так/ні :')
score=0
total_questions=3

if answer.lower()=='так':
    answer=input('Питання 1: Яка улюблена мова програмування?')
    if answer.lower()=='python':
        score += 1
        print('хороший вибір')
    else:
        print('Всеодно Python краще')


    answer=input('Питання 2: Рік хрещення русі? ')
    if answer.lower()=='988':
        score += 1
        print('вірно')
    else:
        print('Не правильно( це було у 988')

    answer=input('Питання 3: Коли було проголошено незалежність України (відповідь у форматі ДД.ММ.РІК')
    if answer.lower()=='24.08.1991':
        score += 1
        print('Да ти молодець!')
    else:
        print('Зовсім поруч 24.08.1991')

print('Дякую що приділив час вікторині. Кількість правильних відповідей',score,)
mark=(score/total_questions)*100
print('Твій бал:',mark)
print('Бувай!')