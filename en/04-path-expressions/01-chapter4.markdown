# Path Expressions 

\index{Path expressions}
\index{Tree!\slash{}files|see{Path expressions}}

Augeas maps configuration files into a tree, and lets you access this tree using XPath expressions.
In this chapter, we will inspect the various XPath expressions offered by Augeas, and give examples of what you can achieve with them.


## Generalities on XPath expressions 


## Using globs 

When you write XPath expressions, you might want to match generic nodes or nodes at any level of the tree. There are two operators for that:

* `*` as a node name matches any node ;
* `//` matches on any sublevel of the tree.


## Conditionals 

Filtering on node names is often not enough to find what you want. You will often wish to find nodes defined by their value or subnodes. XPath offers a syntax of conditionals using square brackets.

__Give examples__


> ![**NOTE**][info]  *In contrast to most XML trees, the Augeas tree contains no attributes, but only nodes with values and children. For this reason, it doesn't use conditional syntaxes featuring the `@` prefix, which is common to many standard XPath queries.*

Conditionals can be combined in different ways. __Give examples__.


## Union of paths

You can use ` | ` to achieve the union of two paths:

	augtool> match '/files/etc/fstab | /files/etc/hosts'

will return the nodes matching `/files/etc/fstab` as well as the ones matching `/files/etc/hosts`.


## Functions 

\index{Path expressions!functions|(}


To enrich the filtering you can achieve with conditionals, Augeas provides a set of functions which can be used in conditional context.


### The last() function 

\index{Path expressions!functions!last()}

### The position() function

\index{Path expressions!functions!position()}

### The label() function 

\index{Path expressions!functions!label()}

### The count() function 

\index{Path expressions!functions!count()}

### The regexp() function

\index{Path expressions!functions!regexp()}


\index{Path expressions!functions|)}

## Node references 

In addition to functions, it is often necessary to refer to nodes relatively as you build complex XPath expressions. Augeas provides special node references for that.



## Using variables in paths 

\index{Path expressions!variables|(}

Augeas provides two ways to declare variables.


### defvar 

\index{Path expressions!variables!defvar}
\index{Commands!defvar}


### defnode 

\index{Path expressions!variables!defnode}
\index{Commands!defnode}



\index{Path expressions!variables|)}

### Using variables to express conditionals 


## Ensuring idempotence

\index{Path expressions!idempotence}

	augtool> set '/files/etc/php.ini/PHP/extension[. = "foo.so"]' foo.so


