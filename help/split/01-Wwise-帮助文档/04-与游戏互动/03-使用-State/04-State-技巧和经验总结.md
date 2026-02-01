# State 技巧和经验总结

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 State](00-使用-State.md) > State 技巧和经验总结

## State 技巧和经验总结

使用 State（状态）时，最好仔细阅读以下各节，其中的一系列技巧和经验总结可以帮您更好地管理 State 在研发中的使用。

### State properties and CPU and memory usage

在不同平台上，Wwise 中的有些相对属性（如音高）可能会对性能造成影响。Wwise 中管理音高的机制基于采样率。调整对象音高时须对文件重新采样，因此会提高 CPU 占用。

---