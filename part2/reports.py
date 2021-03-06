from operator import itemgetter
# Report functions


def file_reader(file_name):
    opened_text = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            opened_text.append(line.split("\t"))
    return opened_text


# What is the title of the most played game?
def get_most_played(file_name):
    most_played = ""
    number_of_sold = 0
    opened_file = file_reader(file_name)
    for line in opened_file:
        if float(line[1]) > float(number_of_sold):
            number_of_sold = float(line[1])
            most_played = line[0]
    return most_played


# How many copies have been sold total?
def sum_sold(file_name):
    total_sold = 0
    opened_file = file_reader(file_name)
    for line in opened_file:
        total_sold = total_sold + float(line[1])
    return total_sold


# What is the average selling?
def get_selling_avg(file_name):
    summa = 0
    counter = 0
    opened_file = file_reader(file_name)
    for line in opened_file:
        counter += 1
        summa = summa + float(line[1])
    average = summa / counter
    return average


# How many characters long is the longest title?
def count_longest_title(file_name):
    counter = 0
    opened_file = file_reader(file_name)
    for line in opened_file:
        if len(line[0]) > counter:
            counter = len(line[0])
    return counter


# What is the average of the release dates?
def get_date_avg(file_name):
    summa, average, counter = 0, 0, 0
    opened_file = file_reader(file_name)
    for line in opened_file:
        counter += 1
        summa = summa + int(line[2])
    average = summa / counter
    average = round(average, 0)
    return average


# What properties has a game?
def get_game(file_name, title):
        opened_file = file_reader(file_name)
        for line in opened_file:
            if line[0] == title:
                line[1] = float(line[1])
                line[2] = int(line[2])
                line[4] = line[4].replace('\n', "")
                return line


# How many games are there grouped by genre?
def count_grouped_by_genre(file_name):
    dictionary = {}
    opened_file = file_reader(file_name)
    for line in opened_file:
        line[3] = line[3].replace('\n', "")
        if line[3] not in dictionary.keys():
            dictionary[line[3]] = 1
        else:
            dictionary[line[3]] += 1
    return dictionary


# What is the date ordered list of the games in descending order?
def get_date_ordered(file_name):
    temp_dict = {}
    date_ordered_list = []
    opened_file = file_reader(file_name)
    for line in opened_file:
        temp_dict[line[0]] = int(line[2])
    temp_dict = sorted(temp_dict.items(), key=lambda x: (-x[1], x[0]))
    for i in temp_dict:
        date_ordered_list.append(i[0])
    return date_ordered_list
