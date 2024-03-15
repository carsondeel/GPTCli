import openai
import os, time
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic, Token, Whitespace
from pygments import highlight
import colorama

#Pygment color scheme
COLOR_SCHEME = {
  Token:              ('gray',                 'gray'),
  Comment:            ('magenta',     'brightmagenta'),
  Comment.Preproc:    ('magenta',     'brightmagenta'),
  Keyword:            ('blue',                   '**'),
  Keyword.Type:       ('green',       '*brightgreen*'),
  Operator.Word:      ('**',                     '**'),
  Name.Builtin:       ('cyan',           'brightblue'),
  Name.Function:      ('blue',           'brightblue'),
  Name.Class:         ('_green_',        'brightblue'),
  Name.Decorator:     ('magenta',     'brightmagenta'),
  Name.Variable:      ('blue',           'brightblue'),
  String:             ('yellow',       'brightyellow'),
  Number:             ('blue',         'brightyellow')
}

#My personal key is removed for privacy. Add user API key as string
openai.api_key = ""

#Set AI behavior
messages=[{'role': 'system', 'content': 'You are a programming assistant in this session.'}]

#Typing emulator that prints the message by letter
def typing(message):
    for l in message:
        print(l, end='', flush=True)

        #Testing with 0.002
        time.sleep(0.002)
    print(flush=True)

#Colored syntax
def colorize(code):
    lexer = guess_lexer(code)
    formatter = TerminalFormatter(bg = 'dark', colorscheme = COLOR_SCHEME)
    return highlight(code, lexer, formatter)

#Main loop
while True:
    try:
        #Get input from terminal
        question = input(colorama.Force.CYAN + 'You: ' + colorama.Style.RESET_ALL, end='')
        if question == 'quit': 
            break

        #Feed question to ChatGPT
        messages.append({
            'role': 'user',
            'content': question
        })

        #API response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        #Get text from API response
        answer = response['choices'][0]['message']['content']

        #Add messages to array
        messages.append({
            'role': 'assistant',
            'content': answer
        })

        #Output to CLI
        print(colorama.Fore.YELLOW + 'ChatGPT: ' + colorama.Style.RESET_ALL, end='')
        parsed = answer.split('```')
        if len(nansw) > 1:
            typing(parsed[0].strip()[:-1])
            for a in parsed:
                if len(a.split('\n')[0]):
                    raw_code = '\n'.join(a.split('\n')[1:])
                    highlighted = colorize(raw_code)
                    if raw_code != "    \n    ": typing(highlighted.strip())
                else: typing('\n' + a.strip())
        else: typing(answer.strip())
    except:
        print(colorama.Fore.YELLOW + "ChatGPT: I'm busy")