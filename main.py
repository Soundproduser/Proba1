# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

score=111
balance=("мой счёт в банке %s рублей")
print(balance % score)
# Spaces — пробелы
# Мы создали переменную spaces, присвоив ей результат умножения символа «пробел» на 25 (то есть строку из 25 пробелов). В следующих трех строках программы мы воспользовались этой переменной, чтобы напе- чатать блок текста со смещением вправо. Вот что должно получиться:
spaces = ' ' * 25
print('%s Задний переулок 12' % spaces)
print('%s Трясогузочья пустошь' % spaces)
print('%s Западный Всхрапшир' % spaces)
print()
print()
print('Уважаемый Сэр,')
print()
print('Хочу сообщить вам, что кое-где накрыше уборной')
print('недостает кусков черепицы.')
print('Думаю, прошлой ночью их сдуло внезапным порывом ветра.')
print()
print('С почтением')
print('Малькольм Конфузли')

wizard_list=['паучьи лапки', 'жабий палец', 'язык улитки', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
wizard_list.append('медвежий коготь')
print(wizard_list)
['паучьи лапки', 'жабий палец', 'язык улитки', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи', 'медвежий коготь']

print(wizard_list[3:5])

del wizard_list[5]
print(wizard_list)
['паучьи лапки', 'жабий палец', 'язык улитки', 'крыло летучей мыши', 'жир слизня', 'медвежий коготь', 'мандрагора', 'болиголов', 'болотный газ']


list1 = [1, 2, 3, 4, 5]
list2 = ['я', 'забрался', 'под', 'кровать']
print(list1 + list2)

#cписок
favorite_sports = ['Ральф Уильямс, Футбол', 'Майкл Типпетт, Баскетбол',
'Эдвард Элгар, Бейсбол',
'Ребекка Кларк, Нетбол',
'Этель Смит, Бадминтон', 'Фрэнк Бридж, Регби']
print(favorite_sports)
 #словарь
favorite_sports1 = {'Ральф Уильямс': 'Футбол', 'Майкл Типпетт': 'Баскетбол',
'Эдвард Элгар': 'Бейсбол',
'Ребекка Кларк': 'Нетбол',
'Этель Смит': 'Бадминтон', 'Фрэнк Бридж': 'Регби'}
print(favorite_sports1)

print(favorite_sports1['Ребекка Кларк'])

#1. Любимые вещи
games=["play tannis","programming","music"]
foods=["orange","apple","carrot"]
favorites=[games+foods]
print(favorites)

#2. Подсчет воинов
print(3*25+2*40)
#3. Приветствие
name="Bogdan"
last_name=" Shaihudinov"
info=name+last_name
приветствие="Привет,%s!"
print(приветствие % info)

twinkies =400
if (twinkies < 100 or twinkies > 500 ):
    print("слишком мало или слишком много")

Money=(3000)
if(Money>100)and(Money<500):

    print("соответствует диапазону значений от 100 до 500")
elif(Money>1000) and(Money<5000):
    print("соответствует диапазону значений от 1000 до 5000")


ninjas=50
if(ninjas>=30 )and(ninjas<=50):
    print("Их слишком много")
elif (ninjas>10)and(ninjas<30):
    print("будет непросто,но я с ними разделаюсь")
elif(ninjas<=10):
    print("я одолею этих ниндзя")










# See PyCharm help at https://www.jetbrains.com/help/pycharm/
