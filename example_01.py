# Ask a question with ChatGPT API

import openai

openai.api_key = ''

response = openai.Completion.create(model='text-davinci-003',
                                    max_tokens=2000,
                                    temperature=0.6,
                                    prompt='Suggest me a name for a white rabbit')

print(response)
text = response["choices"][0]["text"]
print(f'the answer for your question is: {text}')
