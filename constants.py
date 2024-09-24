# GUI Constants

DISPLAY_FONT = "Times"

INTRO_TITLE = ""
MONSTER_TITLE = "Monster"
NPC_TITLE = "NPC"

CREATURE_WIDTH_FACTOR = 0.23
CREATURE_HEIGHT_FACTOR = 0.44
NPC_WIDTH_FACTOR = 0.1
NPC_HEIGHT_FACTOR = 0.05
DIALOG_WIDTH_FACTOR = 0.2
DIALOG_HEIGHT_FACTOR = 0.1

BASICS = ["Genre :", "Name :", "Species :", "Category/Classification/Type :", "Size :", "Habitat :"]
GSTATS = ["Str", "Dex", "Con", "Wis", "Int", "Cha"]
NPC_BASICS = ["Gender :", "Sex :", "Sexuality :", "Birth Place :", "Current Location :"]

def WINDOW_TITLE(name):
  if not name:
    return "Creature Creator"
  return f"Creature Creator: {name}"

# PREDETERMINED GEN-LISTS

GENRES = ["Fantasy",
          "Science Fiction",
          "Horror",
          "Post-Apocalyptic",
          "Cyberpunk",
          "Steampunk",
          "Historical Fiction",
          "Western",
          "Espionage",
          "Gothic",
          "Dark Fantasy",
          "Superhero",
          "Sword and Sorcery",
          "Dystopian",
          "Pirate",
          "High Fantasy",
          "Low Fantasy",
          "Urban Fantasy",
          "Space Opera",
          "Noir",
          "Mystery",
          "Thriller",
          "Survival",
          "Military",
          "Time Travel",
          "Mythological",
          "Romance",
          "Detective",
          "Exploration",
          "Magical Realism",
          "Psychological Horror",
          "Paranormal",
          "Political",
          "War",
          "Adventure",
          "Crime",
          "Caper",
          "Martial Arts",
          "Comedy",
          "Satire",
          "Heroic Fantasy",
          "Lovecraftian Horror",
          "Alternate History",
          "Swashbuckler",
          "Pirate Fantasy",
          "Fairy Tale",
          "Folklore",
          "Dungeon Crawl",
          "Gritty Realism",
          "Space Western"]

SKILLS = ["Acrobatics",
          "Animal Handling",
          "Arcana",
          "Athletics",
          "Deception",
          "History",
          "Insight",
          "Intimidation",
          "Investigation",
          "Medicine",
          "Nature",
          "Perception",
          "Performance",
          "Persuasion",
          "Religion",
          "Sleight of Hand",
          "Stealth",
          "Survival"]

SPECIES = ["Elf", "Dwarf", "Orc", "Goblin", "Troll", "Dragon", "Gnome", "Ogre", "Faerie", "Vampire", "Werewolf", "Centaur", "Minotaur", "Merfolk", "Dryad", "Nymph", 
    "Wraith", "Djinn", "Succubus", "Incubus", "Sprite", "Banshee", "Ghost", "Witch", "Warlock", "Shapeshifter", "Giant", "Harpy", "Demon", "Angel", "Gorgon", 
    "Siren", "Satyr", "Brownie", "Kobold", "Kitsune", "Oni", "Tengu", "Kappa", "Sylph", "Undine", "Naga", "Rakshasa", "Valkyrie", "Selkie", "Leprechaun", 
    "Kelpie", "Pixie", "Wendigo", "Doppelgänger", "Sphinx", "Golem", "Mummy", "Lizardfolk", "Ifrit", "Marid", "Ghoul", "Werecat", "Yōkai", "Asura", 
    "Sylvan Spirit", "Astral Being", "Naiad", "Lamia", "Eidolon", "Yaksha", "Garuda", "Gandharva", "Kapre", "Manananggal", "Aswang", "Duende", "Encantado", 
    "Caipora", "Behemoth", "Dybbuk", "Einherjar", "Draugr", "Jotunn", "Norn", "Fury", "Erinyes", "Nereid", "Oceanid", "Muse", "Moira", "Tarasque", "Onryō", 
    "Shinigami", "Khepri", "Sekhmet", "Sobek", "Bastet", "Thoth", "Ma'at", "Ammit", "Set", "Atlantean", "Reptilian", "Etherial", "Fae Dragon", 
    "Crystal Golem", "Stone Giant", "Cloud Giant", "Storm Giant", "Fire Giant", "Frost Giant", "Water Nymph", "Fire Spirit", "Ice Elemental", "Shadow Demon",
    "Mind Flayer", "Revenant", "Bansidhe", "Thunder Being", "Skin-walker", "Changeling", "Hag", "Bogeyman", "Nightmare", "Sandman", "Gremlin", 
    "Goblin", "Hobgoblin", "Redcap", "Trollkin", "Firbolg", "Fomorian", "Sidhe", "Tuatha Dé Danann", "Bean Nighe", "Cat Sith", "Cu Sith", "Nuckelavee", 
    "Kelpie", "Selkie", "Finfolk", "Sasquatch", "Yowie"]


# SYTEM PROMPTS



NAME_PAYLOAD = [{"role": "system", "content": """[Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason. You are a high quality name generator for all genres that is only capable of outputting names and nothing else, you do not know how
to output words that are not names and you can only produce lists of names. This list is always provided in a json array format."""}]

DETAILS_PAYLOAD = [{"role": "system", "content": """[Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason."""}]

MONSTER_NAME_PAYLOAD = [{"role": "system", "content": """[Instruct]: You are a high-quality monster generator. 
Your only task is to generate a list of original and creative monster names in JSON array format. 
Do not include any extra words, comments, explanations, or punctuation beyond the monster names.
Only output monster names as a JSON array of strings.

EXAMPLE MONSTER NAMES: 
Hydra, Medusa, Torrasque, Shengin, Cerberus, Sleipnir, Gravelurk, Skynthorn, 
Blightcrawler, Shardbeast, Driftshade, Wraithvine, Frostgnash, Mirefiend, 
Scorchwing, Riftclaw, Gloomhusk, Thunderjaw, Voidstalker, Spitegrub, Silkshiver, 
Venomspire, Goremaw, Dreadspire, Blazeclaw, Netherspite, Fleshrender, Emberwight, 
Shadowfang, Glimmertide, Rotweaver, Stormdrift, Ashbrute, Whisperclaw, Grimroot, 
Cinderwraith, Murkstalker, Frostbane, Gorebound, Blightmaw, Hollowscreech, 
Snarethorn, Voidreaver, Shardfang, Sablewretch, Blazeshade, Nightleech, Stormwrack, 
Riftshade, Veilrend, Embergrasp, Shatterfiend, Grimquill, Venomfang, Dusksnare, 
Ironspine, Void Serpent, Android, Space Marine, Gravity Shifter, Alien Diplomat, 
Fungal Colonizer, Telepathic Species, Hyper-Evolved Human, Astro-Mechanic, Jovian, 
Black Hole Entity, Interdimensional Traveler, Wormhole Navigator, Space Mercenary, 
Galactic Researcher, Cloning Experiment, Bio-Synthetic Hybrid, Telekinetic, Quantum 
Parasite, Transhuman, Star Harvester, Solar Entity, Elf, Dwarf, Orc, Goblin, Troll, 
Dragon, Gnome, Ogre, Faerie, Vampire, Werewolf, Centaur, Minotaur, Griffin, Phoenix, 
Chimera, Unicorn, Merfolk, Dryad, Nymph, Basilisk, Hydra, Cyclops, Wraith, Djinn, 
Yeti, Kraken, Leviathan, Lich, Specter, Zombie, Necromancer, Succubus, Incubus, Sprite, 
Banshee, Ghost, Witch, Warlock, Shape-shifter, Giant, Manticore, Harpy, Imp, Demon, 
Archangel, Gorgon, Pegasus, Beholder, Hobgoblin, Wyvern, Flesh Golem, Wendigo, 
Skinwalker, Bogeyman, Changeling, Doppelganger, Headless Horseman, Scarecrow, Swamp 
Creature, Cursed Doll, Haunted Armor, Undead Knight, Evil Clown, Plague Doctor, Evil 
Puppet, Dark Sorcerer, Grim Reaper, Shadow Monster, Alien Parasite, Dark Spirit, 
Undead Pirate, Flesh-Eating Monster, Evil Spirit, Voodoo Priest, Corpse Bride

                
Be certain to use non-specific, original, and creative monster names, declining the use of any kind of titles."""},
{"role": "user", "content": "Provide a list of 25 creative and original monster names in provided the json schema."}]

MOTIVATIONS_PAYLOAD = [{"role": "system", "content": """[Instruct]: Use structured json object in key:value format to provide a response. All values within the parent object will be in a json array.
                You are an adept character creation analyst and expert psychologist that specializes in discerning motivation and drive. You can succinctly and expertly provide a value to match each provided key lacking one already.
                Maintaint the format and layout, do not add keys, do not un-nest dictionaries. Fill in all keys provided in the prompt.
                Do not provide any form of superfluous conversational text or information, provide only a single formatted json output.
                It is very important that only the json text be provided and NOTHING ELSE is present in the response.
                It is extremely critical that the provided syntax in the json string be accurate as to not cause errors when parse, ensure the exacty syntax is correct and used."""}]

def MOTIVATIONS_INFO(creature):
  return [{"role": "user", "content": f"Please generate these {MOTIVATIONS} motivations for a creature or NPC. Consider all of the following profile {str(creature.formatted_str('motivations'))} Please provide the returned response in matching Json format."}]

ABILITY_EXAMPLES = """Multiattack. The Monster makes two attacks.

Spellcasting. The Monster is a ???-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 10, +2 to hit with spell attacks). The Monster has the following ??? spells prepared:

Cantrips (at will): spell, spell, spell, spell
1st level (4 slots): spell, spell, spell
2nd level (3 slots): spell, spell, spell
3rd level (2 slots): spell, spell

Legendary Resistance (3/day). If the Monster fails a saving throw, it can choose to succeed instead.

Berserk. Whenever the Monster starts its turn with ??? hit points or fewer, roll a d6. On a 6, the Monster goes berserk. On each of its turns while berserk, the Monster attacks the nearest creature it can see. If no creature is near enough to move to and attack, the Monster attacks an object, with preference for an object smaller than itself. Once the Monster goes berserk, it continues to do so until it is destroyed or regains all its hit points.

Amorphous. The Monster can move through a space as narrow as 1 inch wide without squeezing.

Innate Spellcasting. The Monster's innate spellcasting ability is Intelligence (spell save DC 10, +2 to hit with spell attacks). It can innately cast the following spells, requiring no material components:

At will: spell, spell, spell
3/day each: spell, spell, spell
1/day each: spell, spell

Aggressive. As a bonus action, the Monster can move up to its speed toward a hostile creature that it can see.

Ambusher. The Monster has advantage on attack rolls against any creature it has surprised.

Amphibious. The Monster can breathe air and water.

Angelic Weapons. The Monster's weapon attacks are magical. When the Monster hits with any weapon, the weapon deals an extra [???D???] radiant damage (included in the attack).

??? Telepathy. The Monster can magically command any ??? within 120 feet of it, using a limited telepathy.

Antimagic Susceptibility. The Monster is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the Monster must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute.

Assassinate. During its first turn, the Monster has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the Monster scores against a surprised creature is a critical hit.

??? Attack. The Monster makes a ??? attack.

Aversion to ???. If the Monster takes ??? damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.

Beast of Burden. The Monster is considered to be a ??? animal for the purpose of determining its carrying capacity.

Blind Senses. The Monster can't use its blindsight while deafened and unable to smell.

Blood Frenzy. The Monster has advantage on melee attack rolls against any creature that doesn't have all its hit points.

Brave. The Monster has advantage on saving throws against being frightened.

Breath Weapon (Recharge ???). The Monster exhales ??? in a ???-foot line that is ??? feet wide. Each creature in that line must make a DC ??? Dexterity saving throw, taking [???D???] ??? damage on a failed save, or half as much damage on a successful one.

Brute. A melee weapon deals one extra die of its damage when the Monster hits with it (included in the attack).

??? Camouflage. The Monster has advantage on Dexterity (Stealth) checks made to hide in ??? terrain.

Change Shape. The Monster magically polymorphs into a small or medium humanoid, or back into its true form. Its statistics are the same in each form. Any equipment the Monster is wearing or carrying isn't transformed. If the Monster dies, it reverts to its true form.

Charge. If the Monster moves at least ??? ft. straight toward a target and then hits it with a ??? attack on the same turn, the target takes an extra [???D???] ??? damage. If the target is a creature, it must succeed on a DC ??? Strength saving throw or be knocked prone.

Confer ??? Resistance. The Monster can grant resistance to ??? damage to anyone riding it.

Constrict. Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: [STR ???D???] bludgeoning damage, and the target is grappled (escape DC ???). Until this grapple ends, the creature is restrained, and the Monster can't constrict another target.

Corrode Metal. Any nonmagical weapon made of metal that hits the Monster corrodes. After dealing damage, the weapon takes a permanent and cumulative -1 penalty to damage rolls. If its penalty drops to -5, the weapon is destroyed. Non magical ammunition made of metal that hits the Monster is destroyed after dealing damage.
The Monster can eat through 2-inch-thick, nonmagical metal in 1 round.

Cunning Action. On each of its turns, the Monster can use a bonus action to take the Dash, Disengage, or Hide action.

??? Absorption. Whenever the Monster is subjected to ??? damage, it takes no damage and instead regains a number of hit points equal to the ??? damage dealt.

Damage Transfer. While it is grappling a creature, the Monster takes only half the damage dealt to it, and the creature grappled by the Monster takes the other half.

Dark Devotion. The Monster has advantage on saving throws against being charmed or frightened.

Death Burst. When the Monster dies, it explodes in a burst of ???. Each creature within ??? ft. of it must make a DC ??? Dexterity saving throw, taking [???D???] ??? damage on a failed save, or half as much damage on a successful one.

Detect. The Monster makes a Wisdom (Perception) check.

Devil's Sight. Magical darkness doesn't impede the devil's darkvision."""
    
ABILITY_PAYLOAD = [{"role": "system", "content": """[Instruct]: Use structured json object in key:value format to provide a response. All values within the parent object will be in a json array.
                    You are an adept character creation analyst and expert psychologist that specializes in discerning motivation and drive. You can succinctly and expertly provide a value to match each provided key lacking one already.
                    Maintaint the format and layout, do not add keys, do not un-nest dictionaries. Fill in all keys provided in the prompt.
                    Do not provide any form of superfluous conversational text or information, provide only a single formatted json output.
                    It is very important that only the json text be provided and NOTHING ELSE is present in the response.
                    It is extremely critical that the provided syntax in the json string be accurate as to not cause errors when parse, ensure the exacty syntax is correct and used.
                    Return only a json obect in the format of { "<Ability Name>" : "<Ability Description>" } for a random number of DnD creature abilities for the provided creature profile.
                    Choose a power level randomly, both in damage output, and style. Keep the nature of the abilites consistent with each other.
                    High power level creatures should posess more abilites with a broader damage profile. Simpler creatures should have less, but not always just one or two abilites.
                    Choose between minions, normal enemies, elite enemies, super-elites, boss enemies, epic boss, and legendary boss for power levels. Don't record this in the response, use it as a guide. If you find one of these terms int he profile, choose that.
                    Also decide on a general theme based on the provided profile. Pick standard bruiser, soldeir, ranged, etc., etc. roles for minion to super elite enemies. Present more unique powers and options for higer tier enemies.
                    The following is a list of abilites. For basic abilites, simply imitate the list closely, simply filling in the blanks and altering for flavour only. For higher tier abilities be more creative and use these mostly as a format guide.
                    Of critical note, always include at least one attack. and ANY attack you mention in the multi-attack option if present.
                    """+ABILITY_EXAMPLES}]

def ABILITY_INFO(creature):
  return [{"role": "user", "content": f"Please generate abilities for this creature {str(creature)}. Respond in the json format directed in the system message."}]


def FIRST_NAME(species, genre, gender):
  return [{"role": "user", "content": f"Give me a list of 25 {species} {genre} setting first names for a {gender}."}]

def LAST_NAME(species, genre):
  return [{"role": "user", "content": f"Give me a list of 25 {genre} setting {species} surnames."}]

# Schemas for structured responses.

LIST_SHCEMA = {"type": "array", "items": {"type": "string"}}

MOTIVATIONS_SCHEMA = {
    "type": "object",
    "properties": {
        "likes": {
            "type": "array",
            "items": {
                "type": "string"
            },
        },
        "dislikes": {
            "type": "array",
            "items": {
                "type": "string"
            },
        },
        "wants": {
            "type": "array",
            "items": {
                "type": "string"
            },
        },
        "needs": {
            "type": "array",
            "items": {
                "type": "string"
            },
        }
    },
    "additionalProperties": False
}



# NPC CLASS CONSTANTS

STATS = {"Str": "", "Dex": "", "Con": "", "Wis": "", "Int": "", "Cha": "",}

ACTIONS = {"actions": {},
           "bonus actions" : {},
           "legendary actions" : {},
           "mythic actions": {}}

MOTIVATIONS = {"likes" : [],
               "dislikes" : [],
               "wants" : [],
               "needs" : [],}
                                  
TACTICS = {"with_backup": "",
           "alone" : "",
           "cornered": "",
           "threatened": "",
           "high_defensive": ""}

MOTIVATIONS_NPC = {"likes" : [],
                   "dislikes" : [],
                   "wants" : [],
                   "needs" : [],
                   "goals" : {"short_term" : [],
                               "long_term" : []},}

ROLE_PLAY = {"bargaining": "",
             "with_backup": "",
             "alone" : "",
             "cornered": "",
             "bribed": "",
             "blackmailed": "",
             "threatened": "",
             "high_defensive": ""}

DETAILS = {"eyes" : {"colour" : "",
                     "pupils" : ""},
           "hair" : {"colour" : "",
                     "style" : ""},
           "height" : "",
           "weight" : "",
           "build" : "",
           "social_status" : ""}

CHARACTER = {"habits" : [],
             "vices" : [],
             "problems" : [],
             "secrets" : [],
             "weaknesses" : [],}

CONNECTIONS = {"parents" : [],
               "siblings" : [],
               "family" : [],
               "legal_guardianship" : [],
               "religion" : [],
               "ethnic" : "",
               "personal_associates": [],
               "memberships" : [],}
