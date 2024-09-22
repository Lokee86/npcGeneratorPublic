from constants import *

class Monster:
    def __init__(self):
        self.genre: str = ""
        self.gender: str = ""
        self.species: str = ""
        self.name: str = ""
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
        return self._generate_str()

    def formatted_str(self, *args):
        return self._generate_str(*args)

    def _generate_str(self, *ignore_attrs):
        # recursively formats and prints nested dictionaries and ignores empty ones.
        def format_dict(d, indent=0):
            formatted_output = ""
            non_empty = False
            for key, value in d.items():
                if isinstance(value, dict):
                    nested_output, is_non_empty = format_dict(value, indent + 4)
                    if is_non_empty:
                        formatted_output += f"{' ' * indent}{key.replace('_', ' ').capitalize()}:\n{nested_output}"
                        non_empty = True
                elif isinstance(value, list):  # Handle lists separately
                    if value:
                        formatted_output += f"{' ' * indent}{key.replace('_', ' ').capitalize()}:\n"
                        for item in value:
                            formatted_output += f"{' ' * (indent + 4)}- {item.capitalize()}\n"
                        non_empty = True
                elif value:  # Check for non-empty string values
                    formatted_output += f"{' ' * indent}{key.replace('_', ' ').capitalize()}: {value.capitalize()}\n"
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
            elif value:
                output += f"{attr.replace('_', ' ').capitalize()}: {value.capitalize()}\n"

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