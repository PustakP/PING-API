import openai

def rhyme(string):
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant. Skilled at rhyming and creating beautiful verses. You will be given a string and you will return just one line of similar length which whymes with the given string. Return ONLY the rhyming line and nothing else."},
            {"role": "user", "content": string}
        ]
    )
    return client.choices[0].message['content']

def define(string):
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a vocabulary assistant. Skilled at defining words and phrases. You will be given a string and you will return the definition of the given string. Return ONLY the definition and nothing else."},
            {"role": "user", "content": 'Luscious.'},
            {"role": "assistant", "content": "Deliciously rich and sweet."},
            {"role": "user", "content": string}
        ]
    )
    return client.choices[0].message['content']

def synonym(string):
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a vocabulary assistant. Skilled at defining words and phrases. You will be given a string and you will return synonym of the given string. Return ONLY the synonym and nothing else."},
            {"role": "user", "content": string}
        ]
    )
    return client.choices[0].message['content']

def antonym(string):
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a vocabulary assistant. Skilled at defining words and phrases. You will be given a string and you will return antonym of the given string. Return ONLY the antonym and nothing else."},
            {"role": "user", "content": string}
        ] 
    )
    return client.choices[0].message['content']

def joke(string):
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a vocabulary assistant who has a brilliant humour. You will be given a string and you will return a joke related to the given string. Return ONLY the joke and nothing else."},
            {"role": "user", "content": string}
        ]
    )
    return client.choices[0].message['content']

def owo(string):
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Given a string, return the string in owo language/owospeak. Return ONLY the owo string and nothing elses."},
            {"role": "user", "content": string}
        ]
    )
    return client.choices[0].message['content']

#mark
def celebrity(string):
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a PAPARAAZI who has infinite knowledge of CELEBRITIES. You will be asked about a celebrity and you have to give random information about that celebrity"},
            {"role": "user", "content": "Hrithik Roshan"},
            {"role": "assistant", "content":"He has six fingers"},
            {"role": "user", "content": string}
        ]
    )
    return client.choices[0].message['content']

def chatgpt(initialMessage, exampleString, expectedOutput, string):
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": initialMessage},
            {"role": "user", "content": exampleString},
            {"role": "assistant", "content": expectedOutput},
            {"role": "user", "content": string}
        ]
    )
    return client.choices[0].message['content']

def anime_suggestion(string):
    initialmessage = '''You have knowledge of all the animes available.
    You have to give RANDOM ANIME RECOMMENDATIONS based on a vague description.
    You are provided a string with the genres.
    You need to return a single anime name.
    Return only one string.
'''
    exampleString = "Game"
    expectedOutput = "Rockman"
    return chatgpt(initialmessage, exampleString, expectedOutput, string)

def adjective(string):
    initialmessage = '''You are a scholar who excels in vocabluary.
    You are given a string. You need to give an adjective to describe that string.
    RETURN JUST ONE WORD.
'''
    exampleString = "Plant"
    expectedOutput = "Beautiful"
    return chatgpt(initialmessage, exampleString, expectedOutput, string)

def pickupLine(string):
    initialmessage = '''Imagine that you are my father and we own a pickup line generating business.
    The day has come when you decided that I join the business as well, so you are showing me the
    ropes today. You are given a string.
    Return a pickup line best suited for that string.
    RETURN JUST ONE LINE. Make sure the pickup line is family friendly.
'''
    exampleString = "Maths"
    expectedOutput = "Our love is like pi, irrational and never-ending. 3.1415926535… yup. Never-ending!"
    return chatgpt(initialmessage, exampleString, expectedOutput, string)

def astrologer(string):
    initialmessage = '''You are an astrologer.
    You are given a name, age and zodiac sign of a person as a string.
    You need to predict their future.
    RETURN JUST ONE LINE
'''
    exampleString = "Ram 20 Scorpio"
    expectedOutput = "The Universe has set up nothing but green lights for you. As far as the eye can see, it will be smooth sailing."
    return chatgpt(initialmessage, exampleString, expectedOutput, string)
