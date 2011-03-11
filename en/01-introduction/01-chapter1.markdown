# Introduction #

In the world of Unix systems, there is no standard way to store configuration. Countless of formats can be found, from standard INI files to complex, specific, multi-level formats.

Augeas provides a way to cleanly manage these configuration files through a unified API.


## Configuration Data Editing Approaches ##

There are three main approaches to the issue of configuration data editing on Unix systems:

* Keyhole approaches ;
* Greenfield approaches ;
* Templating.


### Keyhole Approaches ###

While most programming languages provides modules to edit at least the most standard of these formats, a lot systems administrators and developers have had to manipulate these files using string editing tools such as sed, awk or cut, or even to write scripts dedicated to a specific parsing job. In the majority of these cases, the results are not garanteed, and you are likely to ruin the configuration files if your parsing expressions are wrong.


### Greenfield approaches ###


### Templating ###



## A Unified Configuration API ##



