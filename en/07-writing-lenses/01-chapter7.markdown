# Writing Your Own Lenses #

Augeas comes with a set of various lenses which cover most of the basic configuration files on a Linux machine. However, there are so many configuration file formats on Linux systems, that you are very likely to miss one at some point.

Augeas lenses are written in a ML language that is similar to OCaml. The language consists mostly in regexps and operators to combine them.


## A simple example ##

Since Augeas lenses are mostly a combination of regular expressions that are often complex and fragile, it is safer to consider writing unit tests for each lens to ensure non-regression and confirm that all known cases are met by the lens. Our work will thus begin with the writing of a unit test, which will specify the way we will map the configuration entries to the Augeas tree. For extended information on unit tests, see the end of this chapter.

### Unit Test ###

### Lens ### 


## Regular expressions ##

The bidirectional nature of the Augeas language imposes strict conditions on the language. This makes complex regular expressions languages such as PCRE hard to implement. For this reason, Augeas only supports POSIX simple regular expressions.


## Special keywords ##

key, label, store, value. etc.

## Combination Operators ##

Augeas lenses are put together by assembling regular expressions with combination operators.


## Filters and Autoload ##

Augeas lenses need to specify which files they apply to. If they didn't, Augeas would have no way to know which lens to apply to which files. Trying to guess would be a really bad idea. For example, if you have a file whose only content is the following:

	# this is a comment

Many lenses are able to parse this line, and will mostly likely map it the same way. However, once a lens has been chosen for the file, the rest of the configguration statements are likely to be very different from one lens to another, so you are almost sure that the lens you chose will be wrong.


## Unit tests ##

We have mentionned the importance of unit tests in the beginning of this chapter. It is worth repeting it: unit tests are essential to the stability of an Augeas lens. Unit tests need to be well written and kept up-to-date with new features and bug fixes if you want to ensure that your lens does what it has been written for.

Augeas provides keywords to achieve unit tests in both the get and put directions.





