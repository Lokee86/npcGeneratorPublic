from constants import *

class Monster:
    def __init__(self):
        self.genre: str = ""
        self.gender: str = ""
        self.species: str = ""
        self.name: str = ""
        self.random_names: dict = {"firsts": [], "lasts": []}
        self.category: str  = ""
        self.size_class: str = ""
        self.habitat: str = ""

        self.skills = []

        self.stat_block: dict = STATS
        self.motivations: dict = MOTIVATIONS
        self.tactics : dict  = TACTICS
        self.abilities: dict = {}
        self.actions: dict = ACTIONS

    def __str__(self):
        def format_dict(d, indent=0):
            # Recursively formats nested dictionaries, skipping empty ones.
            formatted_output = ""
            non_empty = False
            for key, value in d.items():
                if isinstance(value, dict):
                    nested_output, is_non_empty = format_dict(value, indent + 4)
                    if is_non_empty:
                        formatted_output += f"{' ' * indent}{key.replace('_', ' ').title()}:\n{nested_output}"
                        non_empty = True
                elif isinstance(value, list):  # Handle lists separately
                    if value:
                        formatted_output += f"{' ' * indent}{key.replace('_', ' ').title()}:\n"
                        for item in value:
                            formatted_output += f"{' ' * (indent + len(key))}- {item.title()}\n"
                        non_empty = True
                elif value:  # Check for non-empty string values
                    formatted_output += f"{' ' * indent}{key.replace('_', ' ').title()}: {value.title()}\n"
                    non_empty = True
            return formatted_output, non_empty

        # Main output string for the Monster class attributes
        output = "\nMonster Information:\n"
        for attr, value in self.__dict__.items():
            if isinstance(value, dict):
                nested_output, is_non_empty = format_dict(value)
                # Only add the attribute if is_non_empty returns False
                if is_non_empty:  
                    output += f"{attr.replace('_', ' ').title()}:\n{nested_output.title()}"
            # Only print non-empty fields
            elif value:  
                output += f"{attr.replace('_', ' ').title()}: {value.title()}\n"

        return output
    

    def show_all(self):
        def format_dict_all(d, indent=0):
            # Recursively formats nested dictionaries, including empty ones.
            formatted_output = ""
            for key, value in d.items():
                if isinstance(value, dict):
                    nested_output = format_dict_all(value, indent + 4)
                    formatted_output += f"{' ' * indent}{key.replace('_', ' ').title()}:\n{nested_output}"
                elif isinstance(value, list):  # Handle lists separately
                    formatted_output += f"{' ' * indent}{key.replace('_', ' ').title()}:\n"
                    for item in value:
                        formatted_output += f"{' ' * (indent + len(key))}- {item.title()}\n" if item else f"{' ' * (indent + len(key))}- [Empty]\n"
                else:  # Include all string values, even empty ones
                    formatted_output += f"{' ' * indent}{key.replace('_', ' ').title()}: {value.title() if value else '[Empty]'}\n"
            return formatted_output

        # Main output string for the Monster class attributes
        output = "\nMonster Information (Including Empty Fields):\n"
        for attr, value in self.__dict__.items():
            if isinstance(value, dict):
                nested_output = format_dict_all(value)
                output += f"{attr.replace('_', ' ').title()}:\n{nested_output}"
            # Print all fields, including empty ones
            else:
                output += f"{attr.replace('_', ' ').title()}: {value.title() if value else '[Empty]'}\n"

        return output


class NPC(Monster):
    def __init__(self):
        super().__init__()
        self.sex: str = ""
        self.sexuality: str = ""
        self.birth_place: str = ""
        self.current_location: str = ""

        self.personality: str = ""
        self.accomplishments = []
        self.associated_locations: list = []

        self.details: dict = DETAILS
        self.motivations: dict = MOTIVATIONS_NPC
        self.character: dict = CHARACTER
        self.roleplay: dict = ROLE_PLAY
        self.connections: dict = CONNECTIONS

if __name__ == "__main__":
    monster = Monster()
    npc = NPC()
    print(monster.show_all())
    print(npc.show_all())