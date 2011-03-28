import re

try:
    set
except NameError:
    from sets import Set as set
from bisect import bisect

from pygments.lexer import Lexer, LexerContext, RegexLexer, ExtendedRegexLexer, \
     bygroups, include, using, this, do_insertions
from pygments.token import Punctuation, Text, Comment, Keyword, Name, String, \
     Generic, Operator, Number, Whitespace, Literal
from pygments.util import get_bool_opt
from pygments.lexers.other import BashLexer

__all__ = ['AugtoolLexer', 'AugeasLexer']


class AugtoolLexer(RegexLexer):
    """
    Lexer for Augtool commands.
    """

    name = 'Augtool'
    aliases = ['augtool']
    filenames = ['*.augtool']
    mimetypes = ['text/x-augtool']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'[;#].*?$', Comment),
            (r'\[.*?\]$', Keyword),
            (r'^augtool\>(\s+)',
             bygroups(Text))
        ]
    }

    def analyse_text(text):
        for line in text.split('\n'):
            line = line.strip()
            if not (line.startswith('#') or line.startswith('augtool> ') or not line):
                return False
        return True

