# AkEmitterListenerPair

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_emitter_listener_pair-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs) |
[Protected 属性](#pro-attribs)

AkEmitterListenerPair类 参考

Emitter-listener pair: Positioning data pertaining to a single pair of emitter and listener.
[更多...](class_ak_emitter_listener_pair.html#details)

`#include <Ak3DObjects.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkEmitterListenerPair](class_ak_emitter_listener_pair_a7f2c3c98af6d4f5945954d9b17efded3.html#a7f2c3c98af6d4f5945954d9b17efded3) () |
|  | Constructor. [更多...](class_ak_emitter_listener_pair_a7f2c3c98af6d4f5945954d9b17efded3.html#a7f2c3c98af6d4f5945954d9b17efded3) |
|  | |
|  | [~AkEmitterListenerPair](class_ak_emitter_listener_pair_a2839f40688dcd399083ea6abad88c217.html#a2839f40688dcd399083ea6abad88c217) () |
|  | Destructor. [更多...](class_ak_emitter_listener_pair_a2839f40688dcd399083ea6abad88c217.html#a2839f40688dcd399083ea6abad88c217) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Distance](class_ak_emitter_listener_pair_aef05e84981e5a8fdcdf7df67b1ce5e7b.html#aef05e84981e5a8fdcdf7df67b1ce5e7b) () const |
|  | Get distance. [更多...](class_ak_emitter_listener_pair_aef05e84981e5a8fdcdf7df67b1ce5e7b.html#aef05e84981e5a8fdcdf7df67b1ce5e7b) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [EmitterAngle](class_ak_emitter_listener_pair_a4610a1a96613ff423888f59809c33a38.html#a4610a1a96613ff423888f59809c33a38) () const |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [ListenerAngle](class_ak_emitter_listener_pair_acad51e4770216574f3200cd1f578c382.html#acad51e4770216574f3200cd1f578c382) () const |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Occlusion](class_ak_emitter_listener_pair_ad1ef229d9b518672b8132018e896c9d0.html#ad1ef229d9b518672b8132018e896c9d0) () const |
|  | Get the occlusion factor for this emitter-listener pair [更多...](class_ak_emitter_listener_pair_ad1ef229d9b518672b8132018e896c9d0.html#ad1ef229d9b518672b8132018e896c9d0) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Obstruction](class_ak_emitter_listener_pair_aaadbb7ef71560fd1d10307737efa9824.html#aaadbb7ef71560fd1d10307737efa9824) () const |
|  | Get the obstruction factor for this emitter-listener pair [更多...](class_ak_emitter_listener_pair_aaadbb7ef71560fd1d10307737efa9824.html#aaadbb7ef71560fd1d10307737efa9824) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Diffraction](class_ak_emitter_listener_pair_afa3f01270b83867a16f386fe592a4163.html#afa3f01270b83867a16f386fe592a4163) () const |
|  | Get the diffraction factor for this emitter-listener pair [更多...](class_ak_emitter_listener_pair_afa3f01270b83867a16f386fe592a4163.html#afa3f01270b83867a16f386fe592a4163) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [TransmissionLoss](class_ak_emitter_listener_pair_a446b02cf755b9025bb8d55ea65c90990.html#a446b02cf755b9025bb8d55ea65c90990) () const |
|  | Get the transmission loss factor for this emitter-listener pair [更多...](class_ak_emitter_listener_pair_a446b02cf755b9025bb8d55ea65c90990.html#a446b02cf755b9025bb8d55ea65c90990) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [PathGain](class_ak_emitter_listener_pair_a5c1cc9fbd4ec1a8fd502fae09bf77d3b.html#a5c1cc9fbd4ec1a8fd502fae09bf77d3b) () const |
|  | Get the overall path-contribution gain, used to scale the dry + gamedef + userdef gains [更多...](class_ak_emitter_listener_pair_a5c1cc9fbd4ec1a8fd502fae09bf77d3b.html#a5c1cc9fbd4ec1a8fd502fae09bf77d3b) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetGainForConnectionType](class_ak_emitter_listener_pair_af8e554be096fd19702beb11bd949112f.html#af8e554be096fd19702beb11bd949112f) ([AkConnectionType](_ak_enums_8h_a6f995e33d25d16eac499fb607bde0e4b.html#a6f995e33d25d16eac499fb607bde0e4b) in\_eType) const |
|  | Get the emitter-listener-pair-specific gain (due to distance and cone attenuation), linear [0,1], for a given connection type. [更多...](class_ak_emitter_listener_pair_af8e554be096fd19702beb11bd949112f.html#af8e554be096fd19702beb11bd949112f) |
|  | |
| [AkRayID](_ak_typedefs_8h_a6b3ca56233651c0a07ca61993688a888.html#a6b3ca56233651c0a07ca61993688a888) | [ID](class_ak_emitter_listener_pair_af274c1f94966ad2fabf37e450b5ca23d.html#af274c1f94966ad2fabf37e450b5ca23d) () const |
|  | Get the emitter-listener pair's ID. [更多...](class_ak_emitter_listener_pair_af274c1f94966ad2fabf37e450b5ca23d.html#af274c1f94966ad2fabf37e450b5ca23d) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [ListenerID](class_ak_emitter_listener_pair_a2b8fbaa29972513b88c9a6c825c43f33.html#a2b8fbaa29972513b88c9a6c825c43f33) () const |
|  | Get listener ID associated with the emitter-listener pair. [更多...](class_ak_emitter_listener_pair_a2b8fbaa29972513b88c9a6c825c43f33.html#a2b8fbaa29972513b88c9a6c825c43f33) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkWorldTransform](struct_ak_world_transform.html) | [emitter](class_ak_emitter_listener_pair_aef493f1d3a77a31504991195aaff83a8.html#aef493f1d3a77a31504991195aaff83a8) |
|  | Emitter position. [更多...](class_ak_emitter_listener_pair_aef493f1d3a77a31504991195aaff83a8.html#aef493f1d3a77a31504991195aaff83a8) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fDistance](class_ak_emitter_listener_pair_a1c2f1f702df96c2c2ccf34f8691aefe3.html#a1c2f1f702df96c2c2ccf34f8691aefe3) |
|  | Distance between emitter and listener. [更多...](class_ak_emitter_listener_pair_a1c2f1f702df96c2c2ccf34f8691aefe3.html#a1c2f1f702df96c2c2ccf34f8691aefe3) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fEmitterAngle](class_ak_emitter_listener_pair_aae46074a79e3f8ff4dc987980788a970.html#aae46074a79e3f8ff4dc987980788a970) |
|  | Angle between position vector and emitter orientation. [更多...](class_ak_emitter_listener_pair_aae46074a79e3f8ff4dc987980788a970.html#aae46074a79e3f8ff4dc987980788a970) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fListenerAngle](class_ak_emitter_listener_pair_a86604096953e030195f3ab24a7ccec52.html#a86604096953e030195f3ab24a7ccec52) |
|  | Angle between position vector and listener orientation. [更多...](class_ak_emitter_listener_pair_a86604096953e030195f3ab24a7ccec52.html#a86604096953e030195f3ab24a7ccec52) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fDryMixGain](class_ak_emitter_listener_pair_a8dce7e8b69d3732f84b546a634d3d8b2.html#a8dce7e8b69d3732f84b546a634d3d8b2) |
|  | Emitter-listener-pair-specific gain (due to distance and cone attenuation) for direct connections. [更多...](class_ak_emitter_listener_pair_a8dce7e8b69d3732f84b546a634d3d8b2.html#a8dce7e8b69d3732f84b546a634d3d8b2) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fGameDefAuxMixGain](class_ak_emitter_listener_pair_a4bfb871202b30de98a9ce4308d170583.html#a4bfb871202b30de98a9ce4308d170583) |
|  | Emitter-listener-pair-specific gain (due to distance and cone attenuation) for game-defined send connections. [更多...](class_ak_emitter_listener_pair_a4bfb871202b30de98a9ce4308d170583.html#a4bfb871202b30de98a9ce4308d170583) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fUserDefAuxMixGain](class_ak_emitter_listener_pair_ab58ab4932cb20b54bb8fd7ec6bff1060.html#ab58ab4932cb20b54bb8fd7ec6bff1060) |
|  | Emitter-listener-pair-specific gain (due to distance and cone attenuation) for user-defined send connections. [更多...](class_ak_emitter_listener_pair_ab58ab4932cb20b54bb8fd7ec6bff1060.html#ab58ab4932cb20b54bb8fd7ec6bff1060) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fOcclusion](class_ak_emitter_listener_pair_a2986a1715abb652f580b68abb2b2e1e1.html#a2986a1715abb652f580b68abb2b2e1e1) |
|  | Emitter-listener-pair-specific occlusion factor [更多...](class_ak_emitter_listener_pair_a2986a1715abb652f580b68abb2b2e1e1.html#a2986a1715abb652f580b68abb2b2e1e1) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fObstruction](class_ak_emitter_listener_pair_adfa61151984d538f64c73491cfdaf024.html#adfa61151984d538f64c73491cfdaf024) |
|  | Emitter-listener-pair-specific obstruction factor [更多...](class_ak_emitter_listener_pair_adfa61151984d538f64c73491cfdaf024.html#adfa61151984d538f64c73491cfdaf024) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fDiffraction](class_ak_emitter_listener_pair_aa0cd5580fe58793bdc5ffb1c48b5af7b.html#aa0cd5580fe58793bdc5ffb1c48b5af7b) |
|  | Emitter-listener-pair-specific diffraction coefficient [更多...](class_ak_emitter_listener_pair_aa0cd5580fe58793bdc5ffb1c48b5af7b.html#aa0cd5580fe58793bdc5ffb1c48b5af7b) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fTransmissionLoss](class_ak_emitter_listener_pair_a3c94dd7d928ed491cb11c2b1b74e5286.html#a3c94dd7d928ed491cb11c2b1b74e5286) |
|  | Emitter-listener-pair-specific transmission occlusion. [更多...](class_ak_emitter_listener_pair_a3c94dd7d928ed491cb11c2b1b74e5286.html#a3c94dd7d928ed491cb11c2b1b74e5286) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fSpread](class_ak_emitter_listener_pair_af2edcb3f68006ec8c31feef70138f689.html#af2edcb3f68006ec8c31feef70138f689) |
|  | Emitter-listener-pair-specific spread [更多...](class_ak_emitter_listener_pair_af2edcb3f68006ec8c31feef70138f689.html#af2edcb3f68006ec8c31feef70138f689) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fAperture](class_ak_emitter_listener_pair_ad93d4317b137948e796bb60e1e81c6f9.html#ad93d4317b137948e796bb60e1e81c6f9) |
|  | Emitter-listener-pair-specific aperture [更多...](class_ak_emitter_listener_pair_ad93d4317b137948e796bb60e1e81c6f9.html#ad93d4317b137948e796bb60e1e81c6f9) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fScalingFactor](class_ak_emitter_listener_pair_ac84f6e5c7747d597470f53df03555e6d.html#ac84f6e5c7747d597470f53df03555e6d) |
|  | Combined scaling factor due to both emitter and listener. [更多...](class_ak_emitter_listener_pair_ac84f6e5c7747d597470f53df03555e6d.html#ac84f6e5c7747d597470f53df03555e6d) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fPathGain](class_ak_emitter_listener_pair_aeb37dc5d27410bea3313943968cf01de.html#aeb37dc5d27410bea3313943968cf01de) |
|  | Emitter-listener-pair-specific overall gain that scales fDryMixGain, fGameDefAuxMixGain and fUserDefAuxMixGain [更多...](class_ak_emitter_listener_pair_aeb37dc5d27410bea3313943968cf01de.html#aeb37dc5d27410bea3313943968cf01de) |
|  | |
| [AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) | [uEmitterChannelMask](class_ak_emitter_listener_pair_a922b0837f0a027aaa2322b2ff6a385df.html#a922b0837f0a027aaa2322b2ff6a385df) |
|  | Channels of the emitter that apply to this ray. [更多...](class_ak_emitter_listener_pair_a922b0837f0a027aaa2322b2ff6a385df.html#a922b0837f0a027aaa2322b2ff6a385df) |
|  | |

|  |  |
| --- | --- |
| Protected 属性 | |
| [AkRayID](_ak_typedefs_8h_a6b3ca56233651c0a07ca61993688a888.html#a6b3ca56233651c0a07ca61993688a888) | [id](class_ak_emitter_listener_pair_abf860750a6cdba817f9a0248641ec0fd.html#abf860750a6cdba817f9a0248641ec0fd) |
|  | ID of this emitter-listener pair, unique for a given emitter. [更多...](class_ak_emitter_listener_pair_abf860750a6cdba817f9a0248641ec0fd.html#abf860750a6cdba817f9a0248641ec0fd) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [m\_uListenerID](class_ak_emitter_listener_pair_aa9f965612c3c69f6122a55bd4784d004.html#aa9f965612c3c69f6122a55bd4784d004) |
|  | Listener game object ID. [更多...](class_ak_emitter_listener_pair_aa9f965612c3c69f6122a55bd4784d004.html#aa9f965612c3c69f6122a55bd4784d004) |
|  | |

## 详细描述

Emitter-listener pair: Positioning data pertaining to a single pair of emitter and listener.

在文件 [Ak3DObjects.h](_ak3_d_objects_8h_source.html) 第 [458](_ak3_d_objects_8h_source.html#l00458) 行定义.