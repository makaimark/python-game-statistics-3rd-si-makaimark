
# Export functions


import reports


def file_export(file_name, year, title, genre):
    with open('export.txt', 'w') as f:
        f.write("1. How many games are in the file?\n")
        f.write(str(reports.count_games(file_name)) + "\n")
        f.write("2. Is there a game from a given year?\n")
        f.write(str(reports.decide(file_name, year)) + "\n")
        f.write("3. Which was the latest game?\n")
        f.write(str(reports.get_latest(file_name)) + "\n")
        f.write("4. How many games do we have by genre?\n")
        f.write(str(reports.count_by_genre(file_name, genre)) + "\n")
        f.write("5. What is the line number of the given game (by title)?\n")
        f.write(str(reports.get_line_number_by_title(file_name, title)) + "\n")
        f.write("------------------------------------\n"+"Extra\n")
        f.write("1. What is the alphabetical ordered list of the titles?\n")
        f.write(str(reports.sort_abc(file_name))+'\n')
        f.write("2. What are the genres?\n")
        f.write(str(reports.get_genres(file_name))+'\n')
        f.write("3. What is the release date of the top sold 'First-person shooter' game?\n")
        f.write(str(reports.when_was_top_sold_fps(file_name)))
