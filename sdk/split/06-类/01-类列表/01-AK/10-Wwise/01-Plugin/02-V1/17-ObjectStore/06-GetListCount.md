# GetListCount

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [ObjectStore](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [CreatePropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a1a507782ef4fee515e91df6426c6fd88.html#a1a507782ef4fee515e91df6426c6fd88) | | [DeletePropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_aac799692bc78125ac4d2ef8c70b5997a.html#aac799692bc78125ac4d2ef8c70b5997a) | | [GetListCount](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a73ef145057358801fe7f40dfba7e50e9.html#a73ef145057358801fe7f40dfba7e50e9) | | [GetListName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a58fc861ef17b997430f6775b905dfc22.html#a58fc861ef17b997430f6775b905dfc22) | | [GetPropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a19d0d8fd9bf69c75a06203e92e7ee4bd.html#a19d0d8fd9bf69c75a06203e92e7ee4bd) | | [GetPropertySetCount](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a23765d008b043c66845c60ccdfc621b2.html#a23765d008b043c66845c60ccdfc621b2) | | [InsertPropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a23316a944101ac1a01d331fd6c187606.html#a23316a944101ac1a01d331fd6c187606) | | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_abc3a8b0601ec4e0856f2d78214c38ae4.html#abc3a8b0601ec4e0856f2d78214c38ae4) | | [RemovePropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a7bea99b254754de1c3bdc148e38762da.html#a7bea99b254754de1c3bdc148e38762da) | | [◆](#a73ef145057358801fe7f40dfba7e50e9)GetListCount() template<typename PropertySetT = AK::Wwise::Plugin::PropertySet>   |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | unsigned int [AK.Wwise::Plugin::V1::ObjectStore](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.html)< PropertySetT >::GetListCount | ( |  | ) | const | | inline |  Returns the number of inner property set lists to be used with GetListName.  返回  Number of property set lists, or 0 if there are none.  在文件 [HostObjectStore.h](_host_object_store_8h_source.html) 第 [570](_host_object_store_8h_source.html#l00570) 行定义.  引用了 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostObjectStore >::g\_cinterface](_plugin_info_generator_8h_source.html#l00089) , 以及 [ak\_wwise\_plugin\_host\_object\_store\_v1::GetListCount](_host_object_store_8h_source.html#l00251). |