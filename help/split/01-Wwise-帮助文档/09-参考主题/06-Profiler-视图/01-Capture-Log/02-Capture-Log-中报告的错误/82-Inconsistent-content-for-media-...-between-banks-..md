# Inconsistent content for media ... between banks ... and ... Soundbanks will have to be regenerated and redeployed.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Inconsistent content for media ... between banks ... and ... Soundbanks will have to be regenerated and redeployed.

#### Inconsistent content for media ... between banks ... and ... Soundbanks will have to be regenerated and redeployed.

When this happens, the second media copy is discarded and this message appears. However, in some situations, this can lead to issues later if the sound is also streaming from disk. This error occurs if all of the following criteria are true:

- A Sound or Music Clip is duplicated in two or more banks.
- One bank was generated.
- A change was made to the media of the sound. For example, any change in the Source Editor or the file itself was edited outside of Wwise.
- The *other* bank was generated alone.
- Both banks are loaded in-game.

Another common workflow that can lead to this error is forgetting to package or deploy all banks on the target console. The effect is the same: the media in one bank doesn't match the media in other banks. In this case, it is not a generation problem but a deployment problem.

**推荐的解决步骤：**

- Regenerate your SoundBanks, repackage them (if needed), and redeploy to the target console.
- Alternatively, clear all SoundBanks from the console working directory.

---