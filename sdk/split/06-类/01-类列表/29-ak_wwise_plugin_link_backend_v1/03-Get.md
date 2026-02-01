# Get

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [ak\_wwise\_plugin\_link\_backend\_v1](structak__wwise__plugin__link__backend__v1.html)

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ak\_wwise\_plugin\_link\_backend\_v1](structak__wwise__plugin__link__backend__v1_a96e42e8ac53f085771bb7a7f3f3eae5c.html#a96e42e8ac53f085771bb7a7f3f3eae5c) | | [Get](structak__wwise__plugin__link__backend__v1_ae3409b86755654f59f4161846eee5466.html#ae3409b86755654f59f4161846eee5466) | | [Instance](structak__wwise__plugin__link__backend__v1_a2712f50d873479cc047f2b5938fe290e.html#a2712f50d873479cc047f2b5938fe290e) | | [◆](#ae3409b86755654f59f4161846eee5466)Get |  | | --- | | [ak\_wwise\_plugin\_backend\_instance](structak__wwise__plugin__backend__instance.html)\*(\* ak\_wwise\_plugin\_link\_backend\_v1::Get) (const [ak\_wwise\_plugin\_link\_backend\_instance\_v1](structak__wwise__plugin__link__backend__instance__v1.html) \*in\_this) |  Retrieves a link to the plug-in's backend instance.   |  |  | | --- | --- | |  | **备注:** The returned pointer might be modified in the frontend lifetime. For example, a plug-in that would undo and redo a plug-in creation might return a different value. As such, you should not store the backend pointer in a class member, but query it at every operation. |   参数  |  |  |  | | --- | --- | --- | | [in] | in\_this | Current instance of this interface. |  返回  Base pointer of the backend instance.  在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [68](_plugin_links_8h_source.html#l00068) 行定义.  被这些函数引用 [AK.Wwise::Plugin::V1::LinkBackend::Get()](_plugin_links_8h_source.html#l00171). |