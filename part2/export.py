
# Export functions

import reports

file_name = "game_stat.txt"
title = "Crysis"


def file_export(export_file_name, title):
    with open(export_file_name, 'w') as f:
        f.write("1. What is the most played game?\n")
        f.write(str(reports.get_most_played(file_name)) + "\n")
        f.write("2. How many copies have been sold total?\n")
        f.write(str(reports.sum_sold(file_name)) + "\n")
        f.write("3. What is the average selling??\n")
        f.write(str(reports.get_selling_avg(file_name)) + "\n")
        f.write("4. How many characters long is the longest title? \n")
        f.write(str(reports.count_longest_title(file_name)) + "\n")
        f.write("5. What is the average of the release dates? \n")
        f.write(str(reports.get_date_avg(file_name)) + "\n")
        f.write("6. What properties has a game? Title =" + title + "\n")
        f.write(str(reports.get_game(file_name, title)) + "\n")
        f.write("------------------------------------\n"+"Extra\n")
        f.write("1. How many games are there grouped by genre?\n")
        f.write(str(reports.count_grouped_by_genre(file_name))+'\n')
        f.write("2. What is the date ordered list of the games in descending order?\n")
        f.write(str(reports.get_date_ordered(file_name))+'\n')

file_export("export.txt", title)
