#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
display yang structure by command tree
"""
from mdcli_lib import MdcliLib


mdcli = MdcliLib()

# Show command that we execute
command = "system-view"
command2 = "tree ifm/interfaces/interface"
output = mdcli.display([command, command2])

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()
