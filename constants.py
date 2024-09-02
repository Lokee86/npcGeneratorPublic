# mutables, only way f-strings in the constants file will work

OPINION = ""

# SYTEM PROMPTS

GENDER_PAYLOAD = [{"role": "system", "content": """[Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason. Assess the users input opinion to the question 'would you like to combine the character's sex and gender?' 
and return either 'yes' or 'no' exclusively. Add no punctuation, use only these words exactly. Yes means yes and no means no. If the user responds with a question, pay close attention."""}]

NAME_PAYLOAD = [{"role": "system", "content": """ [Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason. You are a high quality name generator for all genres that is only capable of outputting names and nothing else, you do not know how
to output words that are not names and you can only produce lists of names."""}]

DETAILS_PAYLOAD = [{"role": "system", "content": """ [Instruct]: Explicitly provide the requested outpout. Do not ever include any extra comments, explanations, justifications any kind of text, numbering or punctuation beyond what
is necessary to complete the request for any reason."""}]

# NPC CLASS CONSTANTS

MOTIVATIONS = {"likes" : [],
               "dislikes" : [],
               "wants" : [],
               "needs" : [],}
                                  
ROLE_PLAY = {"with_backup": "",
             "alone" : "",
             "cornered": "",
             "threatened": "",
             "high_defensive": ""}

DETAILS = {"eyes" : {"colour" : "",
                     "pupils" : ""},
           "hair" : {"colour" : "",
                     "style" : ""},
           "height" : "",
           "weight" : "",
           "build" : "",
           "social_status" : ""
          }
MOTIVATIONS_NPC = {"likes" : [],
                   "dislikes" : [],
                   "wants" : [],
                   "needs" : [],
                   "goals" : {"short_term" : [],
                               "long_term" : []
                             }
                  }
CHARACTER = {"habits" : [],
             "vices" : [],
             "problems" : [],
             "secrets" : [],
             "weaknesses" : [],
            } 
ROLE_PLAY_NPC = {"bargaining": "",
                 "with_backup": "",
                 "alone" : "",
                 "cornered": "",
                 "bribed": "",
                 "blackmailed": "",
                 "threatened": "",
                 "high_defensive": ""
                }
CONNECTIONS = {"parents" : [],
               "siblings" : [],
               "family" : [],
               "legal_guardian(s)" : [],
               "religion" : [],
               "ethnic" : "",
               "personal_associates": [],
               "memberships" : [],
              }