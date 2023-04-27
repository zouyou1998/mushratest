#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
from pandas.core.frame import DataFrame

# Create empty lists to hold the sound and x values from all files
#it is just an example so 3 result are combined
sounds = []
x_values = []
number = 3

# Load each JSON file and add its sound and x values to the lists
for i in range(1,number+1): #here only 3 files
    with open(f'result{i}.json', 'r') as f:
        data = json.load(f)
        sounds.append(data['sound'])
        x_values.append(data['x'])

# Calculate the average value for each x[i]
averages = [sum([x[i] for x in x_values]) / len(x_values) for i in range(len(x_values[0]))]

# Opening JSON file
f = open('saved_data.json')
# returns JSON object as a dictionary
important_data = json.load(f)

# Create a new JSON object with the sound and average values
#insert reference source at the beginning, because the score is always 100
output_data = {'sound': sounds[0], 'averages': averages}
output_data["sound"].insert(0, important_data["reference_source"][0][0])
output_data["averages"].insert(0, 100)

# Write the JSON object to a new file
with open('output.json', 'w') as outfile:
    json.dump(output_data, outfile)
    
f = open('output.json')
# returns JSON object as a dictionary
output_data = json.load(f)

f = open('saved_data.json')
# returns JSON object as a dictionary
important_data = json.load(f)

# Process the "sound" array in json
for i in range(len(output_data["sound"])):
    if output_data["sound"][i] in important_data["reference_source"][0]:
        output_data["sound"][i] += " (reference_source)"
    elif output_data["sound"][i] in important_data["test_source"][0]:
        output_data["sound"][i] += " (test_source)"
    elif output_data["sound"][i] in important_data["anchor"][0]:
        output_data["sound"][i] += " (anchor)"
    elif output_data["sound"][i] in important_data["hidden_reference_source"][0]:
        output_data["sound"][i] += " (hidden_reference_source)"

with open('output.json', 'w') as outfile:
    json.dump(output_data, outfile)

with open('output.json') as f:
    data = json.load(f)

combined_list = []

for i in range(len(data['sound'])):
    combined_list.append(data['sound'][i] + ' - ' + str(data['averages'][i]))

#use panda to show result
c = {"source(source type) - score":combined_list}
data = DataFrame(c)
print(data)


# In[ ]:




