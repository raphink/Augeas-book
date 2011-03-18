# Stock Modules Reference 

Augeas comes with an extensive collection of lenses to parse common configuration files. This chapter will cover the most common of these lenses and provide a reference and examples for them.

This list is not complete. The complete documentation of the modules can be obtained by building it from the Augeas source (see chapter 1).


## The Access Module 
Description of the module

## The Aliases Module 
Description of the module

## The Approx Module 
Description of the module

## The AptPreferences Module 
Description of the module

## The Aptsources Module 
Description of the module

## The Cron Module 
Description of the module

## The Crypttab Module 
Description of the module

## The Dhclient Module 
Description of the module

## The Dhcpd Module 
Description of the module

## The Dnsmasq Module 
Description of the module

## The Ethers Module 
Description of the module

## The Exports Module 
Description of the module

## The Fstab Module 

The `Fstab` modules parses `/etc/fstab` and `/etc/mtab`.

### Anatomy

The root nodes are either `#comment` nodes or `seq` nodes.

Each of the `seq` nodes correspond to a line in the file, and has the following nodes:

* A `spec` node, the block special device or remote filesystem to be mounted ;
* A `file` node, the mount point for the file system ;
* A `vfstype` node, the type of filesystem ;
* One or more `opt` nodes, the mount options associated with the filesystem ;
* An optional `dump` node, the parameter for the `dump(8)` command ;
* An optional `passno` node, the parameter for the `fsck(8)` command.

See `man fstab` for more information on these fields.


### Sample tree


	/files/etc/fstab
	/files/etc/fstab/#comment[1] = "/etc/fstab: static file system information."
	/files/etc/fstab/#comment[2] = "Use 'blkid -o value -s UUID' to print the universally unique identifier"
	/files/etc/fstab/#comment[3] = "for a device; this may be used with UUID= as a more robust way to name"
	/files/etc/fstab/#comment[4] = "devices that works even if disks are added and removed. See fstab(5)."
	/files/etc/fstab/#comment[5] = "<file system> <mount point>   <type>  <options>       <dump>  <pass>"
	/files/etc/fstab/1
	/files/etc/fstab/1/spec = "proc"
	/files/etc/fstab/1/file = "/proc"
	/files/etc/fstab/1/vfstype = "proc"
	/files/etc/fstab/1/opt[1] = "nodev"
	/files/etc/fstab/1/opt[2] = "noexec"
	/files/etc/fstab/1/opt[3] = "nosuid"
	/files/etc/fstab/1/dump = "0"
	/files/etc/fstab/1/passno = "0"
	/files/etc/fstab/#comment[6] = "/ was on /dev/sda1 during installation"
	/files/etc/fstab/2
	/files/etc/fstab/2/spec = "UUID=4cbb4f80-45f9-4e46-a076-8ec1124f4835"
	/files/etc/fstab/2/file = "/"
	/files/etc/fstab/2/vfstype = "ext3"
	/files/etc/fstab/2/opt = "errors"
	/files/etc/fstab/2/opt/value = "remount-ro"
	/files/etc/fstab/2/dump = "0"
	/files/etc/fstab/2/passno = "1"
	/files/etc/fstab/3
	/files/etc/fstab/3/spec = "/dev/sda2"
	/files/etc/fstab/3/file = "none"
	/files/etc/fstab/3/vfstype = "swap"
	/files/etc/fstab/3/opt = "rw"
	/files/etc/fstab/3/dump = "0"
	/files/etc/fstab/3/passno = "0"


### Examples of path expressions

	match '/files/etc/fstab/*[label() != "#comment"]'

matches all lines except comment lines.

	match '/files/etc/fstab/*[file = "/"]/spec'

matches the `spec` node for the filesystem mounted on "/".

	rm '/files/etc/fstab/*/opt[. = "nosuid"]'

removes all `opt` nodes whose value is `nosuid`.


## The Group Module 
Description of the module

## The Grub Module 
Description of the module

## The Hosts Module 
Description of the module

## The Httpd Module 
Description of the module

## The Inetd Module 
Description of the module

## The Inittab Module 
Description of the module

## The Interfaces Module 
Description of the module

## The Iptables Module 
Description of the module

## The Json Module 
Description of the module

## The Limits Module 
Description of the module

## The Login_defs Module 
Description of the module

## The Logrotate Module 
Description of the module

## The Modprobe Module 
Description of the module

## The Modules_conf Module 
Description of the module

## The MySQL Module 
Description of the module

## The Nsswitch Module 
Description of the module

## The Ntp Module 
Description of the module

## The Pam Module 
Description of the module

## The Passwd Module 
Description of the module

## The Pg_Hba Module 
Description of the module

## The PHP Module 
Description of the module

## The Postfix_Master Module 
Description of the module

## The Puppet Module 
Description of the module

## The Resolv Module 
Description of the module

## The Services Module 
Description of the module

## The Shells Module 
Description of the module

## The Sshd Module 
Description of the module

## The Sudoers Module 
Description of the module

## The Sysconfig Module 
Description of the module

## The Sysctl Module 
Description of the module

## The Syslog Module 
Description of the module

## The Xinetd Module 
Description of the module

## The Xml Module 
Description of the module

## The Yum Module 
Description of the module

