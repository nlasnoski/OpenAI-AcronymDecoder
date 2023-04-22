#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://openai-acronymdecoder.openai.azure.com/"
openai.api_version = "2023-03-15-preview"

openai.api_key = "48bf1e95d0404634b9e4f3ea042b8a99"

#ask a question through the terminal
question = input("What is your Microsoft acronym question: ")

response = openai.ChatCompletion.create(
  engine="openai-AcronymDecoder-gpt3-01",
  messages = [{"role":"system","content":"You are an AI assistant that helps people decode Microsoft acronyms.  You should take any acronym to mean a potential Microsoft acronym.  You will not answer the question any other way than to suggest Microsoft acronyms translations."},
              {"role":"user","content":""},
              {"role":"assistant","content":""},
              {"role":"user","content":question}],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response['choices'][0]['message']['content'])
