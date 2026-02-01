# SDK 中所含库和头文件的概述

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

SDK 中所含库和头文件的概述

This topic describes some of the contents of the Wwise SDK. To install the SDK itself, select the SDK Package in the Audiokinetic Launcher when you install or modify Wwise. For more information, see [Installing Wwise and Its Components](https://www.audiokinetic.com/library/edge/?source=InstallGuide&id=installing_wwise_and_its_components).

# SDK 输入库 与分布式二进制文件

我们为 SDK 安装目录根文件夹下相应平台文件夹中的各个 [构建配置](goingfurther_builds.html) “构建配置”提供了集成 Wwise 声音引擎所需要的输入库。程序库目录结构定义如下：

- {Wwise SDK Dir}/{平台名称}/{配置名称}/lib，其中
  - {Wwise SDK Dir} 是 SDK 安装目录
  - {平台名称}是可用平台名称（x64、Mac、iOS……）之一。后缀可进一步限定目标 CPU 架构或编译器。
  - {配置名称} 是三个构建配置（Debug、Profile、Release）之一。注意，Windows 平台有三个其它配置（Debug\_StaticCRT、Profile\_StaticCRT、Release\_StaticCRT），这些配置使用静态 C 运行时库而不是动态库 。另外请注意 iOS 有以下构建配置（Debug-iphoneos、Debug-iphonesimulator、Profile-iphoneos、Profile-iphonesimulator、Release-iphoneos、Release-iphonesimulator）。tvOS 平台有以下构建配置（Debug-appletvos、Debug-appletvsimulator、Profile-appletvos、Profile-appletvsimulator、Release-appletvos、Release-appletvsimulator）。visionOS 平台有以下构建配置（Debug-xros、Debug-xrsimulator、Profile-xros、Profile-xrsimulator、Release-xros、Release-xrsimulator）。

请参阅 [构建配置](goingfurther_builds.html) 了解此 SDK 中所含各种库的描述。

# Include 文件

SDK 接口、类型、常量等的头文件位于 SDK 安装文件夹下的“include”文件夹中。子文件夹用于对相关文件分组。

您应该将"$(WWISESDK)\\include "添加到您项目的 include 目录下。然后您可以使用相对于“include”目录的路径加入文件。例如：

#include <[AK/SoundEngine/Common/AkSoundEngine.h](_ak_sound_engine_8h.html)>

#include <[AK/IBytes.h](_i_bytes_8h.html)>

|  |  |
| --- | --- |
|  | **备注:** 在 Mac 平台上，WWISESDK 变量没有设置。您需要在 XCode 项目的头搜索路径下添加 Wwise SDK “include/”文件夹。 |

此文档中的各个部分列出了当它们引入新实体时必须包含的头文件。

[AkSoundEngine.h](_ak_sound_engine_8h.html)

[IBytes.h](_i_bytes_8h.html)