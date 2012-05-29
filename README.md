Augeas Book Contents
=====================

This is the source code for the Augeas book contents.

Errata
======
If you see anything that is technically wrong or otherwise in need of correction,
please email me at raphink at gmail dot com to inform me.


Building the book
=================

In order to build this book, you need:
 
* LuaLaTeX (I recommend using the latest TeXLive distribution);
* Pygments (``sudo apt-get install python-pygments`` on Debian/Ubuntu).


First, install the augeas lexer for pygments:

    $ cd augeas-lexer/
    $ sudo easy_install .
    $ cd ..

Then, cd to the book directory and type make:

    $ cd en/
    $ make

This should produce the final PDF file.


