import read_file as rd
import export_csv as export_csv
import component_score as component_score
import component_gui as component_gui

points_reference = {
    "1": 8,
    "2": 7,
    "3": 6,
    "4": 5,
    "5": 4,
    "6": 3,
    "7": 2,
    "8": 1,
    ">": 1,
}

# Prompt the user for the parent directory path
parent_directory = input("Enter the path to your parent directory >> ")
print(rd.read_file.return_years(parent_directory))

# Prompt the user to select a specific year
selected_year = int(input("Enter the year you are interested in >> "))
year_path =(rd).read_file.find_year_path(parent_directory, selected_year, "WakaNats")
files_in_year =(rd).read_file.return_files(year_path)

# Prompt the user for a keyword to filter files
keyword_filter = input("Enter a keyword to filter the files >> ").lower()
filtered_files = [file for file in files_in_year if keyword_filter in file.lower()]
print(len(filtered_files), keyword_filter, "found")

# Process the contents of the filtered files
regional_scores = []
for file_name in filtered_files:
    try:
        file_path = f"{year_path}/{file_name}"
        content =(rd).read_file.return_content(file_path)
        
        # Format the content of the file
        formatted_content =(rd).read_file.format_content(content, file_name)
        
        # Check for errors in formatting
        if isinstance(formatted_content, tuple):
            print(formatted_content)
            continue
        
        # Calculate the scores based on the formatted content
        scores = component_score.scoring_c.return_scores(formatted_content, points_reference)
        regional_scores.append(scores)
        
    except Exception as e:
        print(f"ERROR on file | {file_name} | {e}")
        continue

# Calculate the total scores for the selected year
total_scores = component_score.scoring_c.return_scores(regional_scores)

# Sort the scores in descending order
sorted_scores = component_score.scoring_c.score_sort(total_scores)

# Prompt the user to export the scores to a CSV file
save_as_csv = input("Would you like to save the results as a CSV file? (Y/N) >> ")
if save_as_csv.upper() == "Y":
    csv_filename = input("Enter the filename for the CSV >> ")
    export_csv.csv_c.csv_export(sorted_scores, csv_filename)