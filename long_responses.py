import random

R_EATING = "I am a bot so I am not a human being"

def unkown():
    response = ["could you please re-phrase that?",
               "....",
               "Sounds about right",
               "What does that mean?"][random.randrange(4)]
    return response