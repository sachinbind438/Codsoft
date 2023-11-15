import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'
      
    if message == 'What is your name?':
      return 'My name is Bot.' 
      
    if message == 'How are you?':
      return 'I am great.'

    if message == 'knock knock':
       return "Who's there?"

    if message == 'What can you do?':
      return 'Chat with you at the moment'
      
    return 'I didn\'t understand what you wrote. Try typing "!help".'
