# Python (Waapi-Client) – 订阅

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Python (Waapi-Client) – 订阅

- [初始化工程](waapi_client_python_subscription.html#waapi_client_python_subscription_init)
- [工程代码](waapi_client_python_subscription.html#waapi_client_python_subscription_code)
- [运行工程](waapi_client_python_subscription.html#waapi_client_python_subscription_run)

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

client = WaapiClient()

# NOTE: the client must be manually disconnected when instantiated in the global scope

except CannotConnectToWaapiException:

print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

else:

# Callback function with a matching signature.

# Signature (\*args, \*\*kwargs) matches anything, with results being in kwargs.

def on\_name\_changed(\*args, \*\*kwargs):

obj\_type = kwargs.get("object", {}).get("type")

old\_name = kwargs.get("oldName")

new\_name = kwargs.get("newName")

print("Object '{}' (of type '{}') was renamed to '{}'\n".format(old\_name, obj\_type, new\_name))

client.disconnect()

handler = client.subscribe("ak.wwise.core.object.nameChanged", on\_name\_changed, {"return": ["type"]})

print("Subscribed 'ak.wwise.core.object.nameChanged', rename an object in Wwise")

# 运行工程

在 Wwise 中打开工程后，使用以下命令在终端上运行脚本：

# Windows

py subscribe.py

# macOS, Linux

python3 subscribe.py

此时，应会显示如下输出：

Getting Wwise instance information:

Subscribed 'ak.wwise.core.object.nameChanged', rename an object in Wwise

接着，在 Wwise 中重命名对象。此时，应会显示如下输出：

Object 'MySound' (of type 'Sound') was renamed to 'MyOtherSound'