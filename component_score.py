class scoring_c():
    def __init__(self):
        pass

    @staticmethod
    def return_scores(formatted_file_contents,points_reference): #file_contents is a list
        # returns the regional association scores
        
        last_option = False
        if list(points_reference.keys())[-1] == ">":
            last_option = True
            last_option_value = list(points_reference.values())[-1]
            points_reference.pop(">") # removes the 'last option'
            
    regional_association_scores = {}
    
    teams_list = formatted_file_contents[1] # gets the team list
    last_points_reference = list(points_reference.keys())[-1]
    
    for team_dict in teams_list:
        team_place = team_dict["place"]
        team_regional_association = team_dict["regional_association"]
        for place_reference in points_reference.keys():
            if place_reference == team_place:
                
                if team_regional_association in regional_association_scores:
                    regional_association_scores[team_regional_association] += points_reference[place_reference]
                else:
                    regional_association_scores[team_regional_association] = points_reference[place_reference]
                    
            elif last_option == True and team_place > last_option_reference:
                if team_regional_association in regional_association_scores:
                    regional_association_scores[team_regional_association] += last_option_value  
                    
                else:
                    regional_association_scores[team_regional_association] = last_option_value
                                          

    @staticmethod
    def return_year_sum_score(files_regional_association_score_list ): #
        # returns the total year score e.g. {reg1:500,reg2:600}
        
        sum_scores_dictionary = {}
        
        for scores_dictionary in files_regional_association_scores_list: # [{scores_dictioanry}]
            
            for i in scores_dictionary: # {regionalassoc:1}
                if i in sum_scores_dictionary: #sumscores{reg} == reg
                    sum_scores_dictionary[i] += scores_dictionary[i]    
                else:
                    sum_scores_dictionary[i] = scores_dictionary[i]
                    
        return sum_scores_dictionary
    
    @staticmethod
    def sort_score(regional_association_score_dictionary):
        # Sorting the dictioanry by values in descending order
        sorted_desc_scores = dict(sorted(regional_association_score_dictionary.items(), key=lambda item: item[1], reverse=True))
        return sorted_desc_scores
    