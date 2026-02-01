# JavaScript, Node.js - WAMP

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

JavaScript, Node.js - WAMP

- [初始化工程](wamp_js_node.html#wamp_js_node_init)
- [工程代码](wamp_js_node.html#wamp_js_node_code)
- [运行工程](wamp_js_node.html#wamp_js_node_run)

# 初始化工程

|  |  |
| --- | --- |
|  | **备注:** 此示例要求安装最新的 Node.js LTS。 |

从示例文件夹 `<Wwise 安装路径>/SDK/samples/WwiseAuthoringAPI/js/hello-wwise-node-wamp` 中运行以下命令来安装依赖。

npm install

# 工程代码

在示例目录 `hello-wwise-node-wamp` 中的示例文件 index.js 用于连接到 Wwise Authoring API。

var ak = require('../../../../include/AK/WwiseAuthoringAPI/js/waapi.js').ak;

var autobahn = require('autobahn');

// Create the WAMP connection

var connection = new autobahn.Connection({

url: 'ws://127.0.0.1:8080/waapi',

realm: 'realm1',

protocols: ['wamp.2.json']

});

// Setup handler for connection opened

connection.onopen = function (session) {

// Call getInfo

session.call(ak.wwise.core.getInfo, [], {}).then(

function (res) {

console.log(`Hello ${res.kwargs.displayName} ${res.kwargs.version.displayName}!`);

},

function (error) {

console.log(`Error: ${error}`);

}

).then(

function() {

connection.close();

}

);

};

connection.onclose = function (reason, details) {

if (reason !== 'lost') {

console.log("Connection closed. Reason: " + reason);

}

process.exit();

};

// Open the connection

connection.open();

|  |  |
| --- | --- |
|  | **备注:** 命令行 `var ak = require('../../../../include/AK/WwiseAuthoringAPI/js/waapi.js').ak` 会导入 API 路径声明。  它位于 `<Wwise 安装路径>/SDK/include/AK/WwiseAuthoringAPI/js`。  在本示例中，该文件的路径是相对于示例位置的相对路径。 |

# 运行工程

在示例目录中运行以下命令：

node index.js

如果 Wwise Authoring API 成功地连接到 Wwise，您会看到以下输出结果：

Hello Wwise 20??.?.?