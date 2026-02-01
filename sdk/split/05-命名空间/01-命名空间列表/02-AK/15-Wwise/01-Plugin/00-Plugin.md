# Plugin

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)

[命名空间](#namespaces) |
[类](#nested-classes) |
[类型定义](#typedef-members) |
[枚举](#enum-members) |
[函数](#func-members)

AK::Wwise::Plugin 命名空间参考

|  |  |
| --- | --- |
| 命名空间 | |
|  | [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications.html) |
|  | |
|  | [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html) |
|  | |
|  | [V2](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2.html) |
|  | |
|  | [XmlElementType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_element_type.html) |
|  | |
|  | [XmlNodeType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type.html) |
|  | Types of possible XML elements. See MSDN documentation topics for [XmlNodeType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type.html "Types of possible XML elements. See MSDN documentation topics for XmlNodeType."). |
|  | |
|  | [XmlWhiteSpaceHandling](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_white_space_handling.html) |
|  | |
|  | [XmlWriteReady](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready.html) |
|  | Possible error codes when writing XML |
|  | |
|  | [XmlWriteState](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state.html) |
|  | |

|  |  |
| --- | --- |
| 类 | |
| class | [AutoUndoGroup](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group.html) |
|  | |
| class | [CBaseInstanceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Associates an existing C Interface with a variable that can be used. Derives from the instance that uses it. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html#details) |
|  | |
| class | [CBaseInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): For each plug-in interface type, provides a single static instance used throughout this plug-in container. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html#details) |
|  | |
| struct | [ConversionContext](struct_a_k_1_1_wwise_1_1_plugin_1_1_conversion_context.html) |
|  | |
| struct | [ConvertedFileInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_converted_file_info.html) |
|  | |
| class | [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Base class for every C++ instance that retrieves a service from the [Wwise](namespace_a_k_1_1_wwise.html) Authoring host. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html#details) |
|  | |
| class | [HostInterfaceGlue< CPPInstance, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_3_01_c_p_p_instance_00_01true_01_4.html) |
|  | |
| class | [IProgress](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress.html) |
|  | |
| class | [IReadOnlyProperties](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties.html) |
|  | Interfaces used to set and get the properties from a plug in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties.html#details) |
|  | |
| class | [IReadWriteProperties](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties.html) |
|  | |
| class | [IWriteString](class_a_k_1_1_wwise_1_1_plugin_1_1_i_write_string.html) |
|  | |
| struct | [KnownInterfaceClass](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Compile-time dictionary of known interface-version. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class.html#details) |
|  | |
| struct | [KnownInterfaceClass< AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PLUGIN\_CONTAINER, 1 >](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class_3_01_a_k___w_w_i_s_e___p_l_u_g_i_n___i2061849bd7ce9e600e94611bde4bbe05.html) |
|  | |
| struct | [LatestInterfaceVersion](struct_a_k_1_1_wwise_1_1_plugin_1_1_latest_interface_version.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Defines a compile-time dictionary with the latest version known to the SDK for each interface. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_latest_interface_version.html#details) |
|  | |
| struct | [LatestInterfaceVersion< AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PLUGIN\_CONTAINER >](struct_a_k_1_1_wwise_1_1_plugin_1_1_latest_interface_version_3_01_a_k___w_w_i_s_e___p_l_u_g_i_n_1f919b2745dd48bfee90f50effc527af.html) |
|  | |
| struct | [LicenseID](struct_a_k_1_1_wwise_1_1_plugin_1_1_license_i_d.html) |
|  | |
| struct | [MonitorData](struct_a_k_1_1_wwise_1_1_plugin_1_1_monitor_data.html) |
|  | |
| struct | [OpenedConvertedFile](struct_a_k_1_1_wwise_1_1_plugin_1_1_opened_converted_file.html) |
|  | |
| struct | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html) |
|  | C++ PluginInfo Generator. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html#details) |
|  | |
| struct | [PluginInfoTLS](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_t_l_s.html) |
|  | The interface information of the plug-in currently being instantiated. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_t_l_s.html#details) |
|  | |
| class | [PluginMFCWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html) |
|  | Initializes MFC for this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html#details) |
|  | |
| struct | [PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html) |
|  | |
| class | [ReferenceSetBase](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base.html) |
|  | Interface used to interact with reference sets. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base.html#details) |
|  | |
| class | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Requests a host-provided service, and optionally receives a variable containing the default instance. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface.html#details) |
|  | |
| class | [RequestedHostInterface< DataWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_data_writer_01_4.html) |
|  | |
| class | [RequestedHostInterface< FrontendModel >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4.html) |
|  | |
| class | [RequestedHostInterface< Host >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4.html) |
|  | |
| class | [RequestedHostInterface< LinkBackend >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_backend_01_4.html) |
|  | |
| class | [RequestedHostInterface< LinkFrontend >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_frontend_01_4.html) |
|  | |
| class | [RequestedHostInterface< ObjectMedia >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_media_01_4.html) |
|  | |
| class | [RequestedHostInterface< ObjectStore >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_store_01_4.html) |
|  | |
| class | [RequestedHostInterface< PropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4.html) |
|  | |
| class | [RequestedHostInterface< ReferenceSet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4.html) |
|  | |
| class | [RequestedHostInterface< TestService >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_test_service_01_4.html) |
|  | |
| class | [RequestedHostInterface< UndoManager >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_undo_manager_01_4.html) |
|  | |
| class | [RequestedHostInterface< V1::Host >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_v1_1_1_host_01_4.html) |
|  | |
| class | [RequestedHostInterface< V1::PropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_v1_1_1_property_set_01_4.html) |
|  | |
| class | [RequestedHostInterface< V1::TestService >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_v1_1_1_test_service_01_4.html) |
|  | |
| class | [RequestedHostInterface< XmlReader >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4.html) |
|  | |
| class | [RequestedHostInterface< XmlWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_writer_01_4.html) |
|  | |
| struct | [RiffHeader](struct_a_k_1_1_wwise_1_1_plugin_1_1_riff_header.html) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [CAudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_a5b3913f268e5fae72c8a73a2e6f5ca53.html#a5b3913f268e5fae72c8a73a2e6f5ca53) = [V1::CAudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ae5b0d46ea918e3573f5efbd0f6d0b9d0.html#ae5b0d46ea918e3573f5efbd0f6d0b9d0) |
|  | Latest version of the C AudioPlugin interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a5b3913f268e5fae72c8a73a2e6f5ca53.html#a5b3913f268e5fae72c8a73a2e6f5ca53) |
|  | |
| using | [AudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_a989b8417cedde33d928b90171491fcc5.html#a989b8417cedde33d928b90171491fcc5) = [V1::AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html) |
|  | Latest version of the C++ AudioPlugin interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a989b8417cedde33d928b90171491fcc5.html#a989b8417cedde33d928b90171491fcc5) |
|  | |
| using | [CCustomData](namespace_a_k_1_1_wwise_1_1_plugin_a49cd878c81e427439d7e606515774bf7.html#a49cd878c81e427439d7e606515774bf7) = [V1::CCustomData](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_af298eb6c35ed254f6b2b75b2df0ff39a.html#af298eb6c35ed254f6b2b75b2df0ff39a) |
|  | Latest version of the C CustomData interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a49cd878c81e427439d7e606515774bf7.html#a49cd878c81e427439d7e606515774bf7) |
|  | |
| using | [CustomData](namespace_a_k_1_1_wwise_1_1_plugin_ac1f7b957043934f47d294ecd2d71d0ca.html#ac1f7b957043934f47d294ecd2d71d0ca) = [V1::CustomData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.html) |
|  | Latest version of the C++ CustomData interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ac1f7b957043934f47d294ecd2d71d0ca.html#ac1f7b957043934f47d294ecd2d71d0ca) |
|  | |
| using | [CFirstTimeCreationMessage](namespace_a_k_1_1_wwise_1_1_plugin_a67b1d35db15070c3c69c9644357a8981.html#a67b1d35db15070c3c69c9644357a8981) = [V1::CFirstTimeCreationMessage](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_af924488c8495a657722804248de4c2c8.html#af924488c8495a657722804248de4c2c8) |
|  | Latest version of the C FirstTimeCreationMessage interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a67b1d35db15070c3c69c9644357a8981.html#a67b1d35db15070c3c69c9644357a8981) |
|  | |
| using | [FirstTimeCreationMessage](namespace_a_k_1_1_wwise_1_1_plugin_a1120c7a177977ca71bdb7e5190489478.html#a1120c7a177977ca71bdb7e5190489478) = [V1::FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message.html) |
|  | Latest version of the C++ FirstTimeCreationMessage interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a1120c7a177977ca71bdb7e5190489478.html#a1120c7a177977ca71bdb7e5190489478) |
|  | |
| using | [CFrontend](namespace_a_k_1_1_wwise_1_1_plugin_a50e3966725bc51606e5e5200f42c7fb0.html#a50e3966725bc51606e5e5200f42c7fb0) = [V1::CFrontend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_aefff5dbb0c5445942b31da2c4ea2e016.html#aefff5dbb0c5445942b31da2c4ea2e016) |
|  | Latest version of the C Frontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a50e3966725bc51606e5e5200f42c7fb0.html#a50e3966725bc51606e5e5200f42c7fb0) |
|  | |
| using | [Frontend](namespace_a_k_1_1_wwise_1_1_plugin_ade7bf4707d85e10aae30ea0780abe527.html#ade7bf4707d85e10aae30ea0780abe527) = [V1::Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html) |
|  | Latest version of the C++ Frontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ade7bf4707d85e10aae30ea0780abe527.html#ade7bf4707d85e10aae30ea0780abe527) |
|  | |
| using | [CGUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_ab13f5dbcc6517ad4c728d74301996232.html#ab13f5dbcc6517ad4c728d74301996232) = [V1::CGUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_afd79a3a4b81bc5601ec3e2223bcd8974.html#afd79a3a4b81bc5601ec3e2223bcd8974) |
|  | Latest version of the C GUIWindows interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ab13f5dbcc6517ad4c728d74301996232.html#ab13f5dbcc6517ad4c728d74301996232) |
|  | |
| using | [GUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_a5d74c88aa83c4e608fb75d1ac5555c9b.html#a5d74c88aa83c4e608fb75d1ac5555c9b) = [V1::GUIWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.html) |
|  | Latest version of the C++ GUIWindows interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a5d74c88aa83c4e608fb75d1ac5555c9b.html#a5d74c88aa83c4e608fb75d1ac5555c9b) |
|  | |
| using | [CHost](namespace_a_k_1_1_wwise_1_1_plugin_aa96b27e8272b257ab8bf4cedc96122ca.html#aa96b27e8272b257ab8bf4cedc96122ca) = [V2::CHost](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a5af2573092f8990f393f30066f9ea80c.html#a5af2573092f8990f393f30066f9ea80c) |
|  | Latest version of the C Host interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aa96b27e8272b257ab8bf4cedc96122ca.html#aa96b27e8272b257ab8bf4cedc96122ca) |
|  | |
| using | [Host](namespace_a_k_1_1_wwise_1_1_plugin_af6f9dc5d367c3383c37f96fe9e1b943f.html#af6f9dc5d367c3383c37f96fe9e1b943f) = [V2::Host](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host.html) |
|  | Latest version of the C++ Host interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af6f9dc5d367c3383c37f96fe9e1b943f.html#af6f9dc5d367c3383c37f96fe9e1b943f) |
|  | |
| using | [RequestHost](namespace_a_k_1_1_wwise_1_1_plugin_a4ef1b0bee4438ded222bf1a691d61722.html#a4ef1b0bee4438ded222bf1a691d61722) = [V2::RequestHost](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_ae121d77285491869dcc7e169b2342133.html#ae121d77285491869dcc7e169b2342133) |
|  | Latest version of the requested C++ Host interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4ef1b0bee4438ded222bf1a691d61722.html#a4ef1b0bee4438ded222bf1a691d61722) |
|  | |
| using | [CHostDataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a57477155e587be4bb9216ede425ea93e.html#a57477155e587be4bb9216ede425ea93e) = [V1::CHostDataWriter](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_afd451009f6669cae2d5f092544a15f96.html#afd451009f6669cae2d5f092544a15f96) |
|  | Latest version of the C DataWriter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a57477155e587be4bb9216ede425ea93e.html#a57477155e587be4bb9216ede425ea93e) |
|  | |
| using | [DataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a32526a23215a4452f561220b527e12f8.html#a32526a23215a4452f561220b527e12f8) = [V1::DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html) |
|  | Latest version of the C++ DataWriter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a32526a23215a4452f561220b527e12f8.html#a32526a23215a4452f561220b527e12f8) |
|  | |
| using | [RequestWrite](namespace_a_k_1_1_wwise_1_1_plugin_a4b87b9ead392d9ede43fed7d3629496f.html#a4b87b9ead392d9ede43fed7d3629496f) = [V1::RequestWrite](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a367ed0e46ef3a05f90889603621c623f.html#a367ed0e46ef3a05f90889603621c623f) |
|  | Latest version of the requested C++ DataWriter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4b87b9ead392d9ede43fed7d3629496f.html#a4b87b9ead392d9ede43fed7d3629496f) |
|  | |
| using | [CHostFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_af24a3f1547c57009739461b422fb7a90.html#af24a3f1547c57009739461b422fb7a90) = [V1::CHostFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a427443c428bc8db3bcdda5fff6a5fe4a.html#a427443c428bc8db3bcdda5fff6a5fe4a) |
|  | Latest version of the C FrontendModel interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af24a3f1547c57009739461b422fb7a90.html#af24a3f1547c57009739461b422fb7a90) |
|  | |
| using | [FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb) = [V1::FrontendModel](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model.html) |
|  | Latest version of the C++ FrontendModel interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb) |
|  | |
| using | [RequestFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a08800f5f1455eee4531b3ffa1b8fbf7a.html#a08800f5f1455eee4531b3ffa1b8fbf7a) = [V1::RequestFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a04cfe873a10a643f151a6717375312cf.html#a04cfe873a10a643f151a6717375312cf) |
|  | Latest version of the requested C++ FrontendModel interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a08800f5f1455eee4531b3ffa1b8fbf7a.html#a08800f5f1455eee4531b3ffa1b8fbf7a) |
|  | |
| using | [CHostObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a4a7fe49717628bdfda765fbaee107d7a.html#a4a7fe49717628bdfda765fbaee107d7a) = [V1::CHostObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a8022609c599c92d28ea192e81b3175c6.html#a8022609c599c92d28ea192e81b3175c6) |
|  | Latest version of the C ObjectMedia interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4a7fe49717628bdfda765fbaee107d7a.html#a4a7fe49717628bdfda765fbaee107d7a) |
|  | |
| using | [ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a0325d70f4523c31f1b4f5dc8acdf3e2b.html#a0325d70f4523c31f1b4f5dc8acdf3e2b) = [V1::ObjectMedia](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media.html) |
|  | Latest version of the C++ ObjectMedia interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a0325d70f4523c31f1b4f5dc8acdf3e2b.html#a0325d70f4523c31f1b4f5dc8acdf3e2b) |
|  | |
| using | [RequestObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a0d8a1c4d25d025d4614f072197956e60.html#a0d8a1c4d25d025d4614f072197956e60) = [V1::RequestObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_abe0c5913cfd0cf4d76b48f46632d5aa3.html#abe0c5913cfd0cf4d76b48f46632d5aa3) |
|  | Latest version of the requested C++ ObjectMedia interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a0d8a1c4d25d025d4614f072197956e60.html#a0d8a1c4d25d025d4614f072197956e60) |
|  | |
| using | [CHostObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_adaab29f68e9ece2d4649c56f52c53e96.html#adaab29f68e9ece2d4649c56f52c53e96) = [V1::CHostObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a47bf77f6f1de2492c10a8788039f1a08.html#a47bf77f6f1de2492c10a8788039f1a08) |
|  | Latest version of the C ObjectStore interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_adaab29f68e9ece2d4649c56f52c53e96.html#adaab29f68e9ece2d4649c56f52c53e96) |
|  | |
| using | [ObjectStore\_PropertySet\_v1](namespace_a_k_1_1_wwise_1_1_plugin_ac634cf28c4a943245fb6e127758cc02f.html#ac634cf28c4a943245fb6e127758cc02f) = [V1::ObjectStore](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.html)< [AK::Wwise::Plugin::V1::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ab5503ef97167a06c2b7d7be5c043d081.html#ab5503ef97167a06c2b7d7be5c043d081) > |
|  | Latest version of the C++ ObjectStore interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ac634cf28c4a943245fb6e127758cc02f.html#ac634cf28c4a943245fb6e127758cc02f) |
|  | |
| using | [ObjectStore\_PropertySet\_v2](namespace_a_k_1_1_wwise_1_1_plugin_ad0bd3a3df770388385fa7d803d25941e.html#ad0bd3a3df770388385fa7d803d25941e) = [V1::ObjectStore](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.html)< [AK::Wwise::Plugin::V2::PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html) > |
|  | |
| using | [ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_aa1a4c71b6a4959d8e06f9e3cc976c749.html#aa1a4c71b6a4959d8e06f9e3cc976c749) = [ObjectStore\_PropertySet\_v2](namespace_a_k_1_1_wwise_1_1_plugin_ad0bd3a3df770388385fa7d803d25941e.html#ad0bd3a3df770388385fa7d803d25941e) |
|  | |
| using | [RequestObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_aa75f21542f68316133473c611537a0b9.html#aa75f21542f68316133473c611537a0b9) = [V1::RequestObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a1ffe19f6268c48cb9afae1996296714f.html#a1ffe19f6268c48cb9afae1996296714f) |
|  | Latest version of the requested C++ ObjectStore interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aa75f21542f68316133473c611537a0b9.html#aa75f21542f68316133473c611537a0b9) |
|  | |
| using | [CHostPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a485c72db20c02ae9f16af1baca14bde4.html#a485c72db20c02ae9f16af1baca14bde4) = [V2::CHostPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_adadefb669a14a661a38960b441d2de02.html#adadefb669a14a661a38960b441d2de02) |
|  | Latest version of the C PropertySet interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a485c72db20c02ae9f16af1baca14bde4.html#a485c72db20c02ae9f16af1baca14bde4) |
|  | |
| using | [PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de) = [V2::PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html) |
|  | Latest version of the C++ PropertySet interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de) |
|  | |
| using | [RequestPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a5eb9b772d01c414e7c77b44ef66e661f.html#a5eb9b772d01c414e7c77b44ef66e661f) = [V2::RequestPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a75474e2ae58b9851b89d7ccd9a4fbcdf.html#a75474e2ae58b9851b89d7ccd9a4fbcdf) |
|  | Latest version of the requested C++ PropertySet interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a5eb9b772d01c414e7c77b44ef66e661f.html#a5eb9b772d01c414e7c77b44ef66e661f) |
|  | |
| using | [CHostReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_a536d3a045013fa219001b7b005112feb.html#a536d3a045013fa219001b7b005112feb) = [ak\_wwise\_plugin\_host\_reference\_set\_v1](structak__wwise__plugin__host__reference__set__v1.html) |
|  | |
| using | [ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_aa9c66805a7050040225bb144c6be8d06.html#aa9c66805a7050040225bb144c6be8d06) = [ReferenceSetBase](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base.html)<> |
|  | |
| using | [RequestReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_af440c5da9f9765a6b9518ea8b7c3f2c1.html#af440c5da9f9765a6b9518ea8b7c3f2c1) = [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface.html)< [ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_aa9c66805a7050040225bb144c6be8d06.html#aa9c66805a7050040225bb144c6be8d06) > |
|  | Requests a ReferenceSet interface, provided as m\_referenceSet variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af440c5da9f9765a6b9518ea8b7c3f2c1.html#af440c5da9f9765a6b9518ea8b7c3f2c1) |
|  | |
| using | [CUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_ae4ec3b2c8d557d96a6c79ad1f999da0f.html#ae4ec3b2c8d557d96a6c79ad1f999da0f) = [V1::CUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a0af52d142b140c8a7ada1115d2ed005d.html#a0af52d142b140c8a7ada1115d2ed005d) |
|  | Latest version of the C UndoEvent interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ae4ec3b2c8d557d96a6c79ad1f999da0f.html#ae4ec3b2c8d557d96a6c79ad1f999da0f) |
|  | |
| using | [BaseUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_a106b6fb5a0b6171d250ccbb5059e4961.html#a106b6fb5a0b6171d250ccbb5059e4961) = [V1::BaseUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_base_undo_event.html) |
|  | Latest version of the C++ BaseUndoEvent interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a106b6fb5a0b6171d250ccbb5059e4961.html#a106b6fb5a0b6171d250ccbb5059e4961) |
|  | |
| template<typename Backend > | |
| using | [UndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_a88dacbb21afe6f7190ae605d5aeeabd9.html#a88dacbb21afe6f7190ae605d5aeeabd9) = [V1::UndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html)< Backend > |
|  | Latest version of the C++ UndoEvent template helper. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a88dacbb21afe6f7190ae605d5aeeabd9.html#a88dacbb21afe6f7190ae605d5aeeabd9) |
|  | |
| template<typename BackendDerivedClass > | |
| using | [DynamicUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_ab9f3b59b0e77d18ab37a9de10ef22819.html#ab9f3b59b0e77d18ab37a9de10ef22819) = [V1::DynamicUndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_dynamic_undo_event.html)< BackendDerivedClass > |
|  | Latest version of the C++ DynamicUndoEvent template helper. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ab9f3b59b0e77d18ab37a9de10ef22819.html#ab9f3b59b0e77d18ab37a9de10ef22819) |
|  | |
| using | [CHostUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a6f05bedc5077d964a3015045f166aec9.html#a6f05bedc5077d964a3015045f166aec9) = [V1::CHostUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a52afd9e84cbd6263c830cc1340cb27ed.html#a52afd9e84cbd6263c830cc1340cb27ed) |
|  | Latest version of the C UndoManager interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a6f05bedc5077d964a3015045f166aec9.html#a6f05bedc5077d964a3015045f166aec9) |
|  | |
| using | [UndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b) = [V1::UndoManager](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager.html) |
|  | Latest version of the C++ UndoManager interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b) |
|  | |
| using | [RequestUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a30d4abb3af40b4d9340aebfca998aabc.html#a30d4abb3af40b4d9340aebfca998aabc) = [V1::RequestUndoManager](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a9272de2d94abfaabb9d10a1414146a0f.html#a9272de2d94abfaabb9d10a1414146a0f) |
|  | Latest version of the requested C++ UndoManager interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a30d4abb3af40b4d9340aebfca998aabc.html#a30d4abb3af40b4d9340aebfca998aabc) |
|  | |
| using | [CHostXml](namespace_a_k_1_1_wwise_1_1_plugin_a3dc2daeee0ab37ad19f0077ae3bfc9a2.html#a3dc2daeee0ab37ad19f0077ae3bfc9a2) = [V1::CHostXml](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a074a0bfcc47a57a8a183590d1251f4bb.html#a074a0bfcc47a57a8a183590d1251f4bb) |
|  | Latest version of the C XML interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a3dc2daeee0ab37ad19f0077ae3bfc9a2.html#a3dc2daeee0ab37ad19f0077ae3bfc9a2) |
|  | |
| using | [XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150) = [V1::XmlReader](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader.html) |
|  | Latest version of the C++ XmlReader interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150) |
|  | |
| using | [XmlWriter](namespace_a_k_1_1_wwise_1_1_plugin_a3917bff28ad1858f6fca96f72f064792.html#a3917bff28ad1858f6fca96f72f064792) = [V1::XmlWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer.html) |
|  | Latest version of the C++ XmlWriter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a3917bff28ad1858f6fca96f72f064792.html#a3917bff28ad1858f6fca96f72f064792) |
|  | |
| using | [RequestXml](namespace_a_k_1_1_wwise_1_1_plugin_a1612e53e47db2162331f0eb95a1c7b93.html#a1612e53e47db2162331f0eb95a1c7b93) = [V1::RequestXml](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a984cc4dc918e2c4cad2bf43e30c80cbe.html#a984cc4dc918e2c4cad2bf43e30c80cbe) |
|  | Latest version of the requested C++ XML interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a1612e53e47db2162331f0eb95a1c7b93.html#a1612e53e47db2162331f0eb95a1c7b93) |
|  | |
| using | [CLicense](namespace_a_k_1_1_wwise_1_1_plugin_a4011d9267cc30115f858d75973fdce54.html#a4011d9267cc30115f858d75973fdce54) = [V1::CLicense](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a55306977c4bf0fa433a290066c952b96.html#a55306977c4bf0fa433a290066c952b96) |
|  | Latest version of the C License interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4011d9267cc30115f858d75973fdce54.html#a4011d9267cc30115f858d75973fdce54) |
|  | |
| using | [License](namespace_a_k_1_1_wwise_1_1_plugin_a44e186a822b15e2230c95b695b01c101.html#a44e186a822b15e2230c95b695b01c101) = [V1::License](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license.html) |
|  | Latest version of the C++ License interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a44e186a822b15e2230c95b695b01c101.html#a44e186a822b15e2230c95b695b01c101) |
|  | |
| using | [CMediaConverter](namespace_a_k_1_1_wwise_1_1_plugin_aef95c4436b404946c77657144efac8bb.html#aef95c4436b404946c77657144efac8bb) = [V1::CMediaConverter](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a34d8135b75802c9013a7fcc885c29e17.html#a34d8135b75802c9013a7fcc885c29e17) |
|  | Latest version of the C MediaConverter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aef95c4436b404946c77657144efac8bb.html#aef95c4436b404946c77657144efac8bb) |
|  | |
| using | [MediaConverter](namespace_a_k_1_1_wwise_1_1_plugin_aca00f70c566ab8b103a983d07890f430.html#aca00f70c566ab8b103a983d07890f430) = [V1::MediaConverter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter.html) |
|  | Latest version of the C++ MediaConverter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aca00f70c566ab8b103a983d07890f430.html#aca00f70c566ab8b103a983d07890f430) |
|  | |
| using | [InterfaceType](namespace_a_k_1_1_wwise_1_1_plugin_a32695b07bf576e5426c1b727bf4f541b.html#a32695b07bf576e5426c1b727bf4f541b) = decltype([BaseInterface::m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9)) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Type for the m\_interface value in BaseInterface [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a32695b07bf576e5426c1b727bf4f541b.html#a32695b07bf576e5426c1b727bf4f541b) |
|  | |
| using | [InterfaceTypeValue](namespace_a_k_1_1_wwise_1_1_plugin_af1b35c028fe0e61c30385aba36fa6372.html#af1b35c028fe0e61c30385aba36fa6372) = std::underlying\_type< [InterfaceType](namespace_a_k_1_1_wwise_1_1_plugin_a32695b07bf576e5426c1b727bf4f541b.html#a32695b07bf576e5426c1b727bf4f541b) >::type |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Underlying storage type for the m\_interface value in BaseInterface [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af1b35c028fe0e61c30385aba36fa6372.html#af1b35c028fe0e61c30385aba36fa6372) |
|  | |
| using | [InterfaceVersion](namespace_a_k_1_1_wwise_1_1_plugin_a7fa905741ba9846fd2f0c4bfa3fc416b.html#a7fa905741ba9846fd2f0c4bfa3fc416b) = decltype([BaseInterface::m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Type for the m\_version value in BaseInterface [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a7fa905741ba9846fd2f0c4bfa3fc416b.html#a7fa905741ba9846fd2f0c4bfa3fc416b) |
|  | |
| using | [CBaseInterface](namespace_a_k_1_1_wwise_1_1_plugin_a069641ed8537ba2dafcb828dfd5916a9.html#a069641ed8537ba2dafcb828dfd5916a9) = [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface.html) |
|  | Interface description and base class for every [Wwise](namespace_a_k_1_1_wwise.html) Authoring plug-in interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a069641ed8537ba2dafcb828dfd5916a9.html#a069641ed8537ba2dafcb828dfd5916a9) |
|  | |
| using | [CInterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_ade5620136ec8b9def6c7e410f3a794b6.html#ade5620136ec8b9def6c7e410f3a794b6) = ak\_wwise\_plugin\_interface\_ptr |
|  | |
| using | [CInterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_aca26b5c76f95d1a578548c56b0cf1ca5.html#aca26b5c76f95d1a578548c56b0cf1ca5) = [ak\_wwise\_plugin\_interface\_array\_item](structak__wwise__plugin__interface__array__item.html) |
|  | A single instantiatable plug-in interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aca26b5c76f95d1a578548c56b0cf1ca5.html#aca26b5c76f95d1a578548c56b0cf1ca5) |
|  | |
| using | [CPluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_ac61a45449001d6c3d457a50230db20b8.html#ac61a45449001d6c3d457a50230db20b8) = [ak\_wwise\_plugin\_info](structak__wwise__plugin__info.html) |
|  | |
| using | [CPluginContainer](namespace_a_k_1_1_wwise_1_1_plugin_acaeb7e0475ed47dda25a09fe722bb360.html#acaeb7e0475ed47dda25a09fe722bb360) = [ak\_wwise\_plugin\_container](structak__wwise__plugin__container.html) |
|  | Root interface allowing a logical unit (variable, library) to contain more than one interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_acaeb7e0475ed47dda25a09fe722bb360.html#acaeb7e0475ed47dda25a09fe722bb360) |
|  | |
| using | [CWidget](namespace_a_k_1_1_wwise_1_1_plugin_ab9cbb84129fb7bc4f1eeadea41680ea3.html#ab9cbb84129fb7bc4f1eeadea41680ea3) = [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) |
|  | |
| using | [BaseInterface](namespace_a_k_1_1_wwise_1_1_plugin_af12e29db650cd0c58e9880a64ff93b18.html#af12e29db650cd0c58e9880a64ff93b18) = [CBaseInterface](namespace_a_k_1_1_wwise_1_1_plugin_a069641ed8537ba2dafcb828dfd5916a9.html#a069641ed8537ba2dafcb828dfd5916a9) |
|  | Interface description and base class for every [Wwise](namespace_a_k_1_1_wwise.html) Authoring plug-in interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af12e29db650cd0c58e9880a64ff93b18.html#af12e29db650cd0c58e9880a64ff93b18) |
|  | |
| using | [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) = [CInterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_ade5620136ec8b9def6c7e410f3a794b6.html#ade5620136ec8b9def6c7e410f3a794b6) |
|  | |
| using | [InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) = [CInterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_aca26b5c76f95d1a578548c56b0cf1ca5.html#aca26b5c76f95d1a578548c56b0cf1ca5) |
|  | A single instantiatable plug-in interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) |
|  | |
| using | [PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823) = [CPluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_ac61a45449001d6c3d457a50230db20b8.html#ac61a45449001d6c3d457a50230db20b8) |
|  | |
| using | [PluginContainer](namespace_a_k_1_1_wwise_1_1_plugin_afa19c1aec7e87e47a7b3547a072713cc.html#afa19c1aec7e87e47a7b3547a072713cc) = [CPluginContainer](namespace_a_k_1_1_wwise_1_1_plugin_acaeb7e0475ed47dda25a09fe722bb360.html#acaeb7e0475ed47dda25a09fe722bb360) |
|  | Root interface allowing a logical unit (variable, library) to contain more than one interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_afa19c1aec7e87e47a7b3547a072713cc.html#afa19c1aec7e87e47a7b3547a072713cc) |
|  | |
| using | [Widget](namespace_a_k_1_1_wwise_1_1_plugin_a9474b576cd95a3316ae3c4bba7ae18da.html#a9474b576cd95a3316ae3c4bba7ae18da) = [CWidget](namespace_a_k_1_1_wwise_1_1_plugin_ab9cbb84129fb7bc4f1eeadea41680ea3.html#ab9cbb84129fb7bc4f1eeadea41680ea3) |
|  | |
| using | [CLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_acac65e4a746e5104e04b138a7889d3c5.html#acac65e4a746e5104e04b138a7889d3c5) = [V1::CLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_aaa3fe7d7e70babc8d8aa9e0b88171ae6.html#aaa3fe7d7e70babc8d8aa9e0b88171ae6) |
|  | Latest version of the C LinkBackend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_acac65e4a746e5104e04b138a7889d3c5.html#acac65e4a746e5104e04b138a7889d3c5) |
|  | |
| using | [LinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_a3b9372eb28f4ed69d52c8b253b7542fd.html#a3b9372eb28f4ed69d52c8b253b7542fd) = [V1::LinkBackend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend.html) |
|  | Latest version of the C++ LinkBackend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a3b9372eb28f4ed69d52c8b253b7542fd.html#a3b9372eb28f4ed69d52c8b253b7542fd) |
|  | |
| using | [RequestLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_a4d4fbbc7cf09da60c669ce79799feba7.html#a4d4fbbc7cf09da60c669ce79799feba7) = [V1::RequestLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a11cb14ccd572dab75f29946408d5c381.html#a11cb14ccd572dab75f29946408d5c381) |
|  | Latest version of the requested C++ LinkBackend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4d4fbbc7cf09da60c669ce79799feba7.html#a4d4fbbc7cf09da60c669ce79799feba7) |
|  | |
| using | [CLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_aff9067bc56d00cc3f5362d072df8337b.html#aff9067bc56d00cc3f5362d072df8337b) = [V1::CLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ae46b0c1760947987e45c7c736fafbc57.html#ae46b0c1760947987e45c7c736fafbc57) |
|  | Latest version of the C LinkFrontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aff9067bc56d00cc3f5362d072df8337b.html#aff9067bc56d00cc3f5362d072df8337b) |
|  | |
| using | [LinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_a54cf853c2d54b39672aa929f71b0c0c3.html#a54cf853c2d54b39672aa929f71b0c0c3) = [V1::LinkFrontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend.html) |
|  | Latest version of the C++ LinkFrontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a54cf853c2d54b39672aa929f71b0c0c3.html#a54cf853c2d54b39672aa929f71b0c0c3) |
|  | |
| using | [RequestLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_ae784aa1d2e816b127f160a83410ffed8.html#ae784aa1d2e816b127f160a83410ffed8) = [V1::RequestLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a7d7050323515e05e75e34c71aaa8c3ae.html#a7d7050323515e05e75e34c71aaa8c3ae) |
|  | Latest version of the requested C++ LinkFrontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ae784aa1d2e816b127f160a83410ffed8.html#ae784aa1d2e816b127f160a83410ffed8) |
|  | |
| using | [CPropertyDisplayName](namespace_a_k_1_1_wwise_1_1_plugin_a874928bdb5e2c0fccdf1e0c50c1041f3.html#a874928bdb5e2c0fccdf1e0c50c1041f3) = [V1::CPropertyDisplayName](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_aee3bc6e9d3c6b81eb81096cadcb95a50.html#aee3bc6e9d3c6b81eb81096cadcb95a50) |
|  | Latest version of the C PropertyDisplayName interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a874928bdb5e2c0fccdf1e0c50c1041f3.html#a874928bdb5e2c0fccdf1e0c50c1041f3) |
|  | |
| using | [PropertyDisplayName](namespace_a_k_1_1_wwise_1_1_plugin_a6f10eb912f168dc570304ae3ee97ec6f.html#a6f10eb912f168dc570304ae3ee97ec6f) = [V1::PropertyDisplayName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name.html) |
|  | Latest version of the C++ PropertyDisplayName interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a6f10eb912f168dc570304ae3ee97ec6f.html#a6f10eb912f168dc570304ae3ee97ec6f) |
|  | |
| using | [CSinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_a8f050047725e6e92dac6a425db59301b.html#a8f050047725e6e92dac6a425db59301b) = [V1::CSinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a52aaccf63c00774a69e2a66a10163c9a.html#a52aaccf63c00774a69e2a66a10163c9a) |
|  | Latest version of the C SinkDevices interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a8f050047725e6e92dac6a425db59301b.html#a8f050047725e6e92dac6a425db59301b) |
|  | |
| using | [SinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_afd1d6878bfb9cc5c27a1741a7a9cd5d1.html#afd1d6878bfb9cc5c27a1741a7a9cd5d1) = [V1::SinkDevices](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices.html) |
|  | Latest version of the C++ SinkDevices interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_afd1d6878bfb9cc5c27a1741a7a9cd5d1.html#afd1d6878bfb9cc5c27a1741a7a9cd5d1) |
|  | |
| using | [CSource](namespace_a_k_1_1_wwise_1_1_plugin_a38b3d2f1d2482266ceb25c024375134c.html#a38b3d2f1d2482266ceb25c024375134c) = [V1::CSource](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a348aca37a6ae52b1c250d85ad45261d4.html#a348aca37a6ae52b1c250d85ad45261d4) |
|  | Latest version of the C Source interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a38b3d2f1d2482266ceb25c024375134c.html#a38b3d2f1d2482266ceb25c024375134c) |
|  | |
| using | [Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af) = [V1::Source](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source.html) |
|  | Latest version of the C++ Source interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af) |
|  | |
| using | [CTestService](namespace_a_k_1_1_wwise_1_1_plugin_a153b1d2e36ab2eb663b0830baf3b1d72.html#a153b1d2e36ab2eb663b0830baf3b1d72) = [V2::CTestService](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a0e1b0deb15b99022916424617bb4cd25.html#a0e1b0deb15b99022916424617bb4cd25) |
|  | Latest version of the C TestService interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a153b1d2e36ab2eb663b0830baf3b1d72.html#a153b1d2e36ab2eb663b0830baf3b1d72) |
|  | |
| using | [TestService](namespace_a_k_1_1_wwise_1_1_plugin_a49755cf687541087df2007b0303785de.html#a49755cf687541087df2007b0303785de) = [V2::TestService](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service.html) |
|  | Latest version of the C++ TestService interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a49755cf687541087df2007b0303785de.html#a49755cf687541087df2007b0303785de) |
|  | |
| using | [RequestTestService](namespace_a_k_1_1_wwise_1_1_plugin_a37bfa715acab11a6e0025f7c36a47ea6.html#a37bfa715acab11a6e0025f7c36a47ea6) = [V2::RequestTestService](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a144ede7e4897699ff8003e781d7f5e77.html#a144ede7e4897699ff8003e781d7f5e77) |
|  | Latest version of the requested C++ TestService interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a37bfa715acab11a6e0025f7c36a47ea6.html#a37bfa715acab11a6e0025f7c36a47ea6) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [LicenseType](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) { [LicenseType\_Trial](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eba0fde948d3400bb26cd990ddefa70c77e) = 1, [LicenseType\_Purchased](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eba15f3c33f220668c5a63d7245af208453), [LicenseType\_Academic](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eba675553ed9581a261b6cd2028bacd8765) } |
|  | License type. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) |
|  | |
| enum | [LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) { [LicenseStatus\_Unlicensed](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4a8c8e1cff83b5e9cc5530fa23d7960ef1), [LicenseStatus\_Expired](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4a18ce8e3a9a59b5ad2225ccfc11619426), [LicenseStatus\_Valid](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4aa086b65bb2c637bdb40c1fe2f221323b), [LicenseStatus\_Incompatible](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4a1388a62f60f5e74c0a378c8d8dbf6084) } |
|  | License status. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) |
|  | |
| enum | [NotifyInnerObjectOperation](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987) { [InnerObjectAdded](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987aaa6143b3eef559abe9343de72a8d8aae), [InnerObjectRemoved](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987ae45d4ed0bf48bc0b4bd0c9b7c6b1075e) } |
|  | Type of operation for the NotifyInnerObjectAddedRemoved function. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987) |
|  | |
| enum | [AudioFileChannel](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bd) {     [Channel\_mono](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bdad8a49f18aa2494a325962d8e61490eb9) = 0, [Channel\_stereo](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bda9011abe7c385ca940570417bfc6b693c) = 1, [Channel\_mono\_drop](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bdab4e8b33959e6c90b5b367f6186e295a3) = 2, [Channel\_stereo\_drop](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bda965d9a650d2b3dbab8d3f938df25ff66) = 3,     [Channel\_as\_input](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bdae7e5b4dced0ca81802b11356c9fb6232) = 4, [Channel\_mono\_drop\_right](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bda8f4b646bf486d9881566725bc596258a) = 5, [Channel\_stereo\_balance](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bda7b25cc13404f2390bbc8cbb99a8cfab0) = 6   } |
|  | Import channel configuration options. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a3d591eb9b778d69327f6696fdf6a63bd.html#a3d591eb9b778d69327f6696fdf6a63bd) |
|  | |
| enum | [Severity](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67ed) {     [Severity\_Success](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67eda154bdeafd831a9c2856c3c797a37d1f0) = -1, [Severity\_Message](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67eda8985c15e804661fa6ca4fce0873d058b), [Severity\_Warning](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67eda35f7fb0c5c0a59246ed922eb6af25794), [Severity\_Error](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67edad6614394580b0bd272920538d93652f4),     [Severity\_FatalError](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67eda88ae24bc50f05715c7bcd50e4d8e998d)   } |
|  | Log message severity. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67ed) |
|  | |
| enum | [eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) { [SettingsDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da70f74e61c5e7bef5d95559c73c9978cc), [ContentsEditorDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034da6d085e723d1240d119005b403573dfb5) } |
|  | |
| enum | [ConversionResult](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3) { [ConversionSuccess](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3a292220d538f5f5381f6f0514c782059f) = 0, [ConversionWarning](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3a0ec71d22a31f1cd710e9521200e0d1f2) = 1, [ConversionFailed](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3a067c828fdfd88765697e4914fa192efc) = 2 } |
|  | Conversion error code. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_af0fc7e36e72cee4b416aecef62580074.html#af0fc7e36e72cee4b416aecef62580074) ([AudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_a989b8417cedde33d928b90171491fcc5.html#a989b8417cedde33d928b90171491fcc5)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a6323c7c48b3e596a558fe5dfb0f74612.html#a6323c7c48b3e596a558fe5dfb0f74612) ([AudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_a989b8417cedde33d928b90171491fcc5.html#a989b8417cedde33d928b90171491fcc5)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_aa4b2c7dcf92adb095fb6a83278a3c1fb.html#aa4b2c7dcf92adb095fb6a83278a3c1fb) ([CustomData](namespace_a_k_1_1_wwise_1_1_plugin_ac1f7b957043934f47d294ecd2d71d0ca.html#ac1f7b957043934f47d294ecd2d71d0ca)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ac14b35b70e189aa7fdce95fea8684ca0.html#ac14b35b70e189aa7fdce95fea8684ca0) ([CustomData](namespace_a_k_1_1_wwise_1_1_plugin_ac1f7b957043934f47d294ecd2d71d0ca.html#ac1f7b957043934f47d294ecd2d71d0ca)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a81218c5a455aab7138406ad0a566718d.html#a81218c5a455aab7138406ad0a566718d) ([FirstTimeCreationMessage](namespace_a_k_1_1_wwise_1_1_plugin_a1120c7a177977ca71bdb7e5190489478.html#a1120c7a177977ca71bdb7e5190489478)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ad109981b5ef8a531fdd10dadc281e4d4.html#ad109981b5ef8a531fdd10dadc281e4d4) ([FirstTimeCreationMessage](namespace_a_k_1_1_wwise_1_1_plugin_a1120c7a177977ca71bdb7e5190489478.html#a1120c7a177977ca71bdb7e5190489478)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a27dc9d787fc7d362febc033146124b1a.html#a27dc9d787fc7d362febc033146124b1a) ([Frontend](namespace_a_k_1_1_wwise_1_1_plugin_ade7bf4707d85e10aae30ea0780abe527.html#ade7bf4707d85e10aae30ea0780abe527)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a91c243b3733347886fb8b3c2e4d974f1.html#a91c243b3733347886fb8b3c2e4d974f1) ([Frontend](namespace_a_k_1_1_wwise_1_1_plugin_ade7bf4707d85e10aae30ea0780abe527.html#ade7bf4707d85e10aae30ea0780abe527)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a60ee146ea530ccf391bdad675091f24d.html#a60ee146ea530ccf391bdad675091f24d) ([GUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_a5d74c88aa83c4e608fb75d1ac5555c9b.html#a5d74c88aa83c4e608fb75d1ac5555c9b)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a4b75e53ecef29425a5b033bc257e7082.html#a4b75e53ecef29425a5b033bc257e7082) ([GUIWindows](namespace_a_k_1_1_wwise_1_1_plugin_a5d74c88aa83c4e608fb75d1ac5555c9b.html#a5d74c88aa83c4e608fb75d1ac5555c9b)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ae0968ed5f70b5d9ad77150d7149f3d40.html#ae0968ed5f70b5d9ad77150d7149f3d40) ([Host](namespace_a_k_1_1_wwise_1_1_plugin_af6f9dc5d367c3383c37f96fe9e1b943f.html#af6f9dc5d367c3383c37f96fe9e1b943f)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a0014bc14ffa048fa75715061da406527.html#a0014bc14ffa048fa75715061da406527) ([Host](namespace_a_k_1_1_wwise_1_1_plugin_af6f9dc5d367c3383c37f96fe9e1b943f.html#af6f9dc5d367c3383c37f96fe9e1b943f)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a0a7784a13a51940a70f54854680ffb9a.html#a0a7784a13a51940a70f54854680ffb9a) ([DataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a32526a23215a4452f561220b527e12f8.html#a32526a23215a4452f561220b527e12f8)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ac1c1a60136371be582ba5e187f7ee675.html#ac1c1a60136371be582ba5e187f7ee675) ([DataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a32526a23215a4452f561220b527e12f8.html#a32526a23215a4452f561220b527e12f8)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a673a63aed65f792e4a29546d85b723ad.html#a673a63aed65f792e4a29546d85b723ad) ([FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a3e2415c2500d0ce4cd77034397be568e.html#a3e2415c2500d0ce4cd77034397be568e) ([FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a96f3b71d458c24f10227c8e2fc9a0b49.html#a96f3b71d458c24f10227c8e2fc9a0b49) ([ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a0325d70f4523c31f1b4f5dc8acdf3e2b.html#a0325d70f4523c31f1b4f5dc8acdf3e2b)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_af00a7debde2d2e2f857d567c1a9da843.html#af00a7debde2d2e2f857d567c1a9da843) ([ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a0325d70f4523c31f1b4f5dc8acdf3e2b.html#a0325d70f4523c31f1b4f5dc8acdf3e2b)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_aebca6e7ac797d63f22d3895d81da5260.html#aebca6e7ac797d63f22d3895d81da5260) ([Notifications::ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ad0a911acd3094f2ebc4ba43d1421c16d.html#ad0a911acd3094f2ebc4ba43d1421c16d)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a346b0c5c1520ea8c6f01c38357ba7fca.html#a346b0c5c1520ea8c6f01c38357ba7fca) ([Notifications::ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ad0a911acd3094f2ebc4ba43d1421c16d.html#ad0a911acd3094f2ebc4ba43d1421c16d)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ad2eee5be97fa2bc4a8fb3af43eee867a.html#ad2eee5be97fa2bc4a8fb3af43eee867a) ([ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_aa1a4c71b6a4959d8e06f9e3cc976c749.html#aa1a4c71b6a4959d8e06f9e3cc976c749)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ab53d90190847b24b30f0c2fef6d36080.html#ab53d90190847b24b30f0c2fef6d36080) ([ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_aa1a4c71b6a4959d8e06f9e3cc976c749.html#aa1a4c71b6a4959d8e06f9e3cc976c749)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_aff7d0fdb394787aa869eeedd82b22bcd.html#aff7d0fdb394787aa869eeedd82b22bcd) ([Notifications::ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ac1426dcd81fe89e4e0d7d40abd92eb88.html#ac1426dcd81fe89e4e0d7d40abd92eb88)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a1491ed0e88c4ec9dac22da4b27bb0279.html#a1491ed0e88c4ec9dac22da4b27bb0279) ([Notifications::ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ac1426dcd81fe89e4e0d7d40abd92eb88.html#ac1426dcd81fe89e4e0d7d40abd92eb88)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_abb2cf51a8149e8b87c3176e0d6948df5.html#abb2cf51a8149e8b87c3176e0d6948df5) ([PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a86cd47ff2861e2907081e1efd2485e13.html#a86cd47ff2861e2907081e1efd2485e13) ([PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ac83b7f21da2872e6ec16079f4c5d3e0e.html#ac83b7f21da2872e6ec16079f4c5d3e0e) ([ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_aa9c66805a7050040225bb144c6be8d06.html#aa9c66805a7050040225bb144c6be8d06)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a14f5142bd4cf5ca1badadcd692a49f12.html#a14f5142bd4cf5ca1badadcd692a49f12) ([Notifications::ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ae433979cbee5cd9d8ca01fe22da6b377.html#ae433979cbee5cd9d8ca01fe22da6b377)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a5b3707f2b2686106b16b1fa472228562.html#a5b3707f2b2686106b16b1fa472228562) ([Notifications::ReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ae433979cbee5cd9d8ca01fe22da6b377.html#ae433979cbee5cd9d8ca01fe22da6b377)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a3131077b4a41bd0ddbed2fb17f0108e9.html#a3131077b4a41bd0ddbed2fb17f0108e9) ([BaseUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_a106b6fb5a0b6171d250ccbb5059e4961.html#a106b6fb5a0b6171d250ccbb5059e4961)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_acc431a02e3a48459ec26540fc147f79a.html#acc431a02e3a48459ec26540fc147f79a) ([UndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_aa3ab9f1d6ab2fa806a700629b7b77e14.html#aa3ab9f1d6ab2fa806a700629b7b77e14) ([BaseUndoEvent](namespace_a_k_1_1_wwise_1_1_plugin_a106b6fb5a0b6171d250ccbb5059e4961.html#a106b6fb5a0b6171d250ccbb5059e4961)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ace96f8f301cbddb96750ae6535792fe7.html#ace96f8f301cbddb96750ae6535792fe7) ([UndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a8e307c590578e6fb70510fef57545ba3.html#a8e307c590578e6fb70510fef57545ba3) ([XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_aedb0f5b1832f94f67b756e4af140cca7.html#aedb0f5b1832f94f67b756e4af140cca7) ([XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_aa34006f329cf976481aefb5f3d4db338.html#aa34006f329cf976481aefb5f3d4db338) ([License](namespace_a_k_1_1_wwise_1_1_plugin_a44e186a822b15e2230c95b695b01c101.html#a44e186a822b15e2230c95b695b01c101)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a94d6f011e8790b420a14fac03d154468.html#a94d6f011e8790b420a14fac03d154468) ([License](namespace_a_k_1_1_wwise_1_1_plugin_a44e186a822b15e2230c95b695b01c101.html#a44e186a822b15e2230c95b695b01c101)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a4a5307fc7fed7f62ba82803278776355.html#a4a5307fc7fed7f62ba82803278776355) ([MediaConverter](namespace_a_k_1_1_wwise_1_1_plugin_aca00f70c566ab8b103a983d07890f430.html#aca00f70c566ab8b103a983d07890f430)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a81949de0e066e835725453496d91f583.html#a81949de0e066e835725453496d91f583) ([MediaConverter](namespace_a_k_1_1_wwise_1_1_plugin_aca00f70c566ab8b103a983d07890f430.html#aca00f70c566ab8b103a983d07890f430)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ae3dce9779d615c919ba9d4bc1b356444.html#ae3dce9779d615c919ba9d4bc1b356444) ([Notifications::Monitor](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a3693c119618107df7c86de8a4a887320.html#a3693c119618107df7c86de8a4a887320)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a58b2c038aa942d74d243075933a24571.html#a58b2c038aa942d74d243075933a24571) ([Notifications::Monitor](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a3693c119618107df7c86de8a4a887320.html#a3693c119618107df7c86de8a4a887320)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ad4e9968230f88b574a0e597384cc87fc.html#ad4e9968230f88b574a0e597384cc87fc) ([LinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_a3b9372eb28f4ed69d52c8b253b7542fd.html#a3b9372eb28f4ed69d52c8b253b7542fd)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_af187e822bc5afe666401ec3a6f0f3f66.html#af187e822bc5afe666401ec3a6f0f3f66) ([LinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_a3b9372eb28f4ed69d52c8b253b7542fd.html#a3b9372eb28f4ed69d52c8b253b7542fd)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ad0c8bcbead1331781fa72bb8a869626b.html#ad0c8bcbead1331781fa72bb8a869626b) ([LinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_a54cf853c2d54b39672aa929f71b0c0c3.html#a54cf853c2d54b39672aa929f71b0c0c3)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a8f2607f76e734a1b740ae553afb70d21.html#a8f2607f76e734a1b740ae553afb70d21) ([LinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_a54cf853c2d54b39672aa929f71b0c0c3.html#a54cf853c2d54b39672aa929f71b0c0c3)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ab95897d57921201fca57bb3d49bd3a4f.html#ab95897d57921201fca57bb3d49bd3a4f) ([PropertyDisplayName](namespace_a_k_1_1_wwise_1_1_plugin_a6f10eb912f168dc570304ae3ee97ec6f.html#a6f10eb912f168dc570304ae3ee97ec6f)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a76d46caf648ca01da735fb573ae63f00.html#a76d46caf648ca01da735fb573ae63f00) ([PropertyDisplayName](namespace_a_k_1_1_wwise_1_1_plugin_a6f10eb912f168dc570304ae3ee97ec6f.html#a6f10eb912f168dc570304ae3ee97ec6f)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a39373dae3c76178133d93dde57058299.html#a39373dae3c76178133d93dde57058299) ([SinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_afd1d6878bfb9cc5c27a1741a7a9cd5d1.html#afd1d6878bfb9cc5c27a1741a7a9cd5d1)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a20d33cd469f7ec76283f884df02779eb.html#a20d33cd469f7ec76283f884df02779eb) ([SinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_afd1d6878bfb9cc5c27a1741a7a9cd5d1.html#afd1d6878bfb9cc5c27a1741a7a9cd5d1)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ab1c3fdbee20d7c500864d497a485ddd3.html#ab1c3fdbee20d7c500864d497a485ddd3) ([Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ad743420fa3f22b37ac4fdb363c7e5ca1.html#ad743420fa3f22b37ac4fdb363c7e5ca1) ([Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a474a7d81fd6e81f7414806a9a6e114b3.html#a474a7d81fd6e81f7414806a9a6e114b3) ([TestService](namespace_a_k_1_1_wwise_1_1_plugin_a49755cf687541087df2007b0303785de.html#a49755cf687541087df2007b0303785de)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ae5f0fd9f38b858a04593ee2d4474227f.html#ae5f0fd9f38b858a04593ee2d4474227f) ([TestService](namespace_a_k_1_1_wwise_1_1_plugin_a49755cf687541087df2007b0303785de.html#a49755cf687541087df2007b0303785de)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ab8aebd300ad4e0655eeacf4af0ee5ab2.html#ab8aebd300ad4e0655eeacf4af0ee5ab2) ([V1::Host](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a9d626a275c527c46df80b121bcb34187.html#a9d626a275c527c46df80b121bcb34187)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a90773f41f32b15879c680faf4c9727fa.html#a90773f41f32b15879c680faf4c9727fa) ([Notifications::Host](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a6dff5e61f3799bce1119112cfc8da5d2.html#a6dff5e61f3799bce1119112cfc8da5d2)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_afaedc58d039beb0d0b02f1c4241ebfeb.html#afaedc58d039beb0d0b02f1c4241ebfeb) ([Notifications::Host](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a6dff5e61f3799bce1119112cfc8da5d2.html#a6dff5e61f3799bce1119112cfc8da5d2)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_adb5842e5c4c9a1e04a53e64c8f6a14e3.html#adb5842e5c4c9a1e04a53e64c8f6a14e3) ([V1::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ab5503ef97167a06c2b7d7be5c043d081.html#ab5503ef97167a06c2b7d7be5c043d081)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a7737ab85f831030bbff061276168fd6f.html#a7737ab85f831030bbff061276168fd6f) ([Notifications::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ac1ebce6cd84c63ffb93e086d46cbd7f8.html#ac1ebce6cd84c63ffb93e086d46cbd7f8)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a1a3fd520310dbed80d8c6fc0bc1c639b.html#a1a3fd520310dbed80d8c6fc0bc1c639b) ([Notifications::PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_ac1ebce6cd84c63ffb93e086d46cbd7f8.html#ac1ebce6cd84c63ffb93e086d46cbd7f8)) |
|  | |
|  | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_af9f172a87e0a52a87242fcb64fc659a5.html#af9f172a87e0a52a87242fcb64fc659a5) ([V1::TestService](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service.html)) |
|  | |