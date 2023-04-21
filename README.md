# **mdcli-lib**

## **Overview**
Some library interfaces about huawei mdcli operations for Python Developers.

## **Prerequisites**
- Python: 3.7+
- Module: netmiko ( by `pip install netmiko`)

## **Examples**
More examples in dir `examples`.

## **How to use**
You only need two files `config.py` and `mdcli_lib.py`.

## Get Started

```python
from mdcli_lib import MdcliLib

mdcli = MdcliLib()

# Show command that we execute
command = "system-view"
command2 = "tree ifm/interfaces/interface"
output = mdcli.display([command, command2])
```


   
