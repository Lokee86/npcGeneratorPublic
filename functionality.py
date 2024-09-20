from openai import OpenAI
import random
import tkinter as tk
from constants import *
from classes import *


def initialize_client():
    return OpenAI(base_url="http://172.21.224.1:4321/v1", api_key="lm-studio")

def creature_type(creature_type):
    if creature_type == "monster":
        creature_type = Monster()
        return creature_type
    elif creature_type == "npc":
        creature_type = NPC()
        return creature_type   

def generate_npc_name_lists(client, creature):

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

    creature.random_names["firsts"] = first_names.choices[0].message.content.split()
    creature.random_names["lasts"] = last_names.choices[0].message.content.split()

def generate_name(creature):
    firsts = creature.random_names["firsts"]
    if creature.random_names["lasts"]:
        lasts = creature.random_names["lasts"]
        name = f"{firsts[random.randint(0, len(firsts) - 1)]} {lasts[random.randint(0, len(lasts) - 1)]}"
    else:
        name = firsts[random.randint(0, len(firsts) - 1)]
    return name
    
def generate_creature_name(client, creature):
    
    rough_names = client.chat.completions.create(
    model = "",
    messages = MONSTER_NAME_PAYLOAD,
    temperature = 1.0,
    top_p = 1.0,
    max_tokens = 500,
    frequency_penalty = 2,
    presence_penalty = 2
    )

    names = client.chat.completions.create(
    model = "",
    messages = [{"role": "system", "content": """ [Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason. Analyze the following prompt, and return a json formatted list of names from the input, remove any superfluous punctuation, symbols or titles."""},
{"role": "user", "content": f"{rough_names.choices[0].message.content.split()}"}],
    temperature = 1.0,
    top_p = 1.0,
    max_tokens = 500,
    frequency_penalty = 2,
    presence_penalty = 2
    )
    print(names.choices[0].message.content.split(","))
    names = names.choices[0].message.content.split(",")
    for name in names:
        creature.random_names["firsts"].append(name.replace("\n", "").strip('()\'.<>?"[]\\[] ,1234567890'))


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
        creature.stat_block[stat] = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)

def generate_motivations(client, creature, gui):
    pass

def generate_tactics(client, creature, gui):
    pass


def state_check(gui):
    
    info = gui.motivations_entry.index(tk.END)
    content_height = int(gui.motivations_entry.index(tk.END).split(".")[0])
    print(content_height, info)


    # if info:
    #     x, y, width, height, baseline = info
    #     print(f"Line display info: x={x}, y={y}, width={width}, baseline={baseline}")
    # else:
    #     print("The line at index '1.0' is not visible or doesn't exist.")





def main(creature, gui):

    client = initialize_client()
    if gui.genre_gen_check.get():
        creature.genre = generate_genre(creature, gui)
    
    if gui.name_gen_check.get():
        if not creature.random_names["firsts"]:
            if isinstance(creature, NPC):
                generate_npc_name_lists(client, creature)
            else:
                generate_creature_name(client, creature)
        
        name = generate_name(creature)
        creature.name = name
        gui.name_var.set(name)

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
        pass

    if gui.tactics_get_check.get():
        pass

    