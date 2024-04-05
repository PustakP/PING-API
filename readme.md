# PING Bootcamp Practice API Documentation

This API provides various endpoints for generating rhyming lines, defining words or phrases, finding synonyms and antonyms, generating jokes, converting text to owo language, providing celebrity information, and more. The API is built using Python and the `openai` library for interacting with the GPT-3.5-turbo language model.

## Endpoints

### 1. `/rhyme`

This endpoint accepts a string as input and returns a single line of poetry that rhymes with the provided string.

**Example Usage:**

```python
import requests

string = "The sun shines bright on the meadow's path"
url = "http://ping.skarj.pl/rhyme"
payload = {"string": string}

response = requests.post(url, json=payload)

if response.status_code == 200:
    rhyming_line = response.json()["output"]
    print(rhyming_line)
else:
    print(f"Error: {response.status_code}")
```

### 2. `/define`

This endpoint accepts a string as input and returns the definition of the provided word or phrase.

**Example Usage:**

```python
import requests

word = "luscious"
url = "http://ping.skarj.pl/define"
payload = {"string": word}

response = requests.post(url, json=payload)

if response.status_code == 200:
    definition = response.json()["output"]
    print(definition)
else:
    print(f"Error: {response.status_code}")
```

### 3. `/synonym`

This endpoint accepts a string as input and returns a synonym for the provided word or phrase.

**Example Usage:**

```python
import requests

word = "beautiful"
url = "http://ping.skarj.pl/synonym"
payload = {"string": word}

response = requests.post(url, json=payload)

if response.status_code == 200:
    synonym = response.json()["output"]
    print(synonym)
else:
    print(f"Error: {response.status_code}")
```

### 4. `/antonym`

This endpoint accepts a string as input and returns an antonym for the provided word or phrase.

**Example Usage:**

```python
import requests

word = "hot"
url = "http://ping.skarj.pl/antonym"
payload = {"string": word}

response = requests.post(url, json=payload)

if response.status_code == 200:
    antonym = response.json()["output"]
    print(antonym)
else:
    print(f"Error: {response.status_code}")
```

### 5. `/joke`

This endpoint accepts a string as input and returns a joke related to the provided string.

**Example Usage:**

```python
import requests

topic = "dogs"
url = "http://ping.skarj.pl/joke"
payload = {"string": topic}

response = requests.post(url, json=payload)

if response.status_code == 200:
    joke = response.json()["output"]
    print(joke)
else:
    print(f"Error: {response.status_code}")
```

### 6. `/owo`

This endpoint accepts a string as input and returns the string in owo language or owospeak.

**Example Usage:**

```python
import requests

text = "Hello, how are you?"
url = "http://ping.skarj.pl/owo"
payload = {"string": text}

response = requests.post(url, json=payload)

if response.status_code == 200:
    owo_text = response.json()["output"]
    print(owo_text)
else:
    print(f"Error: {response.status_code}")
```

### 7. `/celebrity`

This endpoint accepts a string representing a celebrity name as input and returns random information about that celebrity.

**Example Usage:**

```python
import requests

celebrity_name = "Hrithik Roshan"
url = "http://ping.skarj.pl/celebrity"
payload = {"string": celebrity_name}

response = requests.post(url, json=payload)

if response.status_code == 200:
    celebrity_info = response.json()["output"]
    print(celebrity_info)
else:
    print(f"Error: {response.status_code}")
```

### 8. `/anime_suggestion`

This endpoint accepts a string representing genres as input and returns a random anime recommendation based on those genres.

**Example Usage:**

```python
import requests

genres = "Action, Adventure"
url = "http://ping.skarj.pl/anime_suggestion"
payload = {"string": genres}

response = requests.post(url, json=payload)

if response.status_code == 200:
    anime_suggestion = response.json()["output"]
    print(anime_suggestion)
else:
    print(f"Error: {response.status_code}")
```

### 9. `/adjective`

This endpoint accepts a string as input and returns an adjective that describes the provided string.

**Example Usage:**

```python
import requests

subject = "Ocean"
url = "http://ping.skarj.pl/adjective"
payload = {"string": subject}

response = requests.post(url, json=payload)

if response.status_code == 200:
    adjective = response.json()["output"]
    print(adjective)
else:
    print(f"Error: {response.status_code}")
```

### 10. `/pickup_line`

This endpoint accepts a string as input and returns a family-friendly pickup line related to the provided string.

**Example Usage:**

```python
import requests

topic = "Books"
url = "http://ping.skarj.pl/pickup_line"
payload = {"string": topic}

response = requests.post(url, json=payload)

if response.status_code == 200:
    pickup_line = response.json()["output"]
    print(pickup_line)
else:
    print(f"Error: {response.status_code}")
```

### 11. `/astrologer`

This endpoint accepts a string containing a person's name, age, and zodiac sign as input and returns a prediction about their future.

**Example Usage:**

```python
import requests

person_info = "John 25 Aries"
url = "http://ping.skarj.pl/astrologer"
payload = {"string": person_info}

response = requests.post(url, json=payload)

if response.status_code == 200:
    prediction = response.json()["output"]
    print(prediction)
else:
    print(f"Error: {response.status_code}")
```

## Theoretical Concepts

### Natural Language Processing (NLP)

This API utilizes Natural Language Processing (NLP) techniques to generate responses based on the provided input. NLP is a branch of artificial intelligence that deals with the interaction between computers and human languages, enabling machines to understand, interpret, and generate human-like language.

### Language Models

The API leverages the GPT-3.5-turbo language model from OpenAI, which is a powerful language model capable of generating human-like text based on the given context or prompt.

### Temperature

The `temperature` parameter in the API controls the randomness or creativity of the generated output. A higher temperature value (e.g., 0.8) will result in more diverse and creative responses, while a lower temperature (e.g., 0.2) will produce more predictable and conservative outputs.

### System Prompt

The API utilizes a "system prompt" to instruct the language model on the specific task it should perform. For example, the `/rhyme` endpoint instructs the model to act as a poetic assistant and generate a rhyming line, while the `/define` endpoint instructs the model to act as a vocabulary assistant and provide a definition for the given word or phrase.

### Role-based Conversation

The API simulates a conversation between a user and an assistant by providing a series of messages with assigned roles (`"user"` and `"assistant"`). This conversational format allows the language model to better understand the context and generate more relevant and coherent responses.

## Limitations and Considerations

- The API's performance and output quality may vary depending on the input data and the specific language model used.
- The generated responses are based on the training data and biases present in the language model, which may lead to inconsistencies or inaccuracies.
- The API does not handle edge cases or malformed inputs gracefully, and appropriate input validation should be implemented on the client-side.
- The API does not currently support authentication or rate limiting, which may be necessary for production environments.
