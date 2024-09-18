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

def generate_genre():
    genre = random.randint(0, len(GENRES) - 1)
    return GENRES[genre]


def state_check(gui):
    print(gui.name_gen_check.get())




def main(creature, gui):

    client = initialize_client()
    if gui.genre_gen_check.get():
        creature.genre = generate_genre()
    
    if gui.name_gen_check.get():
        if not creature.random_names["firsts"]:
            if isinstance(creature, NPC):
                generate_npc_name_lists(client, creature)
            else:
                generate_creature_name(client, creature)
        
        name = generate_name(creature)

        gui.name_entry.delete(0, tk.END)
        gui.name_entry.insert(0, name)
    
    if gui.stat_gen_check.get():
        generate_stats(creature)
        for i in range(0, len(creature.stat_block)):
            gui.stat_entries[i][1].delete(0, tk.END)
            gui.stat_entries[i][1].insert(0, creature.stat_block[gui.stat_entries[i][0]])

    