#!/bin/python3

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

#OpenAI authorization
openai.api_key = os.getenv("OPENAI_API_KEY")

#Set AI behavior
messages=[{'role': 'system', 'content': 'You are a programming assistant in this session.'}]

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
    except:
        print(colorama.Fore.YELLOW + "ChatGPT: I'm busy")