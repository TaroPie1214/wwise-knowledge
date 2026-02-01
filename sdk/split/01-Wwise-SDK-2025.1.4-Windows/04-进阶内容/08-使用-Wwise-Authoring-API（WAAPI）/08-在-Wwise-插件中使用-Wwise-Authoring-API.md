# 在 Wwise 插件中使用 Wwise Authoring API

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

在 Wwise 插件中使用 Wwise Authoring API

# 调用远程程序

Wwise Authoring API 可以用来从 Wwise 插件内使用 `AK::Wwise::Plugin::Host::WaapiCall()` 的方法发出远程程序调用。 此方法由 Host 组件提供，可通过从 `AK::Wwise::Plugin::RequestHost` 继承来发送相应请求。

|  |  |
| --- | --- |
|  | **备注:** 对 `AK::Wwise::Plugin::Host::WaapiCall()` 方法的调用总是阻塞的。 |

提供了工具类，供调用者提供内存分配的策略。`AK::Wwise::Mallocator` 使用来自 C 库的函数（如 `malloc`、`free` 和 `realloc`）提供默认实现。不过，也可通过定义类来实现 `AK::IAkPluginMemAlloc`，以此轻松提供自定义策略。最终，封装类 `AK::Wwise::SafeAllocator` 被用于保证类型安全和自动内存管理。

示例：

#include <[AK/Tools/Common/AkAllocator.h](_ak_allocator_8h.html)>

#include <rapidjson/document.h>

// 为结果和错误使用默认分配策略

[AK::Wwise::Mallocator](class_a_k_1_1_wwise_1_1_mallocator.html) alloc;

[AK::Wwise::SafeAllocator<char>](class_a_k_1_1_wwise_1_1_safe_allocator.html) szResults(&alloc);

[AK::Wwise::SafeAllocator<char>](class_a_k_1_1_wwise_1_1_safe_allocator.html) szError(&alloc);

// 对 Wwise Authoring API 发出远程程序调用

m\_host.WaapiCall("ak.wwise.core.getInfo", NULL, NULL, alloc, szResults, szError);

if (!szError)

{

// Parse the results JSON string

[rapidjson::Document](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffafe099684193320746aae4bf5cd0258b7) results;

results.Parse(szResults);

// ...

}

#include <[AK/Tools/Common/AkAllocator.h](_ak_allocator_8h.html)>

#include <rapidjson/document.h>

#include <rapidjson/stringbuffer.h>

#include <rapidjson/writer.h>

// 为结果和错误使用默认分配策略

[AK::Wwise::Mallocator](class_a_k_1_1_wwise_1_1_mallocator.html) alloc;

[AK::Wwise::SafeAllocator<char>](class_a_k_1_1_wwise_1_1_safe_allocator.html) szResults(&alloc);

[AK::Wwise::SafeAllocator<char>](class_a_k_1_1_wwise_1_1_safe_allocator.html) szError(&alloc);

// 建立一个包含该程序参数的 JSON 对象

[rapidjson::Document](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffafe099684193320746aae4bf5cd0258b7) args;

args.SetObject();

args.AddMember("classId", 8192003, args.GetAllocator());

args.AddMember("property", "ModDepth", args.GetAllocator());

// 对 JSON 对象进行字符串化

rapidjson::StringBuffer buffer;

rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);

args.Accept(writer);

// 对 Wwise Authoring API 发出远程程序调用

m\_host.WaapiCall("ak.wwise.core.plugin.getProperty", buffer.GetString(), NULL, alloc, szResults, szError);

if (!szError)

{

// Parse the results JSON string

[rapidjson::Document](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffafe099684193320746aae4bf5cd0258b7) results;

results.Parse(szResults);

// ...

}

|  |  |
| --- | --- |
|  | **备注:** 这里用到的 RapidJSON 只是出于演示目的，并不是必须的库。 |

请参阅 [设计工具插件库格式](plugin_dll.html) 了解 Wwise plug-ins 的更多详情。

[AK.Wwise::Mallocator](class_a_k_1_1_wwise_1_1_mallocator.html)

**Definition:** [AkAllocator.h:47](_ak_allocator_8h_source.html#l00045)

[AK.Wwise::SafeAllocator](class_a_k_1_1_wwise_1_1_safe_allocator.html)

**Definition:** [AkAllocator.h:106](_ak_allocator_8h_source.html#l00105)

[AkAllocator.h](_ak_allocator_8h.html)

[AK.Wwise::Plugin::XmlNodeType::Document](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffafe099684193320746aae4bf5cd0258b7)

@ Document

**Definition:** [HostXml.h:64](_host_xml_8h_source.html#l00064)