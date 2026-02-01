# GetArray

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [ak\_wwise\_plugin\_link\_frontend\_v1](structak__wwise__plugin__link__frontend__v1.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ak\_wwise\_plugin\_link\_frontend\_v1](structak__wwise__plugin__link__frontend__v1_a762aef278af0fdaa1ac1f4e2be0fc4c9.html#a762aef278af0fdaa1ac1f4e2be0fc4c9) | | [GetArray](structak__wwise__plugin__link__frontend__v1_a54de59efdb83e3feeca57605baa5783f.html#a54de59efdb83e3feeca57605baa5783f) | | [Instance](structak__wwise__plugin__link__frontend__v1_ae5416fd3b28a4ef2810238b2c85267d7.html#ae5416fd3b28a4ef2810238b2c85267d7) | | [◆](#a54de59efdb83e3feeca57605baa5783f)GetArray |  | | --- | | [ak\_wwise\_plugin\_frontend\_instance](structak__wwise__plugin__frontend__instance.html)\*\*(\* ak\_wwise\_plugin\_link\_frontend\_v1::GetArray) (const [ak\_wwise\_plugin\_link\_frontend\_instance\_v1](structak__wwise__plugin__link__frontend__instance__v1.html) \*in\_this, int \*out\_count) |  Retrieves an array of the plug-in's frontend instances.   |  |  | | --- | --- | |  | **备注:** The returned array is a temporary TLS pointer that is meant to be retrieved and processed immediately to execute commands. You should not store this data. |   参数  |  |  |  | | --- | --- | --- | | [in] | in\_this | Current instance of this interface. | | [out] | out\_count | How many frontend instances are in the array. |  返回  Temporary pointer to the array of frontend instances.  在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [105](_plugin_links_8h_source.html#l00105) 行定义.  被这些函数引用 [AK.Wwise::Plugin::V1::LinkFrontend::GetArray()](_plugin_links_8h_source.html#l00230). |