from random import choice

def get_input(prompt): # Get input and choose from one or more prompts
    return input(choice(prompt))

number = ["Write a number: ", "Type a numerical value: "]
measure_of_time = ["Write a unit of time: "]
mode_of_transportation = ["Name a mode of transportation: "]
adjective = ["Write an adjective: ", "Describe something with an adjective: ", "Type an adjective: ", "Pick an adjective: ", "Select an adjective: "]
adjective_feeling = ["Write an adjective that describes a feeling: ", "Type an adjective expressing a feeling: "]
noun = ["Write a noun: ", "Name a noun: ", "Name a noun: ", "Type a noun: ", "Pick a noun: "]
noun_plural = ["Write a plural noun: ", "Type a plural noun: "]
color = ["Name a color: "]
part_of_the_body = ["Write a part of the body: ", "Name a part of the body: "]
verb = ["Write a verb: ", "Type a verb: "]
verb_ending_in_ing = ["Write a verb ending in 'ing': "]
silly_word = ["Choose a silly word: "]
proper_noun_persons_name = ["Write a proper noun (Person's Name): "]
animal = ["Type an animal: "]
place = ["Name a place: "]
adverb_ending_in_ly = ["Type an adverb ending in 'ly': "]
magical_creature_plural = ["Name a magical creature (plural): ", "Identify a magical creature (plural): "]
room_in_a_house = ["Name a room in a house: "]



story = int(input("""    Please choose your story by selecting one of the following numbers:
      1. Hospital days
      2. Camping adventure
      3. Something magical \n
      When you have made your choice, please enter the requested words before you see the story." \n            
      """))

if story == 1:
    print(f"""It was about {get_input(number)} {get_input(measure_of_time)} ago when I arrived at the hospital in a {get_input(mode_of_transportation)}. 
The hospital is a {get_input(adjective)} place, there are a lot of {get_input(adjective)} {get_input(noun)} here. 
There are nurses here who have {get_input(color)} {get_input(part_of_the_body)}. 
If someone wants to come into my room I told them that they have to {get_input(verb)} first. 
I’ve decorated my room with {get_input(number)} {get_input(noun)}. 
Today I talked to a doctor and they were wearing a {get_input(noun)} on their {get_input(part_of_the_body)}. 
I heard that all doctors {get_input(verb)} {get_input(noun)} every day for breakfast. 
The most {get_input(adjective)} thing about being in the hospital is the {get_input(silly_word)} {get_input(noun)}!""")

elif story == 2:
    print(f"""This weekend I am going camping with {get_input(proper_noun_persons_name)}. 
I packed my lantern, sleeping bag, and {get_input(noun)}. I am so {get_input(adjective_feeling)} to {get_input(verb)} in a tent. 
I am {get_input(adjective_feeling)} we might see a {get_input(animal)}, I hear they’re kind of dangerous. 
While we’re camping, we are going to hike, fish, and {get_input(verb)}. 
I have heard that the {get_input(color)} lake is great for {get_input(verb_ending_in_ing)}. 
Then we will {get_input(adverb_ending_in_ly)} hike through the forest for {get_input(number)} {get_input(measure_of_time)}. 
If I see a {get_input(color)} {get_input(animal)} while hiking, I am going to bring it home as a pet! 
At night we will tell {get_input(number)} {get_input(silly_word)} stories and roast {get_input(noun)} around the campfire!!
""")

elif story == 3:
    print(f"""Dear {get_input(proper_noun_persons_name)}, I am writing to you from a {get_input(adjective)} castle in an enchanted forest. 
I found myself here one day after going for a ride on a {get_input(color)} {get_input(animal)} in {get_input(place)}. 
There are {get_input(adjective)} {get_input(magical_creature_plural)} and {get_input(adjective)} {get_input(magical_creature_plural)} here! 
In the {get_input(room_in_a_house)} there is a pool full of {get_input(noun)}. 
I fall asleep each night on a {get_input(noun)} of {get_input(noun_plural)} and dream of {get_input(adjective)} {get_input(noun_plural)}. 
It feels as though I have lived here for {get_input(number)} {get_input(measure_of_time)}. 
I hope one day you can visit, although the only way to get here now is {get_input(verb_ending_in_ing)} on a {get_input(adjective)} {get_input(noun)}!!
""") 
    
else: print("    Sorry, there are only 3 stories and nothing else. Write 1, 2 or 3 depending on what story you want to hear.")
