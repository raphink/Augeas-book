# Augeas metadata 

\index{Metadata}
\index{Tree!\slash{}augeas|see{Metadata}}

We have seen earlier that the `/augeas` top node exposes Augeas metadata which can be parsed and modified in the same fashion as the `/files` data.
This chapter will focus on documenting the various parts of the `/augeas` tree and their functions.


## The root node 

\index{Metadata!\slash{}augeas\slash{}root}
\index{augtool!options!--root}
\index{Environment variables!\textsc{augeas\_root}}

The `/augeas/root` node contains the root of the Augeas tree. This is the variable which can be set via either the `AUGEAS_ROOT` environment variable or the `--root` option to `augtool`.

\index{Commands!print}

Example:

	$ augtool --root fakeroot
	augtool> print /augeas/root
	/augeas/root = "fakeroot/"

> ![**NOTE**][info] *As of Augeas 0.8.0, this node is purely informative:
> changing its value has no effect on the way Augeas works.*


## The version tree 

\index{Metadata!\slash{}augeas\slash{}version}

`/augeas/version` is a tree which contains several informations:

* The top node has the version of Augeas as its value ;
* The `save` node contains `mode` nodes which list the known saving modes for this version of Augeas ;
* The `defvar` node contains **what exactly??**.

\index{Commands!print}

Example:

	augtool> print /augeas/version/
	/augeas/version = "0.8.0"
	/augeas/version/save
	/augeas/version/save/mode[1] = "backup"
	/augeas/version/save/mode[2] = "newfile"
	/augeas/version/save/mode[3] = "noop"
	/augeas/version/save/mode[4] = "overwrite"
	/augeas/version/defvar
	/augeas/version/defvar/expr


## The save node 

\index{Metadata!\slash{}augeas\slash{}save}

The `/augeas/save` node contains the saving mode used by Augeas for the session. The value of this node must be one of the values listed in the `/augeas/version/save/mode` nodes.

If this node is modified during the session, it will affect the behaviour of the `save` call whenever it is executed.


## The load tree 

\index{Metadata!\slash{}augeas\slash{}load}

The `/augeas/load` tree contains the lenses metadata. For each lens loaded in the Augeas session, it lists 3 types of nodes:

* a `lens` node, which specifies the name of the module used by this lens ;
* `incl` nodes for each inclusion path to files recognized by this lens ;
* `excl` nodes for each path to be excluded from this lens.

\index{Commands!print}

Example:

	augtool> print /augeas/load/Pam/
	/augeas/load/Pam
	/augeas/load/Pam/lens = "@Pam"
	/augeas/load/Pam/incl = "/etc/pam.d/*"
	/augeas/load/Pam/excl[1] = "*.augnew"
	/augeas/load/Pam/excl[2] = "*.augsave"
	/augeas/load/Pam/excl[3] = "*.dpkg-dist"
	/augeas/load/Pam/excl[4] = "*.dpkg-bak"
	/augeas/load/Pam/excl[5] = "*.dpkg-new"
	/augeas/load/Pam/excl[6] = "*.dpkg-old"
	/augeas/load/Pam/excl[7] = "*.rpmsave"
	/augeas/load/Pam/excl[8] = "*.rpmnew"
	/augeas/load/Pam/excl[9] = "*~"


This tree can be manipulated to fine tune the lenses known by Augeas for a session, as well as the files parsed in the session. When the `/augeas/load` tree is modified, you have to call `load` again for the changes to take effect.

Let us look at some use cases.


### Using only one lens

It is common to use Augeas to modify only one file. In that case you know exactly which lens you want to use and on which file. For performance reasons, you might want to narrow the lenses and files Augeas knows about. For example, if you want to only modify `/etc/fstab`, using the `Fstab` lens. In order to do that, we can start `augtool` without loading any lenses:

\index{augtool!options!--noautoload}

	$ augtool --noautoload
	augtool> print /augeas/load
	/augeas/load

\index{Flags!\textsc{aug\_no\_modl\_autoload}}

> ![**NOTE**][info] *This can also be achieved using the `AUG_NO_MODL_AUTOLOAD` flag with the API*

The `print` command shows us that no lenses are known in the session. We can now tell Augeas to load the `Fstab` lens and to include `/etc/fstab` for it:

\index{Commands!set}
\index{Commands!print}

	augtool> set /augeas/load/Fstab/lens "Fstab.lns"
	augtool> set /augeas/load/Fstab/incl "/etc/fstab"
	augtool> print /augeas/load
	/augeas/load
	/augeas/load/Fstab
	/augeas/load/Fstab/lens = "Fstab.lns"
	/augeas/load/Fstab/incl = "/etc/fstab"


We can now call `load` and list the files in `/files/etc`:

\index{Commands!load}
\index{Commands!ls}

	augtool> load
	augtool> ls /files/etc
	fstab/ = (none)

> ![**NOTE**][info] *Lenses loaded automatically have a `lens` statement which begins with a `@`, such a `@Fstab`. When you set the lens manually however, you have to specify the lens to use, for example `Fstab.lns`. See chapter 9 for more information on writing lenses.*


### Parsing a specific file

Augeas lenses have hardcoded lists of files they know about. For example the `Fstab` lens has an include statement for `/etc/fstab` hardcoded in `fstab.aug`. While Augeas attempts to cover the most common needs for inclusions, it cannot know about all files you are using. Some lenses don't even have default include statements because no common files are known to use them. This is the case of the `Json` lens, which is useful but applies to no common configuration file.

So how do you go about using the `Json` lens on a JSON file? You can modify the `/augeas/load` tree for that. For example if you have a `foo.json` file in your current directory, you could do the following:

\index{augtool!options!--root}
\index{Commands!set}
\index{Commands!load}
\index{Commands!ls}

	$ augtool --root .
	augtool> set /augeas/load/Json/incl "/foo.json"
	augtool> load
	augtool> ls /files
	foo.json/ = (none)


> ![**NOTE**][info] *This technique can be combined with the above to load only the `Json` module*


## The files tree 

\index{Metadata!\slash{}augeas\slash{}files|(}

The `/augeas/files` provides metadata about the files parsed by Augeas. The paths in this tree mirror thoses of the `/files` tree.

For each file, the following nodes may be present.


### The path node

`path` is the path to the file data in the `/files` tree ;


### The mtime node

`mtime` is the last modification time of the file ;


### The lens tree

The `lens` tree indicates the lens used to parse this file, as specified in the `/augeas/load` tree (see above).
The `lens/info` node gives the path to the lens module (physically), as well as the position of the lens declaration in the
 file.


### The error tree

When Augeas fails to parse a file, the parsing error is listed here.

This tree contains several nodes:

* `pos` is the position in the file, relative to the beginning, where Augeas failed to parse ;
* `line` is the line in the file where Augeas failed to parse ;
* `char` is the character of the line where Augeas failed to parse ;
* `lens` is the lens that failed to parse. It is usually the same as as `lens/info` node listed above ;
* `message` is the error message yielded by Augeas.

For more information on interpreting the error messages, see chapter 10.


### Example


	$ augtool 
	augtool> print /augeas/files/etc/ldap.conf/
	/augeas/files/etc/ldap.conf
	/augeas/files/etc/ldap.conf/path = "/files/etc/ldap.conf"
	/augeas/files/etc/ldap.conf/mtime = "1298365882"
	/augeas/files/etc/ldap.conf/lens = "@Spacevars"
	/augeas/files/etc/ldap.conf/lens/info = "/usr/share/augeas/lenses/dist/spacevars.aug:37.23-.46:"
	/augeas/files/etc/ldap.conf/error = "parse_failed"
	/augeas/files/etc/ldap.conf/error/pos = "9510"
	/augeas/files/etc/ldap.conf/error/line = "310"
	/augeas/files/etc/ldap.conf/error/char = "0"
	/augeas/files/etc/ldap.conf/error/lens = "/usr/share/augeas/lenses/dist/spacevars.aug:37.23-.46:"
	/augeas/files/etc/ldap.conf/error/message = "Iterated lens matched less than it should"

In the example above, we see the that `/etc/ldap.conf` uses the `@Spacevars` lens, located in `spacevars.aug` on line 37, between characters 23 et 46.

The parsing of `/etc/ldap.conf` failed on position 9510, which located in beginning of line 310. The error message indicates that the file could not be fully parsed.

\index{Metadata!\slash{}augeas\slash{}files|)}

## The variables tree 

\index{Metadata!\slash{}augeas\slash{}variables}
\index{Path expressions!variables!defvar}

When you set variables in Augeas (see chapter 4), the paths of the variables are recorded here.

\index{Commands!print}
\index{Commands!defvar}

Example:

	augtool> defvar l /augeas/files/etc/ldap.conf/
	augtool> print /augeas/variables/
	/augeas/variables
	/augeas/variables/l = "/augeas/files/etc/ldap.conf"

> ![**NOTE**][info] *As of Augeas 0.8.0, this node is purely informative:
> changing its value has no effect on the way Augeas works.*


## The span node 

\index{Metadata!\slash{}augeas\slash{}span}
\index{augtool!options!--span}
\index{Flags!\textsc{aug\_enable\_span}}

The `/augeas/span` node indicates whether the `span` functionality^[See chapter 2: *Locating nodes in files*] is activated in the session.


