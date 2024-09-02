from constants import *

class Monster:
    def __init__(self):
        self.genre: str = ""
        self.name: str = ""
        self.species: str = ""
        self.category: str  = ""
        self.size_class: str = ""
        self.habitat: str = ""

        self.skills = []

        self.stat_block: dict = {}
        self.motivations: dict = MOTIVATIONS
        self.role_play: dict = ROLE_PLAY
        self.tactics : dict  = {}

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
    
class NPC(Monster):
    def __init__(self):
        super().__init__()
        self.gender: str = ""
        self.sex: str = ""
        self.sexuality: str = ""
        self.birth_place: str = ""
        self.current_location: str = ""

        self.accomplishments = []
        self.associated_locations: list = []

        self.details: dict = DETAILS
        self.motivations: dict = MOTIVATIONS_NPC
        self.character: dict = CHARACTER
        self.roleplay: dict = ROLE_PLAY_NPC
        self.connections: dict = CONNECTIONS
    