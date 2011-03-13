# Troubleshooting Augeas #

The Augeas tree is built using bidirectional grammars called lenses (see chapter 3). The configuration files will not appear in the Augeas tree if the lens responsible for parsing them fails to do so.

In the other direction (the put direction, see chapter 3), lenses may fail to save a tree back to a configuration file if that tree doesn't fit in the given lens.

Whatever you are trying to troubleshoot, you will most likely benefit from the metadata exposed in the "/augeas" node at the top of the Augeas tree.

A simple way to list all known errors in an augtool session is to type:

	> print /augeas//error

The double slash tells Augeas to search for all subnodes under /augeas whose label matches "error". The print command will return all subnodes of the matching nodes, given you the details of the errors.

If you want to see the error on a specific file, you can use the path to that file in the expression. For example, to see the error on /etc/fstab, you can use:

	> print /augeas/files/etc/fstab//error


## Files don't appear in the tree ##

There can be several reasons for a file to not appear in the Augeas tree:

* There is no existing lens for this file, or the lens you expect to parse this file has no filter for this file at this location. See chapter 7 for more information on writing lenses.
* The Unix uid you are using has no right to see the file. The "error" node in the "/augeas" tree will tell you so (__show an example__).
* The lens fails to parse part of the file, or the whole file.

Parsing errors are quite common, and there can be many reasons for them:

* The file uses \r for newlines. Most lenses, having been made for Unix systems, only recognize \n as valid newlines. Getting the file through dos2unix and trying again can confirm this possibility.
* The lens fails to parse a part of the file, for example it doesn't cover a specific case that is valid for this configuration file.
* The lens fails to parse the entire file.

In the last two cases, it is important to check that the configuration is indeed valid. When available, use a command line tool provided with the application owning the configuration file, such as apachectl or visudo:

	$ apachectl configtest
	$ visudo -c

Note that when the application owning the configuration file is happy with the file and Augeas is not, it is always safer to consider that Augeas is wrong and that the lens has to be modified, since other users are likely to be in the same case.


## Save failed ##

Just as files can fail to be parsed by Augeas, trees can fail to be transformed back into files, too. This prevents Augeas from saving a tree that wouldn't make sense to the configuration file, thus preventing from breaking configuration files.



