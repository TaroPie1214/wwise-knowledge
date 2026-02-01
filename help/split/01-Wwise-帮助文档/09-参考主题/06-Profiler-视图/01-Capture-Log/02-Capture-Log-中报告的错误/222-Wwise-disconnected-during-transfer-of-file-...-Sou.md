# Wwise disconnected during transfer of file ... Sound will be terminated. Other errors may occur.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Wwise disconnected during transfer of file ... Sound will be terminated. Other errors may occur.

#### Wwise disconnected during transfer of file ... Sound will be terminated. Other errors may occur.

This error occurs when the Wwise authoring tool disconnects from a game and a WEM file is streaming due to a Live Media Transfer.

This only happens when a Sound or Music Clip is set to Stream and the media of that sound is modified while connected to the Game, which causes the sound to start streaming from the Authoring tool to get the new media. This streaming happens over the network, instead of from disk. Therefore, if the connection is terminated, the stream can't continue.

Note that the Sound associated with that file has stopped. Playing that sound again in game will result in a File Not Found error.

**推荐的解决步骤：**

- Reconnect Wwise to your game to stream the modified files again.
- Rebuild your SoundBanks and redeploy to transfer the new media files to the console, then restart your game.

---