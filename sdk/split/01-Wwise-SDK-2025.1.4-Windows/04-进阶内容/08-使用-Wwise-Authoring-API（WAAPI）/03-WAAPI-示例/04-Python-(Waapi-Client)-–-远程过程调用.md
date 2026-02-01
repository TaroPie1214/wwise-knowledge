# Python (Waapi-Client) – 远程过程调用

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Python (Waapi-Client) – 远程过程调用

- [初始化工程](waapi_client_python_rpc.html#waapi_client_python_rpc_init)
- [工程代码](waapi_client_python_rpc.html#waapi_client_python_rpc_code)
- [运行工程](waapi_client_python_rpc.html#waapi_client_python_rpc_run)

# 初始化工程

|  |  |
| --- | --- |
|  | **备注:** The Python Waapi-Client is intended for use with a non-EOL Python 3.x version. |

从任意目录运行以下命令来安装依赖：

# Windows

py -3 -m pip install waapi-client

# macOS, Linux

python3 -m pip install waapi-client

# 工程代码

该文件包含以下代码，让您能连接到 Wwise Authoring API。

#!/usr/bin/env python3

from waapi import WaapiClient, CannotConnectToWaapiException

from pprint import pprint

try:

# Connecting to Waapi using default URL

with WaapiClient() as client:

# NOTE: client will automatically disconnect at the end of the scope

# == Simple RPC without argument

print("Getting Wwise instance information:")

result = client.call("ak.wwise.core.getInfo")

pprint(result)

# == RPC with arguments

print("Query the Default Work Unit information:")

object\_get\_args = {

"from": {

"path": ["\\Containers\\Default Work Unit"]

},

"options": {

"return": ["id", "name", "type"]

}

}

result = client.call("ak.wwise.core.object.get", object\_get\_args)

pprint(result)

except CannotConnectToWaapiException:

print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

# 运行工程

在 Wwise 中打开工程后，使用以下命令在终端上运行脚本：

# Windows

py rpc.py

# macOS, Linux

python3 rpc.py

此时，应会显示如下输出：

Getting Wwise instance information:

[Wwise Information Dictionary dump]

Query the Default Work Unit information:

{'return': [{'id': '{CDF62889-48AA-436C-B7DD-5B6B1DF5050D}',

'name': 'Default Work Unit',

'type': 'WorkUnit'}]}