# Not sure that everyone will read README so I leave it here.
# This refactor may seem overcomplicated (and it is), but it's made for 2 reasons: 
# to implement important principles and make it within the boundaries of using only print, input and own functions.

# Principles behind this code:
# 1. Stories are stored as dictionaries for human-readable naming and easy addition of new stories.
# 2. Missing words are referenced by short names for readability and flexibility.
# 3. Prompts are stored in dictionaries for reusability across templates.

from random import choice

def tell_story(story) -> str:
    """
    This function finds all placeholders in the text and replaces them with user input
    It contains an imperfect simulator of RegExp for identifying placeholders in the text.
    """
    # Iterating through the text to find every placeholder occurrence, 
    # then assigning these placeholders to the placeholders variable.
    placeholders = [word[1:-1] for word in story.split() if word.startswith("{")] 
    # Iterating through every placeholder in placeholders list
    for placeholder in placeholders:
        # Transform the placeholder to match the format in the prompts dictionary
        # E.g. "transport"} -> "transport", "number" -> "number"
        prompt_key = placeholder.split("}")[0]
        # Replace each placeholder with user input, choosing a random prompt from the prompts dictionary
        if prompt_key in prompts:
            story = story.replace(f"{{{prompt_key}}}", input(choice(prompts[prompt_key])), 1)
    print(story)

def create_stories_list() -> dict:
    """
    Creates and returns a dictionary with the ordinal numbers and story names.
    Prints the ordinal number and name of each story, helping a user select a story.
    """

    counter = 0 # Initialize a story number
    story_numbers_dict = {} # Initialize a dictionary for "story number": "Name of the story"
    for story_name in stories: 
        counter += 1 # Numerate every story starting from 1
        print(counter, story_name) # Print story number and name for story selection
        story_numbers_dict[f'{counter}'] = story_name # Add "story number": "Name of the story" to dictionary
    return story_numbers_dict


# Dictionary of prompts groupped by missing word short discription. 
# Format - {"missing word short discription": ["Prompt for this word 1", "Prompt... n"]}
prompts = {
    "number":              ["Write a number: ", "Type a number: ", "Type a numerical value: ", "Random number? ", 
                            "Name a prime number: "],
    "measure_of_time":     ["Write a measure of time: ", "Name a unit of time: ", "Duration of time? ", 
                            "Common unit of time? "],
    "transport":           ["Name a transport: ", "Using what transport can someone arrive? "],
    "adjective":           ["Write an adjective: ", "Type an adjective: ", "Pick an adjective: ", 
                            "Select an adjective: ", "Favorite adjective? ", "Describe a quality: "],
    "adjective_feeling":   ["Write an adjective that describes a feeling: ", "Type an adjective expressing a feeling: "],
    "noun":                ["Write a noun: ", "Name a noun: ", "Type a noun: ", "Pick a noun: ", "Provide a noun: ", 
                            "Common noun? ", "Singular noun? "],
    "noun_pl":             ["Write a plural noun: ", "Type a plural noun: "],
    "color":               ["Name a color: ", "Pick a color: ", "Favorite color? ", "Rainbow color? ", "Some color? "],
    "body_part":           ["Write a part of the body: ", "Name a part of the body: "],
    "verb":                ["Write a verb: ", "Type a verb: ", "Action word? ", "Common verb? ", "Some verb? "],
    "verb_ing":            ["Write a verb ending in 'ing': ", "Type a verb ending in 'ing': "],
    "silly_word":          ["Choose a silly word: ", "Come up with a silly word: "],
    "person_name":         ["Write a person's Name: ", "What's a person's name? "],
    "animal":              ["Type an animal: ", "Name an animal: "],
    "place":               ["Name a place: ", "Describe a place: "],
    "adverb_ly":           ["Type an adverb ending in 'ly': ", "Write an adverb that ends with 'ly': "],
    "magical_creature_pl": ["Name a magical creature (plural): ", "Type a magical creature (plural): "],
    "room_in_a_house":     ["Name a room in a house: ", "What's a room in a house? "],
    }

# Dictionary of story templates. The placeholders in template corresponds with prompts dictionary keys.
# Format - {"Name of the story": "Story template"}
stories = {
    "Hospital days": """It was about {number} {measure_of_time} ago when I arrived at the hospital in a {transport}. 
The hospital is a {adjective} place, there are a lot of {adjective} {noun} here. 
There are nurses here who have {color} {body_part}. 
If someone wants to come into my room I told them that they have to {verb} first. 
I've decorated my room with {number} {noun}. 
Today I talked to a doctor and they were wearing a {noun} on their {body_part}. 
I heard that all doctors {verb} {noun} every day for breakfast. 
The most {adjective} thing about being in the hospital is the {silly_word} {noun}!""",

    "Camping adventure": """This weekend I am going camping with {person_name}. 
I packed my lantern, sleeping bag, and {noun}. I am so {adjective_feeling} to {verb} in a tent. 
I am {adjective_feeling} we might see a {animal}, I hear they're kind of dangerous. 
While we're camping, we are going to hike, fish, and {verb}. 
I have heard that the {color} lake is great for {verb_ing}. 
Then we will {adverb_ly} hike through the forest for {number} {measure_of_time}. 
If I see a {color} {animal} while hiking, I am going to bring it home as a pet! 
At night we will tell {number} {silly_word} stories and roast {noun} around the campfire!""",

    "Something magical": """Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest. 
I found myself here one day after going for a ride on a {color} {animal} in {place}. 
There are {adjective} {magical_creature_pl} and {adjective} {magical_creature_pl} here! 
In the {room_in_a_house} there is a pool full of {noun}. 
I fall asleep each night on a {noun} of {noun_pl} and dream of {adjective} {noun_pl}. 
It feels as though I have lived here for {number} {measure_of_time}. 
I hope one day you can visit, although the only way to get here  is {verb_ing} on a {adjective} {noun}!"""
}

#Main part of the code
print("Please choose your story by typing one of the following numbers or story's name: \n")
stories_dict = create_stories_list() # Showing a number of a story and its name
story_choice = input("\nWhen you've made your choice, please enter the requested words before you see the story.\n") 

# Validate the input to find the corresponding story by number or name
if story_choice in stories_dict.keys(): 
    tell_story(stories[stories_dict.get(story_choice)]) 
elif story_choice in stories:
    tell_story(stories[story_choice])
else:
    print ("""\nSorry, there's no story with such number or name. 
You need to type its number, for example: 1 or name, for example: Hospital days""")