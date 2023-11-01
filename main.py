import random


# ЗАДАНИЕ 1
class MusicAlbum:
    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def play_random_track(self):
        print(f"Воспроизводится трек: {(random.choice(self.tracklist))}")



album1 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte", ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex", "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo", "Hallomann"])
print("Название:", album1.title)
print("Исполнитель:", album1.artist)
print("Год:", album1.release_year)
print("Жанр:", album1.genre)
print("Треки:", album1.tracklist)
album1.play_random_track()




# ЗАДАНИЕ 2

class Student:

    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def average_score(self):
        self.scores = sum(self.scores) / len(self.scores)
        print("Средний балл: ", self.scores)


student1 = Student("Иван Иванов", 13, "6А", [2, 4, 4, 5])
print("Имя:", student1.name)
print("Возраст:", student1.age)
print("Класс:", student1.grade)
print("Оценки:", *student1.scores)
student1.average_score()

# ЗАДАНИЕ 3

class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f'\nИнгредиенты для {self.name}: ', self.ingredients)


    def cook(self):
        print(f'Сегодня мы готовим {self.name}')
        print(f'Выполняем инструкцию по приготовлению блюда {self.name}...')
        print(f'Блюдо {self.name} готово!')




# создаем рецепт спагетти болоньезе
spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

# печатаем список продуктов для рецепта спагетти
spaghetti.print_ingredients()

# готовим спагетти
spaghetti.cook()

# создаем рецепт для кекса
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

# печатаем рецепт кекса
cake.print_ingredients()

# готовим кекс
cake.cook()
