# Exploring augtool

While Augeas is a C library with bindings, it also provides a command-line tool called `augtool`, which we will be using in the following examples. In chapter 5, we will see how to use the API and bindings directly.

\index{augtool!commands|see{Commands}}

## Parsing your System Configuration Files 

The first thing you might want to do is to see how Augeas sees your system configuration files. Fire up `augtool`:

	$ augtool

\index{Commands!ls}

This will give you an interactive shell which passes commands to Augeas. Augeas transforms your configuration files into a tree, which has two nodes at its root: `/augeas` and `/files`. The `/augeas` node contains metadata, which we will be looking at later on, while `/files` contains the representation of the files Augeas was able to parse. You can see these two nodes by typing `ls /`:

	augtool> ls /
	augeas/ = (none)
	files/ = (none)

What does that mean? We see the two nodes at the top of the Augeas tree, and we see that neither of them has a value. In the Augeas tree, each node can have children and a value associated with it.

`ls` is an `augtool` command which lists the children of the given node and gives their value (if any).

You can see which files (or directories containing files) were successfully parsed by Augeas in `/etc` by typing `ls /files/etc`:

	augtool> ls /files/etc
	nsswitch.conf/ = (none)
	odbc.ini = (none)
	passwd/ = (none)
	ntp.conf/ = (none)
	services/ = (none)
	sysctl.conf/ = (none)
	shells/ = (none)
	samba/ = (none)
	securetty/ = (none)
	crypttab/ = (none)
	...

\index{Commands!print}

Let's inspect the contents of the first line of `/etc/fstab` in the Augeas tree. We can use the `print` command to inspect nodes and their values recursively:

	augtool> print /files/etc/fstab/1
	/files/etc/fstab/1
	/files/etc/fstab/1/spec = "proc"
	/files/etc/fstab/1/file = "/proc"
	/files/etc/fstab/1/vfstype = "proc"
	/files/etc/fstab/1/opt[1] = "nodev"
	/files/etc/fstab/1/opt[2] = "noexec"
	/files/etc/fstab/1/opt[3] = "nosuid"
	/files/etc/fstab/1/dump = "0"
	/files/etc/fstab/1/passno = "0"

Each of the child nodes beneath the `1` node refers to a part of a single line in the `/etc/fstab` file.  The filesystem options are further split into separate nodes under the `opt` node so they can be managed individually.

What if we only wanted to find the `opt` nodes of this first line? The `match` command lets us find the nodes matching an expression:

\index{Commands!match}

	augtool> match /files/etc/fstab/1/opt
	/files/etc/fstab/1/opt[1] = nodev
	/files/etc/fstab/1/opt[2] = noexec
	/files/etc/fstab/1/opt[3] = nosuid

Now, we might want to get the value of the single node matching an expression, and make sure that this node is unique. For example, if we want the value of the first `opt` node of this first line, we could use the `get` command:

	augtool> get /files/etc/fstab/1/opt[1]
	/files/etc/fstab/1/opt[1] = nodev

\index{Commands!quit}

To leave the `augtool` session, you can type `quit` or `^D`:

	augtool> quit


## Using a Fakeroot 

It is often useful to play with `augtool` when you want to understand the Augeas tree or try XPath expressions. However, you likely don't want to play with the files in your `/etc` directory and take the risk of ruining your system. Augeas lets you set a fakeroot so that the files parsed and modified by Augeas are taken from this root instead of the `/` directory of your system.

\index{augtool!options!--root}
\index{Environment variables!\textsc{augeas\_root}}

In `augtool` you can set this fakeroot by using the `--root` option:

	$ mkdir -p myroot/etc
	$ rsync -av /etc/ myroot/etc
	$ augtool -r myroot

In general, you can also set the location of this fakeroot with the `AUGEAS_ROOT` environment variable:

	$ export AUGEAS_ROOT="$(pwd)/myroot"
	$ augtool

This option can also let you modify files inside a chroot for example.


## Modifying Files 

We have seen already how Augeas lets you parse your configuration files in a unified way. The Augeas tree is not only a parsing facility as Augeas exposes commands to modify the tree and save the changes to the original files.

The fakeroot option will be useful for us here, in order to modify the files without affecting the system. We will also use the `--backup` option in `augtool` so that the original files are preserved with a `.augsave` extension.

\index{augtool!options!--backup}
\index{augtool!options!--root}
\index{Commands!rm}
\index{Commands!quit}
\index{Commands!save}
\index{Environment variables!\textsc{augeas\_root}}

Let us change the filesystem options specified on the first line of `/etc/fstab` by removing the third `opt` node:

	$ augtool --backup --root myroot
	augtool> rm /files/etc/fstab/1/opt[3]
	rm : /files/etc/fstab/1/opt[3] 1
	augtool> print /files/etc/fstab/1
	/files/etc/fstab/1 /files/etc/fstab/1/spec = "proc"
	/files/etc/fstab/1/file = "/proc"
	/files/etc/fstab/1/vfstype = "proc"
	/files/etc/fstab/1/opt[1] = "nodev"
	/files/etc/fstab/1/opt[2] = "noexec"
	/files/etc/fstab/1/dump = "0"
	/files/etc/fstab/1/passno = "0"
	augtool> save
	Saved 1 file(s)
	augtool> quit
	$ diff -u myroot/etc/fstab myroot/etc/fstab.augsave
	--- myroot/etc/fstab	2011-03-14 23:46:07.000000000 +0100
	+++ myroot/etc/fstab.augsave	2010-09-30 08:45:53.000000000 +0200
	@@ -5,7 +5,7 @@
	 # devices that works even if disks are added and removed. See fstab(5).
	 
	 # <file system> <mount point>   <type>  <options>       <dump>  <pass>
	-proc            /proc           proc    nodev,noexec 0       0
	+proc            /proc           proc    nodev,noexec,nosuid 0       0
	 # / was on /dev/sdb1 during installation
	 UUID=c8acd38c-037a-46c1-a8ce-3ac1c602c367 /               ext4    errors=remount-ro 0       1
	 # swap was on /dev/sdb5 during installation

The `rm` command removed only the `opt` node we specified, and the saved file has only this option removed.  The rest of the file and even this line was left untouched, preserving the original formatting and layout.


## Preserving existing files 

\index{augtool!options!--backup}
\index{augtool!options!--new}
\index{Metadata!save}

Augeas offers two options to preserve the existing files when saving the tree. In `augtool`, these options can be triggered with the following flags:

* --backup will save the original file with the extension .augsave and write the new file under the original file name ;
* --new will save the modified file with a .augnew extension and leave the original file untouched.

These options actually modify the value of the `/augeas/save` node in the Augeas tree. See chapter __FIXME__ for more information.


