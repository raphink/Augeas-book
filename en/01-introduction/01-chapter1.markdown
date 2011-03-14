# Introduction #

In the world of Unix systems, there is no standard way to store configuration. Countless of formats can be found, from standard INI files to complex, specific, multi-level formats, making the infamous /etc directory a sort of digital Augean stables.

Augeas provides a way to cleanly manage these configuration files through a unified API.


## Configuration Data Editing Approaches ##

While system administrators are well aware of the heterogenous state of the configuration data on Unix systems, these configurations have to be edited automatically in many situations.

There are three main approaches to the issue of configuration data editing on Unix systems.


### Keyhole Approaches ###

While most programming languages provide modules to edit at least the most standard of these formats, a lot of system administrators and developers have had to manipulate these files using string editing tools such as sed, awk or cut, or even to write scripts dedicated to a specific parsing job. In the majority of these cases, the results are not garanteed, and you are likely to ruin the configuration files if your parsing expressions are wrong.

Configuration management tools such as Cfengine provide tools (like AppendIfNoSuchLine) to achieve keyhole approaches, but the problems are similar to using string editing tools: you have no garantee that the result will be a valid configuration file, and you have to write the regexps yourself.

Augeas is particularly useful to ease and secure this kind of approach.


### Greenfield approaches ###

When you are the main system administrator of a machine and you wish to control all the parameters of the machine, you may want to provide the configuration files entirely. In this case, it is common to set a repository of configuration files, or a database, which will contain the whole configuration as will be deployed to the machines.


### Templating ###

If you wish to control whole configuration files but you need a fine-grained mechanism to generate these files, templating is probably the best approach. There are lots of options to achieve this. Puppet, for example, provides ERB templates that let you easily generate configuration files from exported variables.


## A Unified Configuration API ##

In many cases, system administrators and users want to change a single value in their configuration without affecting the rest of it. This is often achieved using the keyhole approach, which as we have seen is not very reliable. A better approach would be to have a unified configuration API that lets you modify configurations in a simple and reliable way, ensuring that the modified files are valid configuration files. This is the goal of Augeas.


## What Augeas is not ##

A principle on Unix systems ensures the stability and simplicity of the system tools: each tool attempts to do one thing, and to do it well. Augeas is no exception to this rule, so that Augeas is as much defined by the things it does not try to accomplish as by its goals.

Before we dive into what Augeas can do for you, it is important to note the following points.


### Not an abstraction layer ###

Augeas does not attempt to provide an abstraction layer from the native configuration format. The organization of the Augeas tree mirrors closely that of the configuration files it represents.

As an example, if the `/etc/foo.conf` configuration file contains an include statement such as the following:

	#include /etc/foo.d/*

Augeas will not attempt to parse the contents of the files in `/etc/foo.d/*` and add them to the `/etc/foo.conf` tree. Instead, it will provide a tree like the following:

	/files/etc/foo.conf
	/files/etc/foo.conf/#include = /etc/foo.d/*

`#include` is just a parameter of the `/etc/foo.conf` configuration file and `/etc/foo.d/*` is the value of the parameter. The contents of `/etc/foo.d/*` will probably appear in the tree if the lens is able to parse them, but in no way will Augeas make a logical link between `/etc/foo.conf` and `/etc/foo.d/*`.

Other software provide this kind of abstraction layer. This is the case of Config::Model, which can use Augeas as a backend, and is able to understand the logic of a configuration files, such as include statements, or the link between several statements in a configuration file.

Another consequence of this non-goal is that the statements in the Augeas tree will appear in the same order as they do in the configuration file. In some cases, it is technically possible to write Augeas lenses that invert parameters or otherwise modify the logic of the configuration statements, but it is not recommended to implement such mechanisms, as the Augeas tree should stay as close as possible in its logic to the configuration files it is representing.


### Not a cross-platform abstraction layer ###

For a similar reason, Augeas does not attempt to be a cross-platform abstraction layer. When Augeas finds Apache configuration files in `/etc/httpd/httpd.conf` on some operating systems and in `/etc/apache2/apache2.conf` in others, these files will be respectively represented in the tree as `/files/etc/httpd/httpd.conf` and `/files/etc/apache2/apache2.conf` respectively.

Similarly, some operating systems provide their network configuration in `/etc/sysconfig/network` while others use `/etc/network/interfaces`. Augeas will represent these two files in different parts of the tree, and the tree will mirror the way each of these files is organized, without attempting to provide a unified way to configure network interfaces across these operating systems.

Other projects such as netcf, based on Augeas, provide a cross-platform abstraction layer to manage network interfaces regardless of the operating system, but it is not Augeas' goal.


### No remote management support ###

When you are dealing with a whole fleet of servers and wish to set a parameter for each of them, it is useful to use a tool that has a network protocol for remote management. Augeas does not attempt to be that tool, and the Augeas API is designed to be a local API.

Remote access to the Augeas API are meant to be added on top of it, not in it.

Puppet is an example of configuration management tool which supports Augeas as a native type and provides remote management fonctionalities.


### Very little modelling ###

Augeas does not attempt to understand or otherwise interprete configuration files. As stated before, Augeas does not attempt to provide an abstraction layer, but it provides a light modelling, although very close to the organization of the configuration files.

For example, an `/etc/hosts` line like the following:

	192.168.0.10	aslan	# Added by NetworkManager

will be represented by the following tree:

	/files/etc/hosts
	/files/etc/hosts/1
	/files/etc/hosts/1/ipaddr = "192.168.0.10"
	/files/etc/hosts/1/canonical = "aslan"
	/files/etc/hosts/1/#comment = "Added by NetworkManager"

The order of the statements is strictly kept, Augeas does not inteprete the configuration files per se, but it labels each of the fields on the line to ease access to the configuration items.


## Installing Augeas ##

### Installing from Source ###

You might want to install Augeas from source if your distribution does not provide any binary packages, or if you simply want to use the latest version of Augeas or tune compilation parameters.

You can find the latest source code on the Augeas website:

	http://augeas.net/download/

Next, install the necessary dependencies to build Augeas. The minimal dependencies you will need are the readline headers. You can use one of these commands to install them:

	$ yum install readline-devel
	$ sudo apt-get install libreadline-dev

Then, extract, compile and install:

	$ tar xvzf augeas-0.8.0.tar.gz
	$ cd augeas-0.8.0
	$ ./configure
	$ make && make install

If you wish to build the documentation for Augeas, you will to add `naturaldocs` and `pdflatex` to the dependencies, and add the `--with-naturaldocs=HTML` and `--with-pdfdocs` flags to the `./configure` command.


### Installing from Binary Packages ###

Most distributions provide Augeas packages.

On RedHat systems, you can install the `augeas` package, using yum for example:

	$ yum install augeas

On Debian and Ubuntu systems, you can install the Augeas library and the augtool command-line interface with the following:

	$ sudo apt-get install augeas-tools

This will actually install 3 packages: libaugeas0 (the library itself), augeas-lenses (the official Augeas lenses), and augeas-tools (the command-line tool).

You might also want to install the documentation package with:

	$ sudo apt-get install augeas-doc


### Installing from the Development Head ###

Augeas is maintained in a public repository which can be cloned and used to test the latest functionalities and fixes before they are released.

If you wish to build and install from the development head, you will need `git` (provided by the `git-core` package on most operating systems), `autoconf`, `automake` and `libtool`, as well as the normal dependencies to build Augeas from source. Then follow these instructions:

	$ git clone git://git.fedorahosted.org/augeas.git
	$ ./autogen.sh
	$ ./configure
	$ make && make install

