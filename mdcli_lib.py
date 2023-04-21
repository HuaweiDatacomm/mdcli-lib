"""
mdcli lib for developers
@author: hwx1045592
@time: 2023-4-20
"""
from netmiko import ConnectHandler
from config import huawei, mdcli


class MdcliLib():
    """
    some utilities of mdcli operations
    """
    def __init__(self):
        # init connect
        self.net_connect = ConnectHandler(**huawei)
        # step in mdcli mode
        self.authenticate()

    def authenticate(self):
        command = 'switch md-cli'
        output = self.net_connect.send_command_timing(command)
        if "Username" in output:
            # print("Starting type username...")
            mdcliuser = mdcli['mdcliusername']
            output += self.net_connect.send_command_timing(f"{mdcliuser}\n")
        if "Password:" in output:
            # print("Starting type Password...")
            mdclipassword = mdcli['mdclipassword']
            output += self.net_connect.send_command_timing(f"{mdclipassword}\n")

    def display(self, command):
        res = ''
        if isinstance(command, list):
            for c in command:
                res += self.net_connect.send_command(c)
        else:
            res += self.net_connect.send_command(command)
        return res

    def curd(self, command):
        res = ''
        if isinstance(command, list):
            for c in command:
                res += self.net_connect.send_command(c)
        else:
            res += self.net_connect.send_command(command)
        return res

    def __del__(self):
        self.net_connect.disconnect()
