# Creating Resource Files for Your Plug-in

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Creating Resource Files for Your Plug-in

The Resource file (with an .rc extension) describes the resources the plug-in uses to create a custom graphical interface. An easy way to manage Resource files is to use the Visual Studio Editor tool, which you can use to drag widgets onto a canvas to build the GUI. This section explains how to create a Resource file for a new plug-in.

Before you proceed, ensure that you are familiar with the development tools. Refer to [使用开发工具](effectplugin_tools.html) for more information.

**To create a Resource file:**

1. Run the following command to create a plug-in. For the purposes of this procedure, select an "effect" type plug-in when prompted:

   python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" new
2. Run the following commands to change to the plug-in directory and then call `premake:`

   cd MyPlugin

   python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" premake Authoring
3. Open the generated solution file (for example, `MyPlugin_Authoring_Windows_vc160.sln`) in Visual Studio 2019.
4. In the Resource View, select the project name and in the menu bar, click **Project** > **Add New Item**. The Add New Item dialog opens.
5. In the left pane, select **Resource**, then in the center pane select **Resource File (.rc)** and click **Add**. A `Resource.rc` file is created and appears under the project name in the Resource View. The file is located in the plug-in's `WwisePlugin` subdirectory.
6. In the Resource View, right-click the `Resource.rc` file and click **Add Resource**. In the Add Resource dialog, select **Dialog** and click **New**. A dialog resource is created and appears in the editing pane.
7. Set the following values in the Properties pane:
   - Appearance/Border: **None**
   - Appearance/Clip Children: **True**
   - Appearance/Style: **Child**
   - Misc/Control: **True**
   - Misc/Control Parent: **True**
8. Drag any desired widgets from the Toolbox, located to the left of the editing pane, onto the dialog. When you are finished, click **Save**.
9. From a command prompt in your plug-in directory, run the following two commands in order:

   python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" premake Authoring

   python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" build -c Release -x x64 -t vc160 Authoring

    The first command includes the `Resource.rc` file in your project, and the second creates a `resource.h` file based on the Resource file.
10. In the plug-in's `Win32` subdirectory, open the `PluginNamePluginGUI.h` file and add the following code:

    #pragma?once

    #include?"../MyPlugin.h"

    #include?"../resource.h"

    class?MyPluginGUI?final

    ????:?public?AK::Wwise::Plugin::PluginMFCWindows<>

    ????,[?public?AK::Wwise::Plugin::GUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_a5d74c88aa83c4e608fb75d1ac5555c9b.html#a5d74c88aa83c4e608fb75d1ac5555c9b)

    {

    public:

    ????MyPluginGUI();

    ????HINSTANCE?GetResourceHandle()?const?override;

    ????bool?GetDialog(

    ????????AK::Wwise::Plugin::eDialog?in\_eDialog,

    ????????UINT&?out\_uiDialogID,

    ????????AK::Wwise::Plugin::PopulateTableItem\*&?out\_pTable

    ????)?const?override;

    ????bool?WindowProc(

    ????????AK::Wwise::Plugin::eDialog?in\_eDialog,

    ????????HWND?in\_hWnd,

    ????????uint32\_t?in\_message,

    ????????WPARAM?in\_wParam,

    ????????LPARAM?in\_lParam,

    ????????LRESULT&?out\_lResult

    ????)?override;

    private:

    ????HWND?m\_hwndPropView?=?nullptr;

    };

     This code overrides the methods provided by `AK::Wwise::Plugin::GUIWindows` and ensures that the plug-in uses the custom interface.
11. Add the following code to the `PluginNamePluginGUI.cpp` file:

    HINSTANCE MyPluginGUI::GetResourceHandle()?const

    {

    ????AFX\_MANAGE\_STATE(?AfxGetStaticModuleState()?);

    ????return?AfxGetStaticModuleState()->m\_hCurrentResourceHandle;

    }

    bool MyPluginGUI::GetDialog(?AK::Wwise::Plugin::eDialog?in\_eDialog,?UINT?&?out\_uiDialogID,?AK::Wwise::Plugin::PopulateTableItem?\*&?out\_pTable?)?const

    {

    ????AKASSERT(?in\_eDialog?==?AK::Wwise::Plugin::SettingsDialog?);

    ????out\_uiDialogID?=?IDD\_DIALOG1;

    ????out\_pTable?=?nullptr;

    ????return?true;

    }

    bool MyPluginGUI::WindowProc(?AK::Wwise::Plugin::eDialog?in\_eDialog,?HWND?in\_hWnd,?uint32\_t?in\_message,?WPARAM?in\_wParam,?LPARAM?in\_lParam,?LRESULT?&?out\_lResult?)

    {

    ????switch?(?in\_message?)

    ????{

    ????case?WM\_INITDIALOG:

    ????????m\_hwndPropView?=?in\_hWnd;

    ????????break;

    ????case?WM\_DESTROY:

    ????????m\_hwndPropView?=?NULL;

    ????????break;

    ????}

    ????out\_lResult?=?0;

    ????return?false;

    }
12. Save your changes and rebuild the plug-in. It is now available in Wwise as an Effect, which you can add to Wwise objects.

[AK.Wwise::Plugin::GUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_a5d74c88aa83c4e608fb75d1ac5555c9b.html#a5d74c88aa83c4e608fb75d1ac5555c9b)

V1::GUIWindows GUIWindows

Latest version of the C++ GUIWindows interface.

**Definition:** [GUIWindows.h:334](_g_u_i_windows_8h_source.html#l00334)