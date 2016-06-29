import reports

file_name = "game_stat.txt"

print("1. What is the title of the most played game?")
print(reports.get_most_played(file_name))

print("2. How many copies have been sold total?")
print(reports.sum_sold(file_name))

print("3. What is the average selling?")
print(reports.get_selling_avg(file_name))

print("4. How many characters long is the longest title?")
print(reports.count_longest_title(file_name))

print("5. What is the average of the release dates? ")
print(reports.get_date_avg(file_name))

title = input("6. What properties has a game?\n")
print(reports.get_game(file_name, title))

print("\n"+"Extra")

grouped_by_genre = reports.count_grouped_by_genre(file_name)
string_grouped_by_genre = ' ,'.join('{}: {}'.format(key, value) for key, value in grouped_by_genre.items())
print("1. How many games are there grouped by genre?")
print(string_grouped_by_genre)

get_date = " ,".join(reports.get_date_ordered(file_name))
print("2. What is the date ordered list of the games (in descending order)?")
print(get_date)
