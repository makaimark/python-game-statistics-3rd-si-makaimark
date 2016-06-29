import reports


file_name = "game_stat.txt"

print("1. How many games are in the file?")
print(reports.count_games(file_name))

year = input("2. Is there a game from a given year?\n")
print(reports.decide(file_name, year))

print("3. Which was the latest game?")
print(reports.get_latest(file_name))

by_genre = input("4. How many games do we have by genre?\n")
print(reports.count_by_genre(file_name, by_genre))

by_title = input("5.What is the line number of the given game (by title)?")
print(reports.get_line_number_by_title(file_name, by_title))

print("Extra")
print("1. What is the alphabetical ordered list of the titles?")
sorted_abc = " ,".join(reports.sort_abc(file_name))
print(sorted_abc)

print("2. What are the genres?")
get_geners = " ,".join(reports.get_genres(file_name))
print(get_geners)

print("3. What is the release date of the top sold 'First-person shooter' game?")
print(reports.when_was_top_sold_fps(file_name))
