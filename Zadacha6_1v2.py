'''
гусей "Серый" и "Белый"
корову "Маньку"
овец "Барашек" и "Кудрявый"
кур "Ко-Ко" и "Кукареку"
коз "Рога" и "Копыта"
и утку "Кряква"
Со всеми животными вам необходимо как-то взаимодействовать:

кормить
корову и коз доить
овец стричь
собирать яйца у кур, утки и гусей
различать по голосам(коровы мычат, утки крякают и т.д.)
'''




class farming_simulate:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
        
        self.eat = 'Животное не покормлено'

    def animal_voices(self,voice):
        if voice == 'Га-га':
            print('Гусь')
        elif voice == 'Му-у-у-у':
            print('Корова')
        elif voice == 'Бе-е':
            print('Овца')
        elif voice == 'Ме-е':
            print('Коза')
        elif voice == 'Ко-ко':
            print('Курица')
        elif voice == 'Кря':
            print('Утка')
        else:
          print('Звук не найден')

    def feeding(self):
      self.eat = 'Покормлено'
      return "Животное покормлено. Его имя: " + self.name


class Eggs(farming_simulate):

  def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.type = 'Приносит яйца'
        self.eat = 'Животное голодно'
        self.eggs = 'Яйца есть'

  def collect_eggs(self):
    if self.eggs == 'Яйца есть':
      self.eggs = 'Яйца собраны'
      return "Яйца собраны у  " + self.name
    else:
      return "У птицы с кличкой " + self.name + " яиц новых нет."
  

class Milk(farming_simulate):

  def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.type = 'Молокодающее'
        self.eat = 'Животное голодно'
        self.milk = 'Молоко есть'

  def collecting_milk(self):
    if self.milk == 'Молоко есть':
      self.milk = 'Молоко сдоено'
      return "Вы подоили скотину с кличкой " + self.name
    else:
      return "У скотины с кличкой " + self.name + " молока нет."


class Cut(farming_simulate):

  def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.type = 'Есть возможность собрать шерсть'
        self.eat = 'Животное голодно'
        self.wool = 'Шерсть есть'

  def collecting_wool(self):
    if self.wool == 'Шерсть есть':
      self.wool = 'Шерсть пострижена'
      return "Вы постригли скотину с кличкой " + self.name
    else:
      return "У скотины с кличкой " + self.name + " шерсти больше нет."

#Либо сделать это в отдельный файл
cook_book = [
goose_one,
goose_two,
cow,
sheep_one,
sheep_two,
chiken_one,
chiken_two,
goat_one,
goat_two,
duck
]

#Второй файл
goose_one = Eggy("Серый",120)
goose_two = Eggy("Белый",9)
cow = Milky("Манька",150)
sheep_one = Cut("Барашек",100)
sheep_two = Cut("Кудрявый",51)
chiken_one = Eggs("Ко-Ко",12)
chiken_two = Eggs("Кукареку",12)
goat_one = Milk("Рога",40)
goat_two = Milk("Копыта",20)
duck_k = Eggs("Кряква",10)

total_weight = 0 
highest_weight = 0



for animal in animals_list:

  if animal.hungriness == 'Животное голодно':
    animal.feeding()

  if animal.type == 'Несет яйца':
    animal.collecting_eggs()

  if animal.type == 'Приносит молоко':
    animal.collecting_milk()

  if animal.type == 'Можно стричь':
    animal.collecting_wool()

  if animal.weight > highest_weight:
    highest_weight = animal.weight
    heaviest_animal = animal.name

  
  total_weight = total_weight + animal.weight


print(f'Общий вес всех животных {total_weight} кг ')

print(f"Самый большой вес у {heaviest_animal}, вес = {highest_weight} кг")

def choise_animal():
    print (cook_book.keys())
    animal = input('Введите нужное животное: ')
    animal= animal.capitalize()
    for list_animal in cook_book.keys():
        if animal == list_animal:
            if animal == 'Корова':
                #print (cow.__dict__)                
                feed(choise_animal,farming_simulate)
                choise_animal()
                
            elif animal == 'Утка' :
                duck = farming_simulate()
                duck.can_eggs_yes()
                feed(choise_animal,farming_simulate)
                #print (duck.__dict__)
                choise_animal()
                
            elif animal == 'Гуси':
                
                goose = farming_simulate()
                goose.can_eggs_yes()
                feed(choise_animal,farming_simulate)
                #print (goose.__dict__)
                choise_animal()
               
            elif animal == 'Овцы' :
                
                sheep = farming_simulate()
                sheep.can_cut_yes()
                feed(choise_animal,farming_simulate)
                #print (sheep.__dict__)
                choise_animal()
                
            elif animal ==  'Курица':
                
                cheek = farming_simulate()
                cheek.can_eggs_yes()
                feed(choise_animal,farming_simulate)
                #print (cheek.__dict__)
                choise_animal()
                
            elif animal == 'Коза':
                
                goat = farming_simulate()
                goat.can_milk_yes()
                feed(choise_animal,farming_simulate)
                #print (goat.__dict__)
                choise_animal()
                 
            elif animal == 'q':
                break
                


def feed(choise_animal,farming_simulate):
    perem = 'Yes'
    feed_status = not_eat()
    if feed_status == '1':
        print ('Это животное уже покормлено', feed_status)
        choise_animal()
    elif feed_status == '0':
        feed_status = eat()
        print ('а так?', feed_status)
    else:
        feed_stat = input('Введите статус кормления данного животного(1 - покормлено, 0 - не покормлено) ')
        if feed_stat == '1':
            print('уже покормлено')
            
            
            
        else:
            perem = input('Животное покормлено. Желаете продолжить работу? (Yes- да, продолжить; No - нет, завершить)')
            perem = perem.capitalize()
            print (feed_status)
            if perem == 'Yes':
                choise_animal()
                feed_status = eat()


            elif feed_stat == '0':
                perem = input('Покормить животное? (Yes- да, покормить; No - нет, вернуться к выбору животного)')
                perem = perem.capitalize()
                if perem == 'Yes':
                    print('Животное покормлено')
                elif perem == 'No':
                    choise_animal()
            
            elif (feed_stat != '0' and feed_stat != '1'):
                perem = input('Введен не известный статус. Желаете повторить ввод? (Yes- да, повторить; No - нет, завершить)')
                perem = perem.capitalize()
                if perem == 'Yes':
                    feed(choise_animal,farming_simulate)
                elif perem == 'No':
                    pass     
