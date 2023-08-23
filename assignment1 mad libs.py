from random import choice

def put(prompt): # Function randomly choose one of the listed prompts and get an input
    return input(choice(prompt))
              
number = ["Write a number: ", "Type a numerical value: "]
measure_of_time = ["Write a measure of time: ", "Name a unit of time: "]
transport = ["Name a transport: ", "Using what transport did you arrive? "]
adjective = ["Write an adjective: ", "Type an adjective: ", "Pick an adjective: ", "Select an adjective: "]
adjective_feeling = ["Write an adjective that describes a feeling: ", "Type an adjective expressing a feeling: "]
noun = ["Write a noun: ", "Write down a noun: ", "Name a noun: ", "Type a noun: ", "Pick a noun: "]
noun_pl = ["Write a plural noun: ", "Type a plural noun: "]
color = ["Name a color: ", "Pick a color: "]
body_part = ["Write a part of the body: ", "Name a part of the body: "]
verb = ["Write a verb: ", "Type a verb: "]
verb_ing = ["Write a verb ending in 'ing': ", "Type a verb ending in 'ing': "]
silly_word = ["Choose a silly word: ", "Come up with a silly word: "]
person_name = ["Write a person's Name): ", "What's a person's name? "]
animal = ["Type an animal: ", "Name an animal: "]
place = ["Name a place: ", "Describe a place: "]
adverb_ly = ["Type an adverb ending in 'ly': ", "Write an adverb that ends with 'ly': "]
magical_creature_pl = ["Name a magical creature (plural): ", "Type a magical creature (plural): "]
room_in_a_house = ["Name a room in a house: ", "What's a room in a house? "]

story = input("""Please choose your story by typing one of the following numbers:
1. Hospital days
2. Camping adventure
3. Something magical  \n
When you have made your choice, please enter the requested words before you see the story. \n""")

if story == '1':
    print(f"""It was about {put(number)} {put(measure_of_time)} ago when I arrived at the hospital in a {put(transport)}. 
The hospital is a {put(adjective)} place, there are a lot of {put(adjective)} {put(noun)} here. 
There are nurses here who have {put(color)} {put(body_part)}. 
If someone wants to come into my room I told them that they have to {put(verb)} first. 
I’ve decorated my room with {put(number)} {put(noun)}. 
Today I talked to a doctor and they were wearing a {put(noun)} on their {put(body_part)}. 
I heard that all doctors {put(verb)} {put(noun)} every day for breakfast. 
The most {put(adjective)} thing about being in the hospital is the {put(silly_word)} {put(noun)}!""")

elif story == '2':
    print(f"""This weekend I am going camping with {put(person_name)}. 
I packed my lantern, sleeping bag, and {put(noun)}. I am so {put(adjective_feeling)} to {put(verb)} in a tent. 
I am {put(adjective_feeling)} we might see a {put(animal)}, I hear they’re kind of dangerous. 
While we’re camping, we are going to hike, fish, and {put(verb)}. 
I have heard that the {put(color)} lake is great for {put(verb_ing)}. 
Then we will {put(adverb_ly)} hike through the forest for {put(number)} {put(measure_of_time)}. 
If I see a {put(color)} {put(animal)} while hiking, I am going to bring it home as a pet! 
At night we will tell {put(number)} {put(silly_word)} stories and roast {put(noun)} around the campfire!""")

elif story == '3':
    print(f"""Dear {put(person_name)}, I am writing to you from a {put(adjective)} castle in an enchanted forest. 
I found myself here one day after going for a ride on a {put(color)} {put(animal)} in {put(place)}. 
There are {put(adjective)} {put(magical_creature_pl)} and {put(adjective)} {put(magical_creature_pl)} here! 
In the {put(room_in_a_house)} there is a pool full of {put(noun)}. 
I fall asleep each night on a {put(noun)} of {put(noun_pl)} and dream of {put(adjective)} {put(noun_pl)}. 
It feels as though I have lived here for {put(number)} {put(measure_of_time)}. 
I hope one day you can visit, although the only way to get here  is {put(verb_ing)} on a {put(adjective)} {put(noun)}!""") 

else: 
    print("Sorry, there are only 3 stories. You need to write: 1, 2 or 3 depending on what story you want to hear.")