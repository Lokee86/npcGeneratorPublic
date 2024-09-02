from openai import OpenAI
import random
from constants import *
from classes import *


def creature_type():
    creature = input("Would you like to generate a monster or an NPC? ").strip().lower()
    while True:
        
        if creature == "monster":
            creature_type = Monster()
            return creature_type
        elif creature == "npc":
            creature_type = NPC()
            return creature_type
        else:
            creature = input("Please enter either 'monster' or 'NPC' ").strip().lower()
    

def basic_info(client, creature):
    opinion = input("Would you like to combine sex and gender? Answering with a question may produce undesirable results. ")
    parsed_opinion = client.chat.completions.create(
    model = "",
    messages = GENDER_PAYLOAD + [{"role": "user", "content": f"{opinion}"}]
    )
    if parsed_opinion.choices[0].message.content.lower() == "no":
        creature.sex = input("What is the sex of your NPC? ")
        creature.gender = input("What gender is your NPC? ")
    else:
        creature.gender = input("What is the gender of your NPC? ")

    creature.genre = input("What is the genre of your game's setting? ")
    creature.species = input("What species is your NPC? (Leave blank for random) ")

    if creature.gender == "":
        creature.gender = random.choice(["male", "female", "non-binary"])
    if creature.genre == "":
        creature.genre = "agnostic"

    

def get_name_lists(client, creature):

    first_names = client.chat.completions.create(
    model = "",
    messages = NAME_PAYLOAD + [{"role": "user", "content": f"Give me a list of 25 {creature.species} {creature.genre} setting first names for a {creature.gender}."}],
    temperature = 1.0,
    top_p = 1.0,
    max_tokens = 500,
    frequency_penalty = 2,
    presence_penalty = 2
    )
    
    last_names = client.chat.completions.create(
    model = "",
    messages = NAME_PAYLOAD + [{"role": "user", "content": f"Give me a list of 25 {creature.genre} setting {creature.species} surnames."}],
    temperature = 1.0,
    top_p = 1.0,
    max_tokens = 500,
    frequency_penalty = 2,
    presence_penalty = 2
    )

    first_posibilities = first_names.choices[0].message.content.split()
    last_posibilities = last_names.choices[0].message.content.split()

    return first_posibilities, last_posibilities

def generate_name(firsts, lasts):
    
    name = f"{firsts[random.randint(0, len(firsts) - 1)]} {lasts[random.randint(0, len(lasts) - 1)]}"
    
    print(f"Your NPCs name is {name}")
    
    satisfied = input("Would you like to roll for another name? ").strip().lower()
    if satisfied != "n":
        return generate_name(firsts, lasts)
    else:
        return name

def generate_details(client, creature):
    
    manual_check = input("Are there any details you would like to manually include[Y/n]? ").strip().lower()
    if manual_check == "y":
        for trait in creature.details:
            if isinstance(creature.details[trait], dict):
                for subtrait in creature.details[trait]:
                    print(f"    {subtrait.title()}:")
            print(trait.title() + ":")



# MAIN FUNCTION BEGINS HERE
def main():
    # Point to the local server
    client = OpenAI(base_url="http://172.21.224.1:4321/v1", api_key="lm-studio")
    
    creature = creature_type()

    basic_info(client, creature)
    
    first_names, last_names = get_name_lists(client, creature)
    
    creature.name = generate_name(first_names, last_names)

    generate_details(client,creature)

    print(creature)
    

if __name__ == "__main__":
    main()