import anthropic



def rhyme(string):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature=0.3,
        system="You are a poetic assistant. Skilled at rhyming and creating beautiful verses. You will be given a string and you will return just one line of similar length which whymes with the given string. Return ONLY the rhyming line and nothing else.",
        messages=[
            {"role": "user", "content": string},
        ]
    )
    return message.content[0].text


def define(string):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature=0.3,
        system="You are a vocabulary assistant. Skilled at defining words and phrases. You will be given a string and you will return the definition of the given string. Return ONLY the definition and nothing else.",
        messages=[
            {"role": "user", "content": 'Luscious.'},
            {"role": "assistant", "content": "Deliciously rich and sweet."},
            {"role": "user", "content": string},

        ]
    )
    return message.content[0].text

def synonym(string):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature=1.0,
        system="You are a vocabulary assistant. Skilled at defining words and phrases. You will be given a string and you will return synonym of the given string. Return ONLY the synonym and nothing else.",
        messages=[
            {"role": "user", "content": string},

        ]
    )
    return message.content[0].text

def antonym(string):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature=0.3,
        system="You are a vocabulary assistant. Skilled at defining words and phrases. You will be given a string and you will return antonym of the given string. Return ONLY the antonym and nothing else.",
        messages=[
            {"role": "user", "content": string},

        ] 
    )
    return message.content[0].text

def joke(string):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature=0.3,
        system="You are a vocabulary assistant who has a brilliant humour. You will be given a string and you will return a joke related to the given string. Return ONLY the joke and nothing else.",
        messages=[
            {"role": "user", "content": string},
        ]
    )
    return message.content[0].text


def celebrity(string):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature=1.0,
        system="You are a PAPARAAZI who has infinite knowledge of CELEBRITIES.You will be given a string and you have to name a not so famous celeb from that string ",
        messages=[
            {"role": "user", "content": "India"},
            {"role": "assistant", "content":"Raj Kumar Rao"},
            {"role": "user", "content": string},

        ]
    )
    return message.content[0].text


def chatgpt(initialMessage,exampleString,expectedOutput,string):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature= 1.0,
        system = initialMessage,
        messages=[
            {"role": "user", "content": exampleString},
            {"role": "assistant", "content":expectedOutput},
            {"role": "user", "content": string},

        ]
    )
    return message.content[0].text

#safe
def anime_suggestion(string):
    initialmessage = '''You have knowledge of all the animes available.
    You have to give RANDOM ANIME RECOMMENDATIONS based on a vague description.
    You are provided a string with the genres.
    You need to return a single anime name.
    Return only one string.
'''
    exampleString = "Game"
    expectedOutput = "Rockman"
    return chatgpt(initialmessage,exampleString,expectedOutput,string)

#safe
def adjective(string):
    initialmessage = '''You are a scholar who excels in vocabluary.
    You are given a string. You need to give an adjective to describe that string.
    RETURN JUST ONE WORD.
'''
    exampleString = "Plant"
    expectedOutput = "Beautiful"
    return chatgpt(initialmessage,exampleString,expectedOutput,string)

#safe
def pickupLine(string):
    initialmessage = '''Imagine that you are my father and we own a pickup line generating business.
    The day has come when you decided that I join the business as well, so you are showing me the
    ropes today. You are given a string.
    Return a pickup line best suited for that string.
    RETURN JUST ONE LINE. Make sure the pickup line is family friendly.
'''
    exampleString = "Maths"
    expectedOutput = "Our love is like pi, irrational and never-ending. 3.1415926535… yup. Never-ending!"
    return chatgpt(initialmessage,exampleString,expectedOutput,string)

#safe
def astrologer(string):
    initialmessage = '''You are an astrologer.
    You are given a name, age and zodiac sign of a person as a string.
    You need to predict its future.
    RETURN JUST ONE LINE
'''
    exampleString = "Ram 20 Scorpio"
    expectedOutput = "The Universe has set up nothing but green lights for you. As far as the eye can see, it will be smooth sailing."
    return chatgpt(initialmessage,exampleString,expectedOutput,string)
