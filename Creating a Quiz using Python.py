# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:57:55 2020

@author: Julie Ann Delda
"""

print("The Philippine Archipelago (Quiz)")
print("How well do you know the Philippine Archipelago? Take this quiz to find out.")
def main():
    
    questions={'What is the capital of the Republic of the Philippines? ':'Manila',
               '\nWhat is the "Summer Capital" of the Philippines? ':'Baguio City', 
               '\nWhat is the oldest city of the Philippines? ':'Cebu', 
               '\nWhat is the largest island of the Philippine Archipelago? ':'Luzon',
               '\nWhat is the longest mountain range in the Country? ':'Sierra Madre', 
               '\nWhere is the highest peak in the Philippines? ':'Mt. Apo', 
               '\nWhat is the longest river in the Philippines? ':'Cagayan River', 
               '\nWhat is the provincial capital of Isabela? ':'Ilagan', 
               '\nThe Philippines is composed of approximately how many islands? ':'7500', 
               '\nWhat is the largest province in the Philippines in terms of land area? ':'Palawan'}
    print("Goodluck! ^_^\n")
    name = input("Please enter your name: ").title()
    print("\nThank you for your time {0}, you scored {1} out of {2}.".format(name, quiz(questions), len(questions)))
 
def quiz(questions):
    score = 0
    for q,a in questions.items():
        if input(q).lower() == a.lower():
            score += 1
            print("Correct.")
    
        else:
            print("Sorry, correct answer is \"{}\".".format(a))

    return score    

if __name__ == "__main__":
    main()