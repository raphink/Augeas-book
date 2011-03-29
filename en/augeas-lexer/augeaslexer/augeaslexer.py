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

__all__ = ['AugtoolShellLexer', 'AugtoolLexer', 'AugeasLexer',
           'PuppetAugeasLexer']


class AugtoolShellLexer(RegexLexer):
    """
    Lexer for Augtool shell sessions.
    """

    name = 'AugtoolShell'
    aliases = ['augtool-shell']
    filenames = ['*.augtoolshell']
    mimetypes = ['text/x-augtool-shell']

    tokens = {
        'root': [
            (r'^\s+$', Text),           # empty line
            (r'^[;#].*?$', Comment),    # comment
            (r'^(rm\s+:.*)', Text),     # removed nodes
            (r'^(Saved.*)', Text),      # saved
            (r'^(augtool\>)(\s+)(\S+)(?:(\s+)(.*))?$',   # augtool prompt
             bygroups(Generic.Prompt, Whitespace, Keyword, Whitespace, String)),
            (r'^([^=]+)(?:(\s+)(=)(\s+)(.*))?$',    # ls/get/print
             bygroups(String, Whitespace, Operator, Whitespace, String)),
            (r'^(\S+)(\s+)(label)(=)(\S+)(\s+)(value)(=)(\S+)(\s+)(span)(=)(\S+)$',  # span output
             bygroups(String, Whitespace, Keyword, Operator, String, Whitespace,
                                    Keyword, Operator, String, Whitespace,
                                    Keyword, Operator, String)),
        ]
    }


class AugtoolLexer(RegexLexer):
    """
    Lexer for Augtool commands
    """

    name = 'Augtool'
    aliases = ['augtool']
    filenames = ['*.augtool']
    mimetypes = ['text/x-augtool']

    tokens = {
        'root': [
            (r'^\s+$', Text),            # empty line
            (r'[;#].*?$', Comment),      # comment
            (r'^(\S+)(?:(\s+)(.*))?$',   # augtool command
             bygroups(Keyword, Whitespace, String)),
        ]
    }


class AugeasLexer(RegexLexer):
    """
    Lexer for Augeas modules
    """

    name = 'Augeas'
    aliases = ['augeas', 'aug']
    filenames = ['*.aug']
    mimetypes = ['text/x-augeas']

    tokens = {
        'root': [
            (r'^\s+$', Text),            # empty line
            (r'\(\*.*', Comment),        # comment
            (r'.*\*\)', Comment),        # comment
            (r'[\[\]=]', Operator),
            (r'\b(autoload|let|test|transform|incl)\b', Keyword),
            (r'\b(key|value|store|label)\b', Keyword),
            (r'\b/.*/\b', String.Regex),
            (r'\b".*"\b', String),
            (r'(let)(\s+)(\S+)(\s+)(=)(?:(\s+)(.*))',
             bygroups(Keyword, Whitespace, Name, Whitespace,
                      Operator, Whitespace, String)),
        ]
    }


class PuppetAugeasLexer(RegexLexer):
    """
    Lexer for the Puppet Augeas type
    """

    name = 'PuppetAugeas'
    aliases = ['puppet-augeas']
    filenames = ['*.pp-aug']
    mimetypes = ['text/x-puppet-augeas']

    tokens = {
        'root': [
            (r'^\s+$', Text),            # empty line
            (r'[;#].*?$', Comment),
            (r'[\[\]{}]', Operator),
            (r'=>', Operator),
            (r',', Text),
            (r'(\w+)(\s+)({)(\s+)(".*")(:)',
             bygroups(Keyword, Whitespace, Operator,
                      Whitespace, Name, Text)),
            (r'(\s*)(context)(\s+)(=>)(\s+)(".*")(,)?',
             bygroups(Whitespace, Keyword, Whitespace, Operator,
                      Whitespace, String, Text)),
            (r'(\s*)(changes)(\s+)(=>)(\s+)(\[)',
             bygroups(Whitespace, Keyword, Whitespace, Operator,
                      Whitespace, Operator)),
            (r'(\s*)(onlyif)(\s+)(=>)(\s+)(".*")(,)?',
             bygroups(Whitespace, Keyword, Whitespace, Operator,
                      Whitespace, String, Text)),
            (r'(\s*)(".*")(,)?',
             bygroups(Whitespace, String, Text)),
            (r'(\s*)(\])(,)?',
             bygroups(Whitespace, Operator, Text)),
        ]
    }



