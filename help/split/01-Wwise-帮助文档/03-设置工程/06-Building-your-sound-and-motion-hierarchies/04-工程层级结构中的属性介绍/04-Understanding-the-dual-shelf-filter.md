# Understanding the dual-shelf filter

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [设置工程](../../00-设置工程.md) > [Building your sound and motion hierarchies](../00-Building-your-sound-and-motion-hierarchies.md) > [工程层级结构中的属性介绍](00-工程层级结构中的属性介绍.md) > Understanding the dual-shelf filter

### Understanding the dual-shelf filter

The dual-shelf filter (DSF) is a type of filter that can attenuate or boost high
frequencies. It is based on the filter design proposed by [Audfray, Rémi; Jot,
Jean-Marc; Dicker, Sam](https://aes2.org/publications/elibrary-page/?id=19780) and is well-suited for accurately simulating physical
acoustic effects such as diffraction. The DSF is also well-suited for situations where tone
control is desired over more dramatic filtering effects that the LPF provides.

The DSF is similar to conventional high-shelf filters (HSF) such as those encountered in the Parametric EQ plugin. However, there are differences between the two that are important to understand.

The filter's transition to the desired high frequency gain is more gradual compared to the conventional shelf filter. The following graph shows the filter response of a conventional HSF with a cutoff frequency of 1 kHz (blue) and DSF (orange). The high frequency gain of both filters is -20 dB. With the HSF, the transition to the high frequency gain of -20 dB begins at around 100 Hz and has a comparatively steeper slope. With the dual-shelf filter, the transition begins much earlier at around 15 Hz and has a much more gradual slope towards -20 dB.

![](../../../../../images/dgm_dsf_vs_hsf.png)

|  |  |
| --- | --- |
| [备注] | 备注 |
| The shape of the transition region can be changed using the emphasis property (see [“Dual-shelf filter properties”一节](04-Understanding-the-dual-shelf-filter.md#dual_shelf_properties "Dual-shelf filter properties")) |

For acoustics, the DSF's gradual slope is a more accurate representation of diffraction. The following image shows a hypothetical scenario of an emitter and various listeners (colored arrows) at different positions behind a wall (triangular shape). The graph on the right shows the filtering effects of diffraction as sound propagates from the emitter (X), around the wall, and eventually to the listeners. As observed in the graph, the effect of diffraction is a gradual reduction of higher frequency gains that is well-approximated by the DSF.

![](../../../../../images/dgm_dsf_diffraction.png)

Another important difference between the DSF and conventional shelf-filter is that unlike the conventional HSF, you cannot change the cutoff frequency of the DSF. However this allows for better performance in terms of CPU cycles as many DSFs along a voice's signal path can be represented by just one equivalent filter (see [“Dual-shelf filter behavior”一节](04-Understanding-the-dual-shelf-filter.md#dual_shelf_behavior "Dual-shelf filter behavior")).

#### Where dual-shelf filters can be used

DSFs are available in the following areas:

- Output Bus（输出总线）
- Game-defined Aux Sends
- Attenuation ShareSets

#### Dual-shelf filter properties

There are two properties that change the behavior of the DSF:

- High Frequency Gain
- Emphasis

Changing the DSF sliders in the vertical property editor and dual-shelf filter curves in attenuation sharesets changes the **high frequency gain**. The following graph shows the degree of high frequency attenuation or boost for various high frequency gain settings.

![](../../../../../images/dgm_dsf_filter_resp.png)

The emphasis property changes the shape of the DSF transition region. This property is similar to the 'Q' parameter, which affects the resonance of conventional shelf filters. Its range is -1 to + 1 and the default is 0.

The following graphs show the effect of emphasis in various settings. In the top graph, the high frequency gain is set to -20 dB. In the bottom graph, the high frequency gain is set to +10 dB.

![](../../../../../images/dgm_dsf_emphasis_attn.png)

![](../../../../../images/dgm_dsf_emphasis_boost.png)

Emphasis is a global property that is changed in the Project Settings.

![](../../../../../images/dgm_dsf_emphasis_slider.png)

|  |  |
| --- | --- |
| [注意] | 注意 |
| The selected emphasis is applied to every DSF filter used in the Wwise project. |

#### Dual-shelf filter behavior

The DSF behavior is additive. When multiple DSFs are present along a signal's path, the high frequency gains are summed.

For example, if a voice signal goes through a distance DSF with -2 dB high frequency gain, then a diffraction DSF with -1 dB high frequency gain before finally going through the output bus DSF with -3 dB high frequency gain, the effective high frequency gain is -6 dB. Moreover, as an optimization, the sound engine will only be processing one effective DSF with the high frequency gain of -6 dB instead of creating 3 different DSF instances and processing them individually.

---