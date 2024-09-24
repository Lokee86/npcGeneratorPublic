from openai import OpenAI
import random
import tkinter as tk
from constants import *
from classes import *
import json as jn
import os

def initialize_client():
    return OpenAI(base_url="https://api.openai.com/v1/", api_key=os.environ.get("API_KEY"))

def creature_type(creature_type):
    if creature_type == "monster":
        creature_type = Monster()
        return creature_type
    elif creature_type == "npc":
        creature_type = NPC()
        return creature_type   

# To be refactored using if-statements for type diffentiation. Refactoring into generate_name_list()
# Will be done when NPC generation is implemented.
def generate_npc_name_lists(client, creature, gui): 

    first_names = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = NAME_PAYLOAD + FIRST_NAME(creature.species, creature.genre, creature.gender),
    temperature = 1.0,
    top_p = 1.0,
    max_tokens = 500,
    frequency_penalty = 2,
    presence_penalty = 2
    )
    
    last_names = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = NAME_PAYLOAD + LAST_NAME(creature.species, creature.genre),
    temperature = 1.0,
    top_p = 1.0,
    max_tokens = 500,
    frequency_penalty = 2,
    presence_penalty = 2
    )

    names = first_names.choices[0].message.content.split()
    for name in names:
        if name:
            gui.random_names["firsts"].append(name.replace("\n", "").strip('()\'.<>?"[]\\[] ,'))
    names = last_names.choices[0].message.content.split()
    for name in names:
        if name:
            gui.random_names["lasts"].append(name.replace("\n", "").strip('()\'.<>?"[]\\[] ,'))

def generate_name_list(client, creature, gui):
    
    names = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = MONSTER_NAME_PAYLOAD,
    # response_format = {"type": "json_object", "schema": LIST_SHCEMA},
    temperature = 1.0,
    max_tokens = 500,
    presence_penalty = 1
    )

    try:
        gui.random_names["firsts"] = jn.loads(names.choices[0].message.content)
    except jn.JSONDecodeError as e:
        print(f"Error: {e}.\nBad json format: Attepmting generation again")
        generate_name_list(client, creature, gui)

def generate_name(creature, gui):
    firsts = gui.random_names["firsts"]
    if gui.random_names["lasts"]:
        lasts = creature.random_names["lasts"]
        name = f"{firsts[random.randint(0, len(firsts) - 1)]} {lasts[random.randint(0, len(lasts) - 1)]}"
    else:
        name = firsts[random.randint(0, len(firsts) - 1)]
    
    creature.name = name
    gui.name_var.set(creature.name)
    

def generate_genre(creature, gui):
    genre = random.randint(0, len(GENRES) - 1)
    creature.genre = GENRES[genre]
    gui.genre_var.set(GENRES[genre])

def generate_species(client, creature, gui): # Not required for monster generation, implement with NPCs
    pass

def generate_category(creature, gui):
    pass

def generate_size(creature, gui):
    pass

def generate_habitat(creature, gui):
    pass

def generate_skills(creature, gui):
    skill_count = random.randint(0, 5)
    skills = 0
    creature.skills = []
    while skills < skill_count:
        new_skill = random.choice(SKILLS)
        if new_skill not in creature.skills:
            creature.skills.append(new_skill)
            skills += 1

    skills_string = process_json_to_string(creature.skills)
    gui.skills_var.set(skills_string)
    
def generate_stats(creature, gui):
    for stat in creature.stat_block:
        creature.stat_block[stat] = str(random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10))
    for i in range(0, len(creature.stat_block)):
        gui.stat_entries[i][2].set(creature.stat_block[gui.stat_entries[i][0]])

def generate_abilities(client, creture, gui):
    pass

def generate_motivations(client, creature, gui):
    if isinstance(creature, NPC):
        species = creature.species
    else:
        species = creature.name

    motivations = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = MOTIVATIONS_PAYLOAD + MOTIVATIONS_INFO(creature, species, MOTIVATIONS),
    # response_format = {"type": "json_object", "schema": MOTIVATIONS_SCHEMA},
    temperature = 1.0,
    max_tokens = 500,
    )

    try:
        creature.motivations = jn.loads(motivations.choices[0].message.content)
    except jn.JSONDecodeError as e:
        print(f"Error: {e}.\nBad json format: Attepmting generation again")
        generate_motivations(creature, client)
    
    motivations_string = process_json_to_string(creature.motivations)
    gui.motivations_var.set(motivations_string)

def generate_tactics(client, creature, gui):
    pass

def process_json_to_string(json_object, indent_level=0):
    # Recursively process a dictionary into a human-readable string format
    # without JSON-specific formatting (no quotes, braces, commas).
    output_str = ""
    indent = "  " * indent_level  # Increase indentation for nested structures

    # Check if the json_object is a dictionary
    if isinstance(json_object, dict):
        for key, value in json_object.items():
            if isinstance(value, dict):
                output_str += f"{indent}{key.replace('_', ' ').capitalize()}:\n"
                output_str += process_json_to_string(value, indent_level + 2)
            elif isinstance(value, list):
                output_str += f"{indent}{key.replace('_', ' ').capitalize()}:\n"
                for item in value:
                    if isinstance(item, dict):  # Recursively process dict items in the list
                        output_str += process_json_to_string(item, indent_level + 4)
                    else:
                        output_str += f"{' ' * (indent_level + 4)}- {str(item).capitalize()}\n"
            else:
                output_str += f"{indent}{key.replace('_', ' ').capitalize()}: {str(value).capitalize()}\n"

    # Check if the json_object is a list
    elif isinstance(json_object, list):
        if any(isinstance(item, dict) for item in json_object):
            for item in json_object:
                if isinstance(item, dict):
                    output_str += process_json_to_string(item, indent_level + 2)
                else:
                    output_str += f"{' ' * indent_level}- {str(item).capitalize()}\n"
        else:
            for index, item in enumerate(json_object):
                if index < len(json_object) - 1:
                    output_str += f"{item}, "
                else:
                    output_str += item

    return output_str


def state_check(creature, gui):
    
    print(creature)
    print(gui.skills_entry.index(f"{tk.END}-1c"))



def main(creature, gui):

    client = initialize_client()
    if gui.genre_gen_check.get():
        creature.genre = generate_genre(creature, gui)
    
    if gui.name_gen_check.get():
        if not gui.random_names["firsts"]:
            generate_name_list(client, creature, gui)
        
        generate_name(creature, gui)

    if isinstance(creature, NPC):
        if gui.species_gen_check.get():
            pass

    if gui.category_gen_check.get():
        pass

    if gui.size_gen_check.get():
        pass

    if gui.habitat_gen_check.get():
        pass

    if gui.skills_gen_check.get():
        generate_skills(creature, gui)
    
    if gui.stat_gen_check.get():
        generate_stats(creature, gui)

    if gui.abilities_gen_check.get():
        pass
    
    if gui.motivations_gen_check.get():
        generate_motivations(client, creature, gui)

    if gui.tactics_gen_check.get():
        pass

    