#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
move various of nodes,
"""
from mdcli_lib import MdcliLib

mdcli = MdcliLib()

# create container
command = "system-view"
command2 = "bfd"
command3 = "touch ifm/interfaces/interface[name=\"MEth0/0/0\"]/ipv6" # or
output = mdcli.curd([command, command2])

# create List
command = "system-view"
command2 = "interface name vlanif100"
command3 = "touch interface[name=\"vlanif100\"]" # or
output = mdcli.curd([command, command2])

# create Leaf
command = "system-view"
command2 = "admin-status up"
command3 = "description To-DeviceB-MEth0/0/0" # or
output = mdcli.curd([command, command2])

# create Leaf-List
command = "system-view"
# in view [*(ex)ADMIN@HUAWEI]/sec-policy/vsys[name="default"]/static-policy/rule[name="r1"]
command2 = "source-zone zone1 zone2"
command3 = "touch source-zone[.=\"zone3\"]" # or
output = mdcli.curd([command, command2])


# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()
