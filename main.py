class Geese:
    animal_list = []

    def __init__(self, name, weight, food, eggs=0, feed=0):
        self.name = name
        self.weight = weight
        self.food = food
        self.feed = feed
        self.eggs = eggs
        self.animal_list.append(self)


    def feed_animal(self, food):
        satiety = 100
        percentage_of_fullness = 0
        if food == 'grain':
            self.feed += 10
            percentage_of_fullness += 100 / (satiety / self.feed)
            return f'Вы покормили животного +10 к сытости\nОно сыто на {percentage_of_fullness} %'

    def voices(self):
        return 'Гуси говарят "Га-га-га"'

    def collect_eggs(self, food):
        if food == 'grain':
            self.eggs += 2
            return f'Эта еда мне подходит +2 яйца! \nВсего {self.eggs} шт. яиц снесла {self.name}'
        else:
            return f'{self.name} говарит: Такое я не ем и яйца нести не буду!'


geese_grey = Geese('Серый', 7, 'grain')
geese_white = Geese('Белый', 6, 'grain')
add = sum((x.weight for x in Geese.animal_list))
print(f'Вес всех гусей {add} кг')
max_add = max((x.weight for x in Geese.animal_list))
for x in Geese.animal_list:
    if x.weight == max_add:
        print('Самый тяжелый гусь', x.name)
        break


class Chickens:
    def __init__(self, name, weight, food, eggs=0, feed=0):
        self.name = name
        self.weight = weight
        self.food = food
        self.eggs = eggs
        self.feed = feed

    def feed_animal(self, food):
        satiety = 100
        percentage_of_fullness = 0
        if food == 'grain':
            self.feed += 10
            percentage_of_fullness += 100 / (satiety / self.feed)
            return f'Вы покормили животного +10 к сытости\nОно сыто на {percentage_of_fullness} %'

    def voices(self):
        return 'Курицы "Кудахчут"'

    def collect_eggs(self, food):
        if food == 'grain':
            self.eggs += 2
            return f'Эта еда мне подходит, вы собрли +2 яйца! \nВсего яиц в корзине {self.eggs}'
        else:
            return f'{self.name} говарит: Такое я не ем и яйца нести не буду!'


chicken_ko_ko = Chickens('Ко-ко', 5, 'grain')
chicken_kukareku = Chickens('Кукареку', 6, 'grain')


class Duck:
    def __init__(self, name, weight, food, eggs=0, feed=0):
        self.name = name
        self.weight = weight
        self.food = food
        self.eggs = eggs
        self.feed = feed

    def feed_animal(self, food):
        satiety = 100
        percentage_of_fullness = 0
        if food == 'fish':
            self.feed += 10
            percentage_of_fullness += 100 / (satiety / self.feed)
            return f'Вы покормили животного +10 к сытости\nОно сыто на {percentage_of_fullness} %'

    def voices(self):
        return 'Утки говарят "Кря-Кря"'

    def collect_eggs(self, food):
        if food == 'grain':
            self.eggs += 2
            return f'Эта еда мне подходит +2 яйца! \nВсего {self.eggs} шт. яиц снесла {self.name}'
        else:
            return f'{self.name} говарит: Такое я не ем и яйца нести не буду!'


krykva = Duck('Кряква', 4, 'fish')


class Cows:
    def __init__(self, name, weight, food, feed=0):
        self.name = name
        self.weight = weight
        self.food = food
        self.feed = feed

    def feed_animal(self, food):
        satiety = 100
        percentage_of_fullness = 0
        if food == 'hay':
            self.feed += 10
            percentage_of_fullness += 100 / (satiety / self.feed)
            return f'Вы покормили животного +10 к сытости\nОно сыто на {percentage_of_fullness} %'

    def voices(self):
        return 'Коровы говарят "Муууу"'

    def milk_the_cow(self):
        return 'Вы подоили корову'


manka = Cows('Манька', 280, 'hay')
marta = Cows('Марта', 345, 'hay')


class Goats:
    def __init__(self, name, weight, food, feed=0):
        self.name = name
        self.weight = weight
        self.food = food
        self.feed = feed

    def feed_animal(self, food):
        satiety = 100
        percentage_of_fullness = 0
        if food == 'hay':
            self.feed += 10
            percentage_of_fullness += 100 / (satiety / self.feed)
            return f'Вы покормили животного +10 к сытости\nОно сыто на {percentage_of_fullness} %'

    def voices(self):
        return 'Козы говарят "Бееее"'

    def milk_the_goats(self):
        return 'Вы подоили козу'


horns = Goats('Рога', 36, 'hay')
hoofs = Goats('Копыта', 24, 'hay')


class Sheep:
    def __init__(self, name, weight, food, feed=0):
        self.name = name
        self.weight = weight
        self.food = food
        self.feed = feed

    def feed_animal(self, food):
        satiety = 100
        percentage_of_fullness = 0
        if food == 'hay':
            self.feed += 10
            percentage_of_fullness += 100 / (satiety / self.feed)
            return f'Вы покормили животного +10 к сытости\nОно сыто на {percentage_of_fullness} %'

    def voices(self):
        return 'Овцы говарят "Бееее"'

    def to_cut_a_sheep(self):
        return 'Вы подстригли овцу'


barashek = Sheep('Барашек', 29, 'hay')
kudrayviy = Sheep('Кудрявый', 41, 'hay')
