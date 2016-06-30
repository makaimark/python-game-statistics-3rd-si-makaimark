import sys
import export


def file_reader(file_name):
    opened_text = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            opened_text.append(line.split('\t'))
    return opened_text


# How many games are in the file? OK
def count_games(file_name):
    opened_text = file_reader(file_name)
    return len(opened_text)


# Is there a game from a given year? OK
def decide(file_name, year):
    opened_text = file_reader(file_name)
    for line in opened_text:
        if str(year) in line:
            return True
    return False


# Which was the latest game? ok
def get_latest(file_name):
    year = 0
    latest_game = ""
    opened_file = file_reader(file_name)
    for line in opened_file:
        if line[2] > str(year):
            year = line[2]
            latest_game = line[0]
    return latest_game


# How many games do we have by genre? ok
def count_by_genre(file_name, genre):
    counter = 0
    opened_file = file_reader(file_name)
    for line in opened_file:
        if line[3] == genre:
            counter += 1
    return counter


# What is the line number of the given game (by title)? ok
def get_line_number_by_title(file_name, title):
    line_number = 0
    opened_file = file_reader(file_name)
    for line in opened_file:
        line_number += 1
        if line[0] == title:
            return line_number
    raise ValueError("could not find %r in %r" % (title, file_name))


# What is the alphabetical ordered list of the titles? ok
def sort_abc(file_name):
    list_of_films = []
    opened_file = file_reader(file_name)
    for line in opened_file:
        list_of_films.append(line[0])
    list_of_films.sort()
    return list_of_films


# What are the genres? It works, but the test.py drop a failure
def get_genres(file_name):
    genres = []
    opened_file = file_reader(file_name)
    for line in opened_file:
        if line[3] not in genres:
            genres.append(line[3])
    genres.sort(key=lambda v: v.upper())
    return genres


# What is the release date of the top sold "First-person shooter" game? ok
def when_was_top_sold_fps(file_name):
    year = 0
    top_sold = 0
    opened_file = file_reader(file_name)
    for line in opened_file:
        if line[3] == "First-person shooter" and float(line[1]) > float(top_sold):
            year = line[2]
            top_sold = line[1]
    if year == 0:
        raise ValueError("could not find First-person shooter")
    return int(year)
