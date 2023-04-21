#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
display configuration data by command display
"""
from mdcli_lib import MdcliLib

mdcli = MdcliLib()

# Show command that we execute
# command = "system-view"
# command2 = "display ifm/interfaces | grep '\"name\":'"
# output = mdcli.display([command, command2])

# Note, check something must step in the corresponding view first
# eg. case below.
# Show command that we execute
command = "system-view"
command2 = "ifm interfaces interface name MEth0/0/0"
command3 = "display dynamic/ all"
output = mdcli.display([command, command2, command3])


# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()
