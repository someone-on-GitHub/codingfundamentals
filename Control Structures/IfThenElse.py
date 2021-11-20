foundanimal = False
while foundanimal == False:
    print("Enter the animal")
    animal = input()

    if animal == "dog":
        foundanimal = True
        print("the animal is a dog")
    elif animal == "cat":
        foundanimal = True
        print("the animal is a cat")
    elif animal == "bird":
        foundanimal = True
        print("the animal is a bird")
    elif animal == "hippo":
        foundanimal = True
        print("the animal is a hippo")
    else:
        print("I have no idea what this animal is!")
        print("do you want to try another animal, Y or N?")
        tryagain = input()
        if tryagain.upper() != "Y":
            foundanimal = True