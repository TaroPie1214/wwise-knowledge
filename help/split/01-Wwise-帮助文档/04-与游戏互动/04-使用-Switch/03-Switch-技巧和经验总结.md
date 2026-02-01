# Switch 技巧和经验总结

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 Switch](00-使用-Switch.md) > Switch 技巧和经验总结

## Switch 技巧和经验总结

使用 Switch（切换开关）时最好能仔细阅读以下各节，其中的一系列技巧和经验总结可以帮您在整个音频开发过程中更好地管理 Switch。

### 重命名 Switch

更改 Switch 名称前，请检查 Switch 是如何集成到游戏中的。如果是用名称字符串集成的，则更名后将需要额外的编程才能使用。

### Assigning objects to more than one Switch Group

通常，对象仅可指定到一个 Switch Group。If, however, your game requires that an object is assigned to Switches in different Switch Groups, you can assign a second Switch Group at a higher level in the Busses or Containers hierarchies .

---