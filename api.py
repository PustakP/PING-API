
import anthropic
import requests


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




