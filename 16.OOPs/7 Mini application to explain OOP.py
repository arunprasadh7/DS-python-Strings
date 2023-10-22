class Movie:
    '''creation of demo class for movie library'''

    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print('Movie name:', self.title)
        print('Hero name:', self.hero)
        print('Heroine name:', self.heroine)


list_of_movies = []
print('Welcome to movies library.')
while True:
    title = input('Enter movie name:')
    hero = input('Enter hero name:')
    heroine = input('Enter heroine name:')
    m = Movie(title, hero, heroine)
    list_of_movies.append(m)
    print('Movie successfully added to the list.')
    print()
    option = input('Do you like to add another movie to the list(Yes/No)?')
    if option.lower() == 'no':
        break

print('All movies list:')
print()
for movie in list_of_movies:
    movie.info()
    print('----------------')

print('Thanks for visiting movies library.')

