# Authoring Lua API

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Authoring Lua API

| 名称 | 说明 | Parameters | Return |
| --- | --- | --- | --- |
| wa\_abs\_path | Returns a path referencing the same file system location as the input, but where wa::Path::IsAbsolute is true | string Path: The directory to convert to absolute path. |  |
| wa\_call | Calls a Waapi function. | string Uri: The identifier of the Waapi function to call.    table Args: The table containing arguments.    table Options: The table containing options. |  |
| wa\_canonicalize\_path | Returns a canonicalized path, which is a path devoid of .. and . parts and with preferred separators | string Path: The path string to canonicalize. |  |
| wa\_connect\_as\_remote | Fakes the WAL behavior when connected to a remote instance. | boolean Value: The boolean value to set offline rendering to. |  |
| wa\_copy\_directory | Copies a source directory to the destination directory. | string Source: The directory path to copy.    string Destination: The destination path directory. |  |
| wa\_copy\_file | Copies a source file to the destination file. | string Source: The file path to copy.    string Destination: The destination file path. |  |
| wa\_copy\_to\_clipboard | Copies a given string to the clipboard. | string Content: The string to copy onto the clipboard. |  |
| wa\_debug\_break | Causes a breakpoint to occur in the current process. |  |  |
| wa\_directory\_exists | Checks whether a given directory exists. | string Path: The directory to validate. |  |
| wa\_enable\_originals\_watcher | Enable or disable the originals directory watcher | boolean Boolean: true to enable directory watchers, |  |
| wa\_ensure\_directory\_exist | Verifies that a given directory exists. If it does not exist, the directory is created. | string Path: The directory to validate or create. |  |
| wa\_get\_api\_statistics | Return the Lua API statistics in a table, then flush the statistic data. |  |  |
| wa\_get\_from\_clipboard | Retrieves the clipboard contents. |  |  |
| wa\_get\_project\_curve | Try to get a project curve and its points | string Arg: The command line argument. |  |
| wa\_get\_session\_guid | Returns a session GUID of the application |  |  |
| wa\_json\_pretty\_print | Convert a lua table to JSON, and return the pretty print string | table Table: to format as |  |
| wa\_log | Logs a string message in Wwise. | string Message: The message to log. |  |
| wa\_move | Moves a source directory to a path destination. | string Path: The source directory to move.    string Path: The destination path to move to. |  |
| wa\_read\_json | Convert a json string to lua table | string strJson: json object in string format |  |
| wa\_remove\_directory | Removes a directory from the filesystem. | string Path: The directory to remove. |  |
| wa\_render\_audio | Renders the audio. |  |  |
| wa\_reset\_transport | Resets the transport. |  |  |
| wa\_set\_local\_read\_only | Sets local read only | boolean Value: The boolean value to set offline rendering to. |  |
| wa\_set\_offline\_rendering | Sets offline rendering to true or false. | boolean Value: The boolean value to set offline rendering to. |  |
| wa\_set\_user\_pref | Sets user preferences. | string Location: The location associated with the preferences to set.    string Name: The name associated with the preferences to set.    number, or boolean, or string Value: The value to set. |  |
| wa\_shell\_execute | Executes a shell command. | string Arg: The command line argument. |  |
| wa\_simulate\_originals\_watcher\_update | Simulate the OS's DirectoryWatch event, specifying the list of paths that changed | table Table: list of paths to declare as changed |  |
| wa\_sleep | Allows the thread to pause execution for a specified number of milliseconds. | number Milliseconds: The number of milliseconds to yield for. |  |
| wa\_start\_capture\_console\_output | Starts capture of the console output. |  |  |
| wa\_start\_output\_capture | Starts output capture. | string Filename: The string path to the file where the output capture should be saved. |  |
| wa\_std\_channel\_index\_to\_meter\_index | Convert a channel index from WEM/Sound Engine order and return the channel index in the meter display order | number ChannelIndex: Index of the channel from WAV file    number ChannelMask: Channel for the configuration |  |
| wa\_stop\_capture\_console\_output | Stops capture of the console output. |  |  |
| wa\_stop\_output\_capture | Stops output capture. |  |  |
| wa\_subscribe | Subscribes to a Waapi function. | string Uri: The identifier of the Waapi function to subscribe to.    table Options: The table containing options.    function Func: The function to call upon event. |  |
| wa\_table\_to\_json | Convert a lua table to AkJson. | table Args: The table to convert. |  |
| wa\_temporary\_directory | Creates a temporary directory. |  |  |
| wa\_time | Retrieves the current time. |  |  |
| wa\_unsubscribe | Unsubscribes from a Waapi subscription. | number IdSubscription: identifier that had been returned by the Waapi function wa\_subscribe. |  |
| wa\_unsubscribe\_all | Unsubscribes from all Waapi subscriptions. |  |  |
| wa\_user\_name | Retrieves the username. |  |  |