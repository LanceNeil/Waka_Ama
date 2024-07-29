#indicates the number of files in the folder

import os



# Create class
class file_read_c():
  def __init__(self):
    pass

  @staticmethod
  def return_years(parent_path):
    #return years in a list e.g.(year1,year2)
    
    years_and_files = {}
    year_list = os.listdir(parent_path)

    for year in year_list:
      years_and_files[year] = len(os.dirlist(parent_path + "/" + year)) #To put this in the dictionary

      return year_list
    
  @staticmethod
  def find_year_path(parent_path, year, prefix):
    # returns the path of the argument year
    year_list = os.listdir(parent_path)
    year_path = None
    
    for i in year_list:
      if i == f"{prefix}{year}":
          year_path = f"{parent_path}/{prefix}{year}"
    return year_path

  @staticmethod
  def return_files(year_path):
    # returns lift of files in a dir e.g. [file1.file2,file3]
    
    files_list = os.listdir(year_path)
    
    return files_list
  
  @staticmethod
  def return_content(filepath):
    # returns dictionary of the contents of a file. Inlcudes its file name and content on a raw form
    """
    ["1,team,reg","2,team,reg"]
    """
    
    
    with open(filepath) as file:
        file_contents = file.readlines()
    return file_contents
  
  @staticmethod
  def format_content(file_contents,filename):
    # returns a dictionary of the formatted/categorized version of the contents of the the file contents

    race_info = file_contents[0]
    subsequent_rows = file_contents[1:-1]
    
    #race_info
    formatted_race_info = race_info.split(',')
    
    clean_formatted_race_info = []
      
    for i in formatted_race_info:
      if i !="":
          clean_formatted_race_info.append(i)
      else:
          continue
    formatted_race_info = clean_formatted_race_info
    
    
    
    
    race_number = formatted_race_info[0]
    race_type = formatted_race_info[1]
    race_heat = formatted_race_info[2]
    race_title = formatted_race_info[3]
    race_length = formatted_race_info[4]
    race_start_time = formatted_race_info[5]
    sunsequent_rows_count = len(subsequent_rows)
    
    race_info_attributes = {"number":race_number,
                            "type":race_type,
                            "heat":race_heat,
                            "title":race_title,
                            "length":race_length,
                            "start_time":race_start_time}
    
    #teams
    team_list = []
    for string_team in subsequent_rows:
      formatted_team = string_team.split(',')
      
      clean_formatted_team = []
      
      for i in formatted_team:
          if i !="":
              clean_formatted_team.append(i)
          else:
              continue
      formatted_team = clean_formatted_team
      
      
      
      
      # after removing the unnecesary commas
      team_place = formatted_team[0]
      team_id = formatted_team[1]
      team_lane = formatted_team[2]
      team_name = formatted_team[3]
      team_regional_association = formatted_team[4]
      team_elapsed_time = formatted_team[5]
      team_difference = formatted_team[6]
      team_start = formatted_team[7]
      team_attributes = {"place":team_place,
                         "id":team_id,
                         "lane":team_lane,
                         "name":team_name,
                         "regional_association":team_regional_association,
                         "elapsed_time":team_elapsed_time,
                         "difference":team_difference,
                         "start":team_start}
      team_list.append(team_attributes)
      
      
    file_attributes = [race_info_attributes,team_list]
    
    return file_attributes
"""""
# number of files int he folder
years_and_files = {}

for every_item in dir_list:
  years_and_files[every_item] = len(os.listdir(path + "/" + every_item)) #put inside the dictionary
  
print(years_and_files) #show the results
"""