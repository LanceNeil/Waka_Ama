import os
import csv
import export_csv as export_csv
import component_score as component_score

# Define the find_year_path function within the script
def find_year_path(parent_directory, selected_year, folder_prefix):
    try:
        year_folder = f"{folder_prefix}{selected_year}"
        year_path = os.path.join(parent_directory, year_folder)
        if os.path.exists(year_path) and os.path.isdir(year_path):
            return year_path
        else:
            raise FileNotFoundError(f"Year folder {year_folder} not found in {parent_directory}")
    except Exception as e:
        return f"Error: {e}"

# Define the return_files function within the script
def return_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def calculate_total_scores(regional_scores):
    total_scores = {}
    for scores in regional_scores:
        for team, score in scores.items():
            if team in total_scores:
                total_scores[team] += score
            else:
                total_scores[team] = score
    return total_scores

# Add return_content function
def return_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Add format_content function
def format_content(content, file_name):
    # This is a placeholder implementation. Adjust according to your specific needs.
    lines = content.split('\n')
    formatted_content = {}
    for line in lines:
        if line.strip():
            parts = line.split()
            if len(parts) >= 2:
                team = ' '.join(parts[1:-1])
                placement = parts[-1]
                formatted_content[team] = placement
    return formatted_content

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

def return_years(parent_directory):
    try:
        years = [name for name in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, name))]
        return sorted(years)
    except Exception as e:
        return f"Error: {e}"

# Prompt the user for the parent directory path
parent_directory = input("Enter the path to your parent directory >> ")
print(return_years(parent_directory))

# Prompt the user to select a specific year
selected_year = int(input("Enter the year you are interested in >> "))
year_path = find_year_path(parent_directory, selected_year, "WakaNats")

# Check if year_path is valid before proceeding
if isinstance(year_path, str) and year_path.startswith("Error:"):
    print(year_path)
    exit()

# Now we can safely use year_path
files_in_year = return_files(year_path)

# Prompt the user for a keyword to filter files
keyword_filter = input("Enter a keyword to filter the files >> ").lower()
filtered_files = [file for file in files_in_year if keyword_filter in file.lower()]
print(len(filtered_files), keyword_filter, "found")

# Process the contents of the filtered files
regional_scores = []
for file_name in filtered_files:
    try:
        file_path = os.path.join(year_path, file_name)
        content = return_content(file_path)
        
        # Format the content of the file
        formatted_content = format_content(content, file_name)
        
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
total_scores = calculate_total_scores(regional_scores)

# Sort the scores in descending order
sorted_scores = component_score.scoring_c.score_sort(total_scores)

# Prompt the user to export the scores to a CSV file
save_as_csv = input("Would you like to save the results as a CSV file? (Y/N) >> ")
if save_as_csv.upper() == "Y":
    csv_filename = input("Enter the filename for the CSV >> ")
    export_csv.csv_c.csv_export(sorted_scores, csv_filename)