# 实现 Windows 前端

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

实现 Windows 前端

此页面将详细介绍 Windows 图形用户界面 (GUI) 实现的各种元素。

|  |  |
| --- | --- |
|  | **备注:** 在 macOS 上，可通过基于开源工程 Wine 的 Crossover 桥接层运行 Wwise 设计工具。 通过为 Windows 创建 GUI 实现，可利用该解决方案在 macOS 上运行这一实现。 |

基类 `AK::Wwise::Plugin::GUIWindows` 可提供相应的实现方法，以便 Wwise 将特定类型的对话框实例化，并将控件与插件的属性绑定。同时还可提供标准 Win32 窗口程序 (WindowProc)，来允许插件对基于插件视图实例的 Windows 事件作出响应。

Wwise 设计工具采用以下方式将插件 GUI 实例化：

- Wwise 通过调用 `AK::Wwise::Plugin::GUIWindows::GetDialog()` ，请求插件将某种类型的对话框实例化（参见 [获取对话框](plugin_frontend_windows.html#wwiseplugin_dialogcode) 章节）。
- 若插件的前端支持对话框类型，则插件返回与类型对应的资源对话框 ID 及可选的属性绑定列表，来将控件 ID 和属性集中的属性键之间的对应关系（由插件 XML 定义，详见 [Wwise 插件 XML 描述文件](plugin_xml.html) 章节）告知 Wwise。
- Wwise 使用插件所提供的资源句柄将对话框实例化（参见 [资源句柄](plugin_frontend_windows.html#wwise_plugin_frontend_windows_resource) 章节）。
- Windows 通过事件（如 WM\_INITDIALOG）调用 WindowProc。

以下章节阐述了如何实现各种方法。

# 使用 MFC

在 Windows 上，通过 [Microsoft](namespace_microsoft.html) Foundation Classes (MFC) 构建 Wwise Authoring GUI。 若选择将 MFC 用于插件，则需初始化相应的库。 该库通过服务 `AK::Wwise::Plugin::PluginMFCWindows` 提供。务必将它作为第一个基类以确保最先对其进行初始化。

class FrontendSourcePluginMFC

: public [AK::Wwise::Plugin::PluginMFCWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html)<>

, public [AK::Wwise::Plugin::GUIWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.html)

{};

|  |  |
| --- | --- |
|  | **备注:** **不要**在插件的后端部分从此基类获取其他类，因为其应当不需要 MFC 或其他任何与 GUI 相关的库。 |

# 资源句柄

资源句柄的类型为 HINSTANCE，其与保存 `.rc` 文件所编译资源数据的动态库对应。它可以使用 [Microsoft](namespace_microsoft.html) Visual Studio 创建，并保存自定义对话框及其内容。 如需进一步了解资源文件，请参阅 the [Microsoft 文档](https://docs.microsoft.com/en-us/cpp/windows/how-to-create-a-resource-script-file)中有关如何创建资源文件的章节。

默认实现通过 MSVC 链接器所注入的 builtin 提供模块实例。

// GUIWindows.h

// Acquire the module instance from the Microsoft linker

extern "C" IMAGE\_DOS\_HEADER [\_\_ImageBase](_g_u_i_windows_8h_a983773bd0fac8b545d479971ff56db4d.html#a983773bd0fac8b545d479971ff56db4d);

virtual HINSTANCE GetResourceHandle() const

{

return (HINSTANCE)&[\_\_ImageBase](_g_u_i_windows_8h_a983773bd0fac8b545d479971ff56db4d.html#a983773bd0fac8b545d479971ff56db4d);

}

除非其他模块拥有对话框资源，否则不需要实现此函数。

若要创建资源文件 (`.rc`)，请参阅 [Creating Resource Files for Your Plug-in](effectplugin_tools_resource_file.html) 章节。

# 获取对话框

Wwise 目前在 `AK::Wwise::Plugin::eDialog` 中定义有两种对话框类型：

- `SettingsDialog`：Source Editor 或 Effect Editor 所用的主插件对话框
- `ContentsEditorDialog`：源插件所用的小对话框（仅 Contents Editor 中）

随后会使用给定的 [资源句柄](plugin_frontend_windows.html#wwise_plugin_frontend_windows_resource) 将返给 Wwise 的对话框实例化。 若要将属性与对话框的控件绑定，可使用列表将控件 ID 映射至插件 XML 定义中的属性名称。该列表使用以下宏创建：

constexpr auto propertyKey = u8"MyProperty";

[AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_BEGIN\_POPULATE\_TABLE](_g_u_i_windows_8h_ace7e697c1d8a310c9794cf05ce8ce1d8.html#ace7e697c1d8a310c9794cf05ce8ce1d8)(PropertyTable)

[AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_POP\_ITEM](_g_u_i_windows_8h_af6140142c9fe6ff132aee5ad0fde1caf.html#af6140142c9fe6ff132aee5ad0fde1caf)(IDC\_MYPROPERTY\_EDIT, propertyKey)

[AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_END\_POPULATE\_TABLE](_g_u_i_windows_8h_a286a575e82a4a1b002ff737b186d4c76.html#a286a575e82a4a1b002ff737b186d4c76)()

在本例中，列表将控件 `IDC_MYPROPERTY_EDIT`（来自与 .rc 文件配套的 resource.h 文件）映射到了属性 `MyProperty`。该 ID 必须与插件 XML 定义中的属性对应。

藉此，可将变量 `PropertyTable` 实例化，进而在 GetDialog() 时转发给 Wwise 设计工具：

bool FrontendSourcePlugin::GetDialog(

[AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog,

UINT& out\_uiDialogID,

[AK::Wwise::Plugin::PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html)\*& out\_pTable) const

{

switch (in\_eDialog)

{

case [SettingsDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da70f74e61c5e7bef5d95559c73c9978cc):

out\_uiDialogID = IDD\_SOURCEPLUGIN\_SETTINGS;

out\_pTable = ToneGenProp;

return true;

case [ContentsEditorDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da6d085e723d1240d119005b403573dfb5):

out\_uiDialogID = IDD\_SOURCEPLUGIN\_CONTENTS;

out\_pTable = nullptr;

return true;

}

return false;

}

若在此函数中返回 false，则将默认对话框而非自定义对话框实例化。

如需详细了解插件中都可使用哪些控件以及如何将其与属性绑定， 请参阅 [Wwise 插件对话框参考文档](wwiseplugin_dialog_guide.html) 章节。

# 通过 WindowProc 处理 Windows 事件

您可以通过解析 `AK::Wwise::Plugin::GUIWindows::WindowProc()` 函数中接收的窗口消息，来针对 UI 更改执行特定的操作（比如启用或禁用控件）。

// 在实现 UI 行为时，标准窗口函数可以让用户拦截任何感兴趣的消息。

bool FrontendSourcePlugin::WindowProc(

[AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog,

HWND in\_hWnd,

UINT in\_message,

WPARAM in\_wParam,

LPARAM in\_lParam,

LRESULT& out\_lResult)

{

if ( in\_message == WM\_INITDIALOG )

{

// Perform anything you need to do on dialog window initialization ...

}

// 例如，捕获窗口命令动作（仅针对主要对话框）来启用/禁用控件

else if ( in\_eDialog == [SettingsDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da70f74e61c5e7bef5d95559c73c9978cc) && in\_message == WM\_COMMAND )

{

// 通知代码

switch ( HIWORD( in\_wParam ) )

{

case BN\_CLICKED:

// 检查哪个按钮被点击

switch ( LOWORD( in\_wParam ) )

{

case IDC\_CHECK\_SWEEPFREQ:

// 验证是否启用了复选框

if ( IsDlgButtonChecked( in\_hWnd, IDC\_CHECK\_SWEEPFREQ ) == BST\_CHECKED )

{

// 启用某些控件...

}

else if ( IsDlgButtonChecked( in\_hWnd, IDC\_CHECK\_SWEEPFREQ ) == BST\_UNCHECKED )

{

// 禁用某些控件...

}

break;

}

} // End switch hi word (notification code)

} // 结束命令窗口事件

// Return false to let the parent window deal with the message.

// Return true for messages you don't want the parent window to handle.

return false;

}

# 显示插件的帮助

在 Wwise 用户单击插件对话框标题栏中的 ? 图标时，将在插件的前端调用 `AK::Wwise::Plugin::GUIWindows::Help()` 。您可以使用包括 HTMLHelp、WinHelp 或第三方帮助浏览器等各种工具来提供帮助。此函数用于接收窗口句柄，此句柄可以用作您要显示的任何窗口的父类。 `AK::Wwise::Plugin::eDialog` 参数可以让您选择具体的帮助主题，来匹配 音频设计师当前打开的对话框。如果您已处理帮助请求，此函数则必须返回 `true，否则返回` `false，在后一种情况下，Wwise` 将显示与 Plug-in Manager 相关的帮助主题。

|  |  |
| --- | --- |
|  | **备注:** 如前所述，源插件具有两个对话框。 如果源插件两个对话框的帮助主题不同，则应使用 `AK::Wwise::Plugin::eDialog` 参数。 |

以下示例展示了使用 HTML 帮助的源插件，其中由 MFC 提供文件的路径：

// Implement online help when the user clicks on the "?" icon

bool FrontendSourcePluginMFC::Help(HWND in\_hWnd, [AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog) const

{

AFX\_MANAGE\_STATE( ::AfxGetStaticModuleState() );

DWORD dwTopic = ONLINEHELP::Tone\_Generator\_Settings;

if ( in\_eDialog == [AK::Wwise::Plugin::ContentsEditorDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da6d085e723d1240d119005b403573dfb5) )

dwTopic = ONLINEHELP::Tone\_Generator\_ContentsEditor;

::HtmlHelp(

NULL, // <<< Must be NULL to launch on the correct parent window

AfxGetApp()->m\_pszHelpFilePath,

HH\_HELP\_CONTEXT,

dwTopic

);

return true;

}

|  |  |
| --- | --- |
|  | **注意:** `AK::Wwise::Plugin::GUIWindows::Help()` 方法不应调用 AfxGetApp()->HtmlHelp()。 它将从错误的父窗口中启动帮助窗口，导致悬浮窗口行为异常。 应使用带 Null 窗口语柄的 `HtmlHelp()` ，如上文示例中所示。 |

[AK.Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d)

eDialog

**Definition:** [PluginDef.h:138](_plugin_def_8h_source.html#l00137)

[AK.Wwise::Plugin::ContentsEditorDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da6d085e723d1240d119005b403573dfb5)

@ ContentsEditorDialog

**Definition:** [PluginDef.h:142](_plugin_def_8h_source.html#l00144)

[AK.Wwise::Plugin::SettingsDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da70f74e61c5e7bef5d95559c73c9978cc)

@ SettingsDialog

**Definition:** [PluginDef.h:139](_plugin_def_8h_source.html#l00141)

[AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_END\_POPULATE\_TABLE](_g_u_i_windows_8h_a286a575e82a4a1b002ff737b186d4c76.html#a286a575e82a4a1b002ff737b186d4c76)

#define AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_END\_POPULATE\_TABLE()

Ends the declaration of a property-control bindings table.

**Definition:** [GUIWindows.h:78](_g_u_i_windows_8h_source.html#l00078)

[AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_POP\_ITEM](_g_u_i_windows_8h_af6140142c9fe6ff132aee5ad0fde1caf.html#af6140142c9fe6ff132aee5ad0fde1caf)

#define AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_POP\_ITEM(theID, theProp)

Declares an association between a control and a property within a property-control bindings table.

**Definition:** [GUIWindows.h:68](_g_u_i_windows_8h_source.html#l00068)

[AK.Wwise::Plugin::PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html)

**Definition:** [PluginDef.h:127](_plugin_def_8h_source.html#l00126)

[AK.Wwise::Plugin::V1::GUIWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.html)

Windows frontend plug-in API for Audio plug-ins.

**Definition:** [GUIWindows.h:200](_g_u_i_windows_8h_source.html#l00199)

[AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_BEGIN\_POPULATE\_TABLE](_g_u_i_windows_8h_ace7e697c1d8a310c9794cf05ce8ce1d8.html#ace7e697c1d8a310c9794cf05ce8ce1d8)

#define AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_BEGIN\_POPULATE\_TABLE(theName)

Starts a new property-control bindings table.

**Definition:** [GUIWindows.h:54](_g_u_i_windows_8h_source.html#l00054)

[\_\_ImageBase](_g_u_i_windows_8h_a983773bd0fac8b545d479971ff56db4d.html#a983773bd0fac8b545d479971ff56db4d)

IMAGE\_DOS\_HEADER \_\_ImageBase

**Definition:** [GUIWindows.h:39](_g_u_i_windows_8h_source.html#l00039)

[AK.Wwise::Plugin::PluginMFCWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html)

Initializes MFC for this plug-in.

**Definition:** [PluginMFCWindows.h:69](_plugin_m_f_c_windows_8h_source.html#l00068)