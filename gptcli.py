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

#OpenAI authorization
openai.api_key = os.getenv("OPENAI_API_KEY")

#Set AI behavior
messages=[{'role': 'system', 'content': 'You are a programming assistant in this session.'}]

