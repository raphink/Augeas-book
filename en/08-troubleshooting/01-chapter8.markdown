# Troubleshooting Augeas #

The Augeas tree is built using bidirectional grammars called lenses (see chapter 3). The configuration files will not appear in the Augeas tree if the lens responsible for parsing them fails to do so.

In the other direction (the put direction, see chapter 3), lenses may fail to save a tree back to a configuration file if that tree doesn't fit in the given lens.


## Files don't appear in the tree ##

## Save failed ##


