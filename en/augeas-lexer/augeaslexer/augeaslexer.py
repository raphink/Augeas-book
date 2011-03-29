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


class AugtoolShellLexer(RegexLexer):
    """
    Lexer for Augtool commands.
    """

    name = 'AugtoolShell'
    aliases = ['augtool-shell']
    filenames = ['*.augtoolshell']
    mimetypes = ['text/x-augtool-shell']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'[;#].*?$', Comment),
            (r'=', Operator),
            (r'^(augtool\>)(\s+)(\S+)(?:(\s+)(.*))?$',   # augtool prompt
             bygroups(Generic.Prompt, Text, Keyword, Text, String)),
            (r'^(Saved \d file\(s\))$', Text),      # saved
            (r'^(rm\s+:.*)', Text),                 # removed nodes
            (r'^([^=]+)(?:(\s+)(=)(\s+)(.*))?$',    # ls/get/print
             bygroups(String, Text, Operator, Text, String)),
            (r'^(\S+)(\s+)(label)(=)(\S+)(\s+)(value)(=)(\S+)(\s+)(span)(=)(\S+)$',  # span output
             bygroups(String, Text, Keyword, Operator, String, Text,
                                    Keyword, Operator, String, Text,
                                    Keyword, Operator, String)),
        ]
    }

    def analyse_text(text):
        for line in text.split('\n'):
            line = line.strip()
            if not (line.startswith('#') or line.startswith('augtool> ') or not line):
                return False
        return True
