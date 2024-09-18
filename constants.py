# GUI Constants

DISPLAY_FONT = "Times"

INTRO_TITLE = ""
MONSTER_TITLE = "Monster"
NPC_TITLE = "NPC"

CREATURE_WIDTH_FACTOR = 0.23
CREATURE_HEIGHT_FACTOR = 0.365
NPC_WIDTH_FACTOR = 0.23
NPC_HEIGHT_FACTOR = 0.5
DIALOG_WIDTH_FACTOR = 0.2
DIALOG_HEIGHT_FACTOR = 0.1

BASICS = ["Genre :", "Name :", "Species :", "Category/Classification/Type :", "Size :", "Habitat :"]
GSTATS = ["Str", "Dex", "Con", "Wis", "Int", "Cha"]
NPC_BASICS = ["Gender :", "Sex :", "Sexuality :", "Birth Place :", "Current Location :"]

def WINDOW_TITLE(name):
  if not name:
    return "Creature Creator"
  return f"Creature Creator: {name}"

# SYTEM PROMPTS

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

GENDER_PAYLOAD = [{"role": "system", "content": """[Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason. Assess the users input opinion to the question 'would you like to combine the character's sex and gender?' 
and return either 'yes' or 'no' exclusively. Add no punctuation, use only these words exactly. Yes means yes and no means no. If the user responds with a question, pay close attention."""}]

NAME_PAYLOAD = [{"role": "system", "content": """ [Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason. You are a high quality name generator for all genres that is only capable of outputting names and nothing else, you do not know how
to output words that are not names and you can only produce lists of names."""}]

DETAILS_PAYLOAD = [{"role": "system", "content": """ [Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason."""}]

MONSTER_NAME_PAYLOAD = [{"role": "system", "content": """ [Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason. You are a high quality monster generator for all genres that is only capable of outputting monster names and nothing else, you do not know how
to output words that are not monster names and you can only produce lists of monster names.
EXAMPLE MONSTER NAMES: Hydra
Medusa
Torrasque
Shengin
Cerberus
Sleipnir
Gravelurk
Skynthorn
Blightcrawler
Shardbeast
Driftshade
Wraithvine
Frostgnash
Mirefiend
Scorchwing
Riftclaw
Gloomhusk
Thunderjaw
Voidstalker
Spitegrub
Silkshiver
Venomspire
Goremaw
Dreadspire
Blazeclaw
Netherspite
Fleshrender
Emberwight
Shadowfang
Glimmertide
Rotweaver
Stormdrift
Ashbrute
Whisperclaw
Grimroot
Cinderwraith
Murkstalker
Frostbane
Gorebound
Blightmaw
Hollowscreech
Snarethorn
Voidreaver
Shardfang
Sablewretch
Blazeshade
Nightleech
Stormwrack
Riftshade
Veilrend
Embergrasp
Shatterfiend
Grimquill
Venomfang
Dusksnare
Ironspine
                         
Decline the use of any sort of word or token that resembles a proper noun"""},
{"role": "user", "content": "Provide a list of 25 creative and original monster names to strike fear and awe in to the hearts of adventurers."}]

def FIRST_NAME(species, genre, gender):
  return [{"role": "user", "content": f"Give me a list of 25 {species} {genre} setting first names for a {gender}."}]

def LAST_NAME(species, genre):
  return [{"role": "user", "content": f"Give me a list of 25 {genre} setting {species} surnames."}]

# NPC CLASS CONSTANTS

STATS = {"Str": "", "Dex": "", "Con": "", "Wis": "", "Int": "", "Cha": "",}

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