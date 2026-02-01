# Media Pool metadata

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [Working with the Media Pool](00-Working-with-the-Media-Pool.md) > Media Pool metadata

## Media Pool metadata

The WAV (Waveform Audio File Format) is a standard digital audio file format used for
storing an audio bit stream. While the core of a WAV file contains the raw audio data,
it can also store a variety of metadata, providing additional information about the
audio content. This metadata can be found in different "chunks" within the file.

The following table lists the fields supported by the Media Pool, which include
standard WAV fields, Broadcast Wave Format (BWF) extension fields, and iXML
metadata:

| Field Name | 描述 |
| --- | --- |
| Filename | Name of the WAV file in the file system; a primary identifier. |
| **WAV** | Standard audio file format. |
| Duration | Total playing time of the audio samples, per channel. |
| 采样 | Total count of individual audio samples, per channel. |
| Data Size（数据大小） | Size (in bytes) of the raw audio data within the 'data' chunk. |
| Loop Start | Time of the beginning of a loop, in seconds; found in 'smpl' chunk. |
| Loop End | Time of the end of a loop, returning to Loop Start, in seconds; found in 'smpl' chunk. |
| Marker Count | Total number of defined markers (cue points) for specific time points in the audio; found in 'cue' chunk. |
| 采样率 | Number of audio samples captured per second (Hz), indicating time resolution; found in the 'fmt' chunk. |
| 位深 | Number of bits per audio sample, indicating amplitude resolution; found in the 'fmt' chunk. Wwise supports the following bit depths; 16-bit integer, 24-bit integer, 32-bit float. |
| Channels（声道） | Number of audio channels, for example, 1 for mono and 2 for stereo; found in the 'fmt' chunk. |
| Channel Configuration | Specifies the channel arrangement and role of audio channels. |
| **BWFXML** | Root XML tag (<BWFXML>) enclosing iXML metadata within a WAV file.  Open standard for embedding detailed XML-based production metadata in Broadcast Wave Format (BWF) files.  <http://www.gallery.co.uk/ixml/> |
| BWFXML/PROJECT | iXML field: Name of the associated project. |
| BWFXML/FILE\_UID | iXML field: Globally unique identifier for the audio file. |
| BWFXML/ASWG | iXML section: Sony PlayStation Studios' Audio Standards Working Group.  <https://github.com/Sony-ASWG/iXML-Extension> |
| BWFXML/BWF | iXML section (<BEXT>) for embedding or referencing BWF 'bext' chunk metadata.  <https://tech.ebu.ch/docs/tech/tech3285.pdf> |
| BWFXML/USER | iXML section for custom, user-defined metadata fields. Used by Strata to store additional information, including TRACKNAME and Universal Category System (UCS) fields, such as CATID and FXNAME.  <https://universalcategorysystem.com/> |

---