import read_file as rd
import export_csv
import component_score
import component_gui


points_reference = {
        "1":8,
        "2":7,
        "3":6,
        "4":5,
        "5":4,
        "6":3,
        "7":2,
        "8":1,
        }

# get years
ask_parent_path = input("Type the name of your parent folder >> ")
parent_path = ask_parent_path
print(rd.file_read_c.return_years(parent_path))

# get all the files
ask_year = int(input("Type the year >> "))
target_year_path = rd.file_read_c.find_year_path(parent_path,ask_year,"Wakanats")
files_list = rd.file_read_c.return_files(target_year_path)

# find specific keyword only
ask_keyword = input("Keyword >> ")
filtered_files_list = []
for file in files_list:
    if ask_keyword in file.lower():
        filtered_files_list.append(file)
    else:
        continue
print(len(filtered_files_list), ask_keyword, "found")

# get contents

files_regional_association_scores_list = []
for filename in filtered_files_list:
    try:
        filepath = f"{target_year_path}/{filename}"
        file_contents = rd.file_read_c.return_content(filepath)
        
        # get formatted version
        
        formatted_file_contents = rd.file_read_c.format_content(file_contents,filename)

        # check if there are errors
        if type(formatted_file_contents) is tuple:
            print(formatted_file_contents)
            continue
        
        # get the regional associations core of the file
        file_regional_association_scores = scoring.scoring_c.return_scores(formatted_file_contents,points_reference)
        files_regional_association_scores_list.append(file_regional_association_scores)
        
    except Exception as e:
        print(f”Error on file: {filename}. Type of error: {e}”)
        continue
    
# get sum of all the regional association scores
year_regional_association_scores = scoring.scoring_c.sreturn_yyear_sum_score(files_regional_association_scores_list)

# sort the file (descending)
year_regional_association_scores = scoring.scoring_c.sort_score(year_regional_association_scores)

# get the csv export option
ask_csv_export = input("Do you want to save this as a CSV?(Y/N) >> ")
if ask_csv_export == "Y":
    ask_csv_filename = input("Type filename >> ")
    csv_export.csv_c.csv_export(year_regional_association_scores,ask_csv_filename)






