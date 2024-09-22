from openai import OpenAI
import random
import tkinter as tk
from constants import *
from classes import *
import json as jn

def initialize_client():
    return OpenAI(base_url="http://172.21.224.1:4321/v1", api_key="lm-studio")

def creature_type(creature_type):
    if creature_type == "monster":
        creature_type = Monster()
        return creature_type
    elif creature_type == "npc":
        creature_type = NPC()
        return creature_type   

def generate_npc_name_lists(client, creature, gui):

    first_names = client.chat.completions.create(
    model = "",
    messages = NAME_PAYLOAD + FIRST_NAME(creature.species, creature.genre, creature.gender),
    temperature = 1.0,
    top_p = 1.0,
    max_tokens = 500,
    frequency_penalty = 2,
    presence_penalty = 2
    )
    
    last_names = client.chat.completions.create(
    model = "",
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
    model = "",
    messages = MONSTER_NAME_PAYLOAD,
    response_format = LIST_SHCEMA,
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

def generate_species(client, creature, gui):
    pass

def generate_category(creature, gui):
    pass

def generate_size(creature, gui):
    pass

def generate_habitat(creature, gui):
    pass

def generate_skills(client, creature, gui):
    pass

def generate_stats(creature):
    for stat in creature.stat_block:
        creature.stat_block[stat] = str(random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10))

def generate_motivations(client, creature):
    if isinstance(creature, NPC):
        species = creature.species
    else:
        species = creature.name
    motivations = client.chat.completions.create(
    model = "",
    messages = MOTIVATIONS_PAYLOAD + MOTIVATIONS_INFO(creature, species, MOTIVATIONS),
    response_format = MOTIVATIONS_SCHEMA,
    temperature = 1.0,
    max_tokens = 500,
    )

    try:
        creature.motivations = jn.loads(motivations.choices[0].message.content)
    except jn.JSONDecodeError as e:
        print(f"Error: {e}.\nBad json format: Attepmting generation again")
        generate_motivations(creature, client)

def generate_tactics(client, creature, gui):
    pass

def process_json_to_string(data_dict, indent_level=0):
    # Recursively process a dictionary into a human-readable string format
    # without JSON-specific formatting (no quotes, braces, commas).
    output_str = ""
    indent = "  " * indent_level  # Increase indentation for nested structures

    for key, value in data_dict.items():
        if isinstance(value, dict):
            output_str += f"{indent}{key.replace('_', ' ').capitalize()}:\n"
            output_str += process_json_to_string(value, indent_level + 2)
        elif isinstance(value, list):
            output_str += f"{indent}{key.replace('_', ' ').capitalize()}:\n"
            for item in value:
                output_str += f"{indent}  - {item.capitalize()}\n"
        else:
            output_str += f"{indent}{key.replace('_', ' ').capitalize()}: {value.capitalize()}\n"

    return output_str


def state_check(creature, gui):
    
    print(creature)



def main(creature, gui):

    client = initialize_client()
    if gui.genre_gen_check.get():
        creature.genre = generate_genre(creature, gui)
    
    if gui.name_gen_check.get():
        if not gui.random_names["firsts"]:
            if isinstance(creature, NPC):
                generate_npc_name_lists(client, creature, gui)
            else:
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
        pass
    
    if gui.stat_gen_check.get():
        generate_stats(creature)
        for i in range(0, len(creature.stat_block)):
            gui.stat_entries[i][2].set(creature.stat_block[gui.stat_entries[i][0]])

    if gui.abilities_gen_check.get():
        pass
    
    if gui.motivations_gen_check.get():
        generate_motivations(client, creature)
        motivations_string = process_json_to_string(creature.motivations)
        gui.motivations_var.set(motivations_string)

    if gui.tactics_gen_check.get():
        pass

    