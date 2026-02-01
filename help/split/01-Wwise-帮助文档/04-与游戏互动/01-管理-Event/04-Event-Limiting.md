# Event Limiting

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [管理 Event](00-管理-Event.md) > Event Limiting

## Event Limiting

The Event Limiting properties of an Event allow you to limit the playback of Events by filtering Post Event commands received from the game.

### Limit

The Limit property sets the maximum number of concurrent Event playbacks for the same Event. When a Post Event command is received by the Sound Engine, the command will be discarded if the number of concurrent Events for this Event is reached.

|  |  |
| --- | --- |
| [备注] | 备注 |
| Setting a value of 0 instances (displayed as Infinite in the Event Editor) disables the Limit property. |

**To set the Limit property:**

1. In the Event Editor, click in the **Limit** field.
2. Select or type the Limit value.

### Cooldown Time

The Cooldown Time property limits the rate, in seconds, at which Post Event commands are accepted by the Sound Engine. When a Post Event command is accepted and processed by the Sound Engine, other Post Event commands for the same Event will be discarded for the duration of the Cooldown Time property.

|  |  |
| --- | --- |
| [备注] | 备注 |
| Setting a time value of 0 seconds disables the Cooldown Time property. |

**To set the Cooldown Time:**

1. In the Event Editor, click in the **Cooldown Time** field.
2. Type the Cooldown Time limit value, in seconds.

### Scope

The Scope property specifies the extent to which the Event Limiting properties are applied to objects within the game. There are two possible values:

- **Global:** The Global scope will apply the limits set by the Event Limiting properties to all Post Event commands received for the same Event, regardless of the Game Object for which they are specified.
- **Game Object:** The Game Object scope will apply the limits set by the Event Limiting properties to Post Events commands received for the same Event only for the Game Object for which they are specified.

|  |  |
| --- | --- |
| [备注] | 备注 |
| If both the Limit and the Cooldown Time properties are disabled, the Event Limiting Scope property is also disabled. |

**Example:** An Event has the following Event Limiting properties:

- Limit: 1
- Cooldown Time: 0.0s
- Scope: Game Object

For this example event, there may be concurrent instances of the Event, but the Event Limiting will only allow one instance of the Event per Game Object, because of the Limit property in combination with Scope property. The Cooldown Time property is not applied, as it is disabled by being set to 0 seconds.

---