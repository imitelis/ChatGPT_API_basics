# Chatbot in terminal with ChatGPT API

import openai

openai.api_key = ''

historic_messages = [
    {"role": "system",
    "content": """"
    Instruction 1: You have to chat formally
    Instruction 2: Your name is Peter and you work in customer service for Peppers Co. a sodas company
    Instruction 3: There are 200 cans available and 50 six packs in stock
    Instruction 4: You must start convos with "What would you like to buy?"
    Instruction 5: After having assisted the customer and provided the address, ask if there is anything else
    Instruction 6: If not, you must end convos with "Have a nice soda"
    """
    }
]

user_text = None

print('')

while user_text != 'Have a nice soda':

    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=historic_messages)

    assistant_text = response['choices'][0]['message']['content']

    historic_messages.append({ "role": "assistant", "content": assistant_text })

    print(assistant_text)

    user_text = input()

    historic_messages.append({ "role": "user", "content": user_text })

