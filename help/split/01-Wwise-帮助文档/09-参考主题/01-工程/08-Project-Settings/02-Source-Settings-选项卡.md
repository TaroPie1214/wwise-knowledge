# Source Settings 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Project Settings](00-Project-Settings.md) > Source Settings 选项卡

### Source Settings 选项卡

源设置。在 Source Settings 选项卡中，您定义工程的以下各项：

- 默认转码设置 ShareSet，用于新创建的对象。
- Sample Rate Automatic Detection（采样率自动检测）
- 音量阈值，由自动采样率检测使用

| 界面元素 | 描述 |
| --- | --- |
| **Default Conversion Settings（默认转码设置）** | |
| (ShareSet) | 将用作工程默认 Conversion Settings（转码设置）的 ShareSet 的名称。  在以下情况下，将使用默认 Conversion Settings：  创建新对象时。仅会在新对象为顶级父对象时使用默认 Conversion Settings。如果新对象是另一对象的子对象，它将继承父对象的 Conversion Settings。  为所有未分配 Conversion Settings 共享集的对象生成 SoundBank 时。 |
| (浏览) | 打开 Project Explorer - Browser（工程资源管理器 - 浏览器）。在此，可浏览并选择要用作工程默认 Conversion Settings 的 ShareSet。 |
| **Sample Rate Automatic Detection（采样率自动检测）** | |
| Auto Detect FFT Window Size | FFT 窗口大小。定义 FFT 算法使用的 Hanning 窗口的大小，以分析媒体文件的声波。  在从 Conversion Settings 对话框的 Sample Rate 列表中选择 Auto Low、Auto Medium 或 Auto High 选项时，Wwise 会使用 FFT 算法来为媒体文件自动检测适宜的采样率。  Default value: 512 |
| **Volume Thresholds（音量阈值）** | |
| Low quality | 定义相应截止音量阈值以识别用于确定给定媒体文件最佳采样率的频率。较高的阈值将导致转码处理中将使用较低品质的采样率。  低品质音量阈值用于归一化频谱的环境下。  在从 Conversion Settings 对话框的 Sample Rate 列表中选择 Auto Low 选项时，将使用低品质音量阈值。  Default value: -30  Range: -96.3 to 0 |
| Medium quality | 定义相应截止音量阈值以识别用于确定给定媒体文件最佳采样率的频率。较高的阈值将导致转码处理中将使用较低品质的采样率。  中等品质音量阈值用于归一化频谱的环境下。  在从 Conversion Settings 对话框的 Sample Rate 列表中选择 Auto Medium 选项时，将使用中品质音量阈值。  Default value: -40  Range: -96.3 to 0 |
| High quality | 定义相应截止音量阈值以识别用于确定给定媒体文件最佳采样率的频率。较高的阈值将导致转码处理中将使用较低品质的采样率。  高品质音量阈值用于归一化频谱的环境下。  在从 Conversion Settings 对话框的 Sample Rate 列表中选择 Auto High 选项时，将使用高品质音量阈值。  Default value: -50  Range: -96.3 to 0 |
|  | 确定。关闭 Project Settings 对话框并保存设置。 |
|  | 取消。关闭 Project Settings 对话框而不保存设置。 |

**相关主题**

- [“指定 Default Conversion Settings”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/02-定义工程的转码设置.md#specifying_default_conversion_settings "指定 Default Conversion Settings")
- [“定义 Sample Rate Automatic Detection 设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/02-定义工程的转码设置.md#defining_sample_rate_automatic_detection_settings "定义 Sample Rate Automatic Detection 设置")

---