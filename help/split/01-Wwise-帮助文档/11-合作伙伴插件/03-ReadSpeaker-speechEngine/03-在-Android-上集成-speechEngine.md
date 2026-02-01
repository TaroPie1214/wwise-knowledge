# 在 Android 上集成 speechEngine

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [合作伙伴插件](../00-合作伙伴插件.md) > [ReadSpeaker speechEngine](00-ReadSpeaker-speechEngine.md) > 在 Android 上集成 speechEngine

## 在 Android 上集成 speechEngine

### 链接

若要集成到应用中，必须链接 `libSpeechEngine` 模块。具体怎么做取决于所用配置和构建系统。

比如，您可以将以下代码添加到应用的 `Android.mk` 文件：

```
include $(CLEAR_VARS)
LOCAL_MODULE := libSpeechEngine
LOCAL_SRC_FILES := $(APP)/$(CONFIG)/bin/libSpeechEngine.so
include $(PREBUILT_SHARED_LIBRARY)
```

在必要时，可将 `libSpeechEngine` 模块作为动态库或共享库添加到配置中。

### 依赖项

speechEngine 模块必须根据所选语音加载与语言对应的动态库。比如，在选用 Adam 时，会加载 `vt_bre.so` (British English) 库。

这些库遵从 `vt_[lang].so` 命名规范，并且要与 `libSpeechEngine.so` 放在同一文件夹中（通常为 `jniLibs` 文件夹）。

在安装插件时，会将这些语音文件复制到 `$WWISEROOT/SDK/Android_{config}/{config}/libs` 中。

---