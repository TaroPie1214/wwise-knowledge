# 浏览器中的 JavaScript - WAMP

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

浏览器中的 JavaScript - WAMP

- [初始化工程](wamp_js_browser.html#wamp_js_browser_init)
- [工程代码](wamp_js_browser.html#wamp_js_browser_code)
- [运行工程](wamp_js_browser.html#wamp_js_browser_run)

# 初始化工程

|  |  |
| --- | --- |
|  | **备注:** 此示例要求随最新的 Node.js LTS 一并安装 npm 并通过 Git 安装 Bower 包。支持的浏览器有 Google Chrome、Mozilla Firefox 和 Opera。 |

从示例文件夹 `<Wwise 安装路径>/SDK/samples/WwiseAuthoringAPI/js/hello-wwise-web-wamp` 中运行以下代码来安装依赖。

npm install -g bower

bower install autobahn

# 工程代码

在示例目录 `hello-wwise-web-wamp` 中的示例文件 index.js 用于连接到 Wwise Authoring API。

var showMessage = function(message){

document.getElementById("message").innerHTML = message;

}

function onBodyLoad() {

// Create the WAMP connection

var connection = new autobahn.Connection({

url: 'ws://localhost:8080/waapi',

realm: 'realm1',

protocols: ['wamp.2.json']

});

// Setup handler for connection closed

connection.onclose = function (reason, details) {

showMessage('wamp connection closed');

return true;

};

// Setup handler for connection opened

connection.onopen = function (session) {

showMessage('wamp connection opened');

// Call getInfo

session.call(ak.wwise.core.getInfo, [], {}).then(

function (res) {

showMessage(`Hello ${res.kwargs.displayName} ${res.kwargs.version.displayName}`);

},

function (error) {

showMessage(`error: ${error}`);

}

);

};

// Open the connection

connection.open();

}

在示例目录 `hello-wwise-web-wamp` 中的示例文件 index.html 是一个简单的网页，它使用之前的脚本来连接到 Wwise Authoring API 并渲染输出信息。

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="utf-8">

<title>Hello Wwise</title>

<script src="node\_modules/autobahn-browser/autobahn.min.js"></script>

<script src="../../../../include/AK/WwiseAuthoringAPI/js/waapi.js"></script>

<script src="index.js"></script>

</head>

<body onload="onBodyLoad()">

<div id="message">

Not connected.

</div>

</body>

</html>

# 运行工程

双击 **index.html** 在 [初始化工程](wamp_js_browser.html#wamp_js_browser_init) “支持的”浏览器中打开。

如果 Wwise Authoring API 成功地连接到 Wwise，您会看到以下输出结果：

Hello Wwise 20??.?.?