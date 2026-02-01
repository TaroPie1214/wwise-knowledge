# 了解 Selection Channel 和 Meter Instance

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [入门](../../00-入门.md) > [个性化您的工作空间](../00-个性化您的工作空间.md) > [处理视图](00-处理视图.md) > 了解 Selection Channel 和 Meter Instance

### 了解 Selection Channel 和 Meter Instance

您可以使用 Selection Channel（选定通道）来在多个视图之间同步所做选择。利用 Meter Instance（电平表实例），可在多个布局之间同步电平表。也就是说，在某个电平表视图中选择总线或 Audio Device（音频设备）时，会在同一实例的所有电平表视图中自动选择对应的总线或 Audio Device。

#### 使用 Selection Channel 来同步视图

您可以采用以下任一方式使用 Selection Channel 来同步视图：

- **In the Project Explorer and Event Viewer**（在工程资源管理器和事件查看器中）：在不同布局内有多个 Project Explorer 或 Event Viewer 实例时，有时可能需要将这些视图同步。若针对多个 Project Explorer 或 Event Viewer 实例选择了同一 Selection Channel，则某一视图实例中所作的选择或移动将自动应用于其他实例。比如，若将三个不同布局内的三个不同 Project Explorer 全部同步到 Selection Channel 1，并切换到其中一个 Project Explorer 中的 Game Syncs（游戏同步器）选项卡，则所有同步到该通道的 Project Explorer 视图也会自动切换到 Game Syncs 选项卡。

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | 同一布局内的多个 Project Explorer 或 Event Viewer 实例不能属于同一 Selection Channel。 |
- **In other views that include the Selection Channel icon in their title bar**（在标题栏中包含“选定通道”图标的其他视图中）：使用此选项来将视图与 Project Explorer 或 Event Viewer 的特定 Selection Channel 同步。也就是说，只要在该通道对应 Project Explorer 或 Event Viewer 内选中对象，就会在同步的视图中自动选中所述对象。

**在布局之间同步多个 Project Explorer 或 Event Viewer 实例：**

1. 在 Project Explorer（工程资源管理器）或 Event Viewer（事件查看器）的标题栏中，单击 Selection Channel（选定通道）图标。
2. 从快捷菜单中，选择以下任一选项：

   - **Pinned**（锁定）：禁止将视图与任何通道同步。
   - **Sync with Selection Channel 1**（与选定通道 1 同步）：将视图同步到通道 1。
   - **Sync with Selection Channel 2**（与选定通道 2 同步）：将视图同步到通道 2。
   - **Sync with Selection Channel 3**（与选定通道 3 同步）：将视图同步到通道 3。
   - **Sync with Selection Channel 4**（与选定通道 4 同步）：将视图同步到通道 4。
3. 若要在其他布局内同步 Project Explorer 和 Event Viewer，请切换布局并重复步骤 1-2。

**将其他视图同步到特定 Project Explorer 或 Event Viewer 通道：**

1. 在视图的标题栏中，单击 Selection Channel（选定通道）图标。
2. 从快捷菜单中，选择以下任一选项：

   - **Sync with Any Selection Channel**（与任意选定通道同步）：将视图同步到任意通道。
   - **Pinned**（锁定）：禁止将视图与任何通道同步。
   - **Sync with Selection Channel 1**（与选定通道 1 同步）：将视图同步到通道 1。
   - **Sync with Selection Channel 2**（与选定通道 2 同步）：将视图同步到通道 2。
   - **Sync with Selection Channel 3**（与选定通道 3 同步）：将视图同步到通道 3。
   - **Sync with Selection Channel 4**（与选定通道 4 同步）：将视图同步到通道 4。

在 Object Tab 或 Event Viewer 中选中对象时，会在同一 Selection Channel 的 Project Explorer 中自动将其选中。若要禁用这一自动选择操作，请清除 **Follow Object Selection**。

#### Using Meter Instances to sync Meters across layouts

共有三个专门用于电平测量的不同视图：Audio Device Meter（音频设备电平表）、Loudness Meter（响度电平表）和 Meter（电平表）。在布局内，最多可同时打开这些视图的四个实例（A、B、C 或 D）。不过，布局内相同类型的视图必须设为不同的实例。在每个实例中选择总线或 Audio Device 时，都会在各个布局的相同视图实例之间自动同步。在针对特定实例选择总线或 Audio Device 后，下次打开同一 Wwise 工程时还会恢复。

**同步两个 Meter 视图：**

1. 在 Wwise 菜单栏中，依次单击 **Views** > **Meter**（视图 > 电平表），然后选择以下任意一项：

   - **Meter - Instance A**
   - **Meter - Instance B**
   - **Meter - Instance C**
   - **Meter - Instance D**
2. 在打开的 Meter 视图中，选择所需总线或 Audio Device（音频设备）。
3. 切换到不同的布局，然后依次单击 **Views** > **Meter**（视图 > 电平表），并从列表中选择与步骤 1 中所选的相同电平表实例。

   在打开的 Meter 视图中，总线或 Audio Device 会与步骤 2 中所选的电平表实例自动匹配。后续对任一布局中所选总线或 Audio Device 做出的更改都会反映到另一布局中。

类似的操作同样适用于 Audio Device Meter 和 Loudness Meter。

**打开未同步/未锁定的电平表：**

1. 在 Wwise 菜单栏中，依次单击 **Views** > **Meter** > **Meter - New Pinned View**（视图 > 电平表 > 电平表 - 新的锁定视图）或按下 Ctrl+Shift+T。
2. 在打开的视图中，选择所需总线或 Audio Device（音频设备）。

   此电平表不会与其他电平表同步。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 您可以打开任意数量的锁定电平表。 |

类似的操作同样适用于 Audio Device Meter。除此之外，还可通过单击视图标题栏中的图钉或字母（A、B、C 或 D）来切换电平表视图实例。

---