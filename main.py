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

def manual_trait_input(trait_dict):
    
    manual_check = input("Are there any details you would like to manually include[Y/n]? ").strip().lower()
    if manual_check == "y":
        print("\nAvailable Traits and Subtraits:\n")
        for trait, value in trait_dict.items():
            print(trait.title().replace("_", " ") + ":")
            if isinstance(value, dict):
                for subtrait in value:
                    print(f"    {subtrait.title().replace('_', ' ')}: {value[subtrait]}")

        cancel = False
        while True:
            if cancel:
                manual_input = input("Would you like to manually input a different trait? [Type 'Cancel' to go back]").strip().lower()
                if manual_input == "cancel":
                    return
                cancel = False  # Reset cancel after re-prompting

            manual_input = input("Which trait would you like to manually enter? [Type 'Cancel' to go back] ").strip().lower()
            if len(manual_input.split()) > 1:
                manual_input = "_".join(manual_input.split())
            if manual_input == "cancel":
                break

            if manual_input in trait_dict:
                if isinstance(trait_dict[manual_input], dict):
                    while True:
                        sub_input = input(f"Which subtrait of {manual_input.replace('_', ' ')} would you like to enter? [Type 'Cancel' to go back] ").strip().lower()
                        if sub_input == "cancel":
                            cancel = True
                            break
                        if sub_input in trait_dict[manual_input]:
                            new_value = input(f"Please enter your manual choice for {sub_input.replace('_', ' ')}: ").strip().lower()
                            trait_dict[manual_input][sub_input] = new_value
                            break
                        else:
                            print("Invalid subtrait.")
                elif isinstance(trait_dict[manual_input], list):
                    new_value = input(f"Please enter your manual choice to append to the list for {manual_input.replace('_', ' ')}: ").strip().lower()
                    trait_dict[manual_input].append(new_value)
                    cancel = True
                    continue                
                else:
                    new_value = input(f"Please enter your manual choice for {manual_input.replace('_', ' ')}: ").strip().lower()
                    trait_dict[manual_input] = new_value
                    cancel = True
                    continue  # Continue to re-check if further input is needed

            elif any(manual_input in subdict for subdict in trait_dict.values() if isinstance(subdict, dict)):
                for trait, subtraits in trait_dict.items():
                    if isinstance(subtraits, dict) and manual_input in subtraits:
                        if isinstance(subtraits[manual_input], list):
                            new_value = input(f"Please enter your manual choice to append to the list for {manual_input.replace('_', ' ')}: ").strip().lower()
                            subtraits[manual_input].append(new_value)
                        else:
                            new_value = input(f"Please enter your manual choice for {manual_input}: ").strip().lower()
                            subtraits[manual_input] = new_value
                        break

            else:
                print("Invalid trait.")



# MAIN FUNCTION BEGINS HERE
def main():
    # Point to the local server
    client = OpenAI(base_url="http://172.21.224.1:4321/v1", api_key="lm-studio")
    
    creature = creature_type()

    # basic_info(client, creature)
    
    # first_names, last_names = get_name_lists(client, creature)
    
    # creature.name = generate_name(first_names, last_names)

    if type(creature) == NPC:
        manual_trait_input(creature.motivations)

    print(creature)
    

if __name__ == "__main__":
    main()