# JavaScript, Node.js - HTTP POST

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

JavaScript, Node.js - HTTP POST

- [初始化工程](http_post_js.html#httpPost_js_init)
- [工程代码](http_post_js.html#httpPost_js_code)
- [运行工程](http_post_js.html#httpPost_js_run)

该例子与 WAMP 的例子执行的是相同功能，但使用的是 HTTP POST。

# 初始化工程

|  |  |
| --- | --- |
|  | **备注:** 此示例要求安装最新的 Node.js LTS。 |

从示例文件夹 `<Wwise 安装路径>/SDK/samples/WwiseAuthoringAPI/js/hello-wwise-node-http` 运行以下命令来安装依赖。

npm install

# 工程代码

在示例目录 **hello-wwise-node-wamp** 中的示例文件 index.js 使用 HTTP POST 对 Wwise Authoring API 进行 RPC 调用。

// Copyright Audiokinetic Inc.

(() => {

const axios = require('axios');

const ak = require('../../../../include/AK/WwiseAuthoringAPI/js/waapi.js').ak;

const data = {

uri: ak.wwise.core.getInfo,

options: {},

args: {}

};

const handleResponse = (status, headers, objectPayload) => {

if (status != 200) {

if (headers["content-type"] == "application/json") {

console.log(`Error: ${objectPayload.uri}: ${JSON.stringify(objectPayload)}`);

} else {

console.log(`Error: ${Buffer.from(objectPayload).toString("utf8")}`);

}

} else {

console.log(`Hello ${objectPayload.displayName} ${objectPayload.version.displayName}`);

}

};

axios({

method: "post",

url: "http://127.0.0.1:8090/waapi",

data: data,

headers: { "content-type": "application/json" }

}).then((response) => {

handleResponse(response.status, response.headers, response.data);

}).catch((err) => {

if (err.response) {

handleResponse(err.response.status, err.response.headers, err.response.data);

} else {

console.log(`Error: ${err.message}`);

}

});

})();

|  |  |
| --- | --- |
|  | **备注:** 命令行 `var ak = require('../../../../include/AK/WwiseAuthoringAPI/js/waapi.js').ak` 会导入 API 路径声明。  它位于 `<Wwise 安装路径>/SDK/include/AK/WwiseAuthoringAPI/js`。  在本示例中，该文件的路径是相对于示例位置的相对路径。 |

# 运行工程

运行以下命令：

node index.js

如果 Wwise Authoring API 成功地连接到 Wwise，您会看到以下输出结果：

Hello Wwise 20??.?.?