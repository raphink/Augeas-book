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


## Installing Augeas ##

### Installing from Source ###

You might want to install Augeas from source if your distribution does not provide any binary packages, or if you simply want to use the latest version of Augeas or tune compilation parameters.

You can find the latest source code on the Augeas website:

 http://augeas.net/download/

Next, install the necessary dependencies to build Augeas. The minimal dependencies you will need are the readline headers. You can use one of these commands to install them:

 $ sudo apt-get install libreadline-dev

Then, extract, compile and install:

 $ tar xvzf augeas-0.8.0.tar.gz
 $ cd augeas-0.8.0
 $ ./configure
 $ make
 $ sudo make install

If you wish to build the documentation for Augeas, you will to add naturaldocs and pdflatex to the dependencies, and add the --with-naturaldocs and --with-pdfdocs flags to the ./configure command.

### Installing from Binary Packages ###

Most distributions provide Augeas packages. On Debian and Ubuntu systems, you can install the Augeas library and the augtool command-line interface with the following:

 $ sudo apt-get install augeas-tools

This will actually install 3 packages: libaugeas0 (the library itself), augeas-lenses (the official Augeas lenses), and augeas-tools (the command-line tool).

You might also want to install the documentation package with:

 $ sudo apt-get install augeas-doc


