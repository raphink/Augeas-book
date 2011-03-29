"""
Augeas syntax highlighting for Pygments.
"""

from setuptools import setup

entry_points = """
[pygments.lexers]
augtool-shell = augeaslexer.augeaslexer:AugtoolShellLexer
augtool = augeaslexer.augeaslexer:AugtoolLexer
puppet-augeas = augeaslexer.augeaslexer:PuppetAugeasLexer
"""

setup(
    name         = 'augeaslexer',
    version      = '0.1',
    description  = __doc__,
    author       = "Raphael Pinson",
    packages     = ['augeaslexer'],
    entry_points = entry_points
) 

