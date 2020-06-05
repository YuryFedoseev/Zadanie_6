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
cook_book = {'Гуси': 'Серый, Белый',
             'Корова': 'Манька',
             'Овцы': 'Барашек, Кудрявый',
             'Курица': 'Ко-ко, Кукареку',
             'Коза': 'Рога, Копыта',
             'Утка': 'Кряква'
             }



class farming_simulate:
    '''Основа '''
    feed_status = 0 #покормлены ли
    weight = 0 #для сравнения веса
    #milk = 'No' #Можно ли доить
    milk_status = 0 #Подоины ли
    cut = 'No' #Можно ли стричь
    cut_status = 0 # Статус стрижки
    eggs = 'No'  #Можно ли собирать яйца
    eggs_status = 'No'  #Собраны ли яйца
    name = 'htoto'
    #sing =''
 
    #def __init__(milk,cut,eggs):
        #self.milk = milk
        #self.cut = cut
        #self.eggs = eggs
        #self.milk_status = milk_status
        #self.cut_status = cut_status
        #self.eggs_status = eggs_status
     
    def feed_yes(self):
        self.feed_status = 1
        
    def feed_no(self):
        self.feed_status = 0

                    
    def can_milk_yes(self):
        self.milk = 'Yes'
        
    def can_milk_no(self):
        self.milk = 'No'

    def can_cut_yes(self):
        self.cut = 'Yes'

    def can_cut_no(self):
        self.cut = 'No'

    def can_eggs_yes(self):
        self.eggs = 'Yes'

    def can_eggs_no(self):
        self.eggs = 'No'
        


class cow(farming_simulate):
    
    cow = farming_simulate()
    cow.can_milk_yes()

class eggs(farming_simulate):
    eggs = farming_simulate()
    eggs.can_eggs_yes()

class cut(farming_simulate):
    cut = farming_simulate()
    cut.can_cut_yes()
  

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
                b = 1
                duck.can_eggs_yes()
                feed(choise_animal,farming_simulate)
                #print (duck.__dict__)
                choise_animal()
                b = 0
            elif animal == 'Гуси':
                b = 1
                goose = farming_simulate()
                goose.can_eggs_yes()
                feed(choise_animal,farming_simulate)
                #print (goose.__dict__)
                choise_animal()
                b = 1
            elif animal == 'Овцы' :
                c = 1
                sheep = farming_simulate()
                sheep.can_cut_yes()
                feed(choise_animal,farming_simulate)
                #print (sheep.__dict__)
                choise_animal()
                c = 0
            elif animal ==  'Курица':
                b = 1
                cheek = farming_simulate()
                cheek.can_eggs_yes()
                feed(choise_animal,farming_simulate)
                #print (cheek.__dict__)
                choise_animal()
                b = 0
            elif animal == 'Коза':
                a = 1
                goat = farming_simulate()
                goat.can_milk_yes()
                feed(choise_animal,farming_simulate)
                #print (goat.__dict__)
                choise_animal()
                a = 0 
            elif animal == 'q':
                break
                


def feed(choise_animal,farming_simulate):
    perem = 'Yes'
    #print (feed_status)
    feed_stat = input('Введите статус кормления данного животного(1 - покормлено, 0 - не покормлено) ')
            
    if feed_stat == '1':
        #что-то менять
        feed_status = 1
        perem = input('Животное покормлено. Желаете продолжить работу? (Yes- да, продолжить; No - нет, завершить)')
        perem = perem.capitalize()
        print (feed_status)
        if perem == 'Yes':
            choise_animal()


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
        

    

        
        
choise_animal()

        
#print (cook_book.values())        
    
