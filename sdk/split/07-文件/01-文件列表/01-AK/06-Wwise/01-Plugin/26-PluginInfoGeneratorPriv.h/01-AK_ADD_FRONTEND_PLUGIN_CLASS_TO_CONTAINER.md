# AK_ADD_FRONTEND_PLUGIN_CLASS_TO_CONTAINER

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)
- [PluginInfoGeneratorPriv.h](_plugin_info_generator_priv_8h.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AK\_ADD\_FRONTEND\_PLUGIN\_CLASS\_TO\_CONTAINER](_plugin_info_generator_priv_8h_aa1a96f91771f45b44b65c7da26e14c8b.html#aa1a96f91771f45b44b65c7da26e14c8b) | | [AK\_ADD\_FRONTEND\_PLUGIN\_CLASSID\_TO\_CONTAINER](_plugin_info_generator_priv_8h_a2f60a565690ef631fec423828961aaff.html#a2f60a565690ef631fec423828961aaff) | | [◆](#aa1a96f91771f45b44b65c7da26e14c8b)AK\_ADD\_FRONTEND\_PLUGIN\_CLASS\_TO\_CONTAINER |  |  |  |  | | --- | --- | --- | --- | | #define AK\_ADD\_FRONTEND\_PLUGIN\_CLASS\_TO\_CONTAINER | ( |  | ContainerName, | |  |  |  | WwiseClassName, | |  |  |  | AudioEngineRegisteredName, | |  |  |  | TemplateName | |  | ) |  |  |  (C++) Adds a Wwise Authoring frontend plug-in and a Sound Engine plug-in to a plug-in container.  Creates a custom namespace with custom plug-in info, that contains the generated plug-in info structure. Then, statically points it to the next pointer for the container.  This uses the Sound Engine part to retrieve the plug-in information (Company id, Plug-in ID and Plug-in Type). It also adds up the Sound Engine's registration structure, so the host can initialize this part on first instantiation.  This uses the Frontend Model to build and manage the lifetime of the plug-in frontend's widgets.  参数  |  |  | | --- | --- | | ContainerName | Container name. | | WwiseClassName | Class name of the plug-in to add to the container. | | AudioEngineRegisteredName | Sound Engine's class name. | | TemplateName | Frontend Model's template name of the plug-in. |  在文件 [PluginInfoGeneratorPriv.h](_plugin_info_generator_priv_8h_source.html) 第 [75](_plugin_info_generator_priv_8h_source.html#l00075) 行定义. |