import random
import bisect
from typing import NamedTuple

class MovieNametuple(NamedTuple):
    name: str
    year: int
    rating: str

class Movie():
    def __init__(self, movie: MovieNametuple):
        self.name = movie.name
        self.year = movie.year
        self.rating = float(movie.rating)

    @property
    def rank(self):
        '''按评分对电影进行分级
        - S： 8.5及以上
        - A： 8~8.5
        - B： 7~8
        - C： 6~7
        - D： 6以下
        '''
        grades = ('D', 'C', 'B', 'A', 'S')
        breakpoints = (6, 7, 8, 8.5)
        idnex = bisect.bisect(breakpoints, self.rating)
        return grades[idnex]


def get_sorted_movie(movies: [Movie], sorting_type):
    '''对电影列表进行排序并返回
        :param movies: Movie 对象列表
        :param sorting_typing: 排序选项，可选值： name（名称）、year（年份）、rating(评分), random（随机乱序）, rank(等级）
        :return [Movie]
        '''
    sorting_algos = {
        'name': (lambda movie: movie.name.lower(), False),
        'year': (lambda movie: movie.year,True),
        'rating': (lambda movie: movie.rating,True),
        'random': (lambda movie: random.random(),False),
    }

    try:
        key_func, reverse = sorting_algos[sorting_type]
    except KeyError:
        raise RuntimeError(f'Unknow sorting type: {sorting_type}')

    sorted_movies = sorted(movies, key = key_func, reverse = reverse)
    return sorted_movies

movies = [
    {'name': 'The Dark Knight', 'year': 2008, 'rating': '9'},
    {'name': 'Kaili Blues', 'year': 2015, 'rating': '7.3'},
    {'name': 'Citizen Kane', 'year': 1941, 'rating': '8.3'},
    {'name': 'Project Gutenberg', 'year': 2018, 'rating': '6.9'},
    {'name': 'Burning', 'year': 2018, 'rating': '7.5'},
    {'name': 'The Shawshank Redemption ', 'year': 1994, 'rating': '9.3'},
    {'name': 'xxxx', 'year': 1923, 'rating': '5'},
]


def main():
    movies_obj = [Movie(MovieNametuple(**item)) for item in movies]
    all_sorting_types = ('name', 'rating', 'year', 'random')


    print(movies_obj)
    while(True):
        sorting_typing = input('请输入排序配型（可选项有：name, year, rating, random）：')

        if sorting_typing == 'exit':
            print('退出程序')
            break

        if sorting_typing not in all_sorting_types:
            print(f'Sorry, "{sorting_typing}" is not a valid sorting type, please choose from "{ "/".join(all_sorting_types) }"')
            continue

        # 排序并输出排好序的电影列表
        movies_sorted  = get_sorted_movie(movies_obj, sorting_typing)
        for movie in movies_sorted:
            print(f'- [{movie.rank}] {movie.name} ({movie.year}) | rating: {movie.rank}')
        print('-------------------------------------')


if __name__ == '__main__':
    main()