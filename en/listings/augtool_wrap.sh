#!/bin/bash
function do_augtool() {
   local command="$1"
   echo -e "$command" | augtool
}

do_augtool "set /files/etc/hosts/1/canonical alice\nsave"
