# Loop back to this point once code finishes

loop = 1
while (loop < 10):
    noun_1 = input("Enter a Noun ")
    pronoun = input("Enter a Pronoun ")
    noun_2 = input("Enter another Noun ")
    place = input("ENter a Place ")
    adjective = input("Enter an Adjective ")
    noun_3 = input ("Enter one more noun ")

# Displays the story based on the users input

    print("----------------------------------------")
    print("Be kind to your", noun_1, "- footed", pronoun)
    print("For a duck may be somebody's", noun_2)
    print("Be kind to your", pronoun, "in", place)
    print("Where the weather is always", adjective, ".")
    print()
    print("You may think that is this the", noun_3, ",")
    print("Well it is.")
    print("-----------------------------------------")

    # Loop back to "Loop =1"
    loop = loop + 1


