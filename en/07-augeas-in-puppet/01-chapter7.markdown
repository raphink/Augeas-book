# Using Augeas in Puppet

\index{Puppet}

Because Augeas is a configuration API, it fits right into tools that are made for configuration management. One of the most widely used of these tools in the open-source world is Puppet, and Augeas has been available as a native type in Puppet since version 0.24.7.

\index{API!bindings!Ruby}
Since Puppet is written in Ruby, the Augeas Puppet type makes use of the Ruby bindings for Augeas.


## The Augeas type

Puppet provides a native Augeas type since version 0.24.7.

\index{Commands!set}
The Augeas type in Puppet takes a list of commands labeled "changes". A simple example is the following:

	augeas { "hosts_alice":
	   changes => [
	      "set /files/etc/hosts/1/canonical alice",
	   ],
	}


The `changes` attribute is an array of Augeas commands, similar to what you would pass to `augtool`.

> ![**NOTE**][info] *It is recommended to use `augtool` to prepare and test the commands before you use them in Puppet.*

\index{Commands!save}
Each call to the Augeas type starts a new Augeas session. The `save` call is ran automatically at the end of each session.


## Setting a context



## Proper quoting

While quoting in `augtool` is strict, quoting in Puppet can be tricky.

**TODO**: explain this



## Puppet and idempotence


Idempotence is very important in configuration management tools such as Puppet. The Augeas type provides a `onlyif` statement to make it easy to ensure that Augeas is only called when necessary.


	augeas { "hosts_alice":
	   context => "/files/etc/hosts/1",
	   changes => [
	      "set canonical alice",
	   ],
	   onlyif => "match canonical[. = 'alice']" size == 0",
	}

> ![**NOTE**][info] *For proper idempotence, this statement has to be coupled with the methods described earlier^[See *ensuring idempotence* on page \pageref{sec:ensuring_idempotence}].*



