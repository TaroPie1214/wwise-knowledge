# GetResourceHandle

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [ak\_wwise\_plugin\_gui\_windows\_v1](structak__wwise__plugin__gui__windows__v1.html)

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ak\_wwise\_plugin\_gui\_windows\_v1](structak__wwise__plugin__gui__windows__v1_a20cada8d06bc0ef19afa66f617f30032.html#a20cada8d06bc0ef19afa66f617f30032) | | [GetDialog](structak__wwise__plugin__gui__windows__v1_a3eb842cb63ed86b621bcea6ed692bd1c.html#a3eb842cb63ed86b621bcea6ed692bd1c) | | [GetResourceHandle](structak__wwise__plugin__gui__windows__v1_a5b036698bfb04694254fe7a1a61ebd79.html#a5b036698bfb04694254fe7a1a61ebd79) | | [Help](structak__wwise__plugin__gui__windows__v1_a1cd16b3f42ff0faf531a190b649da0cf.html#a1cd16b3f42ff0faf531a190b649da0cf) | | [Instance](structak__wwise__plugin__gui__windows__v1_a09c7632c820f2c3e31d583b814463279.html#a09c7632c820f2c3e31d583b814463279) | | [WindowProc](structak__wwise__plugin__gui__windows__v1_a61a4925c4d1df3c0cb1d05b35b5bbc46.html#a61a4925c4d1df3c0cb1d05b35b5bbc46) | | [◆](#a5b036698bfb04694254fe7a1a61ebd79)GetResourceHandle |  | | --- | | HINSTANCE(\* ak\_wwise\_plugin\_gui\_windows\_v1::GetResourceHandle) (const struct [ak\_wwise\_plugin\_gui\_windows\_instance\_v1](structak__wwise__plugin__gui__windows__instance__v1.html) \*in\_this) |  Retrieves the plug-in's HINSTANCE used for loading resources.  参数  |  |  |  | | --- | --- | --- | | [in] | in\_this | Current instance of this interface. |  返回  A handle to the instance of the plug-in DLL  参见  - [获取对话框](plugin_frontend_windows.html#wwiseplugin_dialogcode)  在文件 [GUIWindows.h](_g_u_i_windows_8h_source.html) 第 [114](_g_u_i_windows_8h_source.html#l00114) 行定义.  被这些函数引用 [AK.Wwise::Plugin::V1::GUIWindows::Interface::Interface()](_g_u_i_windows_8h_source.html#l00229). |