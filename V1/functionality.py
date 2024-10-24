from openai import OpenAI
import random
import tkinter as tk
from constants import *
from classes import *
import json as jn
import os

token_usage = {"total_tokens" : 0,
               "completion_tokens" : 0,
               "prompt_tokens" : 0}

session_tokens = {"session_totals" : {"total_tokens" : 0,
                                      "completion_tokens" : 0,
                                      "prompt_tokens" : 0}}

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
    model = MODEL,
    messages = NAME_PAYLOAD + FIRST_NAME(creature.species, creature.genre, creature.gender),
    temperature = 1.0,
    top_p = 1.0,
    max_tokens = 500,
    frequency_penalty = 2,
    presence_penalty = 2
    )
    
    last_names = client.chat.completions.create(
    model = MODEL,
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
    model = MODEL,
    messages = MONSTER_NAME_PAYLOAD + MONSTER_INFO(creature),
    # response_format = {"type": "json_object", "schema": LIST_SHCEMA},
    temperature = 1.0,
    max_tokens = 500,
    presence_penalty = 1
    )

    try:
        gui.random_names["firsts"] = jn.loads(names.choices[0].message.content.strip('`json'))
    except jn.JSONDecodeError as e:
        print(f"Error: {e}.\nBad json format: Attepmting generation again")
        print(names.choices[0].message.content)
        generate_name_list(client, creature, gui)

    token_usage["total_tokens"] += names.usage.total_tokens
    token_usage["completion_tokens"] += names.usage.completion_tokens
    token_usage["prompt_tokens"] += names.usage.prompt_tokens

def generate_name(creature, gui):
    firsts = gui.random_names["firsts"]
    if gui.random_names["lasts"]:
        lasts = creature.random_names["lasts"]
        name = f"{firsts[random.randint(0, len(firsts) - 1)]} {lasts[random.randint(0, len(lasts) - 1)]}"
    else:
        name = firsts[random.randint(0, len(firsts) - 1)]
    
    creature.name = name
    gui.name_var.set(creature.name)
    

def list_picker(creature, field_name, variable, choices): # Will only work for *entry* fields with a list to pick from.
    picked = random.randint(0, len(choices) - 1)
    setattr(creature, field_name, choices[picked])
    variable.set(choices[picked])

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

def generate_dict_to_text_field(client, payload, payload_info, creature, creature_field, gui_variable):

    generations = client.chat.completions.create(
    model = MODEL,
    messages = payload + payload_info(creature),
    # response_format = {"type": "json_object", "schema": MOTIVATIONS_SCHEMA},
    temperature = 1.0,
    max_tokens = 2000,
    )

    try:
        generated_dict = jn.loads(generations.choices[0].message.content.strip('`json'))
    except jn.JSONDecodeError as e:
        print(f"Error: {e}.\nBad json format: Attepmting generation again")
        print(generations.choices[0].message.content)
        generate_dict_to_text_field(client, payload, payload_info, creature, creature_field, gui_variable)
    
    
    dict_string = process_json_to_string(generated_dict)
    gui_variable.set(dict_string)

    token_usage["total_tokens"] += generations.usage.total_tokens
    token_usage["completion_tokens"] += generations.usage.completion_tokens
    token_usage["prompt_tokens"] += generations.usage.prompt_tokens

    match creature_field:
        case "abilities": set_abilities(creature, generated_dict)
        case "motivations": set_motivations(creature, generated_dict)
        case "tactics": set_tactics(creature, generated_dict)


def set_tactics(creature, tactics):
    creature.tactics = tactics

def set_abilities(creature, abilities):
    creature.abilities = abilities

def set_motivations(creature, motivations):
    creature.motivations = motivations

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




def state_check(creature, gui): # This is just being used for building and debugging. Currently tied to the save button.
    
    stats = ""
    for stat in gui.stat_entries:
        stats += f"{stat[2].get()} "
    
    print(creature)

def main(creature, gui):

    
    client = initialize_client()
    for total in token_usage:
        token_usage[total] = 0

    if not gui.select_enemy_var.get():
        list_picker(creature, "NPC_class", gui.select_enemy_var, ENEMY_CLASSES)
    elif gui.select_enemy_gen_check.get():
        list_picker(creature, "NPC_class", gui.select_enemy_var, ENEMY_CLASSES)
    else:
        creature.NPC_class = gui.select_enemy_var.get()

    if gui.genre_gen_check.get():
        list_picker(creature, "genre", gui.genre_var, GENRES)
    else:
        creature.genre = gui.genre_var.get()

    # if isinstance(creature, NPC):  ## NPC function not enabled.
    #     if gui.species_gen_check.get():
    #         list_picker(creature.species, gui.species_var, SPECIES)

    if gui.category_gen_check.get():
        list_picker(creature, "genre", gui.category_var, CATEGORIES)
    else:
        creature.category = gui.category_var.get()

    if gui.size_gen_check.get():
        list_picker(creature, "size", gui.size_var, SIZES)
    else:
        creature.size = gui.size_var.get()

    if gui.habitat_gen_check.get():
        list_picker(creature, "habitat", gui.habitat_var, HABITATS)
    else:
        creature.habitat = gui.habitat_var

    if gui.skills_gen_check.get():
        generate_skills(creature, gui)
    else:
        pass
    
    if gui.name_gen_check.get():
        if not gui.random_names["firsts"]:
            generate_name_list(client, creature, gui)
        elif gui.name_list_gen_check.get():
            generate_name_list(client, creature, gui)
        
        generate_name(creature, gui)
    else:
        creature.name = gui.name_var.get()

    if gui.stat_gen_check.get():
        generate_stats(creature, gui)
    else:
        for stat in gui.stat_entries:
            creature.stat_block[stat[0]] = stat[2].get()

    if gui.abilities_gen_check.get():
        generate_dict_to_text_field(client, ABILITY_PAYLOAD, ABILITY_INFO, creature, "abilities", gui.abilities_var)
    else:
        pass
    
    if gui.motivations_gen_check.get():
        generate_dict_to_text_field(client, MOTIVATIONS_PAYLOAD, MOTIVATIONS_INFO, creature, "motivations", gui.motivations_var)
    else:
        pass

    if gui.tactics_gen_check.get():
        generate_dict_to_text_field(client, TACTICS_PAYLOAD, TACTICS_INFO, creature, "tactics", gui.tactics_var)
    else:
        pass

    for total in token_usage:
        session_tokens["session_totals"][total] += token_usage[total]

    
    gui.add_name_list_check()
    
    print(token_usage)
    print(session_tokens)
    