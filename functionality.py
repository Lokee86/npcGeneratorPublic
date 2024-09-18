from openai import OpenAI
import random
from constants import *
from classes import *


def initialize_client():
    return OpenAI(base_url="http://172.21.224.1:4321/v1", api_key="lm-studio")

def creature_type(creature):
    if creature == "monster":
        creature = Monster()
        return creature
    elif creature == "npc":
        creature = NPC()
        return creature   

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

def generate_name(firsts, lasts):
    
    name = f"{firsts[random.randint(0, len(firsts) - 1)]} {lasts[random.randint(0, len(lasts) - 1)]}"
    
    print(f"Your NPCs name is {name}")
    
    satisfied = input("Would you like to roll for another name? ").strip().lower()
    if satisfied != "n":
        return generate_name(firsts, lasts)
    else:
        return name
    
def main():
    pass