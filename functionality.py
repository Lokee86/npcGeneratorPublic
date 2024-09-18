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

def get_name_lists(client, creature):

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

    first_posibilities = first_names.choices[0].message.content.split()
    last_posibilities = last_names.choices[0].message.content.split()

    return first_posibilities, last_posibilities

def generate_name(client, creature, gui):

    firsts, lasts = get_name_lists(client, creature, gui)

    name = f"{firsts[random.randint(0, len(firsts) - 1)]} {lasts[random.randint(0, len(lasts) - 1)]}"
    
    return name, firsts, lasts
    
def generate_creature_name(client, gui):
    
    names = client.chat.completions.create(
    model = "",
    messages = MONSTER_NAME_PAYLOAD,
    temperature = 1.0,
    top_p = 1.0,
    max_tokens = 500,
    frequency_penalty = 2,
    presence_penalty = 2
    )

    other_names = names.choices[0].message.content.split()
    name = other_names[random.randint(0, len(other_names)-1)]

    return name, other_names

def generate_stats(creature):
    for stat in creature.stat_block:
        creature.stat_block[stat] = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)

def generate_genre(creature):
    name = GENRES[random.randint(0, len(GENRES) - 1)]
    return name

def state_check(gui):
    print(gui.name_gen_check.get())




def main(creature, gui):

    client = initialize_client()
    
    if gui.genre_gen_check.get():
        creature.genre = generate_genre(creature)
        gui.genre_entry.delete(0, tk.END)
        gui.genre_entry.insert(0, creature.genre)
        print(creature.genre)
        
    
    if gui.name_gen_check.get():
        if not creature.random_names["firsts"]:
            if type(creature) == NPC:
                name, firsts, lasts = generate_name(client, creature, gui)        
                creature.random_names["firsts"] = firsts
                creature.random_names["lasts"] = lasts

            if type(creature) == Monster:
                name, other_names = generate_creature_name(client, gui)
                creature.random_names["firsts"] = other_names
            
            gui.name_entry.delete(0, tk.END)
            gui.name_entry.insert(0, name)
        else:
            if type(creature) == NPC:
                firsts = []
                lasts = []
                firsts = creature.random_names['firsts']
                lasts = creature.random_names['lasts']
                name = f"{firsts[random.randint(0, len(firsts) - 1)]} {lasts[random.randint(0, len(lasts) - 1)]}"
            if type(creature) == Monster:
                other_names = firsts = creature.random_names['firsts']
                name = other_names[random.randint(0, len(other_names)-1)]

            gui.name_entry.delete(0, tk.END)
            gui.name_entry.insert(0, name)
    
    if gui.stat_gen_check.get():
        generate_stats(creature)
        for i in range(0, len(creature.stat_block)):
            gui.stat_entries[i][1].delete(0, tk.END)
            gui.stat_entries[i][1].insert(0, creature.stat_block[gui.stat_entries[i][0]])