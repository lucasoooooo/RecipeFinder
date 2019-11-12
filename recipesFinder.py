#Program will read list of ingredients recommend 
# possible meals user could make
# 8/27/2019 By Lucas Balangero
 
#Errors: dictonary if recipes includes "\n" in titles and ingredients
#Working on: removing the error "\n" 
#Missing: check what recipe to give the user based on his choices
#          and test

#Read File and saves into listOfIngredients
recipesAIngredients={}
listOfIngredients = []
title=""
with open("recipes.txt", "r") as f:
    for i,line in enumerate(iter(f.readline, '')):
        #i is line number; line is string in that line number
        if i%3 == 0: #every third line is a title
            title = line
        elif i%3 == 1:
            ingredients = line.split('*')
            for x in ingredients:
                listOfIngredients.append(x)
        elif i%3 == 2:
            recipesAIngredients[title]=[ingredients]
   


print(recipesAIngredients)
#removes repeates
listOfIngredients = list(dict.fromkeys(listOfIngredients))

#checks if ingredient exists

def checkIngredients(userInput):
    for x in listOfIngredients:
        if userInput.upper() == x.upper():
            userIngredients.append(userInput.upper())
            return True
    return False


print("~~~~   Welcome to Recipe Finder   ~~~~\n\n"
     
      "List a single ingredient and press enter\n"
      "  Type 'Done' when finished entering    \n")

userIngredients=[]
userInput=''
while True:
    userInput=input()
    if userInput.upper() == "DONE":
        break
    if checkIngredients(userInput):
        print("Successfully Added!")
    else:
        print("~Ingredient is not in any of the recipes~")
#Remove duplicates from list
userIngredients = list(dict.fromkeys(userIngredients))
print(userIngredients)