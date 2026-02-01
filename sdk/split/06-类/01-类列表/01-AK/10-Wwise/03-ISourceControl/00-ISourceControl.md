# ISourceControl

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [ISourceControl](class_a_k_1_1_wwise_1_1_i_source_control.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_i_source_control-members.html) |
[类](#nested-classes)

AK.Wwise::ISourceControl类 参考abstract

`#include <ISourceControl.h>`

|  |  |
| --- | --- |
| 类 | |
| struct | [FilenameToIconMapItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_filename_to_icon_map_item.html) |
|  | |
| struct | [FilenameToStatusMapItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_filename_to_status_map_item.html) |
|  | |
| class | [IFileOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result.html) |
|  | |
| class | [IOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result.html) |
|  | The base interface for operations that return information to [Wwise](namespace_a_k_1_1_wwise.html) [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result.html#details) |
|  | |
| struct | [OperationListItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_operation_list_item.html) |
|  | Operation list item. This is the type used in the [AK::Wwise::ISourceControl::OperationList](class_a_k_1_1_wwise_1_1_i_source_control_a252fa3e07c09cdc0327d6abfb6edef0e.html#a252fa3e07c09cdc0327d6abfb6edef0e) [SourceControlContainers::IAkList](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list.html) template class. [更多...](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_operation_list_item.html#details) |
|  | |
| class | [PluginInfo](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info.html) |
|  | Plug-in information structure. This structure gives a simple overview of the plug-in's capabilities. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| Enumeration types | |
| enum | [OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) {     [OperationResult\_Succeed](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286a09b97e2038b8711af85e85defb9d60df) = 0, [OperationResult\_Failed](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286a6e32811e5edb7a3759395f80a1a50b8e), [OperationResult\_TimedOut](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286a03b4a0169867eb5f643bb547c4f6f1ac), [OperationResult\_Cancelled](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286a660d057104014101ba9e6bc762c22e0d),     [OperationResult\_NotImplemented](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286a6a6c4097a583049a939fbd9625b5684c)   } |
|  | |
| enum | [OperationMenuType](class_a_k_1_1_wwise_1_1_i_source_control_ad7e6288b68631de09d5e6bbd6102dfdf.html#ad7e6288b68631de09d5e6bbd6102dfdf) { [OperationMenuType\_WorkUnits](class_a_k_1_1_wwise_1_1_i_source_control_ad7e6288b68631de09d5e6bbd6102dfdf.html#ad7e6288b68631de09d5e6bbd6102dfdfa0304cb059d58af3ea65c3f5dd5559309) = 0, [OperationMenuType\_Sources](class_a_k_1_1_wwise_1_1_i_source_control_ad7e6288b68631de09d5e6bbd6102dfdf.html#ad7e6288b68631de09d5e6bbd6102dfdfaf641a937a65bf6be0eb663ec2376b9ac), [OperationMenuType\_Generated](class_a_k_1_1_wwise_1_1_i_source_control_ad7e6288b68631de09d5e6bbd6102dfdf.html#ad7e6288b68631de09d5e6bbd6102dfdfa2e59ee90c2757bebb41738e357daa9d8), [OperationMenuType\_Explorer](class_a_k_1_1_wwise_1_1_i_source_control_ad7e6288b68631de09d5e6bbd6102dfdf.html#ad7e6288b68631de09d5e6bbd6102dfdfa89af338088ea01a6b0941ff5c1adecce) } |
|  | |
| enum | [CreateOrModifyOperation](class_a_k_1_1_wwise_1_1_i_source_control_a5968245c0eb13b2c3f5fc4e1e48150b4.html#a5968245c0eb13b2c3f5fc4e1e48150b4) { [CreateOrModifyOperation\_Create](class_a_k_1_1_wwise_1_1_i_source_control_a5968245c0eb13b2c3f5fc4e1e48150b4.html#a5968245c0eb13b2c3f5fc4e1e48150b4a08efe2931db3f0145e58b00488c78b1c) = 1 << 0, [CreateOrModifyOperation\_Modify](class_a_k_1_1_wwise_1_1_i_source_control_a5968245c0eb13b2c3f5fc4e1e48150b4.html#a5968245c0eb13b2c3f5fc4e1e48150b4a75bc8e4aaa9578dcf8392ec9245f0b30) = 1 << 1 } |
|  | Pre/PostCreateOrModify Operation flags. These flags represent the operation(s) performed on files. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a5968245c0eb13b2c3f5fc4e1e48150b4.html#a5968245c0eb13b2c3f5fc4e1e48150b4) |
|  | |
| enum | [OperationEffect](class_a_k_1_1_wwise_1_1_i_source_control_a5a211138d467837ead81bfa7446aa31b.html#a5a211138d467837ead81bfa7446aa31b) { [OperationEffect\_LocalContentModification](class_a_k_1_1_wwise_1_1_i_source_control_a5a211138d467837ead81bfa7446aa31b.html#a5a211138d467837ead81bfa7446aa31baf7c9ca4cc20d28544f6ae374a5ea4b65) = 1 << 0, [OperationEffect\_ServerContentModification](class_a_k_1_1_wwise_1_1_i_source_control_a5a211138d467837ead81bfa7446aa31b.html#a5a211138d467837ead81bfa7446aa31ba845c2d9ca06a72dbacf2879168900790) = 1 << 1 } |
|  | The operation's effect on the file(s) involved. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a5a211138d467837ead81bfa7446aa31b.html#a5a211138d467837ead81bfa7446aa31b) |
|  | |
| List types | |
| typedef [SourceControlContainers::IAkList](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list.html)< LPCWSTR, LPCWSTR > | [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) |
|  | |
| typedef [SourceControlContainers::IAkList](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list.html)< bool > | [BooleanList](class_a_k_1_1_wwise_1_1_i_source_control_a836e012f96e4b1f37b871797d69e8556.html#a836e012f96e4b1f37b871797d69e8556) |
|  | |
| typedef [SourceControlContainers::IAkList](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list.html)< GUID > | [PluginIDList](class_a_k_1_1_wwise_1_1_i_source_control_aa14dc7e7b43dce0ff7098d8e6e0150c5.html#aa14dc7e7b43dce0ff7098d8e6e0150c5) |
|  | |
| typedef [SourceControlContainers::IAkList](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list.html)< [OperationListItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_operation_list_item.html) > | [OperationList](class_a_k_1_1_wwise_1_1_i_source_control_a252fa3e07c09cdc0327d6abfb6edef0e.html#a252fa3e07c09cdc0327d6abfb6edef0e) |
|  | |
| Exported functions prototypes | |
| typedef void(\_\_stdcall \* | [GetSourceControlIDListFuncPtr](class_a_k_1_1_wwise_1_1_i_source_control_a5884432f102b445c4c3de021a3867e46.html#a5884432f102b445c4c3de021a3867e46)) ([PluginIDList](class_a_k_1_1_wwise_1_1_i_source_control_aa14dc7e7b43dce0ff7098d8e6e0150c5.html#aa14dc7e7b43dce0ff7098d8e6e0150c5) &out\_rPluginIDList) |
|  | Gets the plug-in ID list contained by the DLL file. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a5884432f102b445c4c3de021a3867e46.html#a5884432f102b445c4c3de021a3867e46) |
|  | |
| typedef void(\_\_stdcall \* | [GetSourceControlPluginInfoFuncPtr](class_a_k_1_1_wwise_1_1_i_source_control_a9e3376c6dbaa3e6094e21e04aa2a28e1.html#a9e3376c6dbaa3e6094e21e04aa2a28e1)) (const GUID &in\_rguidPluginID, [PluginInfo](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info.html) &out\_rPluginInfo) |
|  | Gets the [AK::Wwise::ISourceControl::PluginInfo](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info.html "Plug-in information structure. This structure gives a simple overview of the plug-in's capabilities.") class associated with a given plug-in ID. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a9e3376c6dbaa3e6094e21e04aa2a28e1.html#a9e3376c6dbaa3e6094e21e04aa2a28e1) |
|  | |
| typedef [ISourceControl](class_a_k_1_1_wwise_1_1_i_source_control.html) \*(\_\_stdcall \* | [GetSourceControlInstanceFuncPtr](class_a_k_1_1_wwise_1_1_i_source_control_a5ea75c450aecec73c2b29f51d990a206.html#a5ea75c450aecec73c2b29f51d990a206)) (const GUID &in\_guidPluginID) |
|  | |

|  |  |
| --- | --- |
| Map types | |
| typedef [SourceControlContainers::IAkMap](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map.html)< LPCWSTR, LPCWSTR, [FilenameToIconMapItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_filename_to_icon_map_item.html), const [FilenameToIconMapItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_filename_to_icon_map_item.html) & > | [FilenameToIconMap](class_a_k_1_1_wwise_1_1_i_source_control_ae16205a719cf623f73723c682137725d.html#ae16205a719cf623f73723c682137725d) |
|  | |
| typedef [SourceControlContainers::IAkMap](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map.html)< LPCWSTR, LPCWSTR, [FilenameToStatusMapItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_filename_to_status_map_item.html), const [FilenameToStatusMapItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_filename_to_status_map_item.html) & > | [FilenameToStatusMap](class_a_k_1_1_wwise_1_1_i_source_control_a30261059634389631172580a206ae2fd.html#a30261059634389631172580a206ae2fd) |
|  | |
| typedef [SourceControlContainers::IAkMap](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map.html)< LPCWSTR, LPCWSTR, LPCWSTR, LPCWSTR > | [IConnectParameterMap](class_a_k_1_1_wwise_1_1_i_source_control_aa67901d289200c92764d1a3dc3bd035b.html#aa67901d289200c92764d1a3dc3bd035b) |
|  | |
| virtual void | [Init](class_a_k_1_1_wwise_1_1_i_source_control_a965c84c993e7b9644a7d51dafcdeb113.html#a965c84c993e7b9644a7d51dafcdeb113) ([AK::Wwise::ISourceControlUtilities](class_a_k_1_1_wwise_1_1_i_source_control_utilities.html) \*in\_pUtilities, bool in\_bAutoAccept)=0 |
|  | This function is called when the plug-in is initialized after its creation. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a965c84c993e7b9644a7d51dafcdeb113.html#a965c84c993e7b9644a7d51dafcdeb113) |
|  | |
| virtual void | [Term](class_a_k_1_1_wwise_1_1_i_source_control_a488a4e256024111dc7c3eceef7970b11.html#a488a4e256024111dc7c3eceef7970b11) ()=0 |
|  | This function is called when the plug-in is terminated before its destruction. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a488a4e256024111dc7c3eceef7970b11.html#a488a4e256024111dc7c3eceef7970b11) |
|  | |
| virtual void | [Destroy](class_a_k_1_1_wwise_1_1_i_source_control_a7682bc6fd40d00c825703604ab79fc85.html#a7682bc6fd40d00c825703604ab79fc85) ()=0 |
|  | This function destroys the plug-in. The implementation is generally '{ delete this; }'. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a7682bc6fd40d00c825703604ab79fc85.html#a7682bc6fd40d00c825703604ab79fc85) |
|  | |
| virtual [OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [Connect](class_a_k_1_1_wwise_1_1_i_source_control_a71c0972018e84456c33037f17151592a.html#a71c0972018e84456c33037f17151592a) (const [IConnectParameterMap](class_a_k_1_1_wwise_1_1_i_source_control_aa67901d289200c92764d1a3dc3bd035b.html#aa67901d289200c92764d1a3dc3bd035b) &parameterMap)=0 |
|  | This method connects the source control plugin [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a71c0972018e84456c33037f17151592a.html#a71c0972018e84456c33037f17151592a) |
|  | |
| virtual [OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [Disconnect](class_a_k_1_1_wwise_1_1_i_source_control_ababf2c5251d5b1f3d2a057eaf4968922.html#ababf2c5251d5b1f3d2a057eaf4968922) ()=0 |
|  | This method disconnects the source control plugin [更多...](class_a_k_1_1_wwise_1_1_i_source_control_ababf2c5251d5b1f3d2a057eaf4968922.html#ababf2c5251d5b1f3d2a057eaf4968922) |
|  | |
| virtual bool | [ShowConfigDlg](class_a_k_1_1_wwise_1_1_i_source_control_a895acce7b436743e5519245529c97ecd.html#a895acce7b436743e5519245529c97ecd) ()=0 |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [GetOperationList](class_a_k_1_1_wwise_1_1_i_source_control_ad7820c108e50155039c92223eff718f3.html#ad7820c108e50155039c92223eff718f3) ([OperationMenuType](class_a_k_1_1_wwise_1_1_i_source_control_ad7e6288b68631de09d5e6bbd6102dfdf.html#ad7e6288b68631de09d5e6bbd6102dfdf) in\_menuType, const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, [OperationList](class_a_k_1_1_wwise_1_1_i_source_control_a252fa3e07c09cdc0327d6abfb6edef0e.html#a252fa3e07c09cdc0327d6abfb6edef0e) &out\_rOperationList)=0 |
|  | |
| virtual LPCWSTR | [GetOperationName](class_a_k_1_1_wwise_1_1_i_source_control_a817835af7fd2e208f9ba202d6eb5a2eb.html#a817835af7fd2e208f9ba202d6eb5a2eb) (DWORD in\_dwOperationID)=0 |
|  | Gets the operation name to display in user interface [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a817835af7fd2e208f9ba202d6eb5a2eb.html#a817835af7fd2e208f9ba202d6eb5a2eb) |
|  | |
| virtual DWORD | [GetOperationEffect](class_a_k_1_1_wwise_1_1_i_source_control_a1cb1c283baf8b61df030a862dd2dc880.html#a1cb1c283baf8b61df030a862dd2dc880) (DWORD in\_dwOperationID)=0 |
|  | Gets the operation effect on the file(s) involved in the operation. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_a1cb1c283baf8b61df030a862dd2dc880.html#a1cb1c283baf8b61df030a862dd2dc880) |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [GetFileStatus](class_a_k_1_1_wwise_1_1_i_source_control_ad9ed25401176139c3185a5980b6d44d4.html#ad9ed25401176139c3185a5980b6d44d4) (const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, [FilenameToStatusMap](class_a_k_1_1_wwise_1_1_i_source_control_a30261059634389631172580a206ae2fd.html#a30261059634389631172580a206ae2fd) &out\_rFileStatusMap, DWORD in\_dwTimeoutMs=INFINITE)=0 |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [GetFileStatusIcons](class_a_k_1_1_wwise_1_1_i_source_control_a177b1676aeffa151c86255a7b747fcdc.html#a177b1676aeffa151c86255a7b747fcdc) (const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, [FilenameToIconMap](class_a_k_1_1_wwise_1_1_i_source_control_ae16205a719cf623f73723c682137725d.html#ae16205a719cf623f73723c682137725d) &out\_rFileIconsMap, DWORD in\_dwTimeoutMs=INFINITE)=0 |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [GetFileStatusAndIcons](class_a_k_1_1_wwise_1_1_i_source_control_acddafee15f9c40453fdc2c881bb77d3e.html#acddafee15f9c40453fdc2c881bb77d3e) (const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, [FilenameToStatusMap](class_a_k_1_1_wwise_1_1_i_source_control_a30261059634389631172580a206ae2fd.html#a30261059634389631172580a206ae2fd) &out\_rFileStatusMap, [FilenameToIconMap](class_a_k_1_1_wwise_1_1_i_source_control_ae16205a719cf623f73723c682137725d.html#ae16205a719cf623f73723c682137725d) &out\_rFileIconsMap, DWORD in\_dwTimeoutMs=INFINITE)=0 |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [GetMissingFilesInDirectories](class_a_k_1_1_wwise_1_1_i_source_control_acda8ef1d7727c6ba45d302f4c4ee339e.html#acda8ef1d7727c6ba45d302f4c4ee339e) (const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rDirectoryList, [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &out\_rFilenameList)=0 |
|  | |
| virtual [IOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result.html) \* | [DoOperation](class_a_k_1_1_wwise_1_1_i_source_control_a36789a297bc4a85ba0fffb9de9bc0a6f.html#a36789a297bc4a85ba0fffb9de9bc0a6f) (DWORD in\_dwOperationID, const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) \*in\_pTargetFilenameList=NULL)=0 |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [PreCreateOrModify](class_a_k_1_1_wwise_1_1_i_source_control_aba7d81dda40d38b6c8bb81d190b846f7.html#aba7d81dda40d38b6c8bb81d190b846f7) (const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, [CreateOrModifyOperation](class_a_k_1_1_wwise_1_1_i_source_control_a5968245c0eb13b2c3f5fc4e1e48150b4.html#a5968245c0eb13b2c3f5fc4e1e48150b4) in\_eOperation, bool &out\_rContinue)=0 |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [PostCreateOrModify](class_a_k_1_1_wwise_1_1_i_source_control_a9fb467f0d5dbcb386290f53a81bb8dc5.html#a9fb467f0d5dbcb386290f53a81bb8dc5) (const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, [CreateOrModifyOperation](class_a_k_1_1_wwise_1_1_i_source_control_a5968245c0eb13b2c3f5fc4e1e48150b4.html#a5968245c0eb13b2c3f5fc4e1e48150b4) in\_eOperation, bool &out\_rContinue)=0 |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [GetFilesForOperation](class_a_k_1_1_wwise_1_1_i_source_control_aa129444c0cbcbb9a2b1c1c12045c40aa.html#aa129444c0cbcbb9a2b1c1c12045c40aa) (DWORD in\_dwOperationID, const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &out\_rFilenameList, [FilenameToStatusMap](class_a_k_1_1_wwise_1_1_i_source_control_a30261059634389631172580a206ae2fd.html#a30261059634389631172580a206ae2fd) &out\_rFileStatusMap)=0 |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [CheckFilesForOperation](class_a_k_1_1_wwise_1_1_i_source_control_a87b2931fc41f533058657f264f4bfcb2.html#a87b2931fc41f533058657f264f4bfcb2) (DWORD in\_dwOperationID, const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, [BooleanList](class_a_k_1_1_wwise_1_1_i_source_control_a836e012f96e4b1f37b871797d69e8556.html#a836e012f96e4b1f37b871797d69e8556) &out\_rFileStatusList)=0 |
|  | |
| virtual [AK::Wwise::ISourceControl::OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [FilesUnderSourceControl](class_a_k_1_1_wwise_1_1_i_source_control_a7ff14cbefc9af7fbea4a3162a4b0efd5.html#a7ff14cbefc9af7fbea4a3162a4b0efd5) (const [StringList](class_a_k_1_1_wwise_1_1_i_source_control_ad19b864d62ff8aba7da365269242e3c7.html#ad19b864d62ff8aba7da365269242e3c7) &in\_rFilenameList, [BooleanList](class_a_k_1_1_wwise_1_1_i_source_control_a836e012f96e4b1f37b871797d69e8556.html#a836e012f96e4b1f37b871797d69e8556) &out\_rFileStatusList)=0 |
|  | |

## 详细描述

[Wwise](namespace_a_k_1_1_wwise.html) source control plug-in interface. This is the interface that the plug-in must implement. It contains all the necessary functions to perform source control operations and manage the [Wwise](namespace_a_k_1_1_wwise.html) source control UI.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

参见
:   - [构建版本控制插件信息类](source_control_dll.html#source_control_dll_creation_object_information)

在文件 [ISourceControl.h](_i_source_control_8h_source.html) 第 [64](_i_source_control_8h_source.html#l00064) 行定义.