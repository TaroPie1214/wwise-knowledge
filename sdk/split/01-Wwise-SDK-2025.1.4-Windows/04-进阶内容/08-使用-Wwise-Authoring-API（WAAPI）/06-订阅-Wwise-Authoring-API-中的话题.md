# 订阅 Wwise Authoring API 中的话题

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

订阅 Wwise Authoring API 中的话题

# 概述

With the Wwise Authoring API, you can call remote procedures (RPC), and can also subscribe to topics and be notified when a topic is published in Wwise (Pub/Sub). You could, therefore, synchronize data between the WAAPI client and the Wwise process or, for example, be informed when the selection changes in Wwise.

To subscribe to topics, you must use the Web Application Messaging Protocol (WAMP). The details vary by language and library. For examples, see the following documentation topics:

- [Python (Waapi-Client) – 订阅](waapi_client_python_subscription.html)
- [C# WaapiClient - WAMP](wamp_cs.html)

When subscribing to a topic, the specified callback is executed whenever the topic is published. Some of the topics support return options you can use to control the content that is passed in the callback, which avoids unnecessary queries.

For example, someone could subscribe to the [ak.wwise.core.object.nameChanged](ak_wwise_core_object_namechanged.html) topic and provide the following options:

{

"return": ["id", "name", "path"]

}

Every time a Wwise object name changes, the notification is sent to the subscriber with the **id**, **name** and **path** of the object.

|  |  |
| --- | --- |
|  | **备注:** Subscriptions are automatically revoked when the project is closed. 不过，涉及工程事件的主题支持在工程加载过程中订阅。The following topics are exempted topics: [ak.wwise.core.project.loaded](ak_wwise_core_project_loaded.html), [ak.wwise.core.project.preClosed](ak_wwise_core_project_preclosed.html), and [ak.wwise.core.project.postClosed](ak_wwise_core_project_postclosed.html). |

See [返回选项](waapi_query.html#waapi_query_return) for more information about the return statement, and [Wwise Authoring API Reference](waapi_index.html) for more information about the topics.

# Subscribing to Structure Changes

In Wwise projects, objects are related to one another in different ways:

- Objects are organized in a tree structure visible in the Project Explorer, the roots of which correspond to different object types. For example, Containers is one root in the overall object tree, and the objects within it each have a parent and might have children.
- Objects can also have ownership relationships with other objects. Ownership is not visible in the Project Explorer, but instead through properties in the Property Editor. For example, the owner of a Custom Attenuation is the object to which you apply the attenuation.
- ShareSets can have multiple references to other objects, but these references do not reflect ownership or parent/child relationships. Instead, the ShareSets tab in the Project Explorer displays the ShareSet tree structure. Ownership and parent/child relationships are distinct types of relationship: an object can have an owner or a parent but not both.

After you retrieve the tree structure, you can subscribe to [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) to synchronize any changes to object ownership or object location in the tree structure. Subscribing to this topic provides notifications for the following events:

- **create:** An object is created.
- **delete:** An object is deleted.
- **nameChange:** An object's name changes, which occurs when an object is renamed or created.
- **parentChange:** The object's parent changes, which occurs when an object is created, deleted, or moved within the hierarchy.
- **ownerChange:** The object's owner changes, typically when an object is created or deleted.

The changes sent by `ak.wwise.core.object.structureChanged` are grouped into batches by Undo events. Wwise automatically collapses redundant information, and presents a summary of all changes made within the last Undo event in the project. For instance, when copying and pasting multiple objects in the project, multiple changes, such as `create`, `nameChange`, and `parentChange` are grouped together.

|  |  |
| --- | --- |
|  | **备注:** Use [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) instead of the following topics:   - [ak.wwise.core.object.nameChanged](ak_wwise_core_object_namechanged.html) - [ak.wwise.core.object.childAdded](ak_wwise_core_object_childadded.html) - [ak.wwise.core.object.childRemoved](ak_wwise_core_object_childremoved.html) - [ak.wwise.core.object.created](ak_wwise_core_object_created.html) - [ak.wwise.core.object.postDeleted](ak_wwise_core_object_postdeleted.html) - [ak.wwise.core.object.preDeleted](ak_wwise_core_object_predeleted.html)   The [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) topic replaces the topics listed above, and provides more predictable and stable behavior. |