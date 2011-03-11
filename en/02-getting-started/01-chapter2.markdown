# Getting Started #

While Augeas is a C library with bindings, it also provides a command-line tool called augtool, which we will be using in the following examples. In chapter 4, we will see how to use the API and bindings directly.

## Parsing your System Configuration Files ##

The first thing you might want to do is to see how Augeas sees your system configuration files. Fire up augtool:

 $ augtool

This will give you an interactive shell which takes commands passed to Augeas. Augeas transforms your configuration files into a tree, which has two roots at its node: "/augeas" and "/files". The "/augeas" node contains metadata, which we will be looking at later on, while "/files" contains the representation of the files Augeas was able to parse. You can see these two nodes by typing "ls /":

 > ls /


## Using a Fakeroot ##


## Modifying Files ##


