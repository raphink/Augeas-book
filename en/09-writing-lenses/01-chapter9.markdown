# Writing Your Own Lenses #

Augeas comes with a set of various lenses which cover most of the basic configuration files on a Unix machine. However, there are so many configuration file formats on Unix systems, that you are very likely to miss one at some point.

Augeas lenses are written in a ML language that is similar to OCaml. The language consists mostly in regexps and operators to combine them.


## A simple example ##

Since Augeas lenses are mostly a combination of regular expressions that are often complex and fragile, it is safer to consider writing unit tests for each lens to ensure non-regression and confirm that all known cases are met by the lens. Our work will thus begin with the writing of a unit test, which will specify the way we will map the configuration entries to the Augeas tree. For extended information on unit tests, see the end of this chapter.

### Unit Test ###

__Example of a simple key/value conffilem, step by step__


### Module ### 


__Example of a simple key/value conffile, step by step__


## Regular expressions ##

The bidirectional nature of the Augeas language imposes strict conditions on the language (see chapter 3). This makes complex regular expressions languages such as PCRE hard to implement. For this reason, Augeas only supports POSIX simple regular expressions.

__Give Examples__


## Special keywords ##

The Augeas language provides a set of keywords to build lenses.


### key ###


### label ###


### store ###


### value ###


### seq ###


### rec ###


### square ###



## Combination Operators ##

Augeas lenses are put together by assembling regular expressions with combination operators.


### Concatenation Operator ###


### Union Operator ###


## Filters and Autoload ##

Augeas lenses need to specify which files they apply to. If they didn't, Augeas would have no way to know which lens to apply to which files. Trying to guess would be a really bad idea. For example, consider a file whose only content is the following:

	# this is a comment

Many lenses are able to parse this line, and will mostly likely map it the same way. However, once a lens has been chosen for the file, the rest of the configguration statements are likely to be very different from one lens to another, so you are almost sure that the lens you chose will be wrong.

Each lenses may have one and only one autoload statement, involving a lens and a filter, such as the following:

	autoload xfm
	let lns = ...
	let filter = incl "/etc/foo.conf"
	let xfm = transform lns filter


## Typechecking lenses ##


Augeas comes with a command line tool called `augparse` which can be used to typecheck lenses, checking that they meet the conditions to be used as bidirectional transforms.


### Typechecking recursive lenses ###




## Unit tests ##

We have mentionned the importance of unit tests in the beginning of this chapter. It is worth repeting it: unit tests are essential to the stability of an Augeas lens. Unit tests need to be well written and kept up-to-date with new features and bug fixes if you want to ensure that your lens does what it has been written for.

Augeas provides keywords to achieve unit tests in both the get and put directions.


## Using Generic Modules ##

Augeas provides special modules to ease the writing of lenses.


### The Util module ###

The Util (`util.aug`) module provides definitions of comments, empty lines and other utilities.

__List functions__ and give examples.


### The Sep module ###

The Sep (`sep.aug`) module provides definitions for separators.
__List functions__ and give examples.

Note: `Sep.opt_space` is a synonym for `Util.indent`. Both are stricly equivalent, but it is clearer to use the former as a separator and the latter as an indentation.


### The Rx module ###

The Rx (`rx.aug`) module provides definitions for usual regular expressions.
__List functions__ and give examples.


### The Build module ###

The Build (`build.aug`) module provides definitions for usual constuctions of regular expression.
__List functions__ and give examples.


### The IniFile module ###

INI files are quite standard even on Unix systems. However, there are many different implementations and specificities. The Inifile (`inifile.aug`) module provides definitions to ease the writing of lenses for specific INI files. It is used in lenses such as Php (`php.aug`), MySQL (`mysql.aug`) or Puppet (`puppet.aug`).
__List functions__ and give examples.

