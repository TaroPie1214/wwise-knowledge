# NotifyPluginMediaChanged

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [ak\_wwise\_plugin\_notifications\_object\_media\_v1](structak__wwise__plugin__notifications__object__media__v1.html)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ak\_wwise\_plugin\_notifications\_object\_media\_v1](structak__wwise__plugin__notifications__object__media__v1_a6fb00ffd47ea7f2f7ba14a1022cb0678.html#a6fb00ffd47ea7f2f7ba14a1022cb0678) | | [Instance](structak__wwise__plugin__notifications__object__media__v1_ab0fc4bef5cfb0af039208cd8798864db.html#ab0fc4bef5cfb0af039208cd8798864db) | | [NotifyPluginMediaChanged](structak__wwise__plugin__notifications__object__media__v1_a44f854ad97fca4a74adc41d3dae11f5f.html#a44f854ad97fca4a74adc41d3dae11f5f) | | [◆](#a44f854ad97fca4a74adc41d3dae11f5f)NotifyPluginMediaChanged |  | | --- | | void(\* ak\_wwise\_plugin\_notifications\_object\_media\_v1::NotifyPluginMediaChanged) (struct [ak\_wwise\_plugin\_notifications\_object\_media\_instance\_v1](structak__wwise__plugin__notifications__object__media__instance__v1.html) \*in\_this) |  This function is called by Wwise when any of the plug-in media changes.  It is called when plugin media is added, removed or changes. This function is also called during undo or redo operations.  参见  - [管理插件媒体](effectplugin_media.html#effectplugin_media_managing)  参数  |  |  |  | | --- | --- | --- | | [in] | in\_this | Current instance of this interface. |  在文件 [HostObjectMedia.h](_host_object_media_8h_source.html) 第 [271](_host_object_media_8h_source.html#l00271) 行定义.  被这些函数引用 [AK.Wwise::Plugin::V1::Notifications::ObjectMedia\_::Interface::Interface()](_host_object_media_8h_source.html#l00555). |