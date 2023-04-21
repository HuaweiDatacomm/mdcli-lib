#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
功能：mdcli lib接口，
修改记录：2023-3-23 hwx1045592 创建
"""
import time

from netmiko import ConnectHandler
from config import huawei

if __name__ == "__main__":

    huawei1 = {
        "device_type": "huawei",
        "host": "10.137.104.30",
        "username": "dublin123",
        "password": 'Dublin@123',
    }

    command = "dir"
    net_connect = ConnectHandler(**huawei1)
    # with ConnectHandler(**huawei1) as net_connect:
    #     output = net_connect.send_command_timing(command,  strip_prompt=True, strip_command=True)
    #     print(output, bytes(output, 'utf8'), net_connect.find_prompt())
    #     # print(net_connect.find_prompt())
    # exit()
    output = net_connect.send_command(command)
    net_connect.write_channel('\t')
    time.sleep(1)
    o1 = net_connect.read_channel()
    # print(net_connect.find_prompt(), 8, output)

    output += net_connect.send_command('system-view\n', delay_factor=4,)
    print(output, bytes(output, 'utf8'), net_connect.find_prompt(), 444, o1)

    output += net_connect.send_command('system-view\n', delay_factor=4,)
    output += net_connect.send_command('tree ifm/interfaces/interface', delay_factor=4, use_textfsm=True)
    if "Username" in output:
        print("Starting type username...")
        output += net_connect.send_command("mdcliuser\n", delay_factor=2, expect_string=r"Password")

    if "Password" in output:
        print("Starting type Password...")
        output += net_connect.send_command("Root@1234\n", delay_factor=4, expect_string=r"mdcliuser")

    output += net_connect.send_command('system-view\n', delay_factor=4,)
    output += net_connect.send_command('tree ifm/interfaces/interface', delay_factor=4, use_textfsm=True)

