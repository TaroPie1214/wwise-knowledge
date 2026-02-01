# FrontendModel

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [FrontendModel](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::FrontendModel类 参考

Interface used to interact with the frontend model.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model.html#details)

`#include <HostFrontendModel.h>`

类 AK.Wwise::Plugin::V1::FrontendModel 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a2654f823e08ec7a0c3a27945557ce2dc.html#a2654f823e08ec7a0c3a27945557ce2dcaf8c068f3f69e3756a068971bdf7671f3) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_FRONTEND\_MODEL } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a2654f823e08ec7a0c3a27945557ce2dc.html#a2654f823e08ec7a0c3a27945557ce2dc) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a9b660f9a6de426ba9e4fe4905e7730a0.html#a9b660f9a6de426ba9e4fe4905e7730a0a6981865908fba3949cf69f7d7c0075c1) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a9b660f9a6de426ba9e4fe4905e7730a0.html#a9b660f9a6de426ba9e4fe4905e7730a0) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a635cfc453bb42d3f67425e12fd16c73e.html#a635cfc453bb42d3f67425e12fd16c73e) = [CHostFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a427443c428bc8db3bcdda5fff6a5fe4a.html#a427443c428bc8db3bcdda5fff6a5fe4a) |
|  | |
| using | [GenericCallback](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a2dc493bb044bd8785ba87f68faa6f315.html#a2dc493bb044bd8785ba87f68faa6f315) = void(\*)() |
|  | |
| using | [ForEachCallback](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a4c9df33eaac8f25998bb8ec615e13ec8.html#a4c9df33eaac8f25998bb8ec615e13ec8) = void(\*)([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*, void \*) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHostFrontendModel >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostFrontendModel >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHostFrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_af24a3f1547c57009739461b422fb7a90.html#af24a3f1547c57009739461b422fb7a90) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| bool | [HasWidget](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a75d8e17c9bf4a28a33597ffac91a7ff9.html#a75d8e17c9bf4a28a33597ffac91a7ff9) (const char \*in\_absoluteId) |
|  | Checks if a specific widget exists. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a75d8e17c9bf4a28a33597ffac91a7ff9.html#a75d8e17c9bf4a28a33597ffac91a7ff9) |
|  | |
| [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \* | [GetParentWidget](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a78bfbc103ef2b914484633033561dbf2.html#a78bfbc103ef2b914484633033561dbf2) (const char \*in\_absoluteId) |
|  | Returns the parent widget of a given [Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html "Frontend plug-in API for Audio plug-ins.") Handle hierarchy. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a78bfbc103ef2b914484633033561dbf2.html#a78bfbc103ef2b914484633033561dbf2) |
|  | |
| [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \* | [GetRootWidget](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_aafd471e024827a0c10d2b6390682458b.html#aafd471e024827a0c10d2b6390682458b) () |
|  | Returns the main layout widget of a given [Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html "Frontend plug-in API for Audio plug-ins.") Handle hierarchy. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_aafd471e024827a0c10d2b6390682458b.html#aafd471e024827a0c10d2b6390682458b) |
|  | |
| [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \* | [GetWidget](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a6e2e4917ebe639508944bc7c5bbcee8b.html#a6e2e4917ebe639508944bc7c5bbcee8b) (const char \*in\_absoluteId) |
|  | Returns a specific widget of a given [Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html "Frontend plug-in API for Audio plug-ins.") Handle hierarchy. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a6e2e4917ebe639508944bc7c5bbcee8b.html#a6e2e4917ebe639508944bc7c5bbcee8b) |
|  | |
| const char \* | [GetWidgetID](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_aee3a4ba26185b219894f6587a11999f3.html#aee3a4ba26185b219894f6587a11999f3) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Gets the ID of a widget. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_aee3a4ba26185b219894f6587a11999f3.html#aee3a4ba26185b219894f6587a11999f3) |
|  | |
| const char \* | [GetWidgetType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a4fc26d34c41693b98d5b797fc12738bd.html#a4fc26d34c41693b98d5b797fc12738bd) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Gets the type ID of a widget. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a4fc26d34c41693b98d5b797fc12738bd.html#a4fc26d34c41693b98d5b797fc12738bd) |
|  | |
| bool | [IsWidgetContainer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a2edaeb1d1368b3d9ceced72c6e60428a.html#a2edaeb1d1368b3d9ceced72c6e60428a) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Checks if the widget can contain other widgets. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a2edaeb1d1368b3d9ceced72c6e60428a.html#a2edaeb1d1368b3d9ceced72c6e60428a) |
|  | |
| bool | [IsWidgetTopLevel](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_ae865549b760487399117ce16dd701783.html#ae865549b760487399117ce16dd701783) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Checks if the widget is top-level. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_ae865549b760487399117ce16dd701783.html#ae865549b760487399117ce16dd701783) |
|  | |
| bool | [IsWidgetVisible](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a5d7ff12aa094e0886e1a3db77a7bcad9.html#a5d7ff12aa094e0886e1a3db77a7bcad9) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Determines the visibility state of the given widget. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a5d7ff12aa094e0886e1a3db77a7bcad9.html#a5d7ff12aa094e0886e1a3db77a7bcad9) |
|  | |
| bool | [IsWidgetEnabled](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a5058b54b9061efde38b2d4b5d89f309d.html#a5058b54b9061efde38b2d4b5d89f309d) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Determines if a widget is enabled for mouse and keyboard input. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a5058b54b9061efde38b2d4b5d89f309d.html#a5058b54b9061efde38b2d4b5d89f309d) |
|  | |
| void | [EnableWidget](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a35d52582a50863a7b928dd88335ae895.html#a35d52582a50863a7b928dd88335ae895) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget, bool in\_enable) |
|  | Enables or disables mouse and keyboard input for the widget. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a35d52582a50863a7b928dd88335ae895.html#a35d52582a50863a7b928dd88335ae895) |
|  | |
| void | [ShowWidget](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a402a10f3adeb0c52cd4f1ddff6bd054e.html#a402a10f3adeb0c52cd4f1ddff6bd054e) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget, bool in\_show) |
|  | Sets the visibility state of the widget. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a402a10f3adeb0c52cd4f1ddff6bd054e.html#a402a10f3adeb0c52cd4f1ddff6bd054e) |
|  | |
| void | [SetWidgetFocus](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a7f3fc59b3325afc1daef54798a349271.html#a7f3fc59b3325afc1daef54798a349271) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Claims the input focus for the widget. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a7f3fc59b3325afc1daef54798a349271.html#a7f3fc59b3325afc1daef54798a349271) |
|  | |
| bool | [Connect](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a2561b9d053d07593815361e89610404c.html#a2561b9d053d07593815361e89610404c) ([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget, const char \*in\_name, [GenericCallback](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a2dc493bb044bd8785ba87f68faa6f315.html#a2dc493bb044bd8785ba87f68faa6f315) in\_handler, void \*in\_userData) |
|  | Connects a signal to a handler taking some user-defined data. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a2561b9d053d07593815361e89610404c.html#a2561b9d053d07593815361e89610404c) |
|  | |
| void | [ForEachChildren](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_ab0246bd409bf9f80817b492299d82342.html#ab0246bd409bf9f80817b492299d82342) (const char \*in\_absoluteId, [ForEachCallback](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_a4c9df33eaac8f25998bb8ec615e13ec8.html#a4c9df33eaac8f25998bb8ec615e13ec8) in\_handler, void \*in\_userData) |
|  | Applies a user-defined handler to every child of a container. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_model_ab0246bd409bf9f80817b492299d82342.html#ab0246bd409bf9f80817b492299d82342) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostFrontendModel >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

Interface used to interact with the frontend model.

The frontend model is the service in charge of building GUI views and managing the objects's lifetime. It takes the description of a view in the form of a WAFM file, creates the widget hierarchy, and stores the objects in a specific handle. The handle is shared to the user to allow interaction with the view's widgets.

在文件 [HostFrontendModel.h](_host_frontend_model_8h_source.html) 第 [267](_host_frontend_model_8h_source.html#l00267) 行定义.