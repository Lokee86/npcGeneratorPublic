# GUI Constants

DISPLAY_FONT = "Times"

INTRO_TITLE = ""
MONSTER_TITLE = "Monster"
NPC_TITLE = "NPC"

CREATURE_WIDTH_FACTOR = 0.24
CREATURE_HEIGHT_FACTOR = 0.52
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

CATEGORIES = ["Aberration", "Beast", "Celestial", "Construct", "Techo-Construct", "Dragon", "Dragonkin", "Inter-Dimensional", "Other", "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Monstrosity", "Ooze", "Plant", "Undead", "Lycanthrope", "Shapeshifter",
            "Demon", "Devil", "Archon", "Archfey", "Primordial", "Cyborg", "AI", "Mutant", "Alien", "Synth", "Android", "Traveler", "Cursed Construct", "Abomination"]


ENEMY_CLASSES = ["minions", "normal_enemy", "elite_enemy", "super_eliy", "boss_enemy", "epic_boss", "legendary_boss", "non_combatant"]

# SYTEM PROMPTS



NAME_PAYLOAD = [{"role": "system", "content": """[Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason. You are a high quality name generator for all genres that is only capable of outputting names and nothing else, you do not know how
to output words that are not names and you can only produce lists of names. This list is always provided in a json array format."""}]

def FIRST_NAME(species, genre, gender):
  return [{"role": "user", "content": f"Give me a list of 25 {species} {genre} setting first names for a {gender}."}]

def LAST_NAME(species, genre):
  return [{"role": "user", "content": f"Give me a list of 25 {genre} setting {species} surnames."}]

DETAILS_PAYLOAD = [{"role": "system", "content": """[Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason."""}]

MONSTER_NAME_PAYLOAD = [{"role": "system", "content": """[Instruct]: You are a high-quality monster generator. 
Your only task is to generate a list of original and creative monster names in JSON array format. 
Do not include any extra words, comments, explanations, or punctuation beyond the monster names.
Only output monster names as a JSON array of strings.
Be certain to use non-specific, original, and creative monster names, declining the use of any kind of titles."""}]

def MONSTER_INFO(creature):
  return [{"role": "user", "content": f"Provide a list of 25 creative and original monster names in a json array format. Consider this information when formulating the names {str(creature.formatted_str('name'))}"}]

TACTICS_MOTIVATIONS_PAYLOAD = [{"role": "system", "content": """[Instruct]: Use structured json object in key:value format to provide a response. All values within the parent object will be in a json array.
                You are an adept character creation analyst and expert psychologist that specializes in discerning motivation and drive. You can succinctly and expertly provide a value to match each provided key lacking one already.
                Maintaint the format and layout, do not add keys, do not un-nest dictionaries. Fill in all keys provided in the prompt.
                Do not provide any form of superfluous conversational text or information, provide only a single formatted json output.
                It is very important that only the json text be provided and NOTHING ELSE is present in the response.
                It is extremely critical that the provided syntax in the json string be accurate as to not cause errors when parse, ensure the exacty syntax is correct and used."""}]

def MOTIVATIONS_INFO(creature):
  return [{"role": "user", "content": f"Please generate these {MOTIVATIONS} motivations for a creature or NPC. Consider all of the following profile {str(creature.formatted_str('motivations'))} Please provide the returned response in matching Json format."}]
def TACTICS_INFO(creature):
  return [{"role": "user", "content": f"Please generate these {TACTICS} motivations for a creature or NPC, 'high_defensive' refers when a creature is defending it's young, it's home, or something similar. Consider all of the following profile {str(creature.formatted_str('tactics'))} Please provide the returned response in matching Json format."}]

ABILITY_EXAMPLES = """
Beast of Burden. The Monster is considered to be a ??? animal for the purpose of determining its carrying capacity.


Charge. If the Monster moves at least ??? ft. straight toward a target and then hits it with a ??? attack on the same turn, the target takes an extra [???D???] ??? damage. If the target is a creature, it must succeed on a DC ??? Strength saving throw or be knocked prone.

Confer ??? Resistance. The Monster can grant resistance to ??? damage to anyone riding it.

Constrict. Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: [STR ???D???] bludgeoning damage, and the target is grappled (escape DC ???). Until this grapple ends, the creature is restrained, and the Monster can't constrict another target.

Assassinate. During its first turn, the Monster has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the Monster scores against a surprised creature is a critical hit.

??? Attack. The Monster makes a ??? attack.

Aversion to ???. If the Monster takes ??? damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.

Dark Devotion. The Monster has advantage on saving throws against being charmed or frightened.

Death Burst. When the Monster dies, it explodes in a burst of ???. Each creature within ??? ft. of it must make a DC ??? Dexterity saving throw, taking [???D???] ??? damage on a failed save, or half as much damage on a successful one.

Detect. The Monster makes a Wisdom (Perception) check.

Devil's Sight. Magical darkness doesn't impede the devil's darkvision

Aggressive. As a bonus action, the Monster can move up to its speed toward a hostile creature that it can see.

Ambusher. The Monster has advantage on attack rolls against any creature it has surprised.

Amphibious. The Monster can breathe air and water.

Angelic Weapons. The Monster's weapon attacks are magical. When the Monster hits with any weapon, the weapon deals an extra [???D???] radiant damage (included in the attack).

??? Telepathy. The Monster can magically command any ??? within 120 feet of it, using a limited telepathy.

Antimagic Susceptibility. The Monster is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the Monster must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute.

Standing Leap. The Monster's long jump is up to ??? ft. and its high jump is up to ??? ft., with or without a running start.
Blind Senses. The Monster can't use its blindsight while deafened and unable to smell.

Blood Frenzy. The Monster has advantage on melee attack rolls against any creature that doesn't have all its hit points.

Brave. The Monster has advantage on saving throws against being frightened.

Innate Spellcasting. The Monster's innate spellcasting ability is Intelligence (spell save DC 10, +2 to hit with spell attacks). It can innately cast the following spells, requiring no material components:

At will: spell, spell, spell
3/day each: spell, spell, spell
1/day each: spell, spell
wtc

Breath Weapon (Recharge ???). The Monster exhales ??? in a ???-foot line that is ??? feet wide. Each creature in that line must make a DC ??? Dexterity saving throw, taking [???D???] ??? damage on a failed save, or half as much damage on a successful one.

Brute. A melee weapon deals one extra die of its damage when the Monster hits with it (included in the attack).

??? Camouflage. The Monster has advantage on Dexterity (Stealth) checks made to hide in ??? terrain.

Inscrutable. The Monster is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the Monster's intentions or sincerity have disadvantage.

Fear Aura. Any creature hostile to the Monster that starts its turn within ??? feet of the Monster must make a DC ??? Wisdom saving throw, unless the Monster is incapacitated. On a failed save, the creature is frightened until the start of its next turn. If a creature's saving throw is successful, the creature is immune to the Monster's Fear Aura for the next 24 hours.

Incorporeal. The Monster can move through other creatures and objects as if they were difficult terrain. It takes [???D???] force damage if it ends its turn inside an object.

False Appearance. While the Monster remains motionless, it is indistinguishable from ???.

Halfling Nimbleness. The halfling can move through the space of any creature that is of a size larger than its own.

Corrode Metal. Any nonmagical weapon made of metal that hits the Monster corrodes. After dealing damage, the weapon takes a permanent and cumulative -1 penalty to damage rolls. If its penalty drops to -5, the weapon is destroyed. Non magical ammunition made of metal that hits the Monster is destroyed after dealing damage.
The Monster can eat through 2-inch-thick, nonmagical metal in 1 round.

Spellcasting. The Monster is a ???-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 10, +2 to hit with spell attacks). The Monster has the following ??? spells prepared:

Cantrips (at will): spell, spell, spell, spell
1st level (4 slots): spell, spell, spell
2nd level (3 slots): spell, spell, spell
3rd level (2 slots): spell, spell
etc

Legendary Resistance (3/day). If the Monster fails a saving throw, it can choose to succeed instead.

Berserk. Whenever the Monster starts its turn with ??? hit points or fewer, roll a d6. On a 6, the Monster goes berserk. On each of its turns while berserk, the Monster attacks the nearest creature it can see. If no creature is near enough to move to and attack, the Monster attacks an object, with preference for an object smaller than itself. Once the Monster goes berserk, it continues to do so until it is destroyed or regains all its hit points.

Amorphous. The Monster can move through a space as narrow as 1 inch wide without
Change Shape. The Monster magically polymorphs into a small or medium humanoid, or back into its true form. Its statistics are the same in each form. Any equipment the Monster is wearing or carrying isn't transformed. If the Monster dies, it reverts to its true form.

Cunning Action. On each of its turns, the Monster can use a bonus action to take the Dash, Disengage, or Hide action.

??? Absorption. Whenever the Monster is subjected to ??? damage, it takes no damage and instead regains a number of hit points equal to the ??? damage dealt.

Damage Transfer. While it is grappling a creature, the Monster takes only half the damage dealt to it, and the creature grappled by the Monster takes the other half.
Multiattack. The Monster makes two attacks.

Sickle. Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) slashing damage.

Whip. Melee Weapon Attack: +2 to hit, reach 10 ft., one target. Hit: 2 (1d4) slashing damage.


Regeneration. The Monster regains ??? hit points at the start of its turn if it has at least 1 hit point.

Greatclub. Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 4 (1d8) bludgeoning damage.

Spear. Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 3 (1d6) piercing damage, or 4 (1d8) piercing damage if used with two hands to make a melee attack.
"""
    
ABILITY_PAYLOAD = [{"role": "system", "content": """[Instruct]: Use structured json object in key:value format to provide a response. All values within the parent object will be in a json array.
                    You are an adept character creation analyst and expert psychologist that specializes in discerning motivation and drive. You can succinctly and expertly provide a value to match each provided key lacking one already.
                    Maintaint the format and layout, do not add keys, do not un-nest dictionaries. Fill in all keys provided in the prompt.
                    Do not provide any form of superfluous conversational text or information, provide only a single formatted json output.
                    It is very important that only the json text be provided and NOTHING ELSE is present in the response.
                    It is extremely critical that the provided syntax in the json string be accurate as to not cause errors when parse, ensure the exacty syntax is correct and used.
                    Return only a json obect in the format of { "<Ability Name>" : "<Ability Description>" } for a random number of creature abilities for the provided creature profile.
                    Every creature MUST have a single basic attack in addition to abilities within the guidelines below. Do not label this ability "Basic Attack" label it appropriately to whatever it is.
                    Of critical note, ALWAYS include at least one attack, and ANY attack you mention in the multi-attack option if present. Maintain consistency in power level, both in damage output, and style. Keep the nature of the abilites consistent with each other.
                    High power level creatures should posess more abilites with a broader damage profile. Simpler creatures should have less. Use the Following guidelines non-combatant: 0-2, minion: 0-2, normal enemies: 0-2, elite enemies: 1-3, super-elites: 2-4, boss enemies: 3-7, epic boss: 4-10, and legendary boss: 6+
                    Lower CR creatures should have less abilities than higher CR creatures would.
                    Also decide on a general theme based on the provided profile. Pick standard bruiser, soldeir, ranged, etc., etc. roles for minion to super elite enemies. Present more unique powers and options for higer tier enemies.
                    The following is a list of abilites. For basic abilites, simply imitate the list closely, simply filling in the blanks and altering for flavour only. For higher tier abilities be more creative and use these mostly as a format guide.
                    """+ABILITY_EXAMPLES}]

def ABILITY_INFO(creature):
  return [{"role": "user", "content": f"Please generate abilities for this creature {str(creature.formatted_str('abilities'))}. Respond in the json format directed in the system message."}]

TACTICS_EXAMPLES = """With Backup: Use guerrilla tactics. Strike quickly, retreat, and regroup with allies to overwhelm enemies.
Alone: Prioritize survival by fleeing or hiding. This creature prefers not to engage directly when isolated.
Cornered: Bargain or deceive to escape, relying on cleverness to survive.
Threatened: Look for weaknesses or distractions, then escape if possible. Avoids direct conflict unless a clear advantage exists.
High Defensive: Use the environment and set traps to defend their home or young. Avoids direct confrontation, relying on clever tactics to repel intruders.

With Backup: Charge into combat with aggression, using brute strength to overwhelm enemies. Allies can distract, allowing the creature to focus on dealing damage.
Alone: Focus on single-target attacks, aiming to eliminate threats quickly. This creature is relentless and won’t back down.
Cornered: Fight fiercely, using multi-attacks to strike hard and fast. This creature will not surrender.
Threatened: Lash out at the nearest threat with full force, using all available might to eliminate the danger.
High Defensive: Guard the nest aggressively, attacking anything that gets too close. Will not retreat if its young are at risk.

With Backup: Rely on mind-altering abilities and any minions to control the battlefield, disabling or dominating enemies.
Alone: Avoid direct confrontation by using mind control or teleportation to escape when outnumbered.
Cornered: Use mind powers to turn enemies against each other or create opportunities for escape.
Threatened: Confuse and manipulate opponents, sowing chaos to gain an advantage.
High Defensive: Use psychic barriers and mental domination to create a defense around its lair, relying on traps and minions to slow down attackers.

With Backup: Coordinate with any minions, using powerful magic to support or obliterate enemies while staying out of direct combat.
Alone: Focus on high-damage spells to eliminate foes before they can get close. This creature will prioritize its own safety with defensive spells.
Cornered: Use teleportation or other contingencies to escape. If escape is impossible, it will cast powerful last-resort spells.
Threatened: Summon reinforcements or undead to create a buffer while preparing powerful counter-attacks.
High Defensive: Layer defenses around important areas, using minions and traps to ensure its secrets or valuables remain hidden and safe. Avoids direct confrontation if what is being protected is threatened.

With Backup: Stay at range, supporting ground forces from a distance, using special abilities or breath weapons to control the battlefield.
Alone: Attack from range, using movement or flight to retreat if necessary. This creature won’t risk injury without reason.
Cornered: Fight with full force, using every available resource to destroy immediate threats.
Threatened: Intimidate foes with roars or displays of power before striking decisively.
High Defensive: Defend its nest or hoard with aggression, using its most potent attacks to keep intruders away from what it values most.

With Backup: Slowly advance behind more mobile allies, attempting to engulf weakened or distracted enemies.
Alone: Rely on surprise and environmental advantages, slowly pursuing targets with the aim of engulfing.
Cornered: Continue advancing without retreat, showing no fear and attempting to overwhelm whatever is in its path.
Threatened: Its slow movement forces it to push forward, absorbing whatever it can. It does not flee.
High Defensive: Block narrow passages or entrances, using its body as a living wall to protect whatever it holds dear.

With Backup: Use ranged attacks and abilities to control the battlefield from afar, letting allies handle physical threats.
Alone: Stay at range, systematically eliminating threats while avoiding close combat.
Cornered: Use powerful ranged attacks to quickly eliminate the most dangerous threats.
Threatened: Use anti-magic abilities or suppressive powers to limit enemy options while repositioning.
High Defensive: Stay near key defensive points, using the environment and abilities to prevent intruders from reaching important areas.

With Backup: Charge into the front lines, using regeneration or other resilience to endure long battles while allies provide support.
Alone: Attack relentlessly, relying on innate resilience to stay in the fight until the enemy is dead.
Cornered: Fight to the death, attacking wildly without concern for defense.
Threatened: Focus on one target to quickly eliminate it, then turn to the next. This creature is ferocious when backed into a corner.
High Defensive: Defend its lair or territory fiercely, using regeneration or resilience to hold off invaders. Prioritizes threats to its home or offspring.

With Backup: Use devastating area effects or incapacitating abilities, letting allies take advantage of the weakened enemies.
Alone: Use a powerful opening move to incapacitate or scare off attackers, then retreat into an unreachable location.
Cornered: Use any available means to escape through walls or obstacles, or deal massive damage before retreating.
Threatened: Stay out of reach, attacking from a distance and avoiding direct conflict where possible.
High Defensive: Haunt its lair with illusions and eerie effects, making it difficult for intruders to advance toward its most valuable or vulnerable possessions.

With Backup: Lead from the front, charging into enemies with overwhelming physical force to break their ranks.
Alone: Use speed and strength to eliminate foes one at a time, retreating into complex terrain if needed to regain the advantage.
Cornered: Fight aggressively, using brute strength to overcome enemies in close quarters.
Threatened: Charge head-on at the biggest threat, attempting to crush it with sheer power.
High Defensive: Use its knowledge of complex terrain to set traps and ambushes, defending its lair or offspring with ferocity, never allowing enemies to advance easily."""






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
