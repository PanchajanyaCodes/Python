# Problem 2
# Write a program to fill in a letter template given below with name and date.

letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''

name = "Panchajanya"
date = "November 12, 2024"

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
