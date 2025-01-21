from pathlib import Path

import json
current_dir = Path()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#open file
people_all=[]
for letter in alphabet:
    with open(current_dir / "Dataset" / f'{letter}_people.json', encoding='utf-8') as file:
        people_all.append(json.load(file))
 
#create empty lists
#republican_list = [] 
#democrat_list = []

republican_universities={}
democrat_universities={}


for letter in people_all:
    for person in letter:
        if ('ontology/party_label' in person) and ('ontology/almaMater_label' in person):
            party = person['ontology/party_label']
            uni_data = person['ontology/almaMater_label']
            unilist = []
            #MAKE IT A LIST REGARDLESS OF WHETHER THERE IS ONE OR MULTIPLE UNIVERSITIES
            if isinstance(uni_data,str): 
                unilist = [uni_data]
            elif isinstance(uni_data,list):
                unilist = uni_data
            for uni in unilist:
                #ONLY CONSIDER IF IT IS A UNIVERSITY, NOT A HIGH SCHOOL
                if 'high school' not in uni.lower():
                    #CALCULATE THE WEIGHTED VALUE THAT THE UNIVERSITY ATTENDANCE HAS
                    uni_value = 1/len(unilist)
                    if party == 'Republican Party (United States)': 
                        #republican_list.append(person)
                        if uni in republican_universities:
                            republican_universities[uni] = republican_universities[uni] + uni_value
                        else:
                            republican_universities[uni] = uni_value
                    elif party == 'Democratic Party (United States)': 
                        #democrat_list.append(person)
                        if uni in democrat_universities:
                            democrat_universities[uni] = democrat_universities[uni] + uni_value
                        else:
                            democrat_universities[uni] = uni_value

"""
republican_over_10 = {}
for university, frequency in republican_universities.items():
    if frequency >= 10:
        republican_over_10[university] = frequency

democrat_over_10 = {}
for university, frequency in democrat_universities.items():
    if frequency >= 10:
        democrat_over_10[university] = frequency
"""

            
#print(f"Republicans: {len(republican_list)}")
#print(f"Democrats: {len(democrat_list)}")
#print(republican_universities)
#print('\n')
#print(democrat_universities)

import json
with open('republican.json', 'w', encoding='utf-8') as file:
    json.dump(republican_universities, file, indent=4)
with open('democrat.json', 'w', encoding='utf-8') as file:
    json.dump(democrat_universities, file, indent=4)
