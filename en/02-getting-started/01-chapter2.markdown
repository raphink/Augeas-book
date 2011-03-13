# Getting Started #

While Augeas is a C library with bindings, it also provides a command-line tool called augtool, which we will be using in the following examples. In chapter 4, we will see how to use the API and bindings directly.


## Parsing your System Configuration Files ##

The first thing you might want to do is to see how Augeas sees your system configuration files. Fire up augtool:

	$ augtool

This will give you an interactive shell which takes commands passed to Augeas. Augeas transforms your configuration files into a tree, which has two nodes at its root: `/augeas` and `/files`. The `/augeas` node contains metadata, which we will be looking at later on, while `/files` contains the representation of the files Augeas was able to parse. You can see these two nodes by typing `ls /`:

	> ls /
	augeas/ = (none)
	files/ = (none)

What does that mean? We see the two nodes at the top of the Augeas tree, and we see that none of them has a value. In the Augeas tree, each node can have children and a value.

`ls` is an augtool command which lists the children of the given node and gives their value if any.

You can see which files (or directories containing files) were successfully parsed by Augeas in `/etc` by typing `ls /files/etc`.


## Using a Fakeroot ##


## Modifying Files ##


## Preserving existing files ##

Augeas offers two options to preserve the existing files when saving the tree. In `augtool`, these options can be triggered with the following flags:

* --backup will save the original file with the extension .augorig and write the new file under the original file name ;
* --new will save the modified file with a .augnew extension and leave the original file untouched.

These options actually modify the value of the `/augeas/save` node in the Augeas tree. See chapter __FIXME__ for more information.

