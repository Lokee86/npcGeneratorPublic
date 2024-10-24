from constants20 import *

class Monster:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.size = ""
        self.habitat = ""
        self.ac = 0
        self.armor_type = ""
        self.hp = 0
        self.hit_dice = ""
        self.stats = {"str":0, "dex":0, "con":0, "int":0, "wis":0, "cha":0}
        self.saves = {"str":False, "dex":False, "con":False, "int":False, "wis":False, "cha":False}
        self.combat_role = ""
        self.speeds = {"run":0, "swim":0, "fly":0, "burrow":0}
        self.damage_tuning = {"bludgeoning":0, "piercing":0, "slashing":0, "acid":0, "cold":0, "fire":0, "lightning":0, "poison":0, "thunder":0, "force":0, "necrotic":0, "radiant":0, "psychic":0,}
        self.languages = []
        self.skills = {
        "Acrobatics": 0,
        "Animal Handling": 0,
        "Arcana": 0,
        "Athletics": 0,
        "Deception": 0,
        "History": 0,
        "Insight": 0,
        "Intimidation": 0,
        "Investigation": 0,
        "Medicine": 0,
        "Mechanica": 0,
        "Nature": 0,
        "Perception": 0,
        "Performance": 0,
        "Persuasion": 0,
        "Religion": 0,
        "Sleight of Hand": 0,
        "Spiritualism": 0,
        "Stealth": 0,
        "Survival": 0
        }
        self.weapon_tuning = {"adamantine":False, "cold iron":False, "living wood":False, "silvered":False, "mithral":False, "magical":False, "other":False}
        self.other_tuning = ""
        self.condition_immunities = {
        "Blinded": False,
        "Charmed": False,
        "Deafened": False,
        "Frightened": False,
        "Grappled": False,
        "Incapacitated": False,
        "Paralyzed": False,
        "Petrified": False,
        "Poison": False,
        "Prone": False,
        "Restrained": False,
        "Stunned": False,
        "Unconscious": False,
        "Bleeding": False,
        "Confused": False
        }
        self.senses = {"Darkvision": 0, "Blindsight": 0, "Truesight": 0, "Tremorsense": 0}
        self.description = ""
        self.abilities = ""
        self.actions = ""
        self.bonus_actions = ""
        self.reactions = ""
        self.legendary_actions = ""
        self.mythic_actions = ""



    def __str__(self):
        return self._generate_str()

    def formatted_str(self, *args):
        return self._generate_str(*args)

    def _generate_str(self, *ignore_attrs):
        # Recursively formats and prints nested dictionaries and ignores empty ones.
        def format_dict(d, indent=0):
            formatted_output = ""
            non_empty = False
            for key, value in d.items():
                if isinstance(value, dict):
                    nested_output, is_non_empty = format_dict(value, indent + 4)
                    if is_non_empty:
                        formatted_output += f"{' ' * indent}{key.replace('_', ' ').capitalize()}:\n{nested_output}"
                        non_empty = True
                elif isinstance(value, list):  # Handle lists of dictionaries
                    if value:
                        formatted_output += f"{' ' * indent}{key.replace('_', ' ').capitalize()}:\n"
                        for item in value:
                            if isinstance(item, dict):
                                nested_output, _ = format_dict(item, indent + 4)
                                formatted_output += nested_output  # Recursively process dictionary items
                            else:
                                formatted_output += f"{' ' * (indent + 4)}- {item.capitalize()}\n"
                        non_empty = True
                elif value:  # Check for non-empty string values
                    formatted_output += f"{' ' * indent}{key.replace('_', ' ').capitalize()}: {str(value).title()}\n"
                    non_empty = True
            return formatted_output, non_empty

        # Main output string for the Monster class attributes
        output = "\nMonster Information:\n"
        for attr, value in self.__dict__.items():
            # Skip attributes that are in the ignore list
            if attr in ignore_attrs:
                continue
            if isinstance(value, dict):
                nested_output, is_non_empty = format_dict(value)
                if is_non_empty:
                    output += f"{attr.replace('_', ' ').capitalize()}:\n{nested_output}"
            elif isinstance(value, list):
                if value:
                    output += f"{attr.replace('_', ' ').capitalize()}:\n"
                    for item in value:
                        output += f" -{str(item).replace('_', ' ').title()}\n"
            elif value:
                output += f"{attr.replace('_', ' ').capitalize()}: {str(value).title()}\n"

        return output

    

    def show_all(self):
        def format_dict_all(d, indent=0):
            # Recursively formats nested dictionaries, including empty ones.
            formatted_output = ""
            for key, value in d.items():
                if isinstance(value, dict):
                    nested_output = format_dict_all(value, indent + 4)
                    formatted_output += f"{' ' * indent}{key.replace('_', ' ').capitalize()}:\n{nested_output}"
                elif isinstance(value, list):  # Handle lists separately
                    formatted_output += f"{' ' * indent}{key.replace('_', ' ').capitalize()}:\n"
                    for item in value:
                        formatted_output += f"{' ' * (indent + len(key))}- {item.capitalize()}\n" if item else f"{' ' * (indent + len(key))}- [Empty]\n"
                else:  # Include all string values, even empty ones
                    formatted_output += f"{' ' * indent}{key.replace('_', ' ').capitalize()}: {value.capitalize() if value else '[Empty]'}\n"
            return formatted_output

        # Main output string for the Monster class attributes
        output = "\nMonster Information (Including Empty Fields):\n"
        for attr, value in self.__dict__.items():
            if isinstance(value, dict):
                nested_output = format_dict_all(value)
                output += f"{attr.replace('_', ' ').capitalize()}:\n{nested_output}"
            # Print all fields, including empty ones
            else:
                output += f"{attr.replace('_', ' ').capitalize()}: {value.capitalize() if value else '[Empty]'}\n"

        return output

if __name__ == "__main__":
    monster = Monster()
    print(monster.show_all())