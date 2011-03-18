# Using the C API and Bindings 

\index{API|(}
\index{API!calls|see{Calls}}

So far, our examples have been done using `augtool`, the CLI interface to Augeas. However, Augeas is first and foremost a C library.


## Using the C API 

\index{API!C API}


## API Flags

\index{Flags}
\index{API!flags|see{Flags}}


## Using Bindings 

\index{API!bindings|(}


### Haskell bindings

\index{API!bindings!Haskell}


### Java bindings

\index{API!bindings!Java}


### Perl Bindings 

\index{API!bindings!Perl}


### PHP bindings

\index{API!bindings!PHP}


### Python Bindings 

\index{API!bindings!Python}

#### Installation




#### Initialization

Synopsis:

	def __init__(self, root=None, loadpath=None, flags=NONE)

Initialize the library.

Use `root` as the filesystem root. If `root` is None, use the value of
the environment variable AUGEAS_ROOT. If that doesn't exist either,
use `/`.

`loadpath` is a colon-spearated list of directories that modules
should be searched in. This is in addition to the standard load path
and the directories in `AUGEAS_LENS_LIB`.

`flags` is a bitmask made up of values from `AUG_FLAGS`.

Example:

	import augeas
	a = augeas.Augeas(root="fakeroot")


#### The get method

Synopsis:

	def get(self, path)

Lookup the value associated with `path`.
Returns the value at the path specified.
It is an error if more than one node matches `path`.


Example:

	val = a.get("/files/etc/ftab/1/canonical")


### Ruby Bindings 

\index{API!bindings!Ruby}


\index{API!bindings|)}



\index{API|)}

