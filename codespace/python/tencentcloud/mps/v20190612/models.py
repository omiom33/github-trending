# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AIAnalysisTemplateItem(AbstractModel):
    """AI 智能分析模板详情

    """

    def __init__(self):
        r"""
        :param Definition: 智能分析模板唯一标识。
        :type Definition: int
        :param Name: 智能分析模板名称。
        :type Name: str
        :param Comment: 智能分析模板描述信息。
        :type Comment: str
        :param ClassificationConfigure: 智能分类任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationConfigure: :class:`tencentcloud.mps.v20190612.models.ClassificationConfigureInfo`
        :param TagConfigure: 智能标签任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagConfigure: :class:`tencentcloud.mps.v20190612.models.TagConfigureInfo`
        :param CoverConfigure: 智能封面任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverConfigure: :class:`tencentcloud.mps.v20190612.models.CoverConfigureInfo`
        :param FrameTagConfigure: 智能按帧标签任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagConfigure: :class:`tencentcloud.mps.v20190612.models.FrameTagConfigureInfo`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param Type: 模板类型，取值范围：
* Preset：系统预置模板；
* Custom：用户自定义模板。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Type = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIRecognitionTemplateItem(AbstractModel):
    """视频内容识别模板详情

    """

    def __init__(self):
        r"""
        :param Definition: 视频内容识别模板唯一标识。
        :type Definition: int
        :param Name: 视频内容识别模板名称。
        :type Name: str
        :param Comment: 视频内容识别模板描述信息。
        :type Comment: str
        :param FaceConfigure: 人脸识别控制参数。
        :type FaceConfigure: :class:`tencentcloud.mps.v20190612.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: 文本全文识别控制参数。
        :type OcrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: 文本关键词识别控制参数。
        :type OcrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: 语音全文识别控制参数。
        :type AsrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: 语音关键词识别控制参数。
        :type AsrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.AsrWordsConfigureInfo`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param Type: 模板类型，取值范围：
* Preset：系统预置模板；
* Custom：用户自定义模板。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Type = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionConfigInfo(AbstractModel):
    """动作识别参数配置

    """

    def __init__(self):
        r"""
        :param Switch: 动作识别任务开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivityResItem(AbstractModel):
    """编排子任务输出

    """

    def __init__(self):
        r"""
        :param TranscodeTask: 转码任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskTranscodeResult`
        :param AnimatedGraphicTask: 转动图任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type AnimatedGraphicTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskAnimatedGraphicResult`
        :param SnapshotByTimeOffsetTask: 时间点截图任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSampleSnapshotResult`
        :param SampleSnapshotTask: 采样截图任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleSnapshotTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSampleSnapshotResult`
        :param ImageSpriteTask: 雪碧图任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSpriteTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskImageSpriteResult`
        :param AdaptiveDynamicStreamingTask: 自适应码流任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type AdaptiveDynamicStreamingTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskAdaptiveDynamicStreamingResult`
        :param RecognitionTask: 识别任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognitionTask: :class:`tencentcloud.mps.v20190612.models.ScheduleRecognitionTaskResult`
        :param ReviewTask: 审核任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type ReviewTask: :class:`tencentcloud.mps.v20190612.models.ScheduleReviewTaskResult`
        :param AnalysisTask: 分析任务输出
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisTask: :class:`tencentcloud.mps.v20190612.models.ScheduleAnalysisTaskResult`
        """
        self.TranscodeTask = None
        self.AnimatedGraphicTask = None
        self.SnapshotByTimeOffsetTask = None
        self.SampleSnapshotTask = None
        self.ImageSpriteTask = None
        self.AdaptiveDynamicStreamingTask = None
        self.RecognitionTask = None
        self.ReviewTask = None
        self.AnalysisTask = None


    def _deserialize(self, params):
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = MediaProcessTaskTranscodeResult()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("AnimatedGraphicTask") is not None:
            self.AnimatedGraphicTask = MediaProcessTaskAnimatedGraphicResult()
            self.AnimatedGraphicTask._deserialize(params.get("AnimatedGraphicTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = MediaProcessTaskSampleSnapshotResult()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("SampleSnapshotTask") is not None:
            self.SampleSnapshotTask = MediaProcessTaskSampleSnapshotResult()
            self.SampleSnapshotTask._deserialize(params.get("SampleSnapshotTask"))
        if params.get("ImageSpriteTask") is not None:
            self.ImageSpriteTask = MediaProcessTaskImageSpriteResult()
            self.ImageSpriteTask._deserialize(params.get("ImageSpriteTask"))
        if params.get("AdaptiveDynamicStreamingTask") is not None:
            self.AdaptiveDynamicStreamingTask = MediaProcessTaskAdaptiveDynamicStreamingResult()
            self.AdaptiveDynamicStreamingTask._deserialize(params.get("AdaptiveDynamicStreamingTask"))
        if params.get("RecognitionTask") is not None:
            self.RecognitionTask = ScheduleRecognitionTaskResult()
            self.RecognitionTask._deserialize(params.get("RecognitionTask"))
        if params.get("ReviewTask") is not None:
            self.ReviewTask = ScheduleReviewTaskResult()
            self.ReviewTask._deserialize(params.get("ReviewTask"))
        if params.get("AnalysisTask") is not None:
            self.AnalysisTask = ScheduleAnalysisTaskResult()
            self.AnalysisTask._deserialize(params.get("AnalysisTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivityResult(AbstractModel):
    """编排任务输出

    """

    def __init__(self):
        r"""
        :param ActivityType: 原子任务类型。
<li>Transcode：转码。</li>
<li>SampleSnapshot：采样截图。</li>
<li>AnimatedGraphics：转动图。</li>
<li>SnapshotByTimeOffset：时间点截图。</li>
<li>ImageSprites：雪碧图。</li>
<li>AdaptiveDynamicStreaming：自适应码流。</li>
<li>AiContentReview：内容审核。</li>
<li>AIRecognition：智能识别。</li>
<li>AIAnalysis：智能分析。</li>
        :type ActivityType: str
        :param ActivityResItem: 原子任务输出。
        :type ActivityResItem: :class:`tencentcloud.mps.v20190612.models.ActivityResItem`
        """
        self.ActivityType = None
        self.ActivityResItem = None


    def _deserialize(self, params):
        self.ActivityType = params.get("ActivityType")
        if params.get("ActivityResItem") is not None:
            self.ActivityResItem = ActivityResItem()
            self.ActivityResItem._deserialize(params.get("ActivityResItem"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingInfoItem(AbstractModel):
    """转自适应码流信息

    """

    def __init__(self):
        r"""
        :param Definition: 转自适应码流规格。
        :type Definition: int
        :param Package: 打包格式，可能为 HLS和 MPEG-DASH 两种。
        :type Package: str
        :param Path: 播放路径。
        :type Path: str
        :param Storage: 自适应码流文件的存储位置。
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.Package = None
        self.Path = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Package = params.get("Package")
        self.Path = params.get("Path")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingTaskInput(AbstractModel):
    """对视频转自适应码流的输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 转自适应码流模板 ID。
        :type Definition: int
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 转自适应码流后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 转自适应码流后，manifest 文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_adaptiveDynamicStreaming_{definition}.{format}`。
        :type OutputObjectPath: str
        :param SubStreamObjectName: 转自适应码流后，子流文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：`{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}.{format}`。
        :type SubStreamObjectName: str
        :param SegmentObjectName: 转自适应码流（仅 HLS）后，分片文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：`{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}_{segmentNumber}.{format}`。
        :type SegmentObjectName: str
        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.SubStreamObjectName = None
        self.SegmentObjectName = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.SubStreamObjectName = params.get("SubStreamObjectName")
        self.SegmentObjectName = params.get("SegmentObjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingTemplate(AbstractModel):
    """转自适应码流模板详情

    """

    def __init__(self):
        r"""
        :param Definition: 转自适应码流模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 转自适应码流模板名称。
        :type Name: str
        :param Comment: 转自适应码流模板描述信息。
        :type Comment: str
        :param Format: 转自适应码流格式，取值范围：
<li>HLS，</li>
<li>MPEG-DASH。</li>
        :type Format: str
        :param StreamInfos: 转自适应码流输入流参数信息，最多输入10路流。
        :type StreamInfos: list of AdaptiveStreamTemplate
        :param DisableHigherVideoBitrate: 是否禁止视频低码率转高码率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type DisableHigherVideoBitrate: int
        :param DisableHigherVideoResolution: 是否禁止视频分辨率转高分辨率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type DisableHigherVideoResolution: int
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Format = None
        self.StreamInfos = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Format = params.get("Format")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveStreamTemplate(AbstractModel):
    """自适应转码流参数模板

    """

    def __init__(self):
        r"""
        :param Video: 视频参数信息。
        :type Video: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param Audio: 音频参数信息。
        :type Audio: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param RemoveAudio: 是否移除音频流，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type RemoveAudio: int
        :param RemoveVideo: 是否移除视频流，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type RemoveVideo: int
        """
        self.Video = None
        self.Audio = None
        self.RemoveAudio = None
        self.RemoveVideo = None


    def _deserialize(self, params):
        if params.get("Video") is not None:
            self.Video = VideoTemplateInfo()
            self.Video._deserialize(params.get("Video"))
        if params.get("Audio") is not None:
            self.Audio = AudioTemplateInfo()
            self.Audio._deserialize(params.get("Audio"))
        self.RemoveAudio = params.get("RemoveAudio")
        self.RemoveVideo = params.get("RemoveVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisResult(AbstractModel):
    """智能分析结果

    """

    def __init__(self):
        r"""
        :param Type: 任务的类型，可以取的值有：
<li>Classification：智能分类</li>
<li>Cover：智能封面</li>
<li>Tag：智能标签</li>
<li>FrameTag：智能按帧标签</li>
<li>Highlight：智能精彩集锦</li>
        :type Type: str
        :param ClassificationTask: 视频内容分析智能分类任务的查询结果，当任务类型为 Classification 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskClassificationResult`
        :param CoverTask: 视频内容分析智能封面任务的查询结果，当任务类型为 Cover 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverResult`
        :param TagTask: 视频内容分析智能标签任务的查询结果，当任务类型为 Tag 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagResult`
        :param FrameTagTask: 视频内容分析智能按帧标签任务的查询结果，当任务类型为 FrameTag 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagResult`
        """
        self.Type = None
        self.ClassificationTask = None
        self.CoverTask = None
        self.TagTask = None
        self.FrameTagTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ClassificationTask") is not None:
            self.ClassificationTask = AiAnalysisTaskClassificationResult()
            self.ClassificationTask._deserialize(params.get("ClassificationTask"))
        if params.get("CoverTask") is not None:
            self.CoverTask = AiAnalysisTaskCoverResult()
            self.CoverTask._deserialize(params.get("CoverTask"))
        if params.get("TagTask") is not None:
            self.TagTask = AiAnalysisTaskTagResult()
            self.TagTask._deserialize(params.get("TagTask"))
        if params.get("FrameTagTask") is not None:
            self.FrameTagTask = AiAnalysisTaskFrameTagResult()
            self.FrameTagTask._deserialize(params.get("FrameTagTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationInput(AbstractModel):
    """智能分类任务输入类型

    """

    def __init__(self):
        r"""
        :param Definition: 视频智能分类模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationOutput(AbstractModel):
    """智能分类结果信息

    """

    def __init__(self):
        r"""
        :param ClassificationSet: 视频智能分类列表。
        :type ClassificationSet: list of MediaAiAnalysisClassificationItem
        """
        self.ClassificationSet = None


    def _deserialize(self, params):
        if params.get("ClassificationSet") is not None:
            self.ClassificationSet = []
            for item in params.get("ClassificationSet"):
                obj = MediaAiAnalysisClassificationItem()
                obj._deserialize(item)
                self.ClassificationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationResult(AbstractModel):
    """智能分类任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 智能分类任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskClassificationInput`
        :param Output: 智能分类任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskClassificationOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskClassificationInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskClassificationOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverInput(AbstractModel):
    """智能分类任务输入类型

    """

    def __init__(self):
        r"""
        :param Definition: 视频智能封面模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverOutput(AbstractModel):
    """智能封面结果信息

    """

    def __init__(self):
        r"""
        :param CoverSet: 智能封面列表。
        :type CoverSet: list of MediaAiAnalysisCoverItem
        :param OutputStorage: 智能封面的存储位置。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.CoverSet = None
        self.OutputStorage = None


    def _deserialize(self, params):
        if params.get("CoverSet") is not None:
            self.CoverSet = []
            for item in params.get("CoverSet"):
                obj = MediaAiAnalysisCoverItem()
                obj._deserialize(item)
                self.CoverSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverResult(AbstractModel):
    """智能封面结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 智能封面任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverInput`
        :param Output: 智能封面任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskCoverInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskCoverOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagInput(AbstractModel):
    """智能按帧标签任务输入类型

    """

    def __init__(self):
        r"""
        :param Definition: 视频智能按帧标签模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagOutput(AbstractModel):
    """智能按帧标签结果信息

    """

    def __init__(self):
        r"""
        :param SegmentSet: 视频按帧标签列表。
        :type SegmentSet: list of MediaAiAnalysisFrameTagSegmentItem
        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaAiAnalysisFrameTagSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagResult(AbstractModel):
    """智能按帧标签结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 智能按帧标签任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagInput`
        :param Output: 智能按帧标签任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskFrameTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskFrameTagOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskInput(AbstractModel):
    """AI 视频智能分析输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 视频内容分析模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagInput(AbstractModel):
    """智能标签任务输入类型

    """

    def __init__(self):
        r"""
        :param Definition: 视频智能标签模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagOutput(AbstractModel):
    """智能标签结果信息

    """

    def __init__(self):
        r"""
        :param TagSet: 视频智能标签列表。
        :type TagSet: list of MediaAiAnalysisTagItem
        """
        self.TagSet = None


    def _deserialize(self, params):
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagResult(AbstractModel):
    """智能标签结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 智能标签任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagInput`
        :param Output: 智能标签任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskTagOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiContentReviewResult(AbstractModel):
    """内容审核结果

    """

    def __init__(self):
        r"""
        :param Type: 任务的类型，可以取的值有：
<li>Porn：图片鉴黄</li>
<li>Terrorism：图片敏感</li>
<li>Political：图片敏感</li>
<li>Porn.Asr：Asr 文字鉴黄</li>
<li>Porn.Ocr：Ocr 文字鉴黄</li>
<li>Political.Asr：Asr 文字敏感</li>
<li>Political.Ocr：Ocr 文字敏感</li>
<li>Terrorism.Ocr：Ocr 文字敏感</li>
<li>Prohibited.Asr：Asr 文字鉴违禁</li>
<li>Prohibited.Ocr：Ocr 文字鉴违禁</li>
        :type Type: str
        :param SampleRate: 采样频率，即对视频每秒截取进行审核的帧数。
        :type SampleRate: float
        :param Duration: 审核的视频时长，单位：秒。
        :type Duration: float
        :param PornTask: 视频内容审核智能画面鉴黄任务的查询结果，当任务类型为 Porn 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPornResult`
        :param TerrorismTask: 视频内容审核智能画面敏感任务的查询结果，当任务类型为 Terrorism 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorismTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskTerrorismResult`
        :param PoliticalTask: 视频内容审核智能画面敏感任务的查询结果，当任务类型为 Political 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticalTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPoliticalResult`
        :param PornAsrTask: 视频内容审核 Asr 文字鉴黄任务的查询结果，当任务类型为 Porn.Asr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornAsrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPornAsrResult`
        :param PornOcrTask: 视频内容审核 Ocr 文字鉴黄任务的查询结果，当任务类型为 Porn.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPornOcrResult`
        :param PoliticalAsrTask: 视频内容审核 Asr 文字敏感任务的查询结果，当任务类型为 Political.Asr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticalAsrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPoliticalAsrResult`
        :param PoliticalOcrTask: 视频内容审核 Ocr 文字敏感任务的查询结果，当任务类型为 Political.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticalOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPoliticalOcrResult`
        :param TerrorismOcrTask: 视频内容审核 Ocr 文字敏感任务的查询结果，当任务类型为 Terrorism.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorismOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskTerrorismOcrResult`
        :param ProhibitedAsrTask: 视频内容审核 Asr 文字鉴违禁任务的查询结果，当任务类型为 Prohibited.Asr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProhibitedAsrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskProhibitedAsrResult`
        :param ProhibitedOcrTask: 视频内容审核 Ocr 文字鉴违禁任务的查询结果，当任务类型为 Prohibited.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProhibitedOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskProhibitedOcrResult`
        """
        self.Type = None
        self.SampleRate = None
        self.Duration = None
        self.PornTask = None
        self.TerrorismTask = None
        self.PoliticalTask = None
        self.PornAsrTask = None
        self.PornOcrTask = None
        self.PoliticalAsrTask = None
        self.PoliticalOcrTask = None
        self.TerrorismOcrTask = None
        self.ProhibitedAsrTask = None
        self.ProhibitedOcrTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SampleRate = params.get("SampleRate")
        self.Duration = params.get("Duration")
        if params.get("PornTask") is not None:
            self.PornTask = AiReviewTaskPornResult()
            self.PornTask._deserialize(params.get("PornTask"))
        if params.get("TerrorismTask") is not None:
            self.TerrorismTask = AiReviewTaskTerrorismResult()
            self.TerrorismTask._deserialize(params.get("TerrorismTask"))
        if params.get("PoliticalTask") is not None:
            self.PoliticalTask = AiReviewTaskPoliticalResult()
            self.PoliticalTask._deserialize(params.get("PoliticalTask"))
        if params.get("PornAsrTask") is not None:
            self.PornAsrTask = AiReviewTaskPornAsrResult()
            self.PornAsrTask._deserialize(params.get("PornAsrTask"))
        if params.get("PornOcrTask") is not None:
            self.PornOcrTask = AiReviewTaskPornOcrResult()
            self.PornOcrTask._deserialize(params.get("PornOcrTask"))
        if params.get("PoliticalAsrTask") is not None:
            self.PoliticalAsrTask = AiReviewTaskPoliticalAsrResult()
            self.PoliticalAsrTask._deserialize(params.get("PoliticalAsrTask"))
        if params.get("PoliticalOcrTask") is not None:
            self.PoliticalOcrTask = AiReviewTaskPoliticalOcrResult()
            self.PoliticalOcrTask._deserialize(params.get("PoliticalOcrTask"))
        if params.get("TerrorismOcrTask") is not None:
            self.TerrorismOcrTask = AiReviewTaskTerrorismOcrResult()
            self.TerrorismOcrTask._deserialize(params.get("TerrorismOcrTask"))
        if params.get("ProhibitedAsrTask") is not None:
            self.ProhibitedAsrTask = AiReviewTaskProhibitedAsrResult()
            self.ProhibitedAsrTask._deserialize(params.get("ProhibitedAsrTask"))
        if params.get("ProhibitedOcrTask") is not None:
            self.ProhibitedOcrTask = AiReviewTaskProhibitedOcrResult()
            self.ProhibitedOcrTask._deserialize(params.get("ProhibitedOcrTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiContentReviewTaskInput(AbstractModel):
    """智能内容审核任务类型

    """

    def __init__(self):
        r"""
        :param Definition: 视频内容审核模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionResult(AbstractModel):
    """智能识别结果。

    """

    def __init__(self):
        r"""
        :param Type: 任务的类型，取值范围：
<li>FaceRecognition：人脸识别，</li>
<li>AsrWordsRecognition：语音关键词识别，</li>
<li>OcrWordsRecognition：文本关键词识别，</li>
<li>AsrFullTextRecognition：语音全文识别，</li>
<li>OcrFullTextRecognition：文本全文识别。</li>
<li>TransTextRecognition：语音翻译。</li>
        :type Type: str
        :param FaceTask: 人脸识别结果，当 Type 为 
 FaceRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskFaceResult`
        :param AsrWordsTask: 语音关键词识别结果，当 Type 为
 AsrWordsRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrWordsTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResult`
        :param AsrFullTextTask: 语音全文识别结果，当 Type 为
 AsrFullTextRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrFullTextTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResult`
        :param OcrWordsTask: 文本关键词识别结果，当 Type 为
 OcrWordsRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrWordsTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResult`
        :param OcrFullTextTask: 文本全文识别结果，当 Type 为
 OcrFullTextRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrFullTextTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResult`
        :param TransTextTask: 翻译结果，当 Type 为
 TransTextRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransTextTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskTransTextResult`
        """
        self.Type = None
        self.FaceTask = None
        self.AsrWordsTask = None
        self.AsrFullTextTask = None
        self.OcrWordsTask = None
        self.OcrFullTextTask = None
        self.TransTextTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("FaceTask") is not None:
            self.FaceTask = AiRecognitionTaskFaceResult()
            self.FaceTask._deserialize(params.get("FaceTask"))
        if params.get("AsrWordsTask") is not None:
            self.AsrWordsTask = AiRecognitionTaskAsrWordsResult()
            self.AsrWordsTask._deserialize(params.get("AsrWordsTask"))
        if params.get("AsrFullTextTask") is not None:
            self.AsrFullTextTask = AiRecognitionTaskAsrFullTextResult()
            self.AsrFullTextTask._deserialize(params.get("AsrFullTextTask"))
        if params.get("OcrWordsTask") is not None:
            self.OcrWordsTask = AiRecognitionTaskOcrWordsResult()
            self.OcrWordsTask._deserialize(params.get("OcrWordsTask"))
        if params.get("OcrFullTextTask") is not None:
            self.OcrFullTextTask = AiRecognitionTaskOcrFullTextResult()
            self.OcrFullTextTask._deserialize(params.get("OcrFullTextTask"))
        if params.get("TransTextTask") is not None:
            self.TransTextTask = AiRecognitionTaskTransTextResult()
            self.TransTextTask._deserialize(params.get("TransTextTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResult(AbstractModel):
    """语音全文识别结果。

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 语音全文识别任务输入信息。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResultInput`
        :param Output: 语音全文识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResultInput(AbstractModel):
    """语音全文识别的输入。

    """

    def __init__(self):
        r"""
        :param Definition: 语音全文识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResultOutput(AbstractModel):
    """语音全文识别结果。

    """

    def __init__(self):
        r"""
        :param SegmentSet: 语音全文识别片段列表。
        :type SegmentSet: list of AiRecognitionTaskAsrFullTextSegmentItem
        :param SubtitlePath: 字幕文件地址。
        :type SubtitlePath: str
        :param OutputStorage: 字幕文件存储位置。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.SegmentSet = None
        self.SubtitlePath = None
        self.OutputStorage = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.SubtitlePath = params.get("SubtitlePath")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextSegmentItem(AbstractModel):
    """语音全文识别片段。

    """

    def __init__(self):
        r"""
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Text: 识别文本。
        :type Text: str
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResult(AbstractModel):
    """语音关键词识别结果。

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 语音关键词识别任务输入信息。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResultInput`
        :param Output: 语音关键词识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultInput(AbstractModel):
    """语音关键词识别输入。

    """

    def __init__(self):
        r"""
        :param Definition: 语音关键词识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultItem(AbstractModel):
    """语音关键词识别结果。

    """

    def __init__(self):
        r"""
        :param Word: 语音关键词。
        :type Word: str
        :param SegmentSet: 语音关键词出现的时间片段列表。
        :type SegmentSet: list of AiRecognitionTaskAsrWordsSegmentItem
        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultOutput(AbstractModel):
    """语音关键词识别输出。

    """

    def __init__(self):
        r"""
        :param ResultSet: 语音关键词识别结果集。
        :type ResultSet: list of AiRecognitionTaskAsrWordsResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskAsrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsSegmentItem(AbstractModel):
    """语音识别片段。

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResult(AbstractModel):
    """人脸识别结果。

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 人脸识别任务输入信息。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskFaceResultInput`
        :param Output: 人脸识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskFaceResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskFaceResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskFaceResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultInput(AbstractModel):
    """人脸识别输入。

    """

    def __init__(self):
        r"""
        :param Definition: 人脸识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultItem(AbstractModel):
    """人脸识别结果

    """

    def __init__(self):
        r"""
        :param Id: 人物唯一标识 ID。
        :type Id: str
        :param Type: 人物库类型，表示识别出的人物来自哪个人物库：
<li>Default：默认人物库；</li>
<li>UserDefine：用户自定义人物库。</li>
        :type Type: str
        :param Name: 人物名称。
        :type Name: str
        :param SegmentSet: 人物出现的片段结果集。
        :type SegmentSet: list of AiRecognitionTaskFaceSegmentItem
        :param Gender: 人物性别：
<li>Male：男性；</li>
<li>Female：女性。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Gender: str
        :param Birthday: 人物出生日期。
注意：此字段可能返回 null，表示取不到有效值。
        :type Birthday: str
        :param Profession: 人物职业或者职务。
注意：此字段可能返回 null，表示取不到有效值。
        :type Profession: str
        :param SchoolOfGraduation: 人物毕业院校。
注意：此字段可能返回 null，表示取不到有效值。
        :type SchoolOfGraduation: str
        :param Abstract: 人物简介。
注意：此字段可能返回 null，表示取不到有效值。
        :type Abstract: str
        :param PlaceOfBirth: 人物出生地或者籍贯。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlaceOfBirth: str
        :param PersonType: 人物类型：
<li>Politician：官员；</li>
<li>Artist：艺人。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonType: str
        :param Remark: 敏感度标注：
<li>Normal：正常；</li>
<li>Sensitive：敏感。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param Url: 截图链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.SegmentSet = None
        self.Gender = None
        self.Birthday = None
        self.Profession = None
        self.SchoolOfGraduation = None
        self.Abstract = None
        self.PlaceOfBirth = None
        self.PersonType = None
        self.Remark = None
        self.Url = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskFaceSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.Gender = params.get("Gender")
        self.Birthday = params.get("Birthday")
        self.Profession = params.get("Profession")
        self.SchoolOfGraduation = params.get("SchoolOfGraduation")
        self.Abstract = params.get("Abstract")
        self.PlaceOfBirth = params.get("PlaceOfBirth")
        self.PersonType = params.get("PersonType")
        self.Remark = params.get("Remark")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultOutput(AbstractModel):
    """智能人脸识别输出。

    """

    def __init__(self):
        r"""
        :param ResultSet: 智能人脸识别结果集。
        :type ResultSet: list of AiRecognitionTaskFaceResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskFaceResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceSegmentItem(AbstractModel):
    """人脸识别结果片段

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskInput(AbstractModel):
    """视频内容识别输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 视频智能识别模板 ID 。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResult(AbstractModel):
    """文本全文识别结果。

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 文本全文识别任务输入信息。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResultInput`
        :param Output: 文本全文识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResultInput(AbstractModel):
    """文本全文识别输入。

    """

    def __init__(self):
        r"""
        :param Definition: 文本全文识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResultOutput(AbstractModel):
    """文本全文识别输出。

    """

    def __init__(self):
        r"""
        :param SegmentSet: 文本全文识别结果集。
        :type SegmentSet: list of AiRecognitionTaskOcrFullTextSegmentItem
        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextSegmentItem(AbstractModel):
    """文本全文识别片段。

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param TextSet: 识别片段结果集。
        :type TextSet: list of AiRecognitionTaskOcrFullTextSegmentTextItem
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TextSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TextSet") is not None:
            self.TextSet = []
            for item in params.get("TextSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentTextItem()
                obj._deserialize(item)
                self.TextSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextSegmentTextItem(AbstractModel):
    """文本全文识别片段。

    """

    def __init__(self):
        r"""
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoordSet: list of int
        :param Text: 识别文本。
        :type Text: str
        """
        self.Confidence = None
        self.AreaCoordSet = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResult(AbstractModel):
    """文本关键识别结果。

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 文本关键词识别任务输入信息。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResultInput`
        :param Output: 文本关键词识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultInput(AbstractModel):
    """文本关键词识别输入。

    """

    def __init__(self):
        r"""
        :param Definition: 文本关键词识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultItem(AbstractModel):
    """文本关键词识别结果。

    """

    def __init__(self):
        r"""
        :param Word: 文本关键词。
        :type Word: str
        :param SegmentSet: 文本关键出现的片段列表。
        :type SegmentSet: list of AiRecognitionTaskOcrWordsSegmentItem
        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultOutput(AbstractModel):
    """文本关键词识别输出。

    """

    def __init__(self):
        r"""
        :param ResultSet: 文本关键词识别结果集。
        :type ResultSet: list of AiRecognitionTaskOcrWordsResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskOcrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsSegmentItem(AbstractModel):
    """文本识别片段。

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskTransTextResult(AbstractModel):
    """翻译结果。

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 翻译任务输入信息。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskTransTextResultInput`
        :param Output: 翻译任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskTransTextResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskTransTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskTransTextResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskTransTextResultInput(AbstractModel):
    """翻译的输入。

    """

    def __init__(self):
        r"""
        :param Definition: 翻译模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskTransTextResultOutput(AbstractModel):
    """翻译结果。

    """

    def __init__(self):
        r"""
        :param SegmentSet: 翻译片段列表。
        :type SegmentSet: list of AiRecognitionTaskTransTextSegmentItem
        :param SubtitlePath: 字幕文件地址。
        :type SubtitlePath: str
        :param OutputStorage: 字幕文件存储位置。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.SegmentSet = None
        self.SubtitlePath = None
        self.OutputStorage = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskTransTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.SubtitlePath = params.get("SubtitlePath")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskTransTextSegmentItem(AbstractModel):
    """翻译片段。

    """

    def __init__(self):
        r"""
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Text: 识别文本。
        :type Text: str
        :param Trans: 翻译文本。
        :type Trans: str
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Text = None
        self.Trans = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Text = params.get("Text")
        self.Trans = params.get("Trans")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalAsrTaskInput(AbstractModel):
    """内容审核 Asr 文字敏感任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalAsrTaskOutput(AbstractModel):
    """Asr 文字敏感信息

    """

    def __init__(self):
        r"""
        :param Confidence: Asr 文字敏感评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Asr 文字敏感结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Asr 文字敏感嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字敏感任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalOcrTaskOutput(AbstractModel):
    """Ocr 文字敏感信息

    """

    def __init__(self):
        r"""
        :param Confidence: Ocr 文字敏感评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字敏感结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有敏感嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalTaskInput(AbstractModel):
    """内容审核敏感任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalTaskOutput(AbstractModel):
    """涉敏信息

    """

    def __init__(self):
        r"""
        :param Confidence: 视频涉敏评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: 涉敏结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Label: 视频涉敏结果标签。内容审核模板[画面涉敏任务控制参数](https://cloud.tencent.com/document/api/862/37615#AiReviewPoliticalTaskOutput)里 LabelSet 参数与此参数取值范围的对应关系：
violation_photo：
<li>violation_photo：违规图标。</li>
其他（即 politician/entertainment/sport/entrepreneur/scholar/celebrity/military）：
<li>politician：涉敏人物。</li>
        :type Label: str
        :param SegmentSet: 有涉敏嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewPoliticalSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewPoliticalSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornAsrTaskInput(AbstractModel):
    """内容审核 Asr 文字鉴黄任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 鉴黄模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornAsrTaskOutput(AbstractModel):
    """Asr 文字涉黄信息

    """

    def __init__(self):
        r"""
        :param Confidence: Asr 文字涉黄评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Asr 文字涉黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉黄嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴黄任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 鉴黄模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornOcrTaskOutput(AbstractModel):
    """Ocr 文字涉黄信息

    """

    def __init__(self):
        r"""
        :param Confidence: Ocr 文字涉黄评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉黄嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornTaskInput(AbstractModel):
    """内容审核鉴黄任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 鉴黄模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornTaskOutput(AbstractModel):
    """鉴黄结果信息

    """

    def __init__(self):
        r"""
        :param Confidence: 视频鉴黄评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: 鉴黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Label: 视频鉴黄结果标签，取值范围：
<li>porn：色情。</li>
<li>sexy：性感。</li>
<li>vulgar：低俗。</li>
<li>intimacy：亲密行为。</li>
        :type Label: str
        :param SegmentSet: 有涉黄嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedAsrTaskInput(AbstractModel):
    """内容审核 Asr 文字鉴违禁任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 鉴违禁模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedAsrTaskOutput(AbstractModel):
    """Asr 文字涉违禁信息

    """

    def __init__(self):
        r"""
        :param Confidence: Asr 文字涉违禁评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Asr 文字涉违禁结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉违禁嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴违禁任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 鉴违禁模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedOcrTaskOutput(AbstractModel):
    """Ocr 文字涉违禁信息

    """

    def __init__(self):
        r"""
        :param Confidence: Ocr 文字涉违禁评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉违禁结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉违禁嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalAsrResult(AbstractModel):
    """内容审核 Asr 文字敏感任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Asr 文字敏感任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalAsrTaskInput`
        :param Output: 内容审核 Asr 文字敏感任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalAsrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalOcrResult(AbstractModel):
    """内容审核 Ocr 文字敏感任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS，FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Ocr 文字敏感任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalOcrTaskInput`
        :param Output: 内容审核 Ocr 文字敏感任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalResult(AbstractModel):
    """内容审核涉敏任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核涉敏任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalTaskInput`
        :param Output: 内容审核涉敏任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornAsrResult(AbstractModel):
    """内容审核 Asr 文字鉴黄任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Asr 文字鉴黄任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPornAsrTaskInput`
        :param Output: 内容审核 Asr 文字鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPornAsrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴黄任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Ocr 文字鉴黄任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPornOcrTaskInput`
        :param Output: 内容审核 Ocr 文字鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPornOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornResult(AbstractModel):
    """内容审核鉴黄任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核鉴黄任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPornTaskInput`
        :param Output: 内容审核鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPornTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskProhibitedAsrResult(AbstractModel):
    """内容审核 Asr 文字鉴任违禁务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Asr 文字鉴违禁任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedAsrTaskInput`
        :param Output: 内容审核 Asr 文字鉴违禁任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedAsrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskProhibitedOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴任违禁务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Ocr 文字鉴违禁任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedOcrTaskInput`
        :param Output: 内容审核 Ocr 文字鉴违禁任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskTerrorismOcrResult(AbstractModel):
    """内容审核 Ocr 文字敏感任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Ocr 文字敏感任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismOcrTaskInput`
        :param Output: 内容审核 Ocr 文字敏感任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskTerrorismResult(AbstractModel):
    """内容审核涉敏任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核涉敏任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismTaskInput`
        :param Output: 内容审核涉敏任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字敏感任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismOcrTaskOutput(AbstractModel):
    """Ocr 文字涉敏信息

    """

    def __init__(self):
        r"""
        :param Confidence: Ocr 文字涉敏评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉敏结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉敏嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismTaskInput(AbstractModel):
    """内容审核涉敏任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismTaskOutput(AbstractModel):
    """涉敏信息

    """

    def __init__(self):
        r"""
        :param Confidence: 视频涉敏评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: 涉敏结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Label: 视频涉敏结果标签，取值范围：
<li>guns：武器枪支。</li>
<li>crowd：人群聚集。</li>
<li>police：警察部队。</li>
<li>bloody：血腥画面。</li>
<li>banners：涉敏旗帜。</li>
<li>militant：武装分子。</li>
<li>explosion：爆炸火灾。</li>
<li>terrorists：涉敏人物。</li>
<li>scenario：涉敏画面。</li>
        :type Label: str
        :param SegmentSet: 有涉敏嫌疑的视频片段列表。
        :type SegmentSet: list of MediaContentReviewSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFaceInfo(AbstractModel):
    """AI 样本管理，人脸信息。

    """

    def __init__(self):
        r"""
        :param FaceId: 人脸图片 ID。
        :type FaceId: str
        :param Url: 人脸图片地址。
        :type Url: str
        """
        self.FaceId = None
        self.Url = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFaceOperation(AbstractModel):
    """AI 样本管理，人脸数据操作。

    """

    def __init__(self):
        r"""
        :param Type: 操作类型，可选值：add（添加）、delete（删除）、reset（重置）。重置操作将清空该人物已有人脸数据，并添加 FaceContents 指定人脸数据。
        :type Type: str
        :param FaceIds: 人脸 ID 集合，当 Type为delete 时，该字段必填。
        :type FaceIds: list of str
        :param FaceContents: 人脸图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串集合。
<li>当 Type为add 或 reset 时，该字段必填；</li>
<li>数组长度限制：5 张图片。</li>
注意：图片必须是单人像正面人脸较清晰的照片，像素不低于 200*200。
        :type FaceContents: list of str
        """
        self.Type = None
        self.FaceIds = None
        self.FaceContents = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.FaceIds = params.get("FaceIds")
        self.FaceContents = params.get("FaceContents")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFailFaceInfo(AbstractModel):
    """AI 样本管理，处理失败的人脸信息

    """

    def __init__(self):
        r"""
        :param Index: 对应入参 FaceContents 中错误图片下标，从 0 开始。
        :type Index: int
        :param ErrCode: 错误码，取值：
<li>0：成功；</li>
<li>其他：失败。</li>
        :type ErrCode: int
        :param Message: 错误描述。
        :type Message: str
        """
        self.Index = None
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSamplePerson(AbstractModel):
    """AI 样本管理，人物信息。

    """

    def __init__(self):
        r"""
        :param PersonId: 人物 ID。
        :type PersonId: str
        :param Name: 人物名称。
        :type Name: str
        :param Description: 人物描述。
        :type Description: str
        :param FaceInfoSet: 人脸信息。
        :type FaceInfoSet: list of AiSampleFaceInfo
        :param TagSet: 人物标签。
        :type TagSet: list of str
        :param UsageSet: 应用场景。
        :type UsageSet: list of str
        :param CreateTime: 创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.FaceInfoSet = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = AiSampleFaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleTagOperation(AbstractModel):
    """AI 样本管理，标签操作。

    """

    def __init__(self):
        r"""
        :param Type: 操作类型，可选值：add（添加）、delete（删除）、reset（重置）。
        :type Type: str
        :param Tags: 标签，长度限制：128 个字符。
        :type Tags: list of str
        """
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleWord(AbstractModel):
    """AI 样本管理，关键词输出信息。

    """

    def __init__(self):
        r"""
        :param Keyword: 关键词。
        :type Keyword: str
        :param TagSet: 关键词标签。
        :type TagSet: list of str
        :param UsageSet: 关键词应用场景。
        :type UsageSet: list of str
        :param CreateTime: 创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.Keyword = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleWordInfo(AbstractModel):
    """AI 样本管理，关键词输入信息。

    """

    def __init__(self):
        r"""
        :param Keyword: 关键词，长度限制：20 个字符。
        :type Keyword: str
        :param Tags: 关键词标签
<li>数组长度限制：20 个标签；</li>
<li>单个标签长度限制：128 个字符。</li>
        :type Tags: list of str
        """
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnimatedGraphicTaskInput(AbstractModel):
    """转动图任务类型。

    """

    def __init__(self):
        r"""
        :param Definition: 视频转动图模板 ID。
        :type Definition: int
        :param StartTimeOffset: 动图在视频中的开始时间，单位为秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 动图在视频中的结束时间，单位为秒。
        :type EndTimeOffset: float
        :param OutputStorage: 转动图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 转动图后文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_animatedGraphic_{definition}.{format}`。
        :type OutputObjectPath: str
        """
        self.Definition = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.OutputStorage = None
        self.OutputObjectPath = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnimatedGraphicsTemplate(AbstractModel):
    """转动图模板详情。

    """

    def __init__(self):
        r"""
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 转动图模板名称。
        :type Name: str
        :param Comment: 转动图模板描述。
        :type Comment: str
        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 动图格式。
        :type Format: str
        :param Fps: 帧率。
        :type Fps: int
        :param Quality: 图片质量。
        :type Quality: float
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArtifactRepairConfig(AbstractModel):
    """去伪影（毛刺）配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Type: 类型，可选值：
<li>weak</li>
<li>strong</li>
默认值：weak。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Switch = None
        self.Type = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrFullTextConfigureInfo(AbstractModel):
    """语音全文识别任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 语音全文识别任务开关，可选值：
<li>ON：开启智能语音全文识别任务；</li>
<li>OFF：关闭智能语音全文识别任务。</li>
        :type Switch: str
        :param SubtitleFormat: 生成的字幕文件格式，不填或者填空字符串表示不生成字幕文件，可选值：
<li>vtt：生成 WebVTT 字幕文件。</li>
        :type SubtitleFormat: str
        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrFullTextConfigureInfoForUpdate(AbstractModel):
    """语音全文识别任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 语音全文识别任务开关，可选值：
<li>ON：开启智能语音全文识别任务；</li>
<li>OFF：关闭智能语音全文识别任务。</li>
        :type Switch: str
        :param SubtitleFormat: 生成的字幕文件格式，填空字符串表示不生成字幕文件，可选值：
<li>vtt：生成 WebVTT 字幕文件。</li>
        :type SubtitleFormat: str
        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrWordsConfigureInfo(AbstractModel):
    """语音关键词识别控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 语音关键词识别任务开关，可选值：
<li>ON：开启语音关键词识别任务；</li>
<li>OFF：关闭语音关键词识别任务。</li>
        :type Switch: str
        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrWordsConfigureInfoForUpdate(AbstractModel):
    """语音关键词识别控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 语音关键词识别任务开关，可选值：
<li>ON：开启语音关键词识别任务；</li>
<li>OFF：关闭语音关键词识别任务。</li>
        :type Switch: str
        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfo(AbstractModel):
    """音频流配置参数

    """

    def __init__(self):
        r"""
        :param Codec: 音频流的编码格式。
当外层参数 Container 为 mp3 时，可选值为：
<li>libmp3lame。</li>
当外层参数 Container 为 ogg 或 flac 时，可选值为：
<li>flac。</li>
当外层参数 Container 为 m4a 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
当外层参数 Container 为 mp4 或 flv 时，可选值为：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv。</li>
当外层参数 Container 为 hls 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>
        :type Codec: str
        :param Bitrate: 音频流的码率，取值范围：0 和 [26, 256]，单位：kbps。
当取值为 0，表示音频码率和原始音频保持一致。
        :type Bitrate: int
        :param SampleRate: 音频流的采样率，可选值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
单位：Hz。
        :type SampleRate: int
        :param AudioChannel: 音频通道方式，可选值：
<li>1：单通道</li>
<li>2：双通道</li>
<li>6：立体声</li>
当媒体的封装格式是音频格式时（flac，ogg，mp3，m4a）时，声道数不允许设为立体声。
默认值：2。
        :type AudioChannel: int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfoForUpdate(AbstractModel):
    """音频流配置参数

    """

    def __init__(self):
        r"""
        :param Codec: 音频流的编码格式。
当外层参数 Container 为 mp3 时，可选值为：
<li>libmp3lame。</li>
当外层参数 Container 为 ogg 或 flac 时，可选值为：
<li>flac。</li>
当外层参数 Container 为 m4a 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
当外层参数 Container 为 mp4 或 flv 时，可选值为：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
当外层参数 Container 为 hls 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>
        :type Codec: str
        :param Bitrate: 音频流的码率，取值范围：0 和 [26, 256]，单位：kbps。 当取值为 0，表示音频码率和原始音频保持一致。
        :type Bitrate: int
        :param SampleRate: 音频流的采样率，可选值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
单位：Hz。
        :type SampleRate: int
        :param AudioChannel: 音频通道方式，可选值：
<li>1：单通道</li>
<li>2：双通道</li>
<li>6：立体声</li>
当媒体的封装格式是音频格式时（flac，ogg，mp3，m4a）时，声道数不允许设为立体声。
        :type AudioChannel: int
        :param StreamSelects: 指定输出要保留的音频轨道。默认是全部保留源的。
        :type StreamSelects: list of int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None
        self.StreamSelects = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")
        self.StreamSelects = params.get("StreamSelects")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationConfigureInfo(AbstractModel):
    """智能分类任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 智能分类任务开关，可选值：
<li>ON：开启智能分类任务；</li>
<li>OFF：关闭智能分类任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationConfigureInfoForUpdate(AbstractModel):
    """智能分类任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 智能分类任务开关，可选值：
<li>ON：开启智能分类任务；</li>
<li>OFF：关闭智能分类任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ColorEnhanceConfig(AbstractModel):
    """色彩增强配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Type: 类型，可选值：
<li>weak</li>
<li>normal</li>
<li>strong</li>
默认值：weak。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Switch = None
        self.Type = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentReviewTemplateItem(AbstractModel):
    """内容审核模板详情

    """

    def __init__(self):
        r"""
        :param Definition: 内容审核模板唯一标识。
        :type Definition: int
        :param Name: 内容审核模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 内容审核模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param PornConfigure: 鉴黄控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornConfigure: :class:`tencentcloud.mps.v20190612.models.PornConfigureInfo`
        :param TerrorismConfigure: 涉敏控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorismConfigure: :class:`tencentcloud.mps.v20190612.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: 涉敏控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticalConfigure: :class:`tencentcloud.mps.v20190612.models.PoliticalConfigureInfo`
        :param ProhibitedConfigure: 违禁控制参数。违禁内容包括：
<li>谩骂；</li>
<li>涉毒违法。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ProhibitedConfigure: :class:`tencentcloud.mps.v20190612.models.ProhibitedConfigureInfo`
        :param UserDefineConfigure: 用户自定义内容审核控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDefineConfigure: :class:`tencentcloud.mps.v20190612.models.UserDefineConfigureInfo`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param Type: 模板类型，取值范围：
* Preset：系统预置模板；
* Custom：用户自定义模板。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Type = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosFileUploadTrigger(AbstractModel):
    """绑定到 COS 的输入规则。

    """

    def __init__(self):
        r"""
        :param Bucket: 工作流绑定的 COS Bucket 名，如 TopRankVideo-125xxx88。
        :type Bucket: str
        :param Region: 工作流绑定的 COS Bucket 所属园区，如 ap-chongiqng。
        :type Region: str
        :param Dir: 工作流绑定的输入路径目录，必须为绝对路径，即以 `/` 开头和结尾。如`/movie/201907/`，不填代表根目录`/`。
        :type Dir: str
        :param Formats: 工作流允许触发的文件格式列表，如 ["mp4", "flv", "mov"]。不填代表所有格式的文件都可以触发工作流。
        :type Formats: list of str
        """
        self.Bucket = None
        self.Region = None
        self.Dir = None
        self.Formats = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Dir = params.get("Dir")
        self.Formats = params.get("Formats")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosInputInfo(AbstractModel):
    """媒体处理 COS 对象信息。

    """

    def __init__(self):
        r"""
        :param Bucket: 媒体处理对象文件所在的 COS Bucket 名，如 TopRankVideo-125xxx88。
        :type Bucket: str
        :param Region: 媒体处理对象文件所在的 COS Bucket 所属园区，如 ap-chongqing。
        :type Region: str
        :param Object: 媒体处理对象文件的输入路径，如`/movie/201907/WildAnimal.mov`。
        :type Object: str
        """
        self.Bucket = None
        self.Region = None
        self.Object = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosOutputStorage(AbstractModel):
    """媒体处理 COS 输出对象信息。

    """

    def __init__(self):
        r"""
        :param Bucket: 媒体处理生成的文件输出的目标 Bucket 名，如 TopRankVideo-125xxx88。如果不填，表示继承上层。
        :type Bucket: str
        :param Region: 媒体处理生成的文件输出的目标 Bucket 的园区，如 ap-chongqing。如果不填，表示继承上层。
        :type Region: str
        """
        self.Bucket = None
        self.Region = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverConfigureInfo(AbstractModel):
    """智能封面任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 智能封面任务开关，可选值：
<li>ON：开启智能封面任务；</li>
<li>OFF：关闭智能封面任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverConfigureInfoForUpdate(AbstractModel):
    """智能封面任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 智能封面任务开关，可选值：
<li>ON：开启智能封面任务；</li>
<li>OFF：关闭智能封面任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAnalysisTemplateRequest(AbstractModel):
    """CreateAIAnalysisTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 视频内容分析模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 视频内容分析模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param ClassificationConfigure: 智能分类任务控制参数。
        :type ClassificationConfigure: :class:`tencentcloud.mps.v20190612.models.ClassificationConfigureInfo`
        :param TagConfigure: 智能标签任务控制参数。
        :type TagConfigure: :class:`tencentcloud.mps.v20190612.models.TagConfigureInfo`
        :param CoverConfigure: 智能封面任务控制参数。
        :type CoverConfigure: :class:`tencentcloud.mps.v20190612.models.CoverConfigureInfo`
        :param FrameTagConfigure: 智能按帧标签任务控制参数。
        :type FrameTagConfigure: :class:`tencentcloud.mps.v20190612.models.FrameTagConfigureInfo`
        """
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAnalysisTemplateResponse(AbstractModel):
    """CreateAIAnalysisTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 视频内容分析模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAIRecognitionTemplateRequest(AbstractModel):
    """CreateAIRecognitionTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 视频内容识别模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 视频内容识别模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param FaceConfigure: 人脸识别控制参数。
        :type FaceConfigure: :class:`tencentcloud.mps.v20190612.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: 文本全文识别控制参数。
        :type OcrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: 文本关键词识别控制参数。
        :type OcrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: 语音全文识别控制参数。
        :type AsrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: 语音关键词识别控制参数。
        :type AsrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.AsrWordsConfigureInfo`
        """
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIRecognitionTemplateResponse(AbstractModel):
    """CreateAIRecognitionTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 视频内容识别模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Format: 自适应转码格式，取值范围：
<li>HLS，</li>
<li>MPEG-DASH。</li>
        :type Format: str
        :param StreamInfos: 转自适应码流输出子流参数信息，最多输出10路子流。
注意：各个子流的帧率必须保持一致；如果不一致，采用第一个子流的帧率作为输出帧率。
        :type StreamInfos: list of AdaptiveStreamTemplate
        :param Name: 模板名称，长度限制：64 个字符。
        :type Name: str
        :param DisableHigherVideoBitrate: 是否禁止视频低码率转高码率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
默认为否。
        :type DisableHigherVideoBitrate: int
        :param DisableHigherVideoResolution: 是否禁止视频分辨率转高分辨率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
默认为否。
        :type DisableHigherVideoResolution: int
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Format = None
        self.StreamInfos = None
        self.Name = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.Comment = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Name = params.get("Name")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 自适应转码模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAnimatedGraphicsTemplateRequest(AbstractModel):
    """CreateAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Fps: 帧率，取值范围：[1, 30]，单位：Hz。
        :type Fps: int
        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 动图格式，取值为 gif 和 webp。默认为 gif。
        :type Format: str
        :param Quality: 图片质量，取值范围：[1, 100]，默认值为 75。
        :type Quality: float
        :param Name: 转动图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Fps = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Quality = None
        self.Name = None
        self.Comment = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Quality = params.get("Quality")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAnimatedGraphicsTemplateResponse(AbstractModel):
    """CreateAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateContentReviewTemplateRequest(AbstractModel):
    """CreateContentReviewTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 内容审核模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 内容审核模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param PornConfigure: 令人反感的信息的控制参数。
        :type PornConfigure: :class:`tencentcloud.mps.v20190612.models.PornConfigureInfo`
        :param TerrorismConfigure: 令人不安全的信息的控制参数。
        :type TerrorismConfigure: :class:`tencentcloud.mps.v20190612.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: 令人不适宜的信息的控制参数。
        :type PoliticalConfigure: :class:`tencentcloud.mps.v20190612.models.PoliticalConfigureInfo`
        :param ProhibitedConfigure: 违禁控制参数。违禁内容包括：
<li>谩骂；</li>
<li>涉毒违法。</li>
注意：此参数尚未支持。
        :type ProhibitedConfigure: :class:`tencentcloud.mps.v20190612.models.ProhibitedConfigureInfo`
        :param UserDefineConfigure: 用户自定义内容审核控制参数。
        :type UserDefineConfigure: :class:`tencentcloud.mps.v20190612.models.UserDefineConfigureInfo`
        """
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContentReviewTemplateResponse(AbstractModel):
    """CreateContentReviewTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 内容审核模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateImageSpriteTemplateRequest(AbstractModel):
    """CreateImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param SampleType: 采样类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param RowCount: 雪碧图中小图的行数。
        :type RowCount: int
        :param ColumnCount: 雪碧图中小图的列数。
        :type ColumnCount: int
        :param Name: 雪碧图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。
        :type FillType: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param Format: 图片格式，取值为 jpg、png、webp。默认为 jpg。
        :type Format: str
        """
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.FillType = None
        self.Comment = None
        self.Format = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageSpriteTemplateResponse(AbstractModel):
    """CreateImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateInput(AbstractModel):
    """创建输入的配置信息。

    """

    def __init__(self):
        r"""
        :param InputName: 输入名称，可填大小写、数字和下划线，长度为[1, 32]。
        :type InputName: str
        :param Protocol: 输入的协议，可选[SRT|RTP|RTMP|RTMP_PULL]。
        :type Protocol: str
        :param Description: 输入描述，长度为[0, 255]。
        :type Description: str
        :param AllowIpList: 输入的IP白名单，格式为CIDR。
        :type AllowIpList: list of str
        :param SRTSettings: 输入的SRT配置信息。
        :type SRTSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputSRTSettings`
        :param RTPSettings: 输入的RTP配置信息。
        :type RTPSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputRTPSettings`
        :param FailOver: 输入的主备开关，可选[OPEN|CLOSE]，默认为CLOSE。
        :type FailOver: str
        :param RTMPPullSettings: 输入的RTMP_PULL配置信息。
        :type RTMPPullSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputRTMPPullSettings`
        :param RTSPPullSettings: 输入的RTSP_PULL配置信息。
        :type RTSPPullSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputRTSPPullSettings`
        :param HLSPullSettings: 输入的HLS_PULL配置信息。
        :type HLSPullSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputHLSPullSettings`
        :param ResilientStream: 延播平滑吐流配置信息。
        :type ResilientStream: :class:`tencentcloud.mps.v20190612.models.ResilientStreamConf`
        """
        self.InputName = None
        self.Protocol = None
        self.Description = None
        self.AllowIpList = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.FailOver = None
        self.RTMPPullSettings = None
        self.RTSPPullSettings = None
        self.HLSPullSettings = None
        self.ResilientStream = None


    def _deserialize(self, params):
        self.InputName = params.get("InputName")
        self.Protocol = params.get("Protocol")
        self.Description = params.get("Description")
        self.AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateInputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateInputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        self.FailOver = params.get("FailOver")
        if params.get("RTMPPullSettings") is not None:
            self.RTMPPullSettings = CreateInputRTMPPullSettings()
            self.RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        if params.get("RTSPPullSettings") is not None:
            self.RTSPPullSettings = CreateInputRTSPPullSettings()
            self.RTSPPullSettings._deserialize(params.get("RTSPPullSettings"))
        if params.get("HLSPullSettings") is not None:
            self.HLSPullSettings = CreateInputHLSPullSettings()
            self.HLSPullSettings._deserialize(params.get("HLSPullSettings"))
        if params.get("ResilientStream") is not None:
            self.ResilientStream = ResilientStreamConf()
            self.ResilientStream._deserialize(params.get("ResilientStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputHLSPullSettings(AbstractModel):
    """创建的输入HLS拉流的配置信息。

    """

    def __init__(self):
        r"""
        :param SourceAddresses: HLS源站的源站地址，有且只能有一个。
        :type SourceAddresses: list of HLSPullSourceAddress
        """
        self.SourceAddresses = None


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = HLSPullSourceAddress()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputRTMPPullSettings(AbstractModel):
    """创建的输入RTMP拉流的配置信息。

    """

    def __init__(self):
        r"""
        :param SourceAddresses: RTMP源站的源站地址，有且只能有一个。
        :type SourceAddresses: list of RTMPPullSourceAddress
        """
        self.SourceAddresses = None


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = RTMPPullSourceAddress()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputRTPSettings(AbstractModel):
    """创建输入的RTP配置信息。

    """

    def __init__(self):
        r"""
        :param FEC: 默认为“none”，可选值['none']。
        :type FEC: str
        :param IdleTimeout: 空闲超时时间，默认5000，单位ms，范围为[1000, 10000]。
        :type IdleTimeout: int
        """
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputRTSPPullSettings(AbstractModel):
    """创建的输入RTSP拉流的配置信息。

    """

    def __init__(self):
        r"""
        :param SourceAddresses: RTSP源站的源站地址，有且只能有一个。
        :type SourceAddresses: list of RTSPPullSourceAddress
        """
        self.SourceAddresses = None


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = RTSPPullSourceAddress()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputSRTSettings(AbstractModel):
    """创建的输入SRT的配置信息。

    """

    def __init__(self):
        r"""
        :param Mode: SRT模式，可选[LISTENER|CALLER]，默认为LISTENER。
        :type Mode: str
        :param StreamId: 流Id，可选大小写字母、数字和特殊字符（.#!:&,=_-），长度为0~512。
        :type StreamId: str
        :param Latency: 延迟，默认0，单位ms，范围为[0, 3000]。
        :type Latency: int
        :param RecvLatency: 接收延迟，默认120，单位ms，范围为[0, 3000]。
        :type RecvLatency: int
        :param PeerLatency: 对端延迟，默认0，单位ms，范围为[0, 3000]。
        :type PeerLatency: int
        :param PeerIdleTimeout: 对端超时时间，默认5000，单位ms，范围为[1000, 10000]。
        :type PeerIdleTimeout: int
        :param Passphrase: 解密密钥，默认为空，表示不加密。只可填ascii码值，长度为[10, 79]。
        :type Passphrase: str
        :param PbKeyLen: 密钥长度，默认为0，可选[0|16|24|32]。
        :type PbKeyLen: int
        :param SourceAddresses: SRT对端地址，当Mode为CALLER时必填，且只能填1组。
        :type SourceAddresses: list of SRTSourceAddressReq
        """
        self.Mode = None
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None
        self.SourceAddresses = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = SRTSourceAddressReq()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfo(AbstractModel):
    """创建输出的配置信息。

    """

    def __init__(self):
        r"""
        :param OutputName: 输出的名称。
        :type OutputName: str
        :param Description: 输出描述。
        :type Description: str
        :param Protocol: 输出协议，可选[SRT|RTP|RTMP|RTMP_PULL]。
        :type Protocol: str
        :param OutputRegion: 输出地区。
        :type OutputRegion: str
        :param SRTSettings: 输出的SRT的配置。
        :type SRTSettings: :class:`tencentcloud.mps.v20190612.models.CreateOutputSRTSettings`
        :param RTMPSettings: 输出的RTMP的配置。
        :type RTMPSettings: :class:`tencentcloud.mps.v20190612.models.CreateOutputRTMPSettings`
        :param RTPSettings: 输出的RTP的配置。
        :type RTPSettings: :class:`tencentcloud.mps.v20190612.models.CreateOutputInfoRTPSettings`
        :param AllowIpList: IP白名单列表，格式为CIDR，如0.0.0.0/0。
当Protocol为RTMP_PULL有效，为空代表不限制客户端IP。
        :type AllowIpList: list of str
        """
        self.OutputName = None
        self.Description = None
        self.Protocol = None
        self.OutputRegion = None
        self.SRTSettings = None
        self.RTMPSettings = None
        self.RTPSettings = None
        self.AllowIpList = None


    def _deserialize(self, params):
        self.OutputName = params.get("OutputName")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        self.OutputRegion = params.get("OutputRegion")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateOutputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = CreateOutputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateOutputInfoRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        self.AllowIpList = params.get("AllowIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfoRTPSettings(AbstractModel):
    """创建媒体传输流的输出的RTP配置。

    """

    def __init__(self):
        r"""
        :param Destinations: 转推的目标地址，可填1~2个。
        :type Destinations: list of CreateOutputRTPSettingsDestinations
        :param FEC: 只能填none。
        :type FEC: str
        :param IdleTimeout: 空闲超时时间，单位ms。
        :type IdleTimeout: int
        """
        self.Destinations = None
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputRTPSettingsDestinations()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTMPSettings(AbstractModel):
    """创建媒体传输流的输出的RTMP配置。

    """

    def __init__(self):
        r"""
        :param Destinations: 转推的目标地址，可填1~2个。
        :type Destinations: list of CreateOutputRtmpSettingsDestinations
        :param ChunkSize: RTMP的Chunk大小，范围为[4096, 40960]。
        :type ChunkSize: int
        """
        self.Destinations = None
        self.ChunkSize = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputRtmpSettingsDestinations()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.ChunkSize = params.get("ChunkSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTPSettingsDestinations(AbstractModel):
    """创建媒体传输流的输出的RTP的目标地址。

    """

    def __init__(self):
        r"""
        :param Ip: 转推的目标IP。
        :type Ip: str
        :param Port: 转推的目标端口。
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRtmpSettingsDestinations(AbstractModel):
    """创建媒体传输流的输出的RTMP的目标地址。

    """

    def __init__(self):
        r"""
        :param Url: 转推的URL，格式如：rtmp://domain/live。
        :type Url: str
        :param StreamKey: 转推的StreamKey，格式如：stream?key=value。
        :type StreamKey: str
        """
        self.Url = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSRTSettings(AbstractModel):
    """创建媒体传输流的输出的SRT配置。

    """

    def __init__(self):
        r"""
        :param Destinations: 转推的目标地址，当Mode为CALLER时必填，且只能填1组。
        :type Destinations: list of CreateOutputSRTSettingsDestinations
        :param StreamId: 转推SRT的流Id，可选大小写字母、数字和特殊字符（.#!:&,=_-），长度为0~512。
        :type StreamId: str
        :param Latency: 转推SRT的总延迟，默认0，单位ms，范围为[0, 3000]。
        :type Latency: int
        :param RecvLatency: 转推SRT的接收延迟，默认120，单位ms，范围为[0, 3000]。
        :type RecvLatency: int
        :param PeerLatency: 转推SRT的对端延迟，默认0，单位ms，范围为[0, 3000]。
        :type PeerLatency: int
        :param PeerIdleTimeout: 转推SRT的对端空闲超时时间，默认5000，单位ms，范围为[1000, 10000]。
        :type PeerIdleTimeout: int
        :param Passphrase: 转推SRT的加密密钥，默认为空，表示不加密。只可填ascii码值，长度为[10, 79]。
        :type Passphrase: str
        :param PbKeyLen: 转推SRT的密钥长度，默认为0，可选[0|16|24|32]。
        :type PbKeyLen: int
        :param Mode: SRT模式，可选[LISTENER|CALLER]，默认为CALLER。
        :type Mode: str
        """
        self.Destinations = None
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None
        self.Mode = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputSRTSettingsDestinations()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSRTSettingsDestinations(AbstractModel):
    """创建媒体传输流的输出SRT的目标地址。

    """

    def __init__(self):
        r"""
        :param Ip: 输出的IP。
        :type Ip: str
        :param Port: 输出的端口。
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonSampleRequest(AbstractModel):
    """CreatePersonSample请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 素材名称，长度限制：20 个字符。
        :type Name: str
        :param Usages: 素材应用场景，可选值：
1. Recognition：用于内容识别，等价于 Recognition.Face。
2. Review：用于不适宜内容识别，等价于 Review.Face。
3. All：包含以上全部，等价于 1+2。
        :type Usages: list of str
        :param Description: 素材描述，长度限制：1024 个字符。
        :type Description: str
        :param FaceContents: 素材图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串，仅支持 jpeg、png 图片格式。数组长度限制：5 张图片。
注意：图片必须是单人像五官较清晰的照片，像素不低于 200*200。
        :type FaceContents: list of str
        :param Tags: 素材标签
<li>数组长度限制：20 个标签；</li>
<li>单个标签长度限制：128 个字符。</li>
        :type Tags: list of str
        """
        self.Name = None
        self.Usages = None
        self.Description = None
        self.FaceContents = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usages = params.get("Usages")
        self.Description = params.get("Description")
        self.FaceContents = params.get("FaceContents")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonSampleResponse(AbstractModel):
    """CreatePersonSample返回参数结构体

    """

    def __init__(self):
        r"""
        :param Person: 素材信息。
        :type Person: :class:`tencentcloud.mps.v20190612.models.AiSamplePerson`
        :param FailFaceInfoSet: 处理失败的五官定位信息。
        :type FailFaceInfoSet: list of AiSampleFailFaceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateSampleSnapshotTemplateRequest(AbstractModel):
    """CreateSampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param SampleType: 采样截图类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param Name: 采样截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式，取值为 jpg、png、webp。默认为 jpg。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.SampleType = None
        self.SampleInterval = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSampleSnapshotTemplateResponse(AbstractModel):
    """CreateSampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 指定时间点截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式，取值可以为 jpg、png、webp。默认为 jpg。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 时间点截图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateStreamLinkFlowRequest(AbstractModel):
    """CreateStreamLinkFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowName: 流名称。
        :type FlowName: str
        :param MaxBandwidth: 最大带宽，单位bps，可选[10000000, 20000000, 50000000]。
        :type MaxBandwidth: int
        :param InputGroup: 流的输入组。
        :type InputGroup: list of CreateInput
        """
        self.FlowName = None
        self.MaxBandwidth = None
        self.InputGroup = None


    def _deserialize(self, params):
        self.FlowName = params.get("FlowName")
        self.MaxBandwidth = params.get("MaxBandwidth")
        if params.get("InputGroup") is not None:
            self.InputGroup = []
            for item in params.get("InputGroup"):
                obj = CreateInput()
                obj._deserialize(item)
                self.InputGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkFlowResponse(AbstractModel):
    """CreateStreamLinkFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 创建的Flow信息。
        :type Info: :class:`tencentcloud.mps.v20190612.models.DescribeFlow`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeFlow()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class CreateStreamLinkOutputInfoRequest(AbstractModel):
    """CreateStreamLinkOutputInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 传输流Id。
        :type FlowId: str
        :param Output: 传输流的Output配置。
        :type Output: :class:`tencentcloud.mps.v20190612.models.CreateOutputInfo`
        """
        self.FlowId = None
        self.Output = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self.Output = CreateOutputInfo()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkOutputInfoResponse(AbstractModel):
    """CreateStreamLinkOutputInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 创建后的Output信息。
        :type Info: :class:`tencentcloud.mps.v20190612.models.DescribeOutput`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeOutput()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class CreateTranscodeTemplateRequest(AbstractModel):
    """CreateTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。
        :type Container: str
        :param Name: 转码模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
默认值：0。
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
默认值：0。
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数，当 RemoveVideo 为 0，该字段必填。
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: 音频流配置参数，当 RemoveAudio 为 0，该字段必填。
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: 极速高清转码参数。
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`
        :param EnhanceConfig: 音视频增强配置。
        :type EnhanceConfig: :class:`tencentcloud.mps.v20190612.models.EnhanceConfig`
        """
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.EnhanceConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        if params.get("EnhanceConfig") is not None:
            self.EnhanceConfig = EnhanceConfig()
            self.EnhanceConfig._deserialize(params.get("EnhanceConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeTemplateResponse(AbstractModel):
    """CreateTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 转码模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateWatermarkTemplateRequest(AbstractModel):
    """CreateWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 水印类型，可选值：
<li>image：图片水印；</li>
<li>text：文字水印；</li>
<li>svg：SVG 水印。</li>
        :type Type: str
        :param Name: 水印模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param CoordinateOrigin: 原点位置，可选值：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>
默认值：TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。
        :type XPos: str
        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。
        :type YPos: str
        :param ImageTemplate: 图片水印模板，仅当 Type 为 image，该字段必填且有效。
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkInput`
        :param TextTemplate: 文字水印模板，仅当 Type 为 text，该字段必填且有效。
        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG 水印模板，仅当 Type 为 svg，该字段必填且有效。
        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInput`
        """
        self.Type = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWatermarkTemplateResponse(AbstractModel):
    """CreateWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param ImageUrl: 水印图片地址，仅当 Type 为 image，该字段有效。
        :type ImageUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class CreateWordSamplesRequest(AbstractModel):
    """CreateWordSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param Usages: <b>关键词应用场景，可选值：</b>
1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；
2. Recognition.Asr：通过音频识别技术，进行内容识别；
3. Review.Ocr：通过光学字符识别技术，进行不适宜内容识别；
4. Review.Asr：通过音频识别技术，进行不适宜内容识别；
<b>可合并简写为：</b>
5. Recognition：通过光学字符识别技术、音频识别技术，进行内容识别，等价于 1+2；
6. Review：通过光学字符识别技术、音频识别技术，进行不适宜内容识别，等价于 3+4；
7. All：通过光学字符识别技术、音频识别技术，进行内容识别、不适宜内容识别，等价于 1+2+3+4。
        :type Usages: list of str
        :param Words: 关键词，数组长度限制：100。
        :type Words: list of AiSampleWordInfo
        """
        self.Usages = None
        self.Words = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = AiSampleWordInfo()
                obj._deserialize(item)
                self.Words.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWordSamplesResponse(AbstractModel):
    """CreateWordSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWorkflowRequest(AbstractModel):
    """CreateWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkflowName: 工作流名称，最多128字符。同一个用户该名称唯一。
        :type WorkflowName: str
        :param Trigger: 工作流绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。
        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: 媒体处理的文件输出存储位置。不填则继承 Trigger 中的存储位置。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 媒体处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致。
        :type OutputDir: str
        :param MediaProcessTask: 媒体处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 视频内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 视频内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 视频内容识别类型任务参数。
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: 任务的事件通知配置，不填代表不获取事件通知。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TaskPriority: 工作流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TaskPriority: int
        """
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None


    def _deserialize(self, params):
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowResponse(AbstractModel):
    """CreateWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkflowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.RequestId = params.get("RequestId")


class DeleteAIAnalysisTemplateRequest(AbstractModel):
    """DeleteAIAnalysisTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 视频内容分析模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIAnalysisTemplateResponse(AbstractModel):
    """DeleteAIAnalysisTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAIRecognitionTemplateRequest(AbstractModel):
    """DeleteAIRecognitionTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 视频内容识别模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIRecognitionTemplateResponse(AbstractModel):
    """DeleteAIRecognitionTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 自适应转码模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAnimatedGraphicsTemplateRequest(AbstractModel):
    """DeleteAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAnimatedGraphicsTemplateResponse(AbstractModel):
    """DeleteAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteContentReviewTemplateRequest(AbstractModel):
    """DeleteContentReviewTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 内容审核模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteContentReviewTemplateResponse(AbstractModel):
    """DeleteContentReviewTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageSpriteTemplateRequest(AbstractModel):
    """DeleteImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageSpriteTemplateResponse(AbstractModel):
    """DeleteImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonSampleRequest(AbstractModel):
    """DeletePersonSample请求参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 素材 ID。
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonSampleResponse(AbstractModel):
    """DeletePersonSample返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSampleSnapshotTemplateRequest(AbstractModel):
    """DeleteSampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSampleSnapshotTemplateResponse(AbstractModel):
    """DeleteSampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 指定时间点截图模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStreamLinkFlowRequest(AbstractModel):
    """DeleteStreamLinkFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 传输流Id。
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLinkFlowResponse(AbstractModel):
    """DeleteStreamLinkFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStreamLinkOutputRequest(AbstractModel):
    """DeleteStreamLinkOutput请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流Id。
        :type FlowId: str
        :param OutputId: 输出Id。
        :type OutputId: str
        """
        self.FlowId = None
        self.OutputId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.OutputId = params.get("OutputId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLinkOutputResponse(AbstractModel):
    """DeleteStreamLinkOutput返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTranscodeTemplateRequest(AbstractModel):
    """DeleteTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 转码模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTranscodeTemplateResponse(AbstractModel):
    """DeleteTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWatermarkTemplateRequest(AbstractModel):
    """DeleteWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWatermarkTemplateResponse(AbstractModel):
    """DeleteWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWordSamplesRequest(AbstractModel):
    """DeleteWordSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param Keywords: 关键词，数组长度限制：100 个词。
        :type Keywords: list of str
        """
        self.Keywords = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWordSamplesResponse(AbstractModel):
    """DeleteWordSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWorkflowRequest(AbstractModel):
    """DeleteWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowResponse(AbstractModel):
    """DeleteWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAIAnalysisTemplatesRequest(AbstractModel):
    """DescribeAIAnalysisTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 视频内容分析模板唯一标识过滤条件，数组长度限制：10。
        :type Definitions: list of int
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，不填则返回所有，可选值：
* Preset：系统预置模板；
* Custom：用户自定义模板。
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIAnalysisTemplatesResponse(AbstractModel):
    """DescribeAIAnalysisTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param AIAnalysisTemplateSet: 视频内容分析模板详情列表。
        :type AIAnalysisTemplateSet: list of AIAnalysisTemplateItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AIAnalysisTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIAnalysisTemplateSet") is not None:
            self.AIAnalysisTemplateSet = []
            for item in params.get("AIAnalysisTemplateSet"):
                obj = AIAnalysisTemplateItem()
                obj._deserialize(item)
                self.AIAnalysisTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAIRecognitionTemplatesRequest(AbstractModel):
    """DescribeAIRecognitionTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 视频内容识别模板唯一标识过滤条件，数组长度限制：10。
        :type Definitions: list of int
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：50。
        :type Limit: int
        :param Type: 模板类型过滤条件，不填则返回所有，可选值：
* Preset：系统预置模板；
* Custom：用户自定义模板。
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIRecognitionTemplatesResponse(AbstractModel):
    """DescribeAIRecognitionTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param AIRecognitionTemplateSet: 视频内容识别模板详情列表。
        :type AIRecognitionTemplateSet: list of AIRecognitionTemplateItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AIRecognitionTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIRecognitionTemplateSet") is not None:
            self.AIRecognitionTemplateSet = []
            for item in params.get("AIRecognitionTemplateSet"):
                obj = AIRecognitionTemplateItem()
                obj._deserialize(item)
                self.AIRecognitionTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAdaptiveDynamicStreamingTemplatesRequest(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 转自适应码流模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAdaptiveDynamicStreamingTemplatesResponse(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param AdaptiveDynamicStreamingTemplateSet: 转自适应码流模板详情列表。
        :type AdaptiveDynamicStreamingTemplateSet: list of AdaptiveDynamicStreamingTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AdaptiveDynamicStreamingTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AdaptiveDynamicStreamingTemplateSet") is not None:
            self.AdaptiveDynamicStreamingTemplateSet = []
            for item in params.get("AdaptiveDynamicStreamingTemplateSet"):
                obj = AdaptiveDynamicStreamingTemplate()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAnimatedGraphicsTemplatesRequest(AbstractModel):
    """DescribeAnimatedGraphicsTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 转动图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAnimatedGraphicsTemplatesResponse(AbstractModel):
    """DescribeAnimatedGraphicsTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param AnimatedGraphicsTemplateSet: 转动图模板详情列表。
        :type AnimatedGraphicsTemplateSet: list of AnimatedGraphicsTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AnimatedGraphicsTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AnimatedGraphicsTemplateSet") is not None:
            self.AnimatedGraphicsTemplateSet = []
            for item in params.get("AnimatedGraphicsTemplateSet"):
                obj = AnimatedGraphicsTemplate()
                obj._deserialize(item)
                self.AnimatedGraphicsTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeContentReviewTemplatesRequest(AbstractModel):
    """DescribeContentReviewTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 智能审核模板唯一标识过滤条件，数组长度限制：50。
        :type Definitions: list of int
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：50。
        :type Limit: int
        :param Type: 模板类型过滤条件，不填则返回所有，可选值：
* Preset：系统预置模板；
* Custom：用户自定义模板。
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContentReviewTemplatesResponse(AbstractModel):
    """DescribeContentReviewTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param ContentReviewTemplateSet: 内容审核模板详情列表。
        :type ContentReviewTemplateSet: list of ContentReviewTemplateItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ContentReviewTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ContentReviewTemplateSet") is not None:
            self.ContentReviewTemplateSet = []
            for item in params.get("ContentReviewTemplateSet"):
                obj = ContentReviewTemplateItem()
                obj._deserialize(item)
                self.ContentReviewTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlow(AbstractModel):
    """查询Flow的配置信息。

    """

    def __init__(self):
        r"""
        :param FlowId: 流Id。
        :type FlowId: str
        :param FlowName: 流名称。
        :type FlowName: str
        :param State: 流状态，目前有IDLE/RUNNING。
        :type State: str
        :param MaxBandwidth: 最大带宽值。
        :type MaxBandwidth: int
        :param InputGroup: 输入组。
        :type InputGroup: list of DescribeInput
        :param OutputGroup: 输出组。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputGroup: list of DescribeOutput
        """
        self.FlowId = None
        self.FlowName = None
        self.State = None
        self.MaxBandwidth = None
        self.InputGroup = None
        self.OutputGroup = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")
        self.State = params.get("State")
        self.MaxBandwidth = params.get("MaxBandwidth")
        if params.get("InputGroup") is not None:
            self.InputGroup = []
            for item in params.get("InputGroup"):
                obj = DescribeInput()
                obj._deserialize(item)
                self.InputGroup.append(obj)
        if params.get("OutputGroup") is not None:
            self.OutputGroup = []
            for item in params.get("OutputGroup"):
                obj = DescribeOutput()
                obj._deserialize(item)
                self.OutputGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHLSPullSourceAddress(AbstractModel):
    """查询输入的HLS配置信息。

    """

    def __init__(self):
        r"""
        :param Url: HLS源站的Url地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSpriteTemplatesRequest(AbstractModel):
    """DescribeImageSpriteTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 雪碧图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSpriteTemplatesResponse(AbstractModel):
    """DescribeImageSpriteTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param ImageSpriteTemplateSet: 雪碧图模板详情列表。
        :type ImageSpriteTemplateSet: list of ImageSpriteTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageSpriteTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSpriteTemplateSet") is not None:
            self.ImageSpriteTemplateSet = []
            for item in params.get("ImageSpriteTemplateSet"):
                obj = ImageSpriteTemplate()
                obj._deserialize(item)
                self.ImageSpriteTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInput(AbstractModel):
    """查询输入配置信息。

    """

    def __init__(self):
        r"""
        :param InputId: 输入Id。
        :type InputId: str
        :param InputName: 输入名称。
        :type InputName: str
        :param Description: 输入描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Protocol: 输入协议。
        :type Protocol: str
        :param InputAddressList: 输入地址列表。
        :type InputAddressList: list of InputAddress
        :param AllowIpList: 输入IP白名单列表。
        :type AllowIpList: list of str
        :param SRTSettings: 输入的SRT配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SRTSettings: :class:`tencentcloud.mps.v20190612.models.DescribeInputSRTSettings`
        :param RTPSettings: 输入的RTP配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTPSettings: :class:`tencentcloud.mps.v20190612.models.DescribeInputRTPSettings`
        :param InputRegion: 输入的地区。
        :type InputRegion: str
        :param RTMPSettings: 输入的RTMP配置信息。
        :type RTMPSettings: :class:`tencentcloud.mps.v20190612.models.DescribeInputRTMPSettings`
        :param FailOver: 输入的主备开关。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailOver: str
        :param RTMPPullSettings: 输入的RTMP_PULL配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTMPPullSettings: :class:`tencentcloud.mps.v20190612.models.DescribeInputRTMPPullSettings`
        :param RTSPPullSettings: 输入的RTSP_PULL配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTSPPullSettings: :class:`tencentcloud.mps.v20190612.models.DescribeInputRTSPPullSettings`
        :param HLSPullSettings: 输入的HLS_PULL配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type HLSPullSettings: :class:`tencentcloud.mps.v20190612.models.DescribeInputHLSPullSettings`
        :param ResilientStream: 延播平滑吐流配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResilientStream: :class:`tencentcloud.mps.v20190612.models.ResilientStreamConf`
        """
        self.InputId = None
        self.InputName = None
        self.Description = None
        self.Protocol = None
        self.InputAddressList = None
        self.AllowIpList = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.InputRegion = None
        self.RTMPSettings = None
        self.FailOver = None
        self.RTMPPullSettings = None
        self.RTSPPullSettings = None
        self.HLSPullSettings = None
        self.ResilientStream = None


    def _deserialize(self, params):
        self.InputId = params.get("InputId")
        self.InputName = params.get("InputName")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        if params.get("InputAddressList") is not None:
            self.InputAddressList = []
            for item in params.get("InputAddressList"):
                obj = InputAddress()
                obj._deserialize(item)
                self.InputAddressList.append(obj)
        self.AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = DescribeInputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = DescribeInputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        self.InputRegion = params.get("InputRegion")
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = DescribeInputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))
        self.FailOver = params.get("FailOver")
        if params.get("RTMPPullSettings") is not None:
            self.RTMPPullSettings = DescribeInputRTMPPullSettings()
            self.RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        if params.get("RTSPPullSettings") is not None:
            self.RTSPPullSettings = DescribeInputRTSPPullSettings()
            self.RTSPPullSettings._deserialize(params.get("RTSPPullSettings"))
        if params.get("HLSPullSettings") is not None:
            self.HLSPullSettings = DescribeInputHLSPullSettings()
            self.HLSPullSettings._deserialize(params.get("HLSPullSettings"))
        if params.get("ResilientStream") is not None:
            self.ResilientStream = ResilientStreamConf()
            self.ResilientStream._deserialize(params.get("ResilientStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputHLSPullSettings(AbstractModel):
    """查询输入的HLS配置信息。

    """

    def __init__(self):
        r"""
        :param SourceAddresses: HLS源站地址信息。
        :type SourceAddresses: list of DescribeHLSPullSourceAddress
        """
        self.SourceAddresses = None


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = DescribeHLSPullSourceAddress()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTMPPullSettings(AbstractModel):
    """查询输入的RTMP配置信息。

    """

    def __init__(self):
        r"""
        :param SourceAddresses: RTMP源站地址信息。
        :type SourceAddresses: list of DescribeRTMPPullSourceAddress
        """
        self.SourceAddresses = None


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = DescribeRTMPPullSourceAddress()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTMPSettings(AbstractModel):
    """查询输入的RTMP配置信息。

    """

    def __init__(self):
        r"""
        :param AppName: RTMP的推流路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param StreamKey: RTMP的推流StreamKey。
RTMP的推流地址拼接规则为：rtmp://Ip:1935/AppName/StreamKey
        :type StreamKey: str
        """
        self.AppName = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTPSettings(AbstractModel):
    """查询输入的RTP配置信息。

    """

    def __init__(self):
        r"""
        :param FEC: 是否FEC。
        :type FEC: str
        :param IdleTimeout: 空闲超时时间。
        :type IdleTimeout: int
        """
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTSPPullSettings(AbstractModel):
    """查询输入的RTSP配置信息。

    """

    def __init__(self):
        r"""
        :param SourceAddresses: RTSP源站地址信息。
        :type SourceAddresses: list of DescribeRTSPPullSourceAddress
        """
        self.SourceAddresses = None


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = DescribeRTSPPullSourceAddress()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputSRTSettings(AbstractModel):
    """查询输入的SRT配置信息。

    """

    def __init__(self):
        r"""
        :param Mode: SRT模式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param StreamId: 流Id。
        :type StreamId: str
        :param Latency: 延迟。
        :type Latency: int
        :param RecvLatency: 接收延迟。
        :type RecvLatency: int
        :param PeerLatency: 对端延迟。
        :type PeerLatency: int
        :param PeerIdleTimeout: 对端空闲超时时间。
        :type PeerIdleTimeout: int
        :param Passphrase: 解密密钥。
        :type Passphrase: str
        :param PbKeyLen: 密钥长度。
        :type PbKeyLen: int
        :param SourceAddresses: SRT对端地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAddresses: list of SRTSourceAddressResp
        """
        self.Mode = None
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None
        self.SourceAddresses = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = SRTSourceAddressResp()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaMetaDataRequest(AbstractModel):
    """DescribeMediaMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param InputInfo: 需要获取元信息的文件输入信息。
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        """
        self.InputInfo = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaMetaDataResponse(AbstractModel):
    """DescribeMediaMetaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetaData: 媒体元信息。
        :type MetaData: :class:`tencentcloud.mps.v20190612.models.MediaMetaData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class DescribeOutput(AbstractModel):
    """查询输出的配置信息。

    """

    def __init__(self):
        r"""
        :param OutputId: 输出Id。
        :type OutputId: str
        :param OutputName: 输出名称。
        :type OutputName: str
        :param OutputType: 输出类型。
        :type OutputType: str
        :param Description: 输出描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Protocol: 输出协议。
        :type Protocol: str
        :param OutputAddressList: 输出的出口地址信息列表。
        :type OutputAddressList: list of OutputAddress
        :param OutputRegion: 输出的地区。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputRegion: str
        :param SRTSettings: 输出的SRT配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SRTSettings: :class:`tencentcloud.mps.v20190612.models.DescribeOutputSRTSettings`
        :param RTPSettings: 输出的RTP配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTPSettings: :class:`tencentcloud.mps.v20190612.models.DescribeOutputRTPSettings`
        :param RTMPSettings: 输出的RTMP配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTMPSettings: :class:`tencentcloud.mps.v20190612.models.DescribeOutputRTMPSettings`
        :param RTMPPullSettings: 输出的RTMP拉流配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTMPPullSettings: :class:`tencentcloud.mps.v20190612.models.DescribeOutputRTMPPullSettings`
        :param AllowIpList: CIDR白名单列表。
当Protocol为RTMP_PULL有效，为空代表不限制客户端IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowIpList: list of str
        :param RTSPPullSettings: 输出的RTSP拉流配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTSPPullSettings: :class:`tencentcloud.mps.v20190612.models.DescribeOutputRTSPPullSettings`
        :param HLSPullSettings: 输出的HLS拉流配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type HLSPullSettings: :class:`tencentcloud.mps.v20190612.models.DescribeOutputHLSPullSettings`
        """
        self.OutputId = None
        self.OutputName = None
        self.OutputType = None
        self.Description = None
        self.Protocol = None
        self.OutputAddressList = None
        self.OutputRegion = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.RTMPSettings = None
        self.RTMPPullSettings = None
        self.AllowIpList = None
        self.RTSPPullSettings = None
        self.HLSPullSettings = None


    def _deserialize(self, params):
        self.OutputId = params.get("OutputId")
        self.OutputName = params.get("OutputName")
        self.OutputType = params.get("OutputType")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        if params.get("OutputAddressList") is not None:
            self.OutputAddressList = []
            for item in params.get("OutputAddressList"):
                obj = OutputAddress()
                obj._deserialize(item)
                self.OutputAddressList.append(obj)
        self.OutputRegion = params.get("OutputRegion")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = DescribeOutputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = DescribeOutputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = DescribeOutputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))
        if params.get("RTMPPullSettings") is not None:
            self.RTMPPullSettings = DescribeOutputRTMPPullSettings()
            self.RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        self.AllowIpList = params.get("AllowIpList")
        if params.get("RTSPPullSettings") is not None:
            self.RTSPPullSettings = DescribeOutputRTSPPullSettings()
            self.RTSPPullSettings._deserialize(params.get("RTSPPullSettings"))
        if params.get("HLSPullSettings") is not None:
            self.HLSPullSettings = DescribeOutputHLSPullSettings()
            self.HLSPullSettings._deserialize(params.get("HLSPullSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputHLSPullServerUrl(AbstractModel):
    """查询输出的HLS拉流URL信息。

    """

    def __init__(self):
        r"""
        :param Url: HLS拉流地址的Url。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputHLSPullSettings(AbstractModel):
    """查询输出的HLS拉流配置信息。

    """

    def __init__(self):
        r"""
        :param ServerUrls: HLS拉流地址列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerUrls: list of DescribeOutputHLSPullServerUrl
        """
        self.ServerUrls = None


    def _deserialize(self, params):
        if params.get("ServerUrls") is not None:
            self.ServerUrls = []
            for item in params.get("ServerUrls"):
                obj = DescribeOutputHLSPullServerUrl()
                obj._deserialize(item)
                self.ServerUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPPullServerUrl(AbstractModel):
    """查询输出的RTMP拉流URL信息。

    """

    def __init__(self):
        r"""
        :param TcUrl: RTMP拉流地址的tcUrl。
        :type TcUrl: str
        :param StreamKey: RTMP拉流地址的流key。
        :type StreamKey: str
        """
        self.TcUrl = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.TcUrl = params.get("TcUrl")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPPullSettings(AbstractModel):
    """查询输出的RTMP拉流配置信息。

    """

    def __init__(self):
        r"""
        :param ServerUrls: 拉流地址列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerUrls: list of DescribeOutputRTMPPullServerUrl
        """
        self.ServerUrls = None


    def _deserialize(self, params):
        if params.get("ServerUrls") is not None:
            self.ServerUrls = []
            for item in params.get("ServerUrls"):
                obj = DescribeOutputRTMPPullServerUrl()
                obj._deserialize(item)
                self.ServerUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPSettings(AbstractModel):
    """查询输出的RTMP配置信息。

    """

    def __init__(self):
        r"""
        :param IdleTimeout: 空闲超时时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdleTimeout: int
        :param ChunkSize: Chunk大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChunkSize: int
        :param Destinations: 转推RTMP的目标地址信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Destinations: list of RTMPAddressDestination
        """
        self.IdleTimeout = None
        self.ChunkSize = None
        self.Destinations = None


    def _deserialize(self, params):
        self.IdleTimeout = params.get("IdleTimeout")
        self.ChunkSize = params.get("ChunkSize")
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = RTMPAddressDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTPSettings(AbstractModel):
    """查询输出的RTP配置信息。

    """

    def __init__(self):
        r"""
        :param Destinations: 转推RTP的目标地址信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Destinations: list of RTPAddressDestination
        :param FEC: 是否FEC。
注意：此字段可能返回 null，表示取不到有效值。
        :type FEC: str
        :param IdleTimeout: 空闲超时时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdleTimeout: int
        """
        self.Destinations = None
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = RTPAddressDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTSPPullServerUrl(AbstractModel):
    """查询输出的RTSP拉流URL信息。

    """

    def __init__(self):
        r"""
        :param Url: RTSP拉流地址的Url。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTSPPullSettings(AbstractModel):
    """查询输出的RTSP拉流配置信息。

    """

    def __init__(self):
        r"""
        :param ServerUrls: RTSP拉流地址列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerUrls: list of DescribeOutputRTSPPullServerUrl
        """
        self.ServerUrls = None


    def _deserialize(self, params):
        if params.get("ServerUrls") is not None:
            self.ServerUrls = []
            for item in params.get("ServerUrls"):
                obj = DescribeOutputRTSPPullServerUrl()
                obj._deserialize(item)
                self.ServerUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputSRTSettings(AbstractModel):
    """查询输出的SRT配置信息。

    """

    def __init__(self):
        r"""
        :param Destinations: 转推的目标的地址信息列表，SRT模式为CALLER时使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Destinations: list of SRTAddressDestination
        :param StreamId: 流Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamId: str
        :param Latency: 延迟。
注意：此字段可能返回 null，表示取不到有效值。
        :type Latency: int
        :param RecvLatency: 接收延迟。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecvLatency: int
        :param PeerLatency: 对端延迟。
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerLatency: int
        :param PeerIdleTimeout: 对端空闲超时时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerIdleTimeout: int
        :param Passphrase: 加密密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type Passphrase: str
        :param PbKeyLen: 加密密钥长度。
注意：此字段可能返回 null，表示取不到有效值。
        :type PbKeyLen: int
        :param Mode: SRT模式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param SourceAddresses: 服务器监听地址，SRT模式为LISTENER时使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAddresses: list of OutputSRTSourceAddressResp
        """
        self.Destinations = None
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None
        self.Mode = None
        self.SourceAddresses = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = SRTAddressDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
        self.Mode = params.get("Mode")
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = OutputSRTSourceAddressResp()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonSamplesRequest(AbstractModel):
    """DescribePersonSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 拉取的素材类型，可选值：
<li>UserDefine：用户自定义素材库；</li>
<li>Default：系统默认素材库。</li>

默认值：UserDefine，拉取用户自定义素材库素材。
说明：如果是拉取系统默认素材库，只能使用素材名字或者素材 ID + 素材名字的方式进行拉取，且人脸图片只返回一张。
        :type Type: str
        :param PersonIds: 素材 ID，数组长度限制：100。
        :type PersonIds: list of str
        :param Names: 素材名称，数组长度限制：20。
        :type Names: list of str
        :param Tags: 素材标签，数组长度限制：20。
        :type Tags: list of str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：100，最大值：100。
        :type Limit: int
        """
        self.Type = None
        self.PersonIds = None
        self.Names = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PersonIds = params.get("PersonIds")
        self.Names = params.get("Names")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonSamplesResponse(AbstractModel):
    """DescribePersonSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param PersonSet: 素材信息。
        :type PersonSet: list of AiSamplePerson
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PersonSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = AiSamplePerson()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRTMPPullSourceAddress(AbstractModel):
    """查询输入的RTMP配置信息。

    """

    def __init__(self):
        r"""
        :param TcUrl: RTMP源站的TcUrl地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type TcUrl: str
        :param StreamKey: RTMP源站的StreamKey。
RTMP源站地址拼接规则为：$TcUrl/$StreamKey。
        :type StreamKey: str
        """
        self.TcUrl = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.TcUrl = params.get("TcUrl")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRTSPPullSourceAddress(AbstractModel):
    """查询输入的RTSP配置信息。

    """

    def __init__(self):
        r"""
        :param Url: RTSP源站的Url地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleSnapshotTemplatesRequest(AbstractModel):
    """DescribeSampleSnapshotTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 采样截图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleSnapshotTemplatesResponse(AbstractModel):
    """DescribeSampleSnapshotTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param SampleSnapshotTemplateSet: 采样截图模板详情列表。
        :type SampleSnapshotTemplateSet: list of SampleSnapshotTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SampleSnapshotTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SampleSnapshotTemplateSet") is not None:
            self.SampleSnapshotTemplateSet = []
            for item in params.get("SampleSnapshotTemplateSet"):
                obj = SampleSnapshotTemplate()
                obj._deserialize(item)
                self.SampleSnapshotTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotByTimeOffsetTemplatesRequest(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 指定时间点截图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotByTimeOffsetTemplatesResponse(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param SnapshotByTimeOffsetTemplateSet: 指定时间点截图模板详情列表。
        :type SnapshotByTimeOffsetTemplateSet: list of SnapshotByTimeOffsetTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SnapshotByTimeOffsetTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotByTimeOffsetTemplateSet") is not None:
            self.SnapshotByTimeOffsetTemplateSet = []
            for item in params.get("SnapshotByTimeOffsetTemplateSet"):
                obj = SnapshotByTimeOffsetTemplate()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkActivateStateRequest(AbstractModel):
    """DescribeStreamLinkActivateState请求参数结构体

    """


class DescribeStreamLinkActivateStateResponse(AbstractModel):
    """DescribeStreamLinkActivateState返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 用户已激活为0，否则为非0。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowLogsRequest(AbstractModel):
    """DescribeStreamLinkFlowLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 传输流Id。
        :type FlowId: str
        :param StartTime: 统计的开始时间，默认为前一小时，最多支持查询近7天。
UTC时间，如'2020-01-01T12:00:00Z'。
        :type StartTime: str
        :param EndTime: 统计的结束时间，默认为StartTime后一小时，最多支持查询24小时的数据。
UTC时间，如'2020-01-01T12:00:00Z'。
        :type EndTime: str
        :param Type: 输入或输出类型，可选[input|output]。
        :type Type: list of str
        :param Pipeline: 主通道或备通道，可选[0|1]。
        :type Pipeline: list of str
        :param PageSize: 每页大小，默认100，范围为[1, 1000]。
        :type PageSize: int
        :param SortType: 按Timestamp升序或降序排序，默认降序，可选[desc|asc]。
        :type SortType: str
        :param PageNum: 页码，默认1，范围为[1, 1000]。
        :type PageNum: int
        """
        self.FlowId = None
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.Pipeline = None
        self.PageSize = None
        self.SortType = None
        self.PageNum = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Type = params.get("Type")
        self.Pipeline = params.get("Pipeline")
        self.PageSize = params.get("PageSize")
        self.SortType = params.get("SortType")
        self.PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowLogsResponse(AbstractModel):
    """DescribeStreamLinkFlowLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Infos: 日志信息列表。
        :type Infos: list of FlowLogInfo
        :param PageNum: 当前页码。
        :type PageNum: int
        :param PageSize: 每页大小。
        :type PageSize: int
        :param TotalNum: 总数量。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Infos = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = FlowLogInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowMediaStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowMediaStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 传输流ID。
        :type FlowId: str
        :param Type: 输入或输出类型，可选[input|output]。
        :type Type: str
        :param InputOutputId: 输入或输出Id。
        :type InputOutputId: str
        :param Pipeline: 主通道或备通道，可选[0|1]。
        :type Pipeline: str
        :param Period: 查询间隔，可选[5s|1min|5min|15min]。
        :type Period: str
        :param StartTime: 统计的开始时间，默认为前一小时，最多支持查询近7天。
UTC时间，如'2020-01-01T12:00:00Z'。
        :type StartTime: str
        :param EndTime: 统计的结束时间，默认为StartTime后一小时，最多支持查询24小时的数据。
UTC时间，如'2020-01-01T12:00:00Z'。
        :type EndTime: str
        """
        self.FlowId = None
        self.Type = None
        self.InputOutputId = None
        self.Pipeline = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.Type = params.get("Type")
        self.InputOutputId = params.get("InputOutputId")
        self.Pipeline = params.get("Pipeline")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowMediaStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowMediaStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Infos: 传输流的媒体数据列表。
        :type Infos: list of FlowMediaInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = FlowMediaInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRealtimeStatusRequest(AbstractModel):
    """DescribeStreamLinkFlowRealtimeStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流ID。
        :type FlowId: str
        :param InputIds: 输入id数组，如果输入输出数组都为空，则代表全量查询。
        :type InputIds: list of str
        :param OutputIds: 输出id数组，如果输入输出数组都为空，则代表全量查询。
        :type OutputIds: list of str
        """
        self.FlowId = None
        self.InputIds = None
        self.OutputIds = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InputIds = params.get("InputIds")
        self.OutputIds = params.get("OutputIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowRealtimeStatusResponse(AbstractModel):
    """DescribeStreamLinkFlowRealtimeStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Timestamp: 查询时间，单位s。
        :type Timestamp: int
        :param Datas: 实时数据信息列表。
        :type Datas: list of FlowRealtimeStatusItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Timestamp = None
        self.Datas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        if params.get("Datas") is not None:
            self.Datas = []
            for item in params.get("Datas"):
                obj = FlowRealtimeStatusItem()
                obj._deserialize(item)
                self.Datas.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRequest(AbstractModel):
    """DescribeStreamLinkFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流Id。
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowResponse(AbstractModel):
    """DescribeStreamLinkFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 流的配置信息。
        :type Info: :class:`tencentcloud.mps.v20190612.models.DescribeFlow`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeFlow()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowSRTStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowSRTStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 传输流ID。
        :type FlowId: str
        :param Type: 输入或输出类型，可选[input|output]。
        :type Type: str
        :param InputOutputId: 输入或输出Id。
        :type InputOutputId: str
        :param Pipeline: 主通道或备通道，可选[0|1]。
        :type Pipeline: str
        :param StartTime: 统计的开始时间，默认为前一小时，最多支持查询近7天。
UTC时间，如'2020-01-01T12:00:00Z'。
        :type StartTime: str
        :param EndTime: 统计的结束时间，默认为StartTime后一小时，最多支持查询24小时的数据。
UTC时间，如'2020-01-01T12:00:00Z'。
        :type EndTime: str
        :param Period: 查询间隔，可选[5s|1min|5min|15min]。
        :type Period: str
        """
        self.FlowId = None
        self.Type = None
        self.InputOutputId = None
        self.Pipeline = None
        self.StartTime = None
        self.EndTime = None
        self.Period = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.Type = params.get("Type")
        self.InputOutputId = params.get("InputOutputId")
        self.Pipeline = params.get("Pipeline")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowSRTStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowSRTStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Infos: 传输流的SRT质量数据列表。
        :type Infos: list of FlowSRTInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = FlowSRTInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 传输流ID。
        :type FlowId: str
        :param Type: 输入或输出类型，可选[input|output]。
        :type Type: str
        :param InputOutputId: 输入或输出Id。
        :type InputOutputId: str
        :param Pipeline: 主通道或备通道，可选[0|1]。
        :type Pipeline: str
        :param Period: 查询间隔，可选[5s|1min|5min|15min]。
        :type Period: str
        :param StartTime: 统计的开始时间，默认为前一小时，最多支持查询近7天。
UTC时间，如'2020-01-01T12:00:00Z'。
        :type StartTime: str
        :param EndTime: 统计的结束时间，默认为StartTime后一小时，最多支持查询24小时的数据。
UTC时间，如'2020-01-01T12:00:00Z'。
        :type EndTime: str
        """
        self.FlowId = None
        self.Type = None
        self.InputOutputId = None
        self.Pipeline = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.Type = params.get("Type")
        self.InputOutputId = params.get("InputOutputId")
        self.Pipeline = params.get("Pipeline")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Infos: 传输流的媒体数据列表。
        :type Infos: list of FlowStatisticsArray
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = FlowStatisticsArray()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowsRequest(AbstractModel):
    """DescribeStreamLinkFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNum: 当前页数，默认1。
        :type PageNum: int
        :param PageSize: 每页大小，默认10。
        :type PageSize: int
        """
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowsResponse(AbstractModel):
    """DescribeStreamLinkFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param Infos: 流的配置信息列表。
        :type Infos: list of DescribeFlow
        :param PageNum: 当前页数。
        :type PageNum: int
        :param PageSize: 每页大小。
        :type PageSize: int
        :param TotalNum: 总数量。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Infos = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = DescribeFlow()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkRegionsRequest(AbstractModel):
    """DescribeStreamLinkRegions请求参数结构体

    """


class DescribeStreamLinkRegionsResponse(AbstractModel):
    """DescribeStreamLinkRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 媒体传输地区信息。
        :type Info: :class:`tencentcloud.mps.v20190612.models.StreamLinkRegionInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = StreamLinkRegionInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 视频处理任务的任务 ID。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型，目前取值有：
<li>WorkflowTask：视频工作流处理任务。</li>
<li>EditMediaTask：视频编辑任务。</li>
<li>LiveStreamProcessTask：直播流处理任务。</li>
<li>ScheduleTask：编排处理任务。</li>
        :type TaskType: str
        :param Status: 任务状态，取值：
<li>WAITING：等待中；</li>
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param CreateTime: 任务的创建时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param BeginProcessTime: 任务开始执行的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type BeginProcessTime: str
        :param FinishTime: 任务执行完毕的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type FinishTime: str
        :param EditMediaTask: 视频编辑任务信息，仅当 TaskType 为 EditMediaTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type EditMediaTask: :class:`tencentcloud.mps.v20190612.models.EditMediaTask`
        :param WorkflowTask: 视频处理任务信息，仅当 TaskType 为 WorkflowTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowTask: :class:`tencentcloud.mps.v20190612.models.WorkflowTask`
        :param LiveStreamProcessTask: 直播流处理任务信息，仅当 TaskType 为 LiveStreamProcessTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveStreamProcessTask: :class:`tencentcloud.mps.v20190612.models.LiveStreamProcessTask`
        :param TaskNotifyConfig: 任务的事件通知信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: 任务流的优先级，取值范围为 [-10, 10]。
        :type TasksPriority: int
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长50个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长1000个字符。
        :type SessionContext: str
        :param ExtInfo: 扩展信息字段，仅用于特定场景。
        :type ExtInfo: str
        :param ScheduleTask: 编排处理任务信息，仅当 TaskType 为 ScheduleTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleTask: :class:`tencentcloud.mps.v20190612.models.ScheduleTask`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskType = None
        self.Status = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.EditMediaTask = None
        self.WorkflowTask = None
        self.LiveStreamProcessTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None
        self.ExtInfo = None
        self.ScheduleTask = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("EditMediaTask") is not None:
            self.EditMediaTask = EditMediaTask()
            self.EditMediaTask._deserialize(params.get("EditMediaTask"))
        if params.get("WorkflowTask") is not None:
            self.WorkflowTask = WorkflowTask()
            self.WorkflowTask._deserialize(params.get("WorkflowTask"))
        if params.get("LiveStreamProcessTask") is not None:
            self.LiveStreamProcessTask = LiveStreamProcessTask()
            self.LiveStreamProcessTask._deserialize(params.get("LiveStreamProcessTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.ExtInfo = params.get("ExtInfo")
        if params.get("ScheduleTask") is not None:
            self.ScheduleTask = ScheduleTask()
            self.ScheduleTask._deserialize(params.get("ScheduleTask"))
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 过滤条件：任务状态，可选值：WAITING（等待中）、PROCESSING（处理中）、FINISH（已完成）。
        :type Status: str
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param ScrollToken: 翻页标识，分批拉取时使用：当单次请求无法拉取所有数据，接口将会返回 ScrollToken，下一次请求携带该 Token，将会从下一条记录开始获取。
        :type ScrollToken: str
        """
        self.Status = None
        self.Limit = None
        self.ScrollToken = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Limit = params.get("Limit")
        self.ScrollToken = params.get("ScrollToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskSet: 任务概要列表。
        :type TaskSet: list of TaskSimpleInfo
        :param ScrollToken: 翻页标识，当请求未返回所有数据，该字段表示下一条记录的 ID。当该字段为空字符串，说明已无更多数据。
        :type ScrollToken: str
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskSet = None
        self.ScrollToken = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskSimpleInfo()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.ScrollToken = params.get("ScrollToken")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeTemplatesRequest(AbstractModel):
    """DescribeTranscodeTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 转码模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param ContainerType: 封装格式过滤条件，可选值：
<li>Video：视频格式，可以同时包含视频流和音频流的封装格式板；</li>
<li>PureAudio：纯音频格式，只能包含音频流的封装格式。</li>
        :type ContainerType: str
        :param TEHDType: 极速高清过滤条件，用于过滤普通转码或极速高清转码模板，可选值：
<li>Common：普通转码模板；</li>
<li>TEHD：极速高清模板。</li>
        :type TEHDType: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param TranscodeType: 模板类型（替换旧版本 TEHDType），可选值：
<li>Common：普通转码模板；</li>
<li>TEHD：极速高清模板。</li>
<li>Enhance：音视频增强模板。</li>
默认空，不限制类型。
        :type TranscodeType: str
        """
        self.Definitions = None
        self.Type = None
        self.ContainerType = None
        self.TEHDType = None
        self.Offset = None
        self.Limit = None
        self.TranscodeType = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.ContainerType = params.get("ContainerType")
        self.TEHDType = params.get("TEHDType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TranscodeType = params.get("TranscodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeTemplatesResponse(AbstractModel):
    """DescribeTranscodeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param TranscodeTemplateSet: 转码模板详情列表。
        :type TranscodeTemplateSet: list of TranscodeTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TranscodeTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TranscodeTemplateSet") is not None:
            self.TranscodeTemplateSet = []
            for item in params.get("TranscodeTemplateSet"):
                obj = TranscodeTemplate()
                obj._deserialize(item)
                self.TranscodeTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWatermarkTemplatesRequest(AbstractModel):
    """DescribeWatermarkTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definitions: 水印模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int
        :param Type: 水印类型过滤条件，可选值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>
        :type Type: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数
<li>默认值：10；</li>
<li>最大值：100。</li>
        :type Limit: int
        """
        self.Definitions = None
        self.Type = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWatermarkTemplatesResponse(AbstractModel):
    """DescribeWatermarkTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param WatermarkTemplateSet: 水印模板详情列表。
        :type WatermarkTemplateSet: list of WatermarkTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WatermarkTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WatermarkTemplateSet") is not None:
            self.WatermarkTemplateSet = []
            for item in params.get("WatermarkTemplateSet"):
                obj = WatermarkTemplate()
                obj._deserialize(item)
                self.WatermarkTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWordSamplesRequest(AbstractModel):
    """DescribeWordSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param Keywords: 关键词过滤条件，数组长度限制：100 个词。
        :type Keywords: list of str
        :param Usages: <b>关键词应用场景过滤条件，可选值：</b>
1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；
2. Recognition.Asr：通过音频识别技术，进行内容识别；
3. Review.Ocr：通过光学字符识别技术，进行不适宜内容的识别；
4. Review.Asr：通过音频识别技术，进行不适宜内容的识别；
<b>可合并简写为：</b>
5. Recognition：通过光学字符识别技术、音频识别技术，进行内容识别，等价于 1+2；
6. Review：通过光学字符识别技术、音频识别技术，进行不适宜内容的识别，等价于 3+4；
可多选，元素间关系为 or，即关键词的应用场景包含该字段集合中任意元素的记录，均符合该条件。
        :type Usages: list of str
        :param Tags: 标签过滤条件，数组长度限制：20 个词。
        :type Tags: list of str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：100，最大值：100。
        :type Limit: int
        """
        self.Keywords = None
        self.Usages = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.Usages = params.get("Usages")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWordSamplesResponse(AbstractModel):
    """DescribeWordSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的记录总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param WordSet: 关键词信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type WordSet: list of AiSampleWord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WordSet") is not None:
            self.WordSet = []
            for item in params.get("WordSet"):
                obj = AiSampleWord()
                obj._deserialize(item)
                self.WordSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkflowsRequest(AbstractModel):
    """DescribeWorkflows请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkflowIds: 工作流 ID 过滤条件，数组长度限制：100。
        :type WorkflowIds: list of int
        :param Status: 工作流状态，取值范围：
<li>Enabled：已启用，</li>
<li>Disabled：已禁用。</li>
不填此参数，则不区分工作流状态。
        :type Status: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        """
        self.WorkflowIds = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.WorkflowIds = params.get("WorkflowIds")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkflowsResponse(AbstractModel):
    """DescribeWorkflows返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param WorkflowInfoSet: 工作流信息数组。
        :type WorkflowInfoSet: list of WorkflowInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WorkflowInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WorkflowInfoSet") is not None:
            self.WorkflowInfoSet = []
            for item in params.get("WorkflowInfoSet"):
                obj = WorkflowInfo()
                obj._deserialize(item)
                self.WorkflowInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisableWorkflowRequest(AbstractModel):
    """DisableWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWorkflowResponse(AbstractModel):
    """DisableWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditMediaFileInfo(AbstractModel):
    """编辑点播视频文件信息

    """

    def __init__(self):
        r"""
        :param InputInfo: 视频的输入信息。
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param StartTimeOffset: 视频剪辑的起始时间偏移，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 视频剪辑的结束时间偏移，单位：秒。
        :type EndTimeOffset: float
        """
        self.InputInfo = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaOutputConfig(AbstractModel):
    """编辑视频的结果文件输出配置。

    """

    def __init__(self):
        r"""
        :param Container: 封装格式，可选值：mp4、hls、mov、flv、avi。默认是 mp4。
        :type Container: str
        :param Type: 剪辑模式，可选值 normal、fast。默认是精确剪辑 normal
        :type Type: str
        """
        self.Container = None
        self.Type = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaRequest(AbstractModel):
    """EditMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileInfos: 输入的视频文件信息。
        :type FileInfos: list of EditMediaFileInfo
        :param OutputStorage: 媒体处理输出文件的目标存储。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 媒体处理输出文件的目标路径。
        :type OutputObjectPath: str
        :param OutputConfig: 编辑后生成的文件配置。
        :type OutputConfig: :class:`tencentcloud.mps.v20190612.models.EditMediaOutputConfig`
        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: 任务优先级，数值越大优先级越高，取值范围是-10到 10，不填代表0。
        :type TasksPriority: int
        :param SessionId: 用于去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        """
        self.FileInfos = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.OutputConfig = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("OutputConfig") is not None:
            self.OutputConfig = EditMediaOutputConfig()
            self.OutputConfig._deserialize(params.get("OutputConfig"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaResponse(AbstractModel):
    """EditMedia返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 编辑视频的任务 ID，可以通过该 ID 查询编辑任务的状态。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EditMediaTask(AbstractModel):
    """编辑视频任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param Status: 任务状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 视频编辑任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.EditMediaTaskInput`
        :param Output: 视频编辑任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.EditMediaTaskOutput`
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = EditMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = EditMediaTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaTaskInput(AbstractModel):
    """编辑视频任务的输入。

    """

    def __init__(self):
        r"""
        :param FileInfoSet: 输入的视频文件信息。
        :type FileInfoSet: list of EditMediaFileInfo
        """
        self.FileInfoSet = None


    def _deserialize(self, params):
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaTaskOutput(AbstractModel):
    """编辑视频任务的输出

    """

    def __init__(self):
        r"""
        :param OutputStorage: 编辑后文件的目标存储。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: 编辑后的视频文件路径。
        :type Path: str
        """
        self.OutputStorage = None
        self.Path = None


    def _deserialize(self, params):
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWorkflowRequest(AbstractModel):
    """EnableWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWorkflowResponse(AbstractModel):
    """EnableWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnhanceConfig(AbstractModel):
    """音视频增强配置

    """

    def __init__(self):
        r"""
        :param VideoEnhance: 视频增强配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoEnhance: :class:`tencentcloud.mps.v20190612.models.VideoEnhanceConfig`
        """
        self.VideoEnhance = None


    def _deserialize(self, params):
        if params.get("VideoEnhance") is not None:
            self.VideoEnhance = VideoEnhanceConfig()
            self.VideoEnhance._deserialize(params.get("VideoEnhance"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteFunctionRequest(AbstractModel):
    """ExecuteFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionName: 调用后端接口名称。
        :type FunctionName: str
        :param FunctionArg: 接口参数，具体参数格式调用时与后端协调。
        :type FunctionArg: str
        """
        self.FunctionName = None
        self.FunctionArg = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.FunctionArg = params.get("FunctionArg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteFunctionResponse(AbstractModel):
    """ExecuteFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 处理结果打包后的字符串，具体与后台一同协调。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ExpressionConfigInfo(AbstractModel):
    """表情识别参数配置

    """

    def __init__(self):
        r"""
        :param Switch: 表情识别任务开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceConfigureInfo(AbstractModel):
    """人脸识别任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 人脸识别任务开关，可选值：
<li>ON：开启智能人脸识别任务；</li>
<li>OFF：关闭智能人脸识别任务。</li>
        :type Switch: str
        :param Score: 人脸识别过滤分数，当识别结果达到该分数以上，返回识别结果。默认 95 分。取值范围：0 - 100。
        :type Score: float
        :param DefaultLibraryLabelSet: 默认人物过滤标签，指定需要返回的默认人物的标签。如果未填或者为空，则全部默认人物结果都返回。标签可选值：
<li>entertainment：娱乐明星；</li>
<li>sport：体育明星；</li>
<li>politician：敏感人物。</li>
        :type DefaultLibraryLabelSet: list of str
        :param UserDefineLibraryLabelSet: 用户自定义人物过滤标签，指定需要返回的用户自定义人物的标签。如果未填或者为空，则全部自定义人物结果都返回。
标签个数最多 100 个，每个标签长度最多 16 个字符。
        :type UserDefineLibraryLabelSet: list of str
        :param FaceLibrary: 人物库选择，可选值：
<li>Default：使用默认人物库；</li>
<li>UserDefine：使用用户自定义人物库。</li>
<li>All：同时使用默认人物库和用户自定义人物库。</li>
默认值：All，使用系统默认人物库及用户自定义人物库。
        :type FaceLibrary: str
        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceConfigureInfoForUpdate(AbstractModel):
    """人脸识别任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 人脸识别任务开关，可选值：
<li>ON：开启智能人脸识别任务；</li>
<li>OFF：关闭智能人脸识别任务。</li>
        :type Switch: str
        :param Score: 人脸识别过滤分数，当识别结果达到该分数以上，返回识别结果。取值范围：0-100。
        :type Score: float
        :param DefaultLibraryLabelSet: 默认人物过滤标签，指定需要返回的默认人物的标签。如果未填或者为空，则全部默认人物结果都返回。标签可选值：
<li>entertainment：娱乐明星；</li>
<li>sport：体育明星；</li>
<li>politician：敏感人物。</li>
        :type DefaultLibraryLabelSet: list of str
        :param UserDefineLibraryLabelSet: 用户自定义人物过滤标签，指定需要返回的用户自定义人物的标签。如果未填或者为空，则全部自定义人物结果都返回。
标签个数最多 100 个，每个标签长度最多 16 个字符。
        :type UserDefineLibraryLabelSet: list of str
        :param FaceLibrary: 人物库选择，可选值：
<li>Default：使用默认人物库；</li>
<li>UserDefine：使用用户自定义人物库。</li>
<li>All：同时使用默认人物库和用户自定义人物库。</li>
        :type FaceLibrary: str
        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceEnhanceConfig(AbstractModel):
    """人脸增强配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Intensity: 强度，取值范围：0.0~1.0。
默认：0.0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Intensity: float
        """
        self.Switch = None
        self.Intensity = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Intensity = params.get("Intensity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowAudio(AbstractModel):
    """流的音频数据。

    """

    def __init__(self):
        r"""
        :param Fps: 帧率。
        :type Fps: int
        :param Rate: 码率，单位是bps。
        :type Rate: int
        :param Pid: 音频Pid。
        :type Pid: int
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowLogInfo(AbstractModel):
    """传输流日志信息。

    """

    def __init__(self):
        r"""
        :param Timestamp: 时间戳，单位为秒。
        :type Timestamp: int
        :param Type: 输入输出类型（input/output）。
        :type Type: str
        :param InputOutputId: 输入或输出Id。
        :type InputOutputId: str
        :param Protocol: 协议。
        :type Protocol: str
        :param EventCode: 事件代码。
        :type EventCode: str
        :param EventMessage: 事件信息。
        :type EventMessage: str
        :param RemoteIp: 对端IP。
        :type RemoteIp: str
        :param RemotePort: 对端端口。
        :type RemotePort: str
        :param Pipeline: 主备通道，0为主通道，1为备通道。
        :type Pipeline: str
        :param InputOutputName: 输入或输出的名称。
        :type InputOutputName: str
        """
        self.Timestamp = None
        self.Type = None
        self.InputOutputId = None
        self.Protocol = None
        self.EventCode = None
        self.EventMessage = None
        self.RemoteIp = None
        self.RemotePort = None
        self.Pipeline = None
        self.InputOutputName = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Type = params.get("Type")
        self.InputOutputId = params.get("InputOutputId")
        self.Protocol = params.get("Protocol")
        self.EventCode = params.get("EventCode")
        self.EventMessage = params.get("EventMessage")
        self.RemoteIp = params.get("RemoteIp")
        self.RemotePort = params.get("RemotePort")
        self.Pipeline = params.get("Pipeline")
        self.InputOutputName = params.get("InputOutputName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaAudio(AbstractModel):
    """传输流媒体的音频数据。

    """

    def __init__(self):
        r"""
        :param Fps: 帧率。
        :type Fps: int
        :param Rate: 码率，单位是bps。
        :type Rate: int
        :param Pid: 音频Pid。
        :type Pid: int
        :param SessionId: 标志同一次推流。
        :type SessionId: str
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None
        self.SessionId = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaInfo(AbstractModel):
    """传输流的媒体数据。

    """

    def __init__(self):
        r"""
        :param Timestamp: 时间戳，单位是秒。
        :type Timestamp: int
        :param Network: 总带宽。
        :type Network: int
        :param Video: 传输流的视频数据。
        :type Video: list of FlowMediaVideo
        :param Audio: 传输流的音频数据。
        :type Audio: list of FlowMediaAudio
        :param SessionId: 标志同一次推流。
        :type SessionId: str
        :param ClientIp: 客户端IP。
        :type ClientIp: str
        """
        self.Timestamp = None
        self.Network = None
        self.Video = None
        self.Audio = None
        self.SessionId = None
        self.ClientIp = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Network = params.get("Network")
        if params.get("Video") is not None:
            self.Video = []
            for item in params.get("Video"):
                obj = FlowMediaVideo()
                obj._deserialize(item)
                self.Video.append(obj)
        if params.get("Audio") is not None:
            self.Audio = []
            for item in params.get("Audio"):
                obj = FlowMediaAudio()
                obj._deserialize(item)
                self.Audio.append(obj)
        self.SessionId = params.get("SessionId")
        self.ClientIp = params.get("ClientIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaVideo(AbstractModel):
    """传输流媒体的视频数据。

    """

    def __init__(self):
        r"""
        :param Fps: 帧率。
        :type Fps: int
        :param Rate: 码率，单位是bps。
        :type Rate: int
        :param Pid: 视频Pid。
        :type Pid: int
        :param SessionId: 标志同一次推流。
        :type SessionId: str
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None
        self.SessionId = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusCommon(AbstractModel):
    """实时流状态查询的通用状态信息。

    """

    def __init__(self):
        r"""
        :param State: 当前连接状态，Connected|Waiting|Idle。
        :type State: str
        :param Mode: 连接模式，Listener|Caller。
        :type Mode: str
        :param ConnectedTime: 已连接时长，单位为ms。
        :type ConnectedTime: int
        :param Bitrate: 实时码率，单位为bps。
        :type Bitrate: int
        :param Reconnections: 重试次数。
        :type Reconnections: int
        """
        self.State = None
        self.Mode = None
        self.ConnectedTime = None
        self.Bitrate = None
        self.Reconnections = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.Mode = params.get("Mode")
        self.ConnectedTime = params.get("ConnectedTime")
        self.Bitrate = params.get("Bitrate")
        self.Reconnections = params.get("Reconnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusItem(AbstractModel):
    """流状态实时查询接口的流状态信息

    """

    def __init__(self):
        r"""
        :param Type: 类型，Input|Output。
        :type Type: str
        :param InputId: 输入Id，如果Type为Input，此字段不为空。
        :type InputId: str
        :param OutputId: 输出Id，如果Type为Output，此字段不为空。
        :type OutputId: str
        :param FlowId: 流Id。
        :type FlowId: str
        :param Protocol: 协议， SRT | RTMP。
        :type Protocol: str
        :param CommonStatus: 共同状态信息。
        :type CommonStatus: :class:`tencentcloud.mps.v20190612.models.FlowRealtimeStatusCommon`
        :param SRTStatus: 如果是SRT协议则有此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type SRTStatus: :class:`tencentcloud.mps.v20190612.models.FlowRealtimeStatusSRT`
        :param RTMPStatus: 如果是RTMP协议则有此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTMPStatus: :class:`tencentcloud.mps.v20190612.models.FlowRealtimeStatusRTMP`
        :param ConnectServerIP: 服务器IP。
        :type ConnectServerIP: str
        :param RTPStatus: 如果是RTP协议则有此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTPStatus: :class:`tencentcloud.mps.v20190612.models.FlowRealtimeStatusRTP`
        """
        self.Type = None
        self.InputId = None
        self.OutputId = None
        self.FlowId = None
        self.Protocol = None
        self.CommonStatus = None
        self.SRTStatus = None
        self.RTMPStatus = None
        self.ConnectServerIP = None
        self.RTPStatus = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InputId = params.get("InputId")
        self.OutputId = params.get("OutputId")
        self.FlowId = params.get("FlowId")
        self.Protocol = params.get("Protocol")
        if params.get("CommonStatus") is not None:
            self.CommonStatus = FlowRealtimeStatusCommon()
            self.CommonStatus._deserialize(params.get("CommonStatus"))
        if params.get("SRTStatus") is not None:
            self.SRTStatus = FlowRealtimeStatusSRT()
            self.SRTStatus._deserialize(params.get("SRTStatus"))
        if params.get("RTMPStatus") is not None:
            self.RTMPStatus = FlowRealtimeStatusRTMP()
            self.RTMPStatus._deserialize(params.get("RTMPStatus"))
        self.ConnectServerIP = params.get("ConnectServerIP")
        if params.get("RTPStatus") is not None:
            self.RTPStatus = FlowRealtimeStatusRTP()
            self.RTPStatus._deserialize(params.get("RTPStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusRTMP(AbstractModel):
    """流状态实时查询接口的RTMP信息。

    """

    def __init__(self):
        r"""
        :param VideoFPS: 视频帧率。
        :type VideoFPS: int
        :param AudioFPS: 音频帧率。
        :type AudioFPS: int
        """
        self.VideoFPS = None
        self.AudioFPS = None


    def _deserialize(self, params):
        self.VideoFPS = params.get("VideoFPS")
        self.AudioFPS = params.get("AudioFPS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusRTP(AbstractModel):
    """流状态实时查询接口的RTP流状态信息

    """

    def __init__(self):
        r"""
        :param Packets: 传输的包个数
        :type Packets: int
        """
        self.Packets = None


    def _deserialize(self, params):
        self.Packets = params.get("Packets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusSRT(AbstractModel):
    """流状态实时查询接口的SRT信息。

    """

    def __init__(self):
        r"""
        :param Latency: 延迟，单位为ms。
        :type Latency: int
        :param RTT: RTT，单位为ms。
        :type RTT: int
        :param Packets: 实时发包数或者收包数。
        :type Packets: int
        :param PacketLossRate: 丢包率。
        :type PacketLossRate: float
        :param RetransmitRate: 重传率。
        :type RetransmitRate: float
        :param DroppedPackets: 实时丢包数。
        :type DroppedPackets: int
        :param Encryption: 是否加密，On|Off。
        :type Encryption: str
        """
        self.Latency = None
        self.RTT = None
        self.Packets = None
        self.PacketLossRate = None
        self.RetransmitRate = None
        self.DroppedPackets = None
        self.Encryption = None


    def _deserialize(self, params):
        self.Latency = params.get("Latency")
        self.RTT = params.get("RTT")
        self.Packets = params.get("Packets")
        self.PacketLossRate = params.get("PacketLossRate")
        self.RetransmitRate = params.get("RetransmitRate")
        self.DroppedPackets = params.get("DroppedPackets")
        self.Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowSRTInfo(AbstractModel):
    """传输流的SRT质量数据。

    """

    def __init__(self):
        r"""
        :param Timestamp: 时间戳，单位是秒。
        :type Timestamp: int
        :param SendPacketLossRate: 发送丢包率。
        :type SendPacketLossRate: int
        :param SendRetransmissionRate: 发送重传率。
        :type SendRetransmissionRate: int
        :param RecvPacketLossRate: 接收丢包率。
        :type RecvPacketLossRate: int
        :param RecvRetransmissionRate: 接收重传率。
        :type RecvRetransmissionRate: int
        :param RTT: 与对端的RTT时延。
        :type RTT: int
        :param SessionId: 标志同一次推流。
        :type SessionId: str
        :param SendPacketDropNumber: 发送弃包数。
        :type SendPacketDropNumber: int
        :param RecvPacketDropNumber: 接收弃包数。
        :type RecvPacketDropNumber: int
        """
        self.Timestamp = None
        self.SendPacketLossRate = None
        self.SendRetransmissionRate = None
        self.RecvPacketLossRate = None
        self.RecvRetransmissionRate = None
        self.RTT = None
        self.SessionId = None
        self.SendPacketDropNumber = None
        self.RecvPacketDropNumber = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.SendPacketLossRate = params.get("SendPacketLossRate")
        self.SendRetransmissionRate = params.get("SendRetransmissionRate")
        self.RecvPacketLossRate = params.get("RecvPacketLossRate")
        self.RecvRetransmissionRate = params.get("RecvRetransmissionRate")
        self.RTT = params.get("RTT")
        self.SessionId = params.get("SessionId")
        self.SendPacketDropNumber = params.get("SendPacketDropNumber")
        self.RecvPacketDropNumber = params.get("RecvPacketDropNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowStatistics(AbstractModel):
    """流的统计数据。

    """

    def __init__(self):
        r"""
        :param SessionId: 会话Id。
        :type SessionId: str
        :param ClientIp: 对端IP。
        :type ClientIp: str
        :param Network: 总带宽。
        :type Network: int
        :param Video: 视频数据。
        :type Video: list of FlowVideo
        :param Audio: 音频数据。
        :type Audio: list of FlowAudio
        """
        self.SessionId = None
        self.ClientIp = None
        self.Network = None
        self.Video = None
        self.Audio = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.ClientIp = params.get("ClientIp")
        self.Network = params.get("Network")
        if params.get("Video") is not None:
            self.Video = []
            for item in params.get("Video"):
                obj = FlowVideo()
                obj._deserialize(item)
                self.Video.append(obj)
        if params.get("Audio") is not None:
            self.Audio = []
            for item in params.get("Audio"):
                obj = FlowAudio()
                obj._deserialize(item)
                self.Audio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowStatisticsArray(AbstractModel):
    """流的统计数据列表。

    """

    def __init__(self):
        r"""
        :param Timestamp: 时间戳。
        :type Timestamp: int
        :param FlowStatistics: 每个会话的统计数据。
        :type FlowStatistics: list of FlowStatistics
        """
        self.Timestamp = None
        self.FlowStatistics = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        if params.get("FlowStatistics") is not None:
            self.FlowStatistics = []
            for item in params.get("FlowStatistics"):
                obj = FlowStatistics()
                obj._deserialize(item)
                self.FlowStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowVideo(AbstractModel):
    """流的视频数据。

    """

    def __init__(self):
        r"""
        :param Fps: 帧率。
        :type Fps: int
        :param Rate: 码率，单位是bps。
        :type Rate: int
        :param Pid: 音频Pid。
        :type Pid: int
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameRateConfig(AbstractModel):
    """插帧帧率配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Fps: 帧率，取值范围：[0, 100]，单位：Hz。
默认值 0。
注意：对于转码，该参数会覆盖 VideoTemplate 内部的 Fps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Fps: int
        """
        self.Switch = None
        self.Fps = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagConfigureInfo(AbstractModel):
    """智能按帧标签任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 智能按帧标签任务开关，可选值：
<li>ON：开启智能按帧标签任务；</li>
<li>OFF：关闭智能按帧标签任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagConfigureInfoForUpdate(AbstractModel):
    """智能按帧标签任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 智能按帧标签任务开关，可选值：
<li>ON：开启智能按帧标签任务；</li>
<li>OFF：关闭智能按帧标签任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HLSPullSourceAddress(AbstractModel):
    """创建的输入HLS拉流源站配置信息。

    """

    def __init__(self):
        r"""
        :param Url: HLS源站的Url地址。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HdrConfig(AbstractModel):
    """HDR配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Type: 类型，可选值：
<li>HDR10</li>
<li>HLG</li>
默认值：HDR10。
注意：video的编码方式需要为libx265；
注意：视频编码位深为10。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Switch = None
        self.Type = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeadTailParameter(AbstractModel):
    """片头片尾参数

    """

    def __init__(self):
        r"""
        :param HeadSet: 片头列表。
        :type HeadSet: list of MediaInputInfo
        :param TailSet: 片尾列表。
        :type TailSet: list of MediaInputInfo
        """
        self.HeadSet = None
        self.TailSet = None


    def _deserialize(self, params):
        if params.get("HeadSet") is not None:
            self.HeadSet = []
            for item in params.get("HeadSet"):
                obj = MediaInputInfo()
                obj._deserialize(item)
                self.HeadSet.append(obj)
        if params.get("TailSet") is not None:
            self.TailSet = []
            for item in params.get("TailSet"):
                obj = MediaInputInfo()
                obj._deserialize(item)
                self.TailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageQualityEnhanceConfig(AbstractModel):
    """综合增强配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Type: 类型，可选值：
<li>weak</li>
<li>normal</li>
<li>strong</li>
默认值：weak。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Switch = None
        self.Type = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSpriteTaskInput(AbstractModel):
    """对视频截雪碧图任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 雪碧图模板 ID。
        :type Definition: int
        :param OutputStorage: 截取雪碧图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 截取雪碧图后，雪碧图图片文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_imageSprite_{definition}_{number}.{format}`。
        :type OutputObjectPath: str
        :param WebVttObjectName: 截取雪碧图后，Web VTT 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：`{inputName}_imageSprite_{definition}.{format}`。
        :type WebVttObjectName: str
        :param ObjectNumberFormat: 截取雪碧图后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.WebVttObjectName = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.WebVttObjectName = params.get("WebVttObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSpriteTemplate(AbstractModel):
    """雪碧图模板详情

    """

    def __init__(self):
        r"""
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 雪碧图模板名称。
        :type Name: str
        :param Width: 雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param SampleType: 采样类型。
        :type SampleType: str
        :param SampleInterval: 采样间隔。
        :type SampleInterval: int
        :param RowCount: 雪碧图中小图的行数。
        :type RowCount: int
        :param ColumnCount: 雪碧图中小图的列数。
        :type ColumnCount: int
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。
        :type FillType: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param Format: 图片格式。
        :type Format: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None
        self.Comment = None
        self.Format = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkInput(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        r"""
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。
        :type ImageContent: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。取值范围为[8, 4096]。</li>
默认值：10%。
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素。取值范围为0或[8, 4096]。</li>
默认值：0px，表示 Height 按照原始水印图片的宽高比缩放。
        :type Height: str
        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束（默认值）。</li>
        :type RepeatType: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkInputForUpdate(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        r"""
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。
        :type ImageContent: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。取值范围为[8, 4096]。</li>
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素。取值范围为0或[8, 4096]。</li>
默认值：0px，表示 Height 按照原始水印图片的宽高比缩放。
        :type Height: str
        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束。</li>
        :type RepeatType: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkTemplate(AbstractModel):
    """图片水印模板

    """

    def __init__(self):
        r"""
        :param ImageUrl: 水印图片地址。
        :type ImageUrl: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；</li>
0px：表示 Height 按照 Width 对视频宽度的比例缩放。
        :type Height: str
        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束。</li>
        :type RepeatType: str
        """
        self.ImageUrl = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputAddress(AbstractModel):
    """输入地址信息。

    """

    def __init__(self):
        r"""
        :param Ip: 输入地址的IP。
        :type Ip: str
        :param Port: 输入地址的端口。
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiRecognitionResultInfo(AbstractModel):
    """直播流 AI 识别结果

    """

    def __init__(self):
        r"""
        :param ResultSet: 内容识别结果列表。
        :type ResultSet: list of LiveStreamAiRecognitionResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = LiveStreamAiRecognitionResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiRecognitionResultItem(AbstractModel):
    """直播流 AI 识别结果

    """

    def __init__(self):
        r"""
        :param Type: 结果的类型，取值范围：
<li>FaceRecognition：人脸识别，</li>
<li>AsrWordsRecognition：语音关键词识别，</li>
<li>OcrWordsRecognition：文本关键词识别，</li>
<li>AsrFullTextRecognition：语音全文识别，</li>
<li>OcrFullTextRecognition：文本全文识别。</li>
<li>TransTextRecognition：语音翻译。</li>
        :type Type: str
        :param FaceRecognitionResultSet: 人脸识别结果，当 Type 为
FaceRecognition 时有效。
        :type FaceRecognitionResultSet: list of LiveStreamFaceRecognitionResult
        :param AsrWordsRecognitionResultSet: 语音关键词识别结果，当 Type 为
AsrWordsRecognition 时有效。
        :type AsrWordsRecognitionResultSet: list of LiveStreamAsrWordsRecognitionResult
        :param OcrWordsRecognitionResultSet: 文本关键词识别结果，当 Type 为
OcrWordsRecognition 时有效。
        :type OcrWordsRecognitionResultSet: list of LiveStreamOcrWordsRecognitionResult
        :param AsrFullTextRecognitionResultSet: 语音全文识别结果，当 Type 为
AsrFullTextRecognition 时有效。
        :type AsrFullTextRecognitionResultSet: list of LiveStreamAsrFullTextRecognitionResult
        :param OcrFullTextRecognitionResultSet: 文本全文识别结果，当 Type 为
OcrFullTextRecognition 时有效。
        :type OcrFullTextRecognitionResultSet: list of LiveStreamOcrFullTextRecognitionResult
        :param TransTextRecognitionResultSet: 翻译结果，当Type 为 TransTextRecognition 时有效。
        :type TransTextRecognitionResultSet: list of LiveStreamTransTextRecognitionResult
        """
        self.Type = None
        self.FaceRecognitionResultSet = None
        self.AsrWordsRecognitionResultSet = None
        self.OcrWordsRecognitionResultSet = None
        self.AsrFullTextRecognitionResultSet = None
        self.OcrFullTextRecognitionResultSet = None
        self.TransTextRecognitionResultSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("FaceRecognitionResultSet") is not None:
            self.FaceRecognitionResultSet = []
            for item in params.get("FaceRecognitionResultSet"):
                obj = LiveStreamFaceRecognitionResult()
                obj._deserialize(item)
                self.FaceRecognitionResultSet.append(obj)
        if params.get("AsrWordsRecognitionResultSet") is not None:
            self.AsrWordsRecognitionResultSet = []
            for item in params.get("AsrWordsRecognitionResultSet"):
                obj = LiveStreamAsrWordsRecognitionResult()
                obj._deserialize(item)
                self.AsrWordsRecognitionResultSet.append(obj)
        if params.get("OcrWordsRecognitionResultSet") is not None:
            self.OcrWordsRecognitionResultSet = []
            for item in params.get("OcrWordsRecognitionResultSet"):
                obj = LiveStreamOcrWordsRecognitionResult()
                obj._deserialize(item)
                self.OcrWordsRecognitionResultSet.append(obj)
        if params.get("AsrFullTextRecognitionResultSet") is not None:
            self.AsrFullTextRecognitionResultSet = []
            for item in params.get("AsrFullTextRecognitionResultSet"):
                obj = LiveStreamAsrFullTextRecognitionResult()
                obj._deserialize(item)
                self.AsrFullTextRecognitionResultSet.append(obj)
        if params.get("OcrFullTextRecognitionResultSet") is not None:
            self.OcrFullTextRecognitionResultSet = []
            for item in params.get("OcrFullTextRecognitionResultSet"):
                obj = LiveStreamOcrFullTextRecognitionResult()
                obj._deserialize(item)
                self.OcrFullTextRecognitionResultSet.append(obj)
        if params.get("TransTextRecognitionResultSet") is not None:
            self.TransTextRecognitionResultSet = []
            for item in params.get("TransTextRecognitionResultSet"):
                obj = LiveStreamTransTextRecognitionResult()
                obj._deserialize(item)
                self.TransTextRecognitionResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewImagePoliticalResult(AbstractModel):
    """直播 AI 内容审核图片敏感结果

    """

    def __init__(self):
        r"""
        :param StartPtsTime: 嫌疑片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 嫌疑片段结束的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 嫌疑片段敏感分数。
        :type Confidence: float
        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: 视频敏感结果标签，取值范围：
<li>politician：敏感人物。</li>
<li>violation_photo：违规图标。</li>
        :type Label: str
        :param Name: 敏感人物、违规图标名字。
        :type Name: str
        :param AreaCoordSet: 敏感人物、违规图标出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
        :type AreaCoordSet: list of int
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Name = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Name = params.get("Name")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewImagePornResult(AbstractModel):
    """直播 AI 内容审核图片鉴黄结果

    """

    def __init__(self):
        r"""
        :param StartPtsTime: 嫌疑片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 嫌疑片段结束的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 嫌疑片段涉黄分数。
        :type Confidence: float
        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: 视频鉴黄结果标签，取值范围：
<li>porn：色情。</li>
<li>sexy：性感。</li>
<li>vulgar：低俗。</li>
<li>intimacy：亲密行为。</li>
        :type Label: str
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewImageTerrorismResult(AbstractModel):
    """直播 AI 内容审核图片涉敏结果

    """

    def __init__(self):
        r"""
        :param StartPtsTime: 嫌疑片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 嫌疑片段结束的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 嫌疑片段涉敏分数。
        :type Confidence: float
        :param Suggestion: 嫌疑片段涉敏结果建议，取值范围：
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: 视频涉敏结果标签，取值范围：
<li>guns：武器枪支。</li>
<li>crowd：人群聚集。</li>
<li>police：警察部队。</li>
<li>bloody：血腥画面。</li>
<li>banners：涉敏旗帜。</li>
<li>militant：武装分子。</li>
<li>explosion：爆炸火灾。</li>
<li>terrorists：涉敏人物。</li>
        :type Label: str
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewResultInfo(AbstractModel):
    """直播流 AI 审核结果

    """

    def __init__(self):
        r"""
        :param ResultSet: 内容审核结果列表。
        :type ResultSet: list of LiveStreamAiReviewResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = LiveStreamAiReviewResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewResultItem(AbstractModel):
    """直播流 AI 审核结果

    """

    def __init__(self):
        r"""
        :param Type: 审核结果的类型，可以取的值有：
<li>ImagePorn：图片鉴黄</li>
<li>ImageTerrorism：图片涉敏</li>
<li>ImagePolitical：图片涉敏</li>
<li>PornVoice：声音鉴黄</li>
        :type Type: str
        :param ImagePornResultSet: 图片鉴黄的结果，当 Type 为 ImagePorn 时有效。
        :type ImagePornResultSet: list of LiveStreamAiReviewImagePornResult
        :param ImageTerrorismResultSet: 图片涉敏的结果，当 Type 为 ImageTerrorism 时有效。
        :type ImageTerrorismResultSet: list of LiveStreamAiReviewImageTerrorismResult
        :param ImagePoliticalResultSet: 图片涉敏的结果，当 Type 为 ImagePolitical 时有效。
        :type ImagePoliticalResultSet: list of LiveStreamAiReviewImagePoliticalResult
        :param VoicePornResultSet: 声音鉴黄的结果，当 Type 为 PornVoice 时有效。
        :type VoicePornResultSet: list of LiveStreamAiReviewVoicePornResult
        """
        self.Type = None
        self.ImagePornResultSet = None
        self.ImageTerrorismResultSet = None
        self.ImagePoliticalResultSet = None
        self.VoicePornResultSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ImagePornResultSet") is not None:
            self.ImagePornResultSet = []
            for item in params.get("ImagePornResultSet"):
                obj = LiveStreamAiReviewImagePornResult()
                obj._deserialize(item)
                self.ImagePornResultSet.append(obj)
        if params.get("ImageTerrorismResultSet") is not None:
            self.ImageTerrorismResultSet = []
            for item in params.get("ImageTerrorismResultSet"):
                obj = LiveStreamAiReviewImageTerrorismResult()
                obj._deserialize(item)
                self.ImageTerrorismResultSet.append(obj)
        if params.get("ImagePoliticalResultSet") is not None:
            self.ImagePoliticalResultSet = []
            for item in params.get("ImagePoliticalResultSet"):
                obj = LiveStreamAiReviewImagePoliticalResult()
                obj._deserialize(item)
                self.ImagePoliticalResultSet.append(obj)
        if params.get("VoicePornResultSet") is not None:
            self.VoicePornResultSet = []
            for item in params.get("VoicePornResultSet"):
                obj = LiveStreamAiReviewVoicePornResult()
                obj._deserialize(item)
                self.VoicePornResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewVoicePornResult(AbstractModel):
    """直播 AI 内容审核声音鉴黄结果

    """

    def __init__(self):
        r"""
        :param StartPtsTime: 嫌疑片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 嫌疑片段结束的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 嫌疑片段涉黄分数。
        :type Confidence: float
        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: 视频鉴黄结果标签，取值范围：
<li>sexual_moan：呻吟。</li>
        :type Label: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAsrFullTextRecognitionResult(AbstractModel):
    """直播识别 Asr 全文识别

    """

    def __init__(self):
        r"""
        :param Text: 识别文本。
        :type Text: str
        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        """
        self.Text = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAsrWordsRecognitionResult(AbstractModel):
    """直播 AI Asr 单词识别结果

    """

    def __init__(self):
        r"""
        :param Word: 语音关键词。
        :type Word: str
        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        """
        self.Word = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamFaceRecognitionResult(AbstractModel):
    """直播 AI 人脸识别结果

    """

    def __init__(self):
        r"""
        :param Id: 人物唯一标识 ID。
        :type Id: str
        :param Name: 人物名称。
        :type Name: str
        :param Type: 人物库类型，表示识别出的人物来自哪个人物库：
<li>Default：默认人物库；</li><li>UserDefine：用户自定义人物库。</li>
        :type Type: str
        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoordSet: list of int
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamOcrFullTextRecognitionResult(AbstractModel):
    """直播识别 Ocr 全文识别

    """

    def __init__(self):
        r"""
        :param Text: 语音文本。
        :type Text: str
        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoordSet: list of int
        """
        self.Text = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamOcrWordsRecognitionResult(AbstractModel):
    """直播 AI Ocr 单词识别结果

    """

    def __init__(self):
        r"""
        :param Word: 文本关键词。
        :type Word: str
        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoords: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoords: list of int
        """
        self.Word = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoords = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoords = params.get("AreaCoords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamProcessErrorInfo(AbstractModel):
    """直播流处理错误信息

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码：
<li>0表示没有错误；</li>
<li>非0表示错误，请参考 Message 错误信息。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        """
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamProcessTask(AbstractModel):
    """直播处理任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 媒体处理任务 ID。
        :type TaskId: str
        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Url: 直播流 URL。
        :type Url: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Url = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamTaskNotifyConfig(AbstractModel):
    """任务处理的事件通知配置。

    """

    def __init__(self):
        r"""
        :param CmqModel: CMQ 的模型，有 Queue 和 Topic 两种，目前仅支持 Queue。
        :type CmqModel: str
        :param CmqRegion: CMQ 的园区，如 sh，bj 等。
        :type CmqRegion: str
        :param QueueName: 当模型为 Queue 时有效，表示接收事件通知的 CMQ 的队列名。
        :type QueueName: str
        :param TopicName: 当模型为 Topic 时有效，表示接收事件通知的 CMQ 的主题名。
        :type TopicName: str
        :param NotifyType: 通知类型，默认CMQ，指定URL时HTTP回调推送到 NotifyUrl 指定的地址。
        :type NotifyType: str
        :param NotifyUrl: HTTP回调地址，NotifyType为URL时必填。
        :type NotifyUrl: str
        """
        self.CmqModel = None
        self.CmqRegion = None
        self.QueueName = None
        self.TopicName = None
        self.NotifyType = None
        self.NotifyUrl = None


    def _deserialize(self, params):
        self.CmqModel = params.get("CmqModel")
        self.CmqRegion = params.get("CmqRegion")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")
        self.NotifyType = params.get("NotifyType")
        self.NotifyUrl = params.get("NotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamTransTextRecognitionResult(AbstractModel):
    """直播实时翻译结果

    """

    def __init__(self):
        r"""
        :param Text: 识别文本。
        :type Text: str
        :param StartPtsTime: 翻译片段起始的 PTS 时间，单位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 翻译片段终止的 PTS 时间，单位：秒。
        :type EndPtsTime: float
        :param Confidence: 翻译片段置信度。取值：0~100。
        :type Confidence: float
        :param Trans: 翻译文本。
        :type Trans: str
        """
        self.Text = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Trans = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Trans = params.get("Trans")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowLightEnhanceConfig(AbstractModel):
    """低光照增强配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Type: 类型，可选值：
<li>normal</li>
默认值：normal。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Switch = None
        self.Type = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageTaskRequest(AbstractModel):
    """ManageTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param OperationType: 操作类型，取值范围：
<ul>
<li>Abort：终止任务。使用说明：
<ul><li>若 [任务类型](/document/product/862/37614#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 为直播流处理任务（LiveStreamProcessTask），支持终止 [任务状态](/document/product/862/37614#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 为等待中（WAITING）或处理中（PROCESSING）的任务；</li>
<li>否则，对于其他 [任务类型](/document/product/862/37614#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)，只支持终止 [任务状态](/document/product/862/37614#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 为等待中（WAITING）的任务。</li></ul>
</li></ul>
        :type OperationType: str
        :param TaskId: 视频处理的任务 ID。
        :type TaskId: str
        """
        self.OperationType = None
        self.TaskId = None


    def _deserialize(self, params):
        self.OperationType = params.get("OperationType")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageTaskResponse(AbstractModel):
    """ManageTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MediaAiAnalysisClassificationItem(AbstractModel):
    """智能分类结果

    """

    def __init__(self):
        r"""
        :param Classification: 智能分类的类别名称。
        :type Classification: str
        :param Confidence: 智能分类的可信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Classification = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisCoverItem(AbstractModel):
    """智能封面信息

    """

    def __init__(self):
        r"""
        :param CoverPath: 智能封面存储路径。
        :type CoverPath: str
        :param Confidence: 智能封面的可信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.CoverPath = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverPath = params.get("CoverPath")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisFrameTagItem(AbstractModel):
    """智能按帧标签结果信息

    """

    def __init__(self):
        r"""
        :param Tag: 按帧标签名称。
        :type Tag: str
        :param CategorySet: 按帧标签名称的分类列表，CategorySet.N 表示第 N+1级分类。
比如 Tag 为“塔楼”时，CategorySet 包含两个元素：CategorySet.0 为“场景”，CategorySet.1为 “建筑”，表示按帧标签为“塔楼”，且第1级分类是“场景”，第2级分类是“建筑”。
        :type CategorySet: list of str
        :param Confidence: 按帧标签的可信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.CategorySet = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.CategorySet = params.get("CategorySet")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisFrameTagSegmentItem(AbstractModel):
    """按帧标签片段列表

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: 按帧标签起始的偏移时间。
        :type StartTimeOffset: float
        :param EndTimeOffset: 按帧标签结束的偏移时间。
        :type EndTimeOffset: float
        :param TagSet: 时间片段内的标签列表。
        :type TagSet: list of MediaAiAnalysisFrameTagItem
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TagSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisFrameTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisTagItem(AbstractModel):
    """智能标签结果信息

    """

    def __init__(self):
        r"""
        :param Tag: 标签名称。
        :type Tag: str
        :param Confidence: 标签的可信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAnimatedGraphicsItem(AbstractModel):
    """视频转动图结果信息

    """

    def __init__(self):
        r"""
        :param Storage: 转动图文件的存储位置。
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: 转动图的文件路径。
        :type Path: str
        :param Definition: 转动图模板 ID，参见[转动图参数模板](https://cloud.tencent.com/document/product/862/37042#.E9.A2.84.E7.BD.AE.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Container: 动图格式，如 gif。
        :type Container: str
        :param Height: 动图的高度，单位：px。
        :type Height: int
        :param Width: 动图的宽度，单位：px。
        :type Width: int
        :param Bitrate: 动图码率，单位：bps。
        :type Bitrate: int
        :param Size: 动图大小，单位：字节。
        :type Size: int
        :param Md5: 动图的md5值。
        :type Md5: str
        :param StartTimeOffset: 动图在视频中的起始时间偏移，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 动图在视频中的结束时间偏移，单位：秒。
        :type EndTimeOffset: float
        """
        self.Storage = None
        self.Path = None
        self.Definition = None
        self.Container = None
        self.Height = None
        self.Width = None
        self.Bitrate = None
        self.Size = None
        self.Md5 = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Bitrate = params.get("Bitrate")
        self.Size = params.get("Size")
        self.Md5 = params.get("Md5")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAudioStreamItem(AbstractModel):
    """点播文件音频流信息

    """

    def __init__(self):
        r"""
        :param Bitrate: 音频流的码率，单位：bps。
        :type Bitrate: int
        :param SamplingRate: 音频流的采样率，单位：hz。
        :type SamplingRate: int
        :param Codec: 音频流的编码格式，例如 aac。
        :type Codec: str
        :param Channel: 音频声道数，例如 2。
注意：此字段可能返回 null，表示取不到有效值。
        :type Channel: int
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None
        self.Channel = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewAsrTextSegmentItem(AbstractModel):
    """内容审核 Asr 文字审核嫌疑片段

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
        :type Confidence: float
        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param KeywordSet: 嫌疑关键词列表。
        :type KeywordSet: list of str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewOcrTextSegmentItem(AbstractModel):
    """内容审核 Ocr 文字审核嫌疑片段

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
        :type Confidence: float
        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param KeywordSet: 嫌疑关键词列表。
        :type KeywordSet: list of str
        :param AreaCoordSet: 嫌疑文字出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
        :type AreaCoordSet: list of int
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewPoliticalSegmentItem(AbstractModel):
    """内容审核涉敏嫌疑片段

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉敏分数。
        :type Confidence: float
        :param Suggestion: 嫌疑片段涉敏结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Name: 涉敏人物、违规图标名字。
        :type Name: str
        :param Label: 嫌疑片段涉敏结果标签。内容审核模板[画面涉敏任务控制参数](https://cloud.tencent.com/document/api/862/37615#PoliticalImgReviewTemplateInfo)里 LabelSet 参数与此参数取值范围的对应关系：
violation_photo：
<li>violation_photo：违规图标。</li>
politician：
<li>nation_politician：国家领导人；</li>
<li>province_politician: 省部级领导人；</li>
<li>bureau_politician：厅局级领导人；</li>
<li>county_politician：县处级领导人；</li>
<li>rural_politician：乡科级领导人；</li>
<li>sensitive_politician：涉敏人物；</li>
<li>foreign_politician：国外领导人。</li>
entertainment：
<li>sensitive_entertainment：敏感娱乐人物。</li>
sport：
<li>sensitive_sport：敏感体育人物。</li>
entrepreneur：
<li>sensitive_entrepreneur：敏感商业人物。</li>
scholar：
<li>sensitive_scholar：敏感教育学者。</li>
celebrity：
<li>sensitive_celebrity：敏感知名人物；</li>
<li>historical_celebrity：历史知名人物。</li>
military：
<li>sensitive_military：敏感军事人物。</li>
        :type Label: str
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
 PicUrlExpireTime 时间点后图片将被删除）。
        :type Url: str
        :param AreaCoordSet: 涉敏人物、违规图标出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
        :type AreaCoordSet: list of int
        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.Name = None
        self.Label = None
        self.Url = None
        self.AreaCoordSet = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewSegmentItem(AbstractModel):
    """内容审核涉黄/涉敏嫌疑片段

    """

    def __init__(self):
        r"""
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉黄分数。
        :type Confidence: float
        :param Label: 嫌疑片段鉴黄结果标签。
        :type Label: str
        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
 PicUrlExpireTime 时间点后图片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Label = None
        self.Suggestion = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaImageSpriteItem(AbstractModel):
    """雪碧图信息

    """

    def __init__(self):
        r"""
        :param Definition: 雪碧图规格，参见[雪碧图参数模板](https://cloud.tencent.com/document/product/266/33480#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Height: 雪碧图小图的高度。
        :type Height: int
        :param Width: 雪碧图小图的宽度。
        :type Width: int
        :param TotalCount: 每一张雪碧图大图里小图的数量。
        :type TotalCount: int
        :param ImagePathSet: 每一张雪碧图大图的路径。
        :type ImagePathSet: list of str
        :param WebVttPath: 雪碧图子图位置与时间关系的 WebVtt 文件路径。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在雪碧大图里的坐标位置，一般被播放器用于实现预览。
        :type WebVttPath: str
        :param Storage: 雪碧图文件的存储位置。
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImagePathSet = None
        self.WebVttPath = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImagePathSet = params.get("ImagePathSet")
        self.WebVttPath = params.get("WebVttPath")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInputInfo(AbstractModel):
    """媒体处理的输入对象信息。

    """

    def __init__(self):
        r"""
        :param Type: 输入来源对象的类型，支持 COS 和 URL 两种。
        :type Type: str
        :param CosInputInfo: 当 Type 为 COS 时有效，则该项为必填，表示媒体处理 COS 对象信息。
        :type CosInputInfo: :class:`tencentcloud.mps.v20190612.models.CosInputInfo`
        :param UrlInputInfo: 当 Type 为 URL 时有效，则该项为必填，表示媒体处理 URL 对象信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlInputInfo: :class:`tencentcloud.mps.v20190612.models.UrlInputInfo`
        """
        self.Type = None
        self.CosInputInfo = None
        self.UrlInputInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosInputInfo") is not None:
            self.CosInputInfo = CosInputInfo()
            self.CosInputInfo._deserialize(params.get("CosInputInfo"))
        if params.get("UrlInputInfo") is not None:
            self.UrlInputInfo = UrlInputInfo()
            self.UrlInputInfo._deserialize(params.get("UrlInputInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMetaData(AbstractModel):
    """点播媒体文件元信息

    """

    def __init__(self):
        r"""
        :param Size: 上传的媒体文件大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
        :type Size: int
        :param Container: 容器类型，例如 m4a，mp4 等。
        :type Container: str
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        :param Duration: 视频时长，单位：秒。
        :type Duration: float
        :param Rotate: 视频拍摄时的选择角度，单位：度。
        :type Rotate: int
        :param VideoStreamSet: 视频流信息。
        :type VideoStreamSet: list of MediaVideoStreamItem
        :param AudioStreamSet: 音频流信息。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoDuration: 视频时长，单位：秒。
        :type VideoDuration: float
        :param AudioDuration: 音频时长，单位：秒。
        :type AudioDuration: float
        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Rotate = None
        self.VideoStreamSet = None
        self.AudioStreamSet = None
        self.VideoDuration = None
        self.AudioDuration = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Rotate = params.get("Rotate")
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        self.VideoDuration = params.get("VideoDuration")
        self.AudioDuration = params.get("AudioDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskAdaptiveDynamicStreamingResult(AbstractModel):
    """对视频转自适应码流任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频转自适应码流任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AdaptiveDynamicStreamingTaskInput`
        :param Output: 对视频转自适应码流任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.AdaptiveDynamicStreamingInfoItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AdaptiveDynamicStreamingTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AdaptiveDynamicStreamingInfoItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskAnimatedGraphicResult(AbstractModel):
    """转动图任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 转动图任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AnimatedGraphicTaskInput`
        :param Output: 转动图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaAnimatedGraphicsItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AnimatedGraphicTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaAnimatedGraphicsItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskImageSpriteResult(AbstractModel):
    """对视频截雪碧图任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频截雪碧图任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.ImageSpriteTaskInput`
        :param Output: 对视频截雪碧图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaImageSpriteItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = ImageSpriteTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaImageSpriteItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskInput(AbstractModel):
    """媒体处理任务类型

    """

    def __init__(self):
        r"""
        :param TranscodeTaskSet: 视频转码任务列表。
        :type TranscodeTaskSet: list of TranscodeTaskInput
        :param AnimatedGraphicTaskSet: 视频转动图任务列表。
        :type AnimatedGraphicTaskSet: list of AnimatedGraphicTaskInput
        :param SnapshotByTimeOffsetTaskSet: 对视频按时间点截图任务列表。
        :type SnapshotByTimeOffsetTaskSet: list of SnapshotByTimeOffsetTaskInput
        :param SampleSnapshotTaskSet: 对视频采样截图任务列表。
        :type SampleSnapshotTaskSet: list of SampleSnapshotTaskInput
        :param ImageSpriteTaskSet: 对视频截雪碧图任务列表。
        :type ImageSpriteTaskSet: list of ImageSpriteTaskInput
        :param AdaptiveDynamicStreamingTaskSet: 转自适应码流任务列表。
        :type AdaptiveDynamicStreamingTaskSet: list of AdaptiveDynamicStreamingTaskInput
        """
        self.TranscodeTaskSet = None
        self.AnimatedGraphicTaskSet = None
        self.SnapshotByTimeOffsetTaskSet = None
        self.SampleSnapshotTaskSet = None
        self.ImageSpriteTaskSet = None
        self.AdaptiveDynamicStreamingTaskSet = None


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self.TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskInput()
                obj._deserialize(item)
                self.TranscodeTaskSet.append(obj)
        if params.get("AnimatedGraphicTaskSet") is not None:
            self.AnimatedGraphicTaskSet = []
            for item in params.get("AnimatedGraphicTaskSet"):
                obj = AnimatedGraphicTaskInput()
                obj._deserialize(item)
                self.AnimatedGraphicTaskSet.append(obj)
        if params.get("SnapshotByTimeOffsetTaskSet") is not None:
            self.SnapshotByTimeOffsetTaskSet = []
            for item in params.get("SnapshotByTimeOffsetTaskSet"):
                obj = SnapshotByTimeOffsetTaskInput()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTaskSet.append(obj)
        if params.get("SampleSnapshotTaskSet") is not None:
            self.SampleSnapshotTaskSet = []
            for item in params.get("SampleSnapshotTaskSet"):
                obj = SampleSnapshotTaskInput()
                obj._deserialize(item)
                self.SampleSnapshotTaskSet.append(obj)
        if params.get("ImageSpriteTaskSet") is not None:
            self.ImageSpriteTaskSet = []
            for item in params.get("ImageSpriteTaskSet"):
                obj = ImageSpriteTaskInput()
                obj._deserialize(item)
                self.ImageSpriteTaskSet.append(obj)
        if params.get("AdaptiveDynamicStreamingTaskSet") is not None:
            self.AdaptiveDynamicStreamingTaskSet = []
            for item in params.get("AdaptiveDynamicStreamingTaskSet"):
                obj = AdaptiveDynamicStreamingTaskInput()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTaskSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskResult(AbstractModel):
    """任务查询结果类型

    """

    def __init__(self):
        r"""
        :param Type: 任务的类型，可以取的值有：
<li>Transcode：转码</li>
<li>AnimatedGraphics：转动图</li>
<li>SnapshotByTimeOffset：时间点截图</li>
<li>SampleSnapshot：采样截图</li>
<li>ImageSprites：雪碧图</li>
<li>CoverBySnapshot：截图做封面</li>
<li>AdaptiveDynamicStreaming：自适应码流</li>
        :type Type: str
        :param TranscodeTask: 视频转码任务的查询结果，当任务类型为 Transcode 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskTranscodeResult`
        :param AnimatedGraphicTask: 视频转动图任务的查询结果，当任务类型为 AnimatedGraphics 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AnimatedGraphicTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskAnimatedGraphicResult`
        :param SnapshotByTimeOffsetTask: 对视频按时间点截图任务的查询结果，当任务类型为 SnapshotByTimeOffset 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSnapshotByTimeOffsetResult`
        :param SampleSnapshotTask: 对视频采样截图任务的查询结果，当任务类型为 SampleSnapshot 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleSnapshotTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSampleSnapshotResult`
        :param ImageSpriteTask: 对视频截雪碧图任务的查询结果，当任务类型为 ImageSprite 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSpriteTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskImageSpriteResult`
        :param AdaptiveDynamicStreamingTask: 转自适应码流任务查询结果，当任务类型为 AdaptiveDynamicStreaming 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdaptiveDynamicStreamingTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskAdaptiveDynamicStreamingResult`
        """
        self.Type = None
        self.TranscodeTask = None
        self.AnimatedGraphicTask = None
        self.SnapshotByTimeOffsetTask = None
        self.SampleSnapshotTask = None
        self.ImageSpriteTask = None
        self.AdaptiveDynamicStreamingTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = MediaProcessTaskTranscodeResult()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("AnimatedGraphicTask") is not None:
            self.AnimatedGraphicTask = MediaProcessTaskAnimatedGraphicResult()
            self.AnimatedGraphicTask._deserialize(params.get("AnimatedGraphicTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = MediaProcessTaskSnapshotByTimeOffsetResult()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("SampleSnapshotTask") is not None:
            self.SampleSnapshotTask = MediaProcessTaskSampleSnapshotResult()
            self.SampleSnapshotTask._deserialize(params.get("SampleSnapshotTask"))
        if params.get("ImageSpriteTask") is not None:
            self.ImageSpriteTask = MediaProcessTaskImageSpriteResult()
            self.ImageSpriteTask._deserialize(params.get("ImageSpriteTask"))
        if params.get("AdaptiveDynamicStreamingTask") is not None:
            self.AdaptiveDynamicStreamingTask = MediaProcessTaskAdaptiveDynamicStreamingResult()
            self.AdaptiveDynamicStreamingTask._deserialize(params.get("AdaptiveDynamicStreamingTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskSampleSnapshotResult(AbstractModel):
    """对视频做采样截图任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频做采样截图任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.SampleSnapshotTaskInput`
        :param Output: 对视频做采样截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaSampleSnapshotItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SampleSnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSampleSnapshotItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskSnapshotByTimeOffsetResult(AbstractModel):
    """对视频按指定时间点截图任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频按指定时间点截图任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.SnapshotByTimeOffsetTaskInput`
        :param Output: 对视频按指定时间点截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaSnapshotByTimeOffsetItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SnapshotByTimeOffsetTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSnapshotByTimeOffsetItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskTranscodeResult(AbstractModel):
    """转码任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 转码任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.TranscodeTaskInput`
        :param Output: 转码任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaTranscodeItem`
        :param Progress: 转码进度，取值范围 [0-100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.Progress = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = TranscodeTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaTranscodeItem()
            self.Output._deserialize(params.get("Output"))
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSampleSnapshotItem(AbstractModel):
    """采样截图信息

    """

    def __init__(self):
        r"""
        :param Definition: 采样截图规格 ID，参见[采样截图参数模板](https://cloud.tencent.com/document/product/266/33480#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param SampleType: 采样方式，取值范围：
<li>Percent：根据百分比间隔采样。</li>
<li>Time：根据时间间隔采样。</li>
        :type SampleType: str
        :param Interval: 采样间隔
<li>当 SampleType 为 Percent 时，该值表示多少百分比一张图。</li>
<li>当 SampleType 为 Time 时，该值表示多少时间间隔一张图，单位秒， 第一张图均为视频首帧。</li>
        :type Interval: int
        :param Storage: 截图后文件的存储位置。
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param ImagePathSet: 生成的截图 path 列表。
        :type ImagePathSet: list of str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
        :type WaterMarkDefinition: list of int
        """
        self.Definition = None
        self.SampleType = None
        self.Interval = None
        self.Storage = None
        self.ImagePathSet = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SampleType = params.get("SampleType")
        self.Interval = params.get("Interval")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.ImagePathSet = params.get("ImagePathSet")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSnapshotByTimeOffsetItem(AbstractModel):
    """点播文件指定时间点截图信息

    """

    def __init__(self):
        r"""
        :param Definition: 指定时间点截图规格，参见[指定时间点截图参数模板](https://cloud.tencent.com/document/product/266/33480#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param PicInfoSet: 同一规格的截图信息集合，每个元素代表一张截图。
        :type PicInfoSet: list of MediaSnapshotByTimePicInfoItem
        :param Storage: 指定时间点截图文件的存储位置。
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.PicInfoSet = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("PicInfoSet") is not None:
            self.PicInfoSet = []
            for item in params.get("PicInfoSet"):
                obj = MediaSnapshotByTimePicInfoItem()
                obj._deserialize(item)
                self.PicInfoSet.append(obj)
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSnapshotByTimePicInfoItem(AbstractModel):
    """指定时间点截图信息

    """

    def __init__(self):
        r"""
        :param TimeOffset: 该张截图对应视频文件中的时间偏移，单位为秒。
        :type TimeOffset: float
        :param Path: 该张截图的路径。
        :type Path: str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
        :type WaterMarkDefinition: list of int
        """
        self.TimeOffset = None
        self.Path = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Path = params.get("Path")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTranscodeItem(AbstractModel):
    """转码信息

    """

    def __init__(self):
        r"""
        :param OutputStorage: 转码后文件的目标存储。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: 转码后的视频文件路径。
        :type Path: str
        :param Definition: 转码规格 ID，参见[转码参数模板](https://cloud.tencent.com/document/product/862/37042)。
        :type Definition: int
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和， 单位：bps。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        :param Size: 媒体文件总大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
        :type Size: int
        :param Duration: 视频时长，单位：秒。
        :type Duration: float
        :param Container: 容器类型，例如 m4a，mp4 等。
        :type Container: str
        :param Md5: 视频的 md5 值。
        :type Md5: str
        :param AudioStreamSet: 音频流信息。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoStreamSet: 视频流信息。
        :type VideoStreamSet: list of MediaVideoStreamItem
        """
        self.OutputStorage = None
        self.Path = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Size = None
        self.Duration = None
        self.Container = None
        self.Md5 = None
        self.AudioStreamSet = None
        self.VideoStreamSet = None


    def _deserialize(self, params):
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Size = params.get("Size")
        self.Duration = params.get("Duration")
        self.Container = params.get("Container")
        self.Md5 = params.get("Md5")
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaVideoStreamItem(AbstractModel):
    """点播文件视频流信息

    """

    def __init__(self):
        r"""
        :param Bitrate: 视频流的码率，单位：bps。
        :type Bitrate: int
        :param Height: 视频流的高度，单位：px。
        :type Height: int
        :param Width: 视频流的宽度，单位：px。
        :type Width: int
        :param Codec: 视频流的编码格式，例如 h264。
        :type Codec: str
        :param Fps: 帧率，单位：hz。
        :type Fps: int
        :param ColorPrimaries: 色彩空间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ColorPrimaries: str
        :param ColorSpace: 色彩空间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ColorSpace: str
        :param ColorTransfer: 色彩空间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ColorTransfer: str
        :param HdrType: HDR类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type HdrType: str
        """
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Codec = None
        self.Fps = None
        self.ColorPrimaries = None
        self.ColorSpace = None
        self.ColorTransfer = None
        self.HdrType = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.ColorPrimaries = params.get("ColorPrimaries")
        self.ColorSpace = params.get("ColorSpace")
        self.ColorTransfer = params.get("ColorTransfer")
        self.HdrType = params.get("HdrType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIAnalysisTemplateRequest(AbstractModel):
    """ModifyAIAnalysisTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 视频内容分析模板唯一标识。
        :type Definition: int
        :param Name: 视频内容分析模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 视频内容分析模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param ClassificationConfigure: 智能分类任务控制参数。
        :type ClassificationConfigure: :class:`tencentcloud.mps.v20190612.models.ClassificationConfigureInfoForUpdate`
        :param TagConfigure: 智能标签任务控制参数。
        :type TagConfigure: :class:`tencentcloud.mps.v20190612.models.TagConfigureInfoForUpdate`
        :param CoverConfigure: 智能封面任务控制参数。
        :type CoverConfigure: :class:`tencentcloud.mps.v20190612.models.CoverConfigureInfoForUpdate`
        :param FrameTagConfigure: 智能按帧标签任务控制参数。
        :type FrameTagConfigure: :class:`tencentcloud.mps.v20190612.models.FrameTagConfigureInfoForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfoForUpdate()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfoForUpdate()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfoForUpdate()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfoForUpdate()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIAnalysisTemplateResponse(AbstractModel):
    """ModifyAIAnalysisTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAIRecognitionTemplateRequest(AbstractModel):
    """ModifyAIRecognitionTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 视频内容识别模板唯一标识。
        :type Definition: int
        :param Name: 视频内容识别模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 视频内容识别模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param FaceConfigure: 人脸识别控制参数。
        :type FaceConfigure: :class:`tencentcloud.mps.v20190612.models.FaceConfigureInfoForUpdate`
        :param OcrFullTextConfigure: 文本全文识别控制参数。
        :type OcrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.OcrFullTextConfigureInfoForUpdate`
        :param OcrWordsConfigure: 文本关键词识别控制参数。
        :type OcrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.OcrWordsConfigureInfoForUpdate`
        :param AsrFullTextConfigure: 语音全文识别控制参数。
        :type AsrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.AsrFullTextConfigureInfoForUpdate`
        :param AsrWordsConfigure: 语音关键词识别控制参数。
        :type AsrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.AsrWordsConfigureInfoForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfoForUpdate()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfoForUpdate()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfoForUpdate()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfoForUpdate()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfoForUpdate()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIRecognitionTemplateResponse(AbstractModel):
    """ModifyAIRecognitionTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 转自适应码流模板唯一标识。
        :type Definition: int
        :param Name: 模板名称，长度限制：64 个字符。
        :type Name: str
        :param Format: 转自适应码流格式，取值范围：
<li>HLS，</li>
<li>MPEG-DASH。</li>
        :type Format: str
        :param DisableHigherVideoBitrate: 是否禁止视频低码率转高码率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type DisableHigherVideoBitrate: int
        :param DisableHigherVideoResolution: 是否禁止视频分辨率转高分辨率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type DisableHigherVideoResolution: int
        :param StreamInfos: 转自适应码流输入流参数信息，最多输入10路流。
注意：各个流的帧率必须保持一致；如果不一致，采用第一个流的帧率作为输出帧率。
        :type StreamInfos: list of AdaptiveStreamTemplate
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Format = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.StreamInfos = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Format = params.get("Format")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAnimatedGraphicsTemplateRequest(AbstractModel):
    """ModifyAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        :param Name: 转动图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 动图格式，取值为 gif 和 webp。
        :type Format: str
        :param Fps: 帧率，取值范围：[1, 30]，单位：Hz。
        :type Fps: int
        :param Quality: 图片质量，取值范围：[1, 100]，默认值为 75。
        :type Quality: float
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAnimatedGraphicsTemplateResponse(AbstractModel):
    """ModifyAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyContentReviewTemplateRequest(AbstractModel):
    """ModifyContentReviewTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 内容审核模板唯一标识。
        :type Definition: int
        :param Name: 内容审核模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 内容审核模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param PornConfigure: 令人反感的信息的控制参数。
        :type PornConfigure: :class:`tencentcloud.mps.v20190612.models.PornConfigureInfoForUpdate`
        :param TerrorismConfigure: 令人不安全的信息的控制参数。
        :type TerrorismConfigure: :class:`tencentcloud.mps.v20190612.models.TerrorismConfigureInfoForUpdate`
        :param PoliticalConfigure: 令人不适宜的控制参数。
        :type PoliticalConfigure: :class:`tencentcloud.mps.v20190612.models.PoliticalConfigureInfoForUpdate`
        :param ProhibitedConfigure: 违禁控制参数。违禁内容包括：
<li>谩骂；</li>
<li>涉毒违法。</li>
注意：此参数尚未支持。
        :type ProhibitedConfigure: :class:`tencentcloud.mps.v20190612.models.ProhibitedConfigureInfoForUpdate`
        :param UserDefineConfigure: 用户自定义内容审核控制参数。
        :type UserDefineConfigure: :class:`tencentcloud.mps.v20190612.models.UserDefineConfigureInfoForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfoForUpdate()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfoForUpdate()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfoForUpdate()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfoForUpdate()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfoForUpdate()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyContentReviewTemplateResponse(AbstractModel):
    """ModifyContentReviewTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSpriteTemplateRequest(AbstractModel):
    """ModifyImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param Name: 雪碧图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param SampleType: 采样类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param RowCount: 雪碧图中小图的行数。
        :type RowCount: int
        :param ColumnCount: 雪碧图中小图的列数。
        :type ColumnCount: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。
        :type FillType: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param Format: 图片格式，取值可以为 jpg、png、webp。
        :type Format: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.FillType = None
        self.Comment = None
        self.Format = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageSpriteTemplateResponse(AbstractModel):
    """ModifyImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInput(AbstractModel):
    """修改输入信息的参数。

    """

    def __init__(self):
        r"""
        :param InputId: 输入Id。
        :type InputId: str
        :param InputName: 输入名称。
        :type InputName: str
        :param Description: 输入描述。
        :type Description: str
        :param AllowIpList: 允许的推流的IP，CIDR格式。
        :type AllowIpList: list of str
        :param SRTSettings: SRT的配置信息。
        :type SRTSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputSRTSettings`
        :param RTPSettings: RTP的配置信息。
        :type RTPSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputRTPSettings`
        :param Protocol: 输入的协议，可选[SRT|RTP|RTMP]。
当输出包含RTP时，输入只能是RTP。
当输出包含RTMP时，输入可以是SRT/RTMP。
当输出包含SRT时，输入只能是SRT。
        :type Protocol: str
        :param FailOver: 输入的主备开关，可选[OPEN|CLOSE]。
        :type FailOver: str
        :param RTMPPullSettings: RTMP_PULL的配置信息。
        :type RTMPPullSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputRTMPPullSettings`
        :param RTSPPullSettings: RTSP_PULL的配置信息。
        :type RTSPPullSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputRTSPPullSettings`
        :param HLSPullSettings: HLS_PULL的配置信息。
        :type HLSPullSettings: :class:`tencentcloud.mps.v20190612.models.CreateInputHLSPullSettings`
        :param ResilientStream: 延播平滑吐流配置信息。
        :type ResilientStream: :class:`tencentcloud.mps.v20190612.models.ResilientStreamConf`
        """
        self.InputId = None
        self.InputName = None
        self.Description = None
        self.AllowIpList = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.Protocol = None
        self.FailOver = None
        self.RTMPPullSettings = None
        self.RTSPPullSettings = None
        self.HLSPullSettings = None
        self.ResilientStream = None


    def _deserialize(self, params):
        self.InputId = params.get("InputId")
        self.InputName = params.get("InputName")
        self.Description = params.get("Description")
        self.AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateInputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateInputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        self.Protocol = params.get("Protocol")
        self.FailOver = params.get("FailOver")
        if params.get("RTMPPullSettings") is not None:
            self.RTMPPullSettings = CreateInputRTMPPullSettings()
            self.RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        if params.get("RTSPPullSettings") is not None:
            self.RTSPPullSettings = CreateInputRTSPPullSettings()
            self.RTSPPullSettings._deserialize(params.get("RTSPPullSettings"))
        if params.get("HLSPullSettings") is not None:
            self.HLSPullSettings = CreateInputHLSPullSettings()
            self.HLSPullSettings._deserialize(params.get("HLSPullSettings"))
        if params.get("ResilientStream") is not None:
            self.ResilientStream = ResilientStreamConf()
            self.ResilientStream._deserialize(params.get("ResilientStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOutputInfo(AbstractModel):
    """修改Output配置。

    """

    def __init__(self):
        r"""
        :param OutputId: 需要修改的Output的Id。
        :type OutputId: str
        :param OutputName: 输出的名称。
        :type OutputName: str
        :param Description: 输出的描述。
        :type Description: str
        :param Protocol: 输出的转推协议，支持SRT|RTP|RTMP。
        :type Protocol: str
        :param SRTSettings: 转推SRT的配置。
        :type SRTSettings: :class:`tencentcloud.mps.v20190612.models.CreateOutputSRTSettings`
        :param RTPSettings: 转推RTP的配置。
        :type RTPSettings: :class:`tencentcloud.mps.v20190612.models.CreateOutputInfoRTPSettings`
        :param RTMPSettings: 转推RTMP的配置。
        :type RTMPSettings: :class:`tencentcloud.mps.v20190612.models.CreateOutputRTMPSettings`
        :param AllowIpList: IP白名单列表，格式为CIDR，如0.0.0.0/0。
当Protocol为RTMP_PULL有效，为空代表不限制客户端IP。
        :type AllowIpList: list of str
        """
        self.OutputId = None
        self.OutputName = None
        self.Description = None
        self.Protocol = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.RTMPSettings = None
        self.AllowIpList = None


    def _deserialize(self, params):
        self.OutputId = params.get("OutputId")
        self.OutputName = params.get("OutputName")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateOutputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateOutputInfoRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = CreateOutputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))
        self.AllowIpList = params.get("AllowIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonSampleRequest(AbstractModel):
    """ModifyPersonSample请求参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 素材 ID。
        :type PersonId: str
        :param Name: 名称，长度限制：128 个字符。
        :type Name: str
        :param Description: 描述，长度限制：1024 个字符。
        :type Description: str
        :param Usages: 素材应用场景，可选值：
1. Recognition：用于内容识别，等价于 Recognition.Face。
2. Review：用于不适宜的内容识别，等价于 Review.Face。
3. All：用于内容识别、不适宜的内容识别，等价于 1+2。
        :type Usages: list of str
        :param FaceOperationInfo: 五官操作信息。
        :type FaceOperationInfo: :class:`tencentcloud.mps.v20190612.models.AiSampleFaceOperation`
        :param TagOperationInfo: 标签操作信息。
        :type TagOperationInfo: :class:`tencentcloud.mps.v20190612.models.AiSampleTagOperation`
        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.Usages = None
        self.FaceOperationInfo = None
        self.TagOperationInfo = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Usages = params.get("Usages")
        if params.get("FaceOperationInfo") is not None:
            self.FaceOperationInfo = AiSampleFaceOperation()
            self.FaceOperationInfo._deserialize(params.get("FaceOperationInfo"))
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonSampleResponse(AbstractModel):
    """ModifyPersonSample返回参数结构体

    """

    def __init__(self):
        r"""
        :param Person: 素材信息。
        :type Person: :class:`tencentcloud.mps.v20190612.models.AiSamplePerson`
        :param FailFaceInfoSet: 处理失败的五官信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailFaceInfoSet: list of AiSampleFailFaceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifySampleSnapshotTemplateRequest(AbstractModel):
    """ModifySampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param Name: 采样截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param SampleType: 采样截图类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param Format: 图片格式，取值为 jpg、png、webp。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySampleSnapshotTemplateResponse(AbstractModel):
    """ModifySampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 指定时间点截图模板唯一标识。
        :type Definition: int
        :param Name: 指定时间点截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式，取值可以为 jpg、png、webp。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyStreamLinkFlowRequest(AbstractModel):
    """ModifyStreamLinkFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流Id。
        :type FlowId: str
        :param FlowName: 需要修改的流名称。
        :type FlowName: str
        """
        self.FlowId = None
        self.FlowName = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkFlowResponse(AbstractModel):
    """ModifyStreamLinkFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyStreamLinkInputRequest(AbstractModel):
    """ModifyStreamLinkInput请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流Id。
        :type FlowId: str
        :param Input: 需要修改的Input信息。
        :type Input: :class:`tencentcloud.mps.v20190612.models.ModifyInput`
        """
        self.FlowId = None
        self.Input = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Input") is not None:
            self.Input = ModifyInput()
            self.Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkInputResponse(AbstractModel):
    """ModifyStreamLinkInput返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 修改后的Input信息。
        :type Info: :class:`tencentcloud.mps.v20190612.models.DescribeInput`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeInput()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class ModifyStreamLinkOutputInfoRequest(AbstractModel):
    """ModifyStreamLinkOutputInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流Id。
        :type FlowId: str
        :param Output: 需要修改的Output配置。
        :type Output: :class:`tencentcloud.mps.v20190612.models.ModifyOutputInfo`
        """
        self.FlowId = None
        self.Output = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self.Output = ModifyOutputInfo()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkOutputInfoResponse(AbstractModel):
    """ModifyStreamLinkOutputInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 修改后的Output配置。
        :type Info: :class:`tencentcloud.mps.v20190612.models.DescribeOutput`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeOutput()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class ModifyTranscodeTemplateRequest(AbstractModel):
    """ModifyTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 转码模板唯一标识。
        :type Definition: int
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。
        :type Container: str
        :param Name: 转码模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数。
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfoForUpdate`
        :param AudioTemplate: 音频流配置参数。
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfoForUpdate`
        :param TEHDConfig: 极速高清转码参数。
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfigForUpdate`
        :param EnhanceConfig: 音视频增强参数。
        :type EnhanceConfig: :class:`tencentcloud.mps.v20190612.models.EnhanceConfig`
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.EnhanceConfig = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        if params.get("EnhanceConfig") is not None:
            self.EnhanceConfig = EnhanceConfig()
            self.EnhanceConfig._deserialize(params.get("EnhanceConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTranscodeTemplateResponse(AbstractModel):
    """ModifyTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWatermarkTemplateRequest(AbstractModel):
    """ModifyWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param Name: 水印模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param CoordinateOrigin: 原点位置，可选值：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>
        :type CoordinateOrigin: str
        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
        :type XPos: str
        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
        :type YPos: str
        :param ImageTemplate: 图片水印模板，该字段仅对图片水印模板有效。
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkInputForUpdate`
        :param TextTemplate: 文字水印模板，该字段仅对文字水印模板有效。
        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInputForUpdate`
        :param SvgTemplate: SVG水印模板，当 Type 为 svg，该字段必填。当 Type 为 image 或 text，该字段无效。
        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInputForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInputForUpdate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInputForUpdate()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInputForUpdate()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWatermarkTemplateResponse(AbstractModel):
    """ModifyWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片水印地址，仅当 ImageTemplate.ImageContent 非空，该字段有效。
        :type ImageUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class ModifyWordSampleRequest(AbstractModel):
    """ModifyWordSample请求参数结构体

    """

    def __init__(self):
        r"""
        :param Keyword: 关键词，长度限制：128 个字符。
        :type Keyword: str
        :param Usages: <b>关键词应用场景，可选值：</b>
1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；
2. Recognition.Asr：通过音频识别技术，进行内容识别；
3. Review.Ocr：通过光学字符识别技术，进行不适宜的内容识别；
4. Review.Asr：通过音频识别技术，进行不适宜的音频识别；
<b>可合并简写为：</b>
5. Recognition：通过光学字符识别技术、音频识别技术，进行内容识别，等价于 1+2；
6. Review：通过光学字符识别技术、音频识别技术，进行不适宜的内容识别，等价于 3+4；
7. All：包含以上全部，等价于 1+2+3+4。
        :type Usages: list of str
        :param TagOperationInfo: 标签操作信息。
        :type TagOperationInfo: :class:`tencentcloud.mps.v20190612.models.AiSampleTagOperation`
        """
        self.Keyword = None
        self.Usages = None
        self.TagOperationInfo = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Usages = params.get("Usages")
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWordSampleResponse(AbstractModel):
    """ModifyWordSample返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MosaicInput(AbstractModel):
    """媒体处理任务中的马赛克参数类型

    """

    def __init__(self):
        r"""
        :param CoordinateOrigin: 原点位置，目前仅支持：
<li>TopLeft：表示坐标原点位于视频图像左上角，马赛克原点为图片或文字的左上角。</li>
默认值：TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 马赛克原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。
        :type XPos: str
        :param YPos: 马赛克原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。
        :type YPos: str
        :param Width: 马赛克的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
默认值：10%。
        :type Width: str
        :param Height: 马赛克的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 Height 单位为像素，如 100px 表示 Height 为 100 像素。</li>
默认值：10%。
        :type Height: str
        :param StartTimeOffset: 马赛克的起始时间偏移，单位：秒。不填或填0，表示马赛克从画面出现时开始显现。
<li>不填或填0，表示马赛克从画面开始就出现；</li>
<li>当数值大于0时（假设为 n），表示马赛克从画面开始的第 n 秒出现；</li>
<li>当数值小于0时（假设为 -n），表示马赛克从离画面结束 n 秒前开始出现。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 马赛克的结束时间偏移，单位：秒。
<li>不填或填0，表示马赛克持续到画面结束；</li>
<li>当数值大于0时（假设为 n），表示马赛克持续到第 n 秒时消失；</li>
<li>当数值小于0时（假设为 -n），表示马赛克持续到离画面结束 n 秒前消失。</li>
        :type EndTimeOffset: float
        """
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NumberFormat(AbstractModel):
    """输出文件名的`{number}`变量的规则。

    """

    def __init__(self):
        r"""
        :param InitialValue: `{number}`变量的起始值，默认为0。
        :type InitialValue: int
        :param Increment: `{number}`变量的增长步长，默认为1。
        :type Increment: int
        :param MinLength: `{number}`变量的最小长度，不足时补占位符。默认为1。
        :type MinLength: int
        :param PlaceHolder: `{number}`变量的长度不足时，补充的占位符。默认为"0"。
        :type PlaceHolder: str
        """
        self.InitialValue = None
        self.Increment = None
        self.MinLength = None
        self.PlaceHolder = None


    def _deserialize(self, params):
        self.InitialValue = params.get("InitialValue")
        self.Increment = params.get("Increment")
        self.MinLength = params.get("MinLength")
        self.PlaceHolder = params.get("PlaceHolder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrFullTextConfigureInfo(AbstractModel):
    """文本全文本识别任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 文本全文识别任务开关，可选值：
<li>ON：开启智能文本全文识别任务；</li>
<li>OFF：关闭智能文本全文识别任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrFullTextConfigureInfoForUpdate(AbstractModel):
    """文本全文本识别任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 文本全文识别任务开关，可选值：
<li>ON：开启智能文本全文识别任务；</li>
<li>OFF：关闭智能文本全文识别任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrWordsConfigureInfo(AbstractModel):
    """文本关键词识别控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 文本关键词识别任务开关，可选值：
<li>ON：开启文本关键词识别任务；</li>
<li>OFF：关闭文本关键词识别任务。</li>
        :type Switch: str
        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrWordsConfigureInfoForUpdate(AbstractModel):
    """文本关键词识别控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 文本关键词识别任务开关，可选值：
<li>ON：开启文本关键词识别任务；</li>
<li>OFF：关闭文本关键词识别任务。</li>
        :type Switch: str
        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputAddress(AbstractModel):
    """输出的出口的地址。

    """

    def __init__(self):
        r"""
        :param Ip: 出口IP。
        :type Ip: str
        """
        self.Ip = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputSRTSourceAddressResp(AbstractModel):
    """SRT输出的监听地址。

    """

    def __init__(self):
        r"""
        :param Ip: 监听IP。
        :type Ip: str
        :param Port: 监听端口。
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverrideTranscodeParameter(AbstractModel):
    """自定义转码的规格参数。用于覆盖模板中对应参数值。

    """

    def __init__(self):
        r"""
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。
        :type Container: str
        :param RemoveVideo: 是否去除视频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数。
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfoForUpdate`
        :param AudioTemplate: 音频流配置参数。
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfoForUpdate`
        :param TEHDConfig: 极速高清转码参数。
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfigForUpdate`
        :param SubtitleTemplate: 字幕流配置参数。
        :type SubtitleTemplate: :class:`tencentcloud.mps.v20190612.models.SubtitleTemplate`
        """
        self.Container = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.SubtitleTemplate = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        if params.get("SubtitleTemplate") is not None:
            self.SubtitleTemplate = SubtitleTemplate()
            self.SubtitleTemplate._deserialize(params.get("SubtitleTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseLiveStreamProcessNotificationRequest(AbstractModel):
    """ParseLiveStreamProcessNotification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Content: 从 CMQ 获取到的直播流事件通知内容。
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseLiveStreamProcessNotificationResponse(AbstractModel):
    """ParseLiveStreamProcessNotification返回参数结构体

    """

    def __init__(self):
        r"""
        :param NotificationType: 直播流处理结果类型，包含：
<li>AiReviewResult：内容审核结果；</li>
<li>AiRecognitionResult：内容识别结果；</li>
<li>ProcessEof：直播流处理结束。</li>
        :type NotificationType: str
        :param TaskId: 视频处理任务 ID。
        :type TaskId: str
        :param ProcessEofInfo: 直播流处理错误信息，当 NotificationType 为 ProcessEof 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessEofInfo: :class:`tencentcloud.mps.v20190612.models.LiveStreamProcessErrorInfo`
        :param AiReviewResultInfo: 内容审核结果，当 NotificationType 为 AiReviewResult 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiReviewResultInfo: :class:`tencentcloud.mps.v20190612.models.LiveStreamAiReviewResultInfo`
        :param AiRecognitionResultInfo: 内容识别结果，当 NotificationType 为 AiRecognitionResult 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiRecognitionResultInfo: :class:`tencentcloud.mps.v20190612.models.LiveStreamAiRecognitionResultInfo`
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长50个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长1000个字符。
        :type SessionContext: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotificationType = None
        self.TaskId = None
        self.ProcessEofInfo = None
        self.AiReviewResultInfo = None
        self.AiRecognitionResultInfo = None
        self.SessionId = None
        self.SessionContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotificationType = params.get("NotificationType")
        self.TaskId = params.get("TaskId")
        if params.get("ProcessEofInfo") is not None:
            self.ProcessEofInfo = LiveStreamProcessErrorInfo()
            self.ProcessEofInfo._deserialize(params.get("ProcessEofInfo"))
        if params.get("AiReviewResultInfo") is not None:
            self.AiReviewResultInfo = LiveStreamAiReviewResultInfo()
            self.AiReviewResultInfo._deserialize(params.get("AiReviewResultInfo"))
        if params.get("AiRecognitionResultInfo") is not None:
            self.AiRecognitionResultInfo = LiveStreamAiRecognitionResultInfo()
            self.AiRecognitionResultInfo._deserialize(params.get("AiRecognitionResultInfo"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.RequestId = params.get("RequestId")


class ParseNotificationRequest(AbstractModel):
    """ParseNotification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Content: 从 CMQ 获取到的事件通知内容。
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseNotificationResponse(AbstractModel):
    """ParseNotification返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventType: 支持事件类型，目前取值有：
<li>WorkflowTask：视频工作流处理任务。</li>
<li>EditMediaTask：视频编辑任务。</li>
<li>ScheduleTask：编排任务。</li>
        :type EventType: str
        :param WorkflowTaskEvent: 视频处理任务信息，仅当 EventType 为 WorkflowTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowTaskEvent: :class:`tencentcloud.mps.v20190612.models.WorkflowTask`
        :param EditMediaTaskEvent: 视频编辑任务信息，仅当 EventType 为 EditMediaTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type EditMediaTaskEvent: :class:`tencentcloud.mps.v20190612.models.EditMediaTask`
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长50个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长1000个字符。
        :type SessionContext: str
        :param ScheduleTaskEvent: 编排任务信息，仅当 EventType 为 ScheduleTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleTaskEvent: :class:`tencentcloud.mps.v20190612.models.ScheduleTask`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventType = None
        self.WorkflowTaskEvent = None
        self.EditMediaTaskEvent = None
        self.SessionId = None
        self.SessionContext = None
        self.ScheduleTaskEvent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventType = params.get("EventType")
        if params.get("WorkflowTaskEvent") is not None:
            self.WorkflowTaskEvent = WorkflowTask()
            self.WorkflowTaskEvent._deserialize(params.get("WorkflowTaskEvent"))
        if params.get("EditMediaTaskEvent") is not None:
            self.EditMediaTaskEvent = EditMediaTask()
            self.EditMediaTaskEvent._deserialize(params.get("EditMediaTaskEvent"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        if params.get("ScheduleTaskEvent") is not None:
            self.ScheduleTaskEvent = ScheduleTask()
            self.ScheduleTaskEvent._deserialize(params.get("ScheduleTaskEvent"))
        self.RequestId = params.get("RequestId")


class PoliticalAsrReviewTemplateInfo(AbstractModel):
    """语音涉敏任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 语音涉敏任务开关，可选值：
<li>ON：开启语音涉敏任务；</li>
<li>OFF：关闭语音涉敏任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalAsrReviewTemplateInfoForUpdate(AbstractModel):
    """语音涉敏任务控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 语音涉敏任务开关，可选值：
<li>ON：开启语音涉敏任务；</li>
<li>OFF：关闭语音涉敏任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalConfigureInfo(AbstractModel):
    """涉敏任务控制参数

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: 画面涉敏控制参数。
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalImgReviewTemplateInfo`
        :param AsrReviewInfo: 语音涉敏控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本涉敏控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalConfigureInfoForUpdate(AbstractModel):
    """涉敏任务控制参数。

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: 画面涉敏控制参数。
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 语音涉敏控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本涉敏控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalImgReviewTemplateInfo(AbstractModel):
    """画面涉敏任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 画面涉敏任务开关，可选值：
<li>ON：开启画面涉敏任务；</li>
<li>OFF：关闭画面涉敏任务。</li>
        :type Switch: str
        :param LabelSet: 画面涉敏过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>violation_photo：违规图标；</li>
<li>politician：涉敏人物；</li>
<li>entertainment：娱乐人物；</li>
<li>sport：体育人物；</li>
<li>entrepreneur：商业人物；</li>
<li>scholar：教育学者；</li>
<li>celebrity：知名人物；</li>
<li>military：军事人物。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 97 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 95 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalImgReviewTemplateInfoForUpdate(AbstractModel):
    """画面涉敏任务控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 画面涉敏任务开关，可选值：
<li>ON：开启画面涉敏任务；</li>
<li>OFF：关闭画面涉敏任务。</li>
        :type Switch: str
        :param LabelSet: 画面涉敏过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>violation_photo：违规图标；</li>
<li>politician：涉敏人物；</li>
<li>entertainment：娱乐人物；</li>
<li>sport：体育人物；</li>
<li>entrepreneur：商业人物；</li>
<li>scholar：教育学者；</li>
<li>celebrity：知名人物；</li>
<li>military：军事人物。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalOcrReviewTemplateInfo(AbstractModel):
    """文本涉敏任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 文本涉敏任务开关，可选值：
<li>ON：开启文本涉敏任务；</li>
<li>OFF：关闭文本涉敏任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本涉敏任务控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 文本涉敏任务开关，可选值：
<li>ON：开启文本涉敏任务；</li>
<li>OFF：关闭文本涉敏任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornAsrReviewTemplateInfo(AbstractModel):
    """语音鉴黄任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 语音鉴黄任务开关，可选值：
<li>ON：开启语音鉴黄任务；</li>
<li>OFF：关闭语音鉴黄任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornAsrReviewTemplateInfoForUpdate(AbstractModel):
    """语音鉴黄任务控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 语音鉴黄任务开关，可选值：
<li>ON：开启语音鉴黄任务；</li>
<li>OFF：关闭语音鉴黄任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornConfigureInfo(AbstractModel):
    """鉴黄任务控制参数

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: 画面鉴黄控制参数。
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornImgReviewTemplateInfo`
        :param AsrReviewInfo: 语音鉴黄控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本鉴黄控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornConfigureInfoForUpdate(AbstractModel):
    """鉴黄任务控制参数。

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: 画面鉴黄控制参数。
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 语音鉴黄控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本鉴黄控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornImgReviewTemplateInfo(AbstractModel):
    """画面鉴黄任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 画面鉴黄任务开关，可选值：
<li>ON：开启画面鉴黄任务；</li>
<li>OFF：关闭画面鉴黄任务。</li>
        :type Switch: str
        :param LabelSet: 画面鉴黄过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>porn：色情；</li>
<li>vulgar：低俗；</li>
<li>intimacy：亲密行为；</li>
<li>sexy：性感。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 90 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 0 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornImgReviewTemplateInfoForUpdate(AbstractModel):
    """画面鉴黄任务控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 画面鉴黄任务开关，可选值：
<li>ON：开启画面鉴黄任务；</li>
<li>OFF：关闭画面鉴黄任务。</li>
        :type Switch: str
        :param LabelSet: 画面鉴黄过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>porn：色情；</li>
<li>vulgar：低俗；</li>
<li>intimacy：亲密行为；</li>
<li>sexy：性感。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornOcrReviewTemplateInfo(AbstractModel):
    """文本鉴黄任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 文本鉴黄任务开关，可选值：
<li>ON：开启文本鉴黄任务；</li>
<li>OFF：关闭文本鉴黄任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本鉴黄任务控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 文本鉴黄任务开关，可选值：
<li>ON：开启文本鉴黄任务；</li>
<li>OFF：关闭文本鉴黄任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessLiveStreamRequest(AbstractModel):
    """ProcessLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 直播流 URL（必须是直播文件地址，支持 rtmp，hls 和 flv 等）。
        :type Url: str
        :param TaskNotifyConfig: 任务的事件通知信息，用于指定直播流处理的结果。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.LiveStreamTaskNotifyConfig`
        :param OutputStorage: 直播流处理输出文件的目标存储。如处理有文件输出，该参数为必填项。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 直播流处理生成的文件输出的目标目录，如`/movie/201909/`，如果不填为 `/` 目录。
        :type OutputDir: str
        :param AiContentReviewTask: 视频内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiRecognitionTask: 视频内容识别类型任务参数。
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        """
        self.Url = None
        self.TaskNotifyConfig = None
        self.OutputStorage = None
        self.OutputDir = None
        self.AiContentReviewTask = None
        self.AiRecognitionTask = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = LiveStreamTaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessLiveStreamResponse(AbstractModel):
    """ProcessLiveStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProcessMediaRequest(AbstractModel):
    """ProcessMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param InputInfo: 媒体处理的文件输入信息。
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param OutputStorage: 媒体处理输出文件的目标存储。不填则继承 InputInfo 中的存储位置。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 媒体处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与 InputInfo 中文件所在的目录一致。
        :type OutputDir: str
        :param MediaProcessTask: 媒体处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 视频内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 视频内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 视频内容识别类型任务参数。
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: 任务流的优先级，数值越大优先级越高，取值范围是-10到 10，不填代表0。
        :type TasksPriority: int
        :param SessionId: 用于去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param ScheduleId: 编排ID。
注意1：对于OutputStorage、OutputDir参数：
<li>当服务编排中子任务节点配置了OutputStorage、OutputDir时，该子任务节点中配置的输出作为子任务的输出。</li>
<li>当服务编排中子任务节点没有配置OutputStorage、OutputDir时，若创建任务接口（ProcessMedia）有输出，将覆盖原有编排的默认输出。</li>
注意2：对于TaskNotifyConfig参数，若创建任务接口（ProcessMedia）有设置，将覆盖原有编排的默认回调。

注意3：编排的 Trigger 只是用来自动化触发场景，在手动发起的请求中已经配置的 Trigger 无意义。
        :type ScheduleId: int
        """
        self.InputInfo = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None
        self.ScheduleId = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.ScheduleId = params.get("ScheduleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMediaResponse(AbstractModel):
    """ProcessMedia返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProhibitedAsrReviewTemplateInfo(AbstractModel):
    """语音违禁任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 语音违禁任务开关，可选值：
<li>ON：开启语音违禁任务；</li>
<li>OFF：关闭语音违禁任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedAsrReviewTemplateInfoForUpdate(AbstractModel):
    """语音违禁任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 语音违禁任务开关，可选值：
<li>ON：开启语音违禁任务；</li>
<li>OFF：关闭语音违禁任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedConfigureInfo(AbstractModel):
    """违禁任务控制参数

    """

    def __init__(self):
        r"""
        :param AsrReviewInfo: 语音违禁控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本违禁控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedOcrReviewTemplateInfo`
        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedConfigureInfoForUpdate(AbstractModel):
    """违禁任务控制参数

    """

    def __init__(self):
        r"""
        :param AsrReviewInfo: 语音违禁控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本违禁控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedOcrReviewTemplateInfoForUpdate`
        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedOcrReviewTemplateInfo(AbstractModel):
    """文本违禁任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 文本违禁任务开关，可选值：
<li>ON：开启文本违禁任务；</li>
<li>OFF：关闭文本违禁任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本违禁任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 文本违禁任务开关，可选值：
<li>ON：开启文本违禁任务；</li>
<li>OFF：关闭文本违禁任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTMPAddressDestination(AbstractModel):
    """RTMP转推的目标地址信息。

    """

    def __init__(self):
        r"""
        :param Url: 转推RTMP的目标Url，格式如'rtmp://domain/live'。
        :type Url: str
        :param StreamKey: 转推RTMP的目标StreamKey，格式如'steamid?key=value'。
        :type StreamKey: str
        """
        self.Url = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTMPPullSourceAddress(AbstractModel):
    """创建的输入RTMP拉流源站配置信息。

    """

    def __init__(self):
        r"""
        :param TcUrl: RTMP源站的TcUrl地址。
        :type TcUrl: str
        :param StreamKey: RTMP源站的StreamKey信息。
        :type StreamKey: str
        """
        self.TcUrl = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.TcUrl = params.get("TcUrl")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTPAddressDestination(AbstractModel):
    """转推的RTP目标地址信息。

    """

    def __init__(self):
        r"""
        :param Ip: 转推的目标地址的IP。
        :type Ip: str
        :param Port: 转推的目标地址的端口。
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTSPPullSourceAddress(AbstractModel):
    """创建的输入RTSP拉流源站配置信息。

    """

    def __init__(self):
        r"""
        :param Url: RTSP源站的Url地址。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawImageWatermarkInput(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        r"""
        :param ImageContent: 水印图片的输入内容。支持 jpeg、png 图片格式。
        :type ImageContent: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
默认值：10%。
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素。</li>
默认值：0px，表示 Height 按照原始水印图片的宽高比缩放。
        :type Height: str
        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束（默认值）。</li>
        :type RepeatType: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        if params.get("ImageContent") is not None:
            self.ImageContent = MediaInputInfo()
            self.ImageContent._deserialize(params.get("ImageContent"))
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawTranscodeParameter(AbstractModel):
    """自定义转码的规格参数。

    """

    def __init__(self):
        r"""
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。
        :type Container: str
        :param RemoveVideo: 是否去除视频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数，当 RemoveVideo 为 0，该字段必填。
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: 音频流配置参数，当 RemoveAudio 为 0，该字段必填。
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: 极速高清转码参数。
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`
        """
        self.Container = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawWatermarkParameter(AbstractModel):
    """自定义水印规格参数。

    """

    def __init__(self):
        r"""
        :param Type: 水印类型，可选值：
<li>image：图片水印。</li>
        :type Type: str
        :param CoordinateOrigin: 原点位置，目前仅支持：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角。</li>
默认值：TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。
        :type XPos: str
        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。
        :type YPos: str
        :param ImageTemplate: 图片水印模板，当 Type 为 image，该字段必填。当 Type 为 text，该字段无效。
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.RawImageWatermarkInput`
        """
        self.Type = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = RawImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeMediaForZhiXueRequest(AbstractModel):
    """RecognizeMediaForZhiXue请求参数结构体

    """

    def __init__(self):
        r"""
        :param InputInfo: 输入媒体文件存储信息。
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param ExpressionConfig: 表情识别参数配置。默认开启。
        :type ExpressionConfig: :class:`tencentcloud.mps.v20190612.models.ExpressionConfigInfo`
        :param ActionConfig: 动作识别参数配置。默认开启。
        :type ActionConfig: :class:`tencentcloud.mps.v20190612.models.ActionConfigInfo`
        """
        self.InputInfo = None
        self.ExpressionConfig = None
        self.ActionConfig = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("ExpressionConfig") is not None:
            self.ExpressionConfig = ExpressionConfigInfo()
            self.ExpressionConfig._deserialize(params.get("ExpressionConfig"))
        if params.get("ActionConfig") is not None:
            self.ActionConfig = ActionConfigInfo()
            self.ActionConfig._deserialize(params.get("ActionConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeMediaForZhiXueResponse(AbstractModel):
    """RecognizeMediaForZhiXue返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID，可以通过该 ID 查询任务状态和结果。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地区信息。

    """

    def __init__(self):
        r"""
        :param Name: 地区名称。
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetWorkflowRequest(AbstractModel):
    """ResetWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        :param WorkflowName: 工作流名称，最多128字符。同一个用户该名称唯一。
        :type WorkflowName: str
        :param Trigger: 工作流绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。
        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: 视频处理的文件输出配置。不填则继承 Trigger 中的存储位置。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致，即`{inputDir}`。
        :type OutputDir: str
        :param MediaProcessTask: 视频处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 视频内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 视频内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 视频内容识别类型任务参数。
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskPriority: 工作流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TaskPriority: int
        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskPriority = None
        self.TaskNotifyConfig = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.TaskPriority = params.get("TaskPriority")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetWorkflowResponse(AbstractModel):
    """ResetWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResilientStreamConf(AbstractModel):
    """延播平滑吐流配置。

    """

    def __init__(self):
        r"""
        :param Enable: 是否开启延播平滑吐流，true开启，false不开启，默认不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: bool
        :param BufferTime: 延播时间，单位秒，目前支持的范围为10~300秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type BufferTime: int
        """
        self.Enable = None
        self.BufferTime = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.BufferTime = params.get("BufferTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTAddressDestination(AbstractModel):
    """转推的目标地址信息。

    """

    def __init__(self):
        r"""
        :param Ip: 目标地址的IP。
        :type Ip: str
        :param Port: 目标地址的端口。
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTSourceAddressReq(AbstractModel):
    """SRT输入源地址。

    """

    def __init__(self):
        r"""
        :param Ip: 对端IP。
        :type Ip: str
        :param Port: 对端端口。
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTSourceAddressResp(AbstractModel):
    """SRT输入源地址。

    """

    def __init__(self):
        r"""
        :param Ip: 对端IP。
        :type Ip: str
        :param Port: 对端端口。
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleSnapshotTaskInput(AbstractModel):
    """对视频做采样截图任务输入参数类型。

    """

    def __init__(self):
        r"""
        :param Definition: 采样截图模板 ID。
        :type Definition: int
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 采样截图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 采样截图后图片文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_sampleSnapshot_{definition}_{number}.{format}`。
        :type OutputObjectPath: str
        :param ObjectNumberFormat: 采样截图后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleSnapshotTemplate(AbstractModel):
    """采样截图模板详情

    """

    def __init__(self):
        r"""
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 采样截图模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式。
        :type Format: str
        :param SampleType: 采样截图类型。
        :type SampleType: str
        :param SampleInterval: 采样间隔。
        :type SampleInterval: int
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.SampleType = None
        self.SampleInterval = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleAnalysisTaskResult(AbstractModel):
    """编排视频分析任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 分析任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param Output: 分析任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: list of AiAnalysisResult
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = []
            for item in params.get("Output"):
                obj = AiAnalysisResult()
                obj._deserialize(item)
                self.Output.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleRecognitionTaskResult(AbstractModel):
    """编排视频识别任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 识别任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param Output: 识别任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: list of AiRecognitionResult
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = []
            for item in params.get("Output"):
                obj = AiRecognitionResult()
                obj._deserialize(item)
                self.Output.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleReviewTaskResult(AbstractModel):
    """编排视频审核任务结果类型

    """

    def __init__(self):
        r"""
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 审核任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param Output: 审核任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: list of AiContentReviewResult
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiContentReviewTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = []
            for item in params.get("Output"):
                obj = AiContentReviewResult()
                obj._deserialize(item)
                self.Output.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleTask(AbstractModel):
    """编排任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 编排任务 ID。
        :type TaskId: str
        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param InputInfo: 媒体处理的目标文件信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param MetaData: 原始视频的元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.mps.v20190612.models.MediaMetaData`
        :param ActivityResultSet: 编排任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityResultSet: list of ActivityResult
        """
        self.TaskId = None
        self.Status = None
        self.InputInfo = None
        self.MetaData = None
        self.ActivityResultSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("ActivityResultSet") is not None:
            self.ActivityResultSet = []
            for item in params.get("ActivityResultSet"):
                obj = ActivityResult()
                obj._deserialize(item)
                self.ActivityResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScratchRepairConfig(AbstractModel):
    """去划痕配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Intensity: 强度，取值范围：0.0~1.0。
默认：0.0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Intensity: float
        """
        self.Switch = None
        self.Intensity = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Intensity = params.get("Intensity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SharpEnhanceConfig(AbstractModel):
    """细节增强配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Intensity: 强度，取值范围：0.0~1.0。
默认：0.0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Intensity: float
        """
        self.Switch = None
        self.Intensity = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Intensity = params.get("Intensity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotByTimeOffsetTaskInput(AbstractModel):
    """对视频按指定时间点截图任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 指定时间点截图模板 ID。
        :type Definition: int
        :param ExtTimeOffsetSet: 截图时间点列表，时间点支持 s、% 两种格式：
<li>当字符串以 s 结尾，表示时间点单位为秒，如 3.5s 表示时间点为第3.5秒；</li>
<li>当字符串以 % 结尾，表示时间点为视频时长的百分比大小，如10%表示时间点为视频前第10%的时间。</li>
        :type ExtTimeOffsetSet: list of str
        :param TimeOffsetSet: 截图时间点列表，单位为<font color=red>秒</font>。此参数已不再建议使用，建议您使用 ExtTimeOffsetSet 参数。
        :type TimeOffsetSet: list of float
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 时间点截图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 时间点截图后图片文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_snapshotByTimeOffset_{definition}_{number}.{format}`。
        :type OutputObjectPath: str
        :param ObjectNumberFormat: 时间点截图后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.ExtTimeOffsetSet = None
        self.TimeOffsetSet = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ExtTimeOffsetSet = params.get("ExtTimeOffsetSet")
        self.TimeOffsetSet = params.get("TimeOffsetSet")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotByTimeOffsetTemplate(AbstractModel):
    """时间点截图模板详情

    """

    def __init__(self):
        r"""
        :param Definition: 时间点截图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 时间点截图模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式。
        :type Format: str
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>black：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>black：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLinkFlowRequest(AbstractModel):
    """StartStreamLinkFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流Id。
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLinkFlowResponse(AbstractModel):
    """StartStreamLinkFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopStreamLinkFlowRequest(AbstractModel):
    """StopStreamLinkFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流Id。
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopStreamLinkFlowResponse(AbstractModel):
    """StopStreamLinkFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamLinkRegionInfo(AbstractModel):
    """媒体传输的地区信息。

    """

    def __init__(self):
        r"""
        :param Regions: 媒体直传输的地区信息列表。
        :type Regions: list of RegionInfo
        """
        self.Regions = None


    def _deserialize(self, params):
        if params.get("Regions") is not None:
            self.Regions = []
            for item in params.get("Regions"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.Regions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubtitleTemplate(AbstractModel):
    """字幕流配置参数。

    """

    def __init__(self):
        r"""
        :param Path: 要压制到视频中的字幕文件地址。
        :type Path: str
        :param StreamIndex: 指定要压制到视频中的字幕轨道，如果有指定Path，则Path 优先级更高。Path 和 StreamIndex 至少指定一个。
        :type StreamIndex: int
        :param FontType: 字体类型，
<li>hei.ttf：黑体</li>
<li>song.ttf：宋体</li>
<li>simkai.ttf：楷体</li>
<li>arial.ttf：仅支持英文</li>
默认hei.ttf
        :type FontType: str
        :param FontSize: 字体大小，格式：Npx，N 为数值，不指定则以字幕文件中为准。
        :type FontSize: str
        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（白色）
        :type FontColor: str
        :param FontAlpha: 文字透明度，取值范围：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
默认值：1。
        :type FontAlpha: float
        """
        self.Path = None
        self.StreamIndex = None
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.StreamIndex = params.get("StreamIndex")
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuperResolutionConfig(AbstractModel):
    """超分配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Type: 类型，可选值：
<li>lq：针对低清晰度有较多噪声视频的超分；</li>
<li>hq：针对高清晰度视频超分。</li>
默认值：lq。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Size: 超分倍数，可选值：
<li>2：目前只支持 2 倍超分。</li>
默认值：2。
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        """
        self.Switch = None
        self.Type = None
        self.Size = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Type = params.get("Type")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SvgWatermarkInput(AbstractModel):
    """SVG水印模板输入参数

    """

    def __init__(self):
        r"""
        :param Width: 水印的宽度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；当填 0px 且
 Height 不为 0px 时，表示水印的宽度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的宽度取原始 SVG 图像的宽度；</li>
<li>当字符串以 W% 结尾，表示水印 Width 为视频宽度的百分比大小，如 10W% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Width 为视频高度的百分比大小，如 10H% 表示 Width 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Width 为视频短边的百分比大小，如 10S% 表示 Width 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Width 为视频长边的百分比大小，如 10L% 表示 Width 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 W%。</li>
默认值为 10W%。
        :type Width: str
        :param Height: 水印的高度，支持 px，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；当填 0px 且
 Width 不为 0px 时，表示水印的高度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的高度取原始 SVG 图像的高度；</li>
<li>当字符串以 W% 结尾，表示水印 Height 为视频宽度的百分比大小，如 10W% 表示 Height 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Height 为视频高度的百分比大小，如 10H% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Height 为视频短边的百分比大小，如 10S% 表示 Height 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Height 为视频长边的百分比大小，如 10L% 表示 Height 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 H%。</li>
默认值为 0px。
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SvgWatermarkInputForUpdate(AbstractModel):
    """SVG水印模板输入参数

    """

    def __init__(self):
        r"""
        :param Width: 水印的宽度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；当填 0px 且
 Height 不为 0px 时，表示水印的宽度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的宽度取原始 SVG 图像的宽度；</li>
<li>当字符串以 W% 结尾，表示水印 Width 为视频宽度的百分比大小，如 10W% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Width 为视频高度的百分比大小，如 10H% 表示 Width 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Width 为视频短边的百分比大小，如 10S% 表示 Width 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Width 为视频长边的百分比大小，如 10L% 表示 Width 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 W%。</li>
默认值为 10W%。
        :type Width: str
        :param Height: 水印的高度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；当填 0px 且
 Width 不为 0px 时，表示水印的高度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的高度取原始 SVG 图像的高度；</li>
<li>当字符串以 W% 结尾，表示水印 Height 为视频宽度的百分比大小，如 10W% 表示 Height 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Height 为视频高度的百分比大小，如 10H% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Height 为视频短边的百分比大小，如 10S% 表示 Height 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Height 为视频长边的百分比大小，如 10L% 表示 Height 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 H%。
默认值为 0px。
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TEHDConfig(AbstractModel):
    """极速高清参数配置。

    """

    def __init__(self):
        r"""
        :param Type: 极速高清类型，可选值：
<li>TEHD-100：极速高清-100。</li>
不填代表不启用极速高清。
        :type Type: str
        :param MaxVideoBitrate: 视频码率上限，当 Type 指定了极速高清类型时有效。
不填或填0表示不设视频码率上限。
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TEHDConfigForUpdate(AbstractModel):
    """极速高清参数配置。

    """

    def __init__(self):
        r"""
        :param Type: 极速高清类型，可选值：
<li>TEHD-100：极速高清-100。</li>
不填代表不修改。
        :type Type: str
        :param MaxVideoBitrate: 视频码率上限，不填代表不修改。
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagConfigureInfo(AbstractModel):
    """智能标签任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 智能标签任务开关，可选值：
<li>ON：开启智能标签任务；</li>
<li>OFF：关闭智能标签任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagConfigureInfoForUpdate(AbstractModel):
    """智能标签任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 智能标签任务开关，可选值：
<li>ON：开启智能标签任务；</li>
<li>OFF：关闭智能标签任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskNotifyConfig(AbstractModel):
    """任务的事件通知配置。

    """

    def __init__(self):
        r"""
        :param CmqModel: CMQ或TDMQ-CMQ 的模型，有 Queue 和 Topic 两种。
        :type CmqModel: str
        :param CmqRegion: CMQ或TDMQ-CMQ 的园区，如 sh，bj 等。
        :type CmqRegion: str
        :param TopicName: 当模型为 Topic 时有效，表示接收事件通知的 CMQ 或 TDMQ-CMQ 的主题名。
        :type TopicName: str
        :param QueueName: 当模型为 Queue 时有效，表示接收事件通知的 CMQ 或 TDMQ-CMQ 的队列名。
        :type QueueName: str
        :param NotifyMode: 工作流通知的模式，可取值有 Finish 和 Change，不填代表 Finish。
        :type NotifyMode: str
        :param NotifyType: 通知类型，可选值：
<li>CMQ：已下线，建议切换到TDMQ-CMQ</li>
<li>TDMQ-CMQ：消息队列</li>
<li>URL：指定URL时HTTP回调推送到 NotifyUrl 指定的地址，回调协议http+json，包体内容同解析事件通知接口的输出参数 </li>
<li>SCF：不推荐使用，需要在控制台额外配置SCF</li>
目前 默认CMQ。
        :type NotifyType: str
        :param NotifyUrl: HTTP回调地址，NotifyType为URL时必填。
        :type NotifyUrl: str
        """
        self.CmqModel = None
        self.CmqRegion = None
        self.TopicName = None
        self.QueueName = None
        self.NotifyMode = None
        self.NotifyType = None
        self.NotifyUrl = None


    def _deserialize(self, params):
        self.CmqModel = params.get("CmqModel")
        self.CmqRegion = params.get("CmqRegion")
        self.TopicName = params.get("TopicName")
        self.QueueName = params.get("QueueName")
        self.NotifyMode = params.get("NotifyMode")
        self.NotifyType = params.get("NotifyType")
        self.NotifyUrl = params.get("NotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOutputStorage(AbstractModel):
    """媒体处理输出对象信息。

    """

    def __init__(self):
        r"""
        :param Type: 媒体处理输出对象存储位置的类型，现在仅支持 COS。
        :type Type: str
        :param CosOutputStorage: 当 Type 为 COS 时有效，则该项为必填，表示媒体处理 COS 输出位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosOutputStorage: :class:`tencentcloud.mps.v20190612.models.CosOutputStorage`
        """
        self.Type = None
        self.CosOutputStorage = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosOutputStorage") is not None:
            self.CosOutputStorage = CosOutputStorage()
            self.CosOutputStorage._deserialize(params.get("CosOutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSimpleInfo(AbstractModel):
    """任务概要信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param TaskType: 任务类型，包含：
<li> WorkflowTask：工作流处理任务；</li>
<li> EditMediaTask：视频编辑任务；</li>
<li> LiveProcessTask：直播处理任务。</li>
        :type TaskType: str
        :param CreateTime: 任务创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param BeginProcessTime: 任务开始执行时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。若任务尚未开始，该字段为：0000-00-00T00:00:00Z。
        :type BeginProcessTime: str
        :param FinishTime: 任务结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。若任务尚未完成，该字段为：0000-00-00T00:00:00Z。
        :type FinishTime: str
        :param SubTaskTypes: 子任务类型。
        :type SubTaskTypes: list of str
        """
        self.TaskId = None
        self.TaskType = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.SubTaskTypes = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        self.SubTaskTypes = params.get("SubTaskTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismConfigureInfo(AbstractModel):
    """涉敏任务控制参数

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: 画面涉敏任务控制参数。
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismImgReviewTemplateInfo`
        :param OcrReviewInfo: 文本涉敏任务控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismConfigureInfoForUpdate(AbstractModel):
    """涉敏任务控制参数。

    """

    def __init__(self):
        r"""
        :param ImgReviewInfo: 画面涉敏任务控制参数。
        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismImgReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本涉敏任务控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismImgReviewTemplateInfo(AbstractModel):
    """画面涉敏任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 画面涉敏任务开关，可选值：
<li>ON：开启画面涉敏任务；</li>
<li>OFF：关闭画面涉敏任务。</li>
        :type Switch: str
        :param LabelSet: 画面涉敏过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>guns：武器枪支；</li>
<li>crowd：人群聚集；</li>
<li>bloody：血腥画面；</li>
<li>police：警察部队；</li>
<li>banners：涉敏旗帜；</li>
<li>militant：武装分子；</li>
<li>explosion：爆炸火灾；</li>
<li>terrorists：涉敏人物；</li>
<li>scenario：涉敏画面。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 90 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 80 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismImgReviewTemplateInfoForUpdate(AbstractModel):
    """画面涉敏任务控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 画面涉敏任务开关，可选值：
<li>ON：开启画面涉敏任务；</li>
<li>OFF：关闭画面涉敏任务。</li>
        :type Switch: str
        :param LabelSet: 画面涉敏过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>guns：武器枪支；</li>
<li>crowd：人群聚集；</li>
<li>bloody：血腥画面；</li>
<li>police：警察部队；</li>
<li>banners：涉敏旗帜；</li>
<li>militant：武装分子；</li>
<li>explosion：爆炸火灾；</li>
<li>terrorists：涉敏人物；</li>
<li>scenario：涉敏画面。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismOcrReviewTemplateInfo(AbstractModel):
    """文本涉敏任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 文本涉敏任务开关，可选值：
<li>ON：开启文本涉敏任务；</li>
<li>OFF：关闭文本涉敏任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本涉敏任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 文本涉敏任务开关，可选值：
<li>ON：开启文本涉敏任务；</li>
<li>OFF：关闭文本涉敏任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWatermarkTemplateInput(AbstractModel):
    """文字水印模板

    """

    def __init__(self):
        r"""
        :param FontType: 字体类型，目前可以支持两种：
<li>simkai.ttf：可以支持中文和英文；</li>
<li>arial.ttf：仅支持英文。</li>
        :type FontType: str
        :param FontSize: 字体大小，格式：Npx，N 为数值。
        :type FontSize: str
        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（白色）。
        :type FontColor: str
        :param FontAlpha: 文字透明度，取值范围：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
默认值：1。
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWatermarkTemplateInputForUpdate(AbstractModel):
    """文字水印模板

    """

    def __init__(self):
        r"""
        :param FontType: 字体类型，目前可以支持两种：
<li>simkai.ttf：可以支持中文和英文；</li>
<li>arial.ttf：仅支持英文。</li>
        :type FontType: str
        :param FontSize: 字体大小，格式：Npx，N 为数值。
        :type FontSize: str
        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（白色）。
        :type FontColor: str
        :param FontAlpha: 文字透明度，取值范围：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskInput(AbstractModel):
    """转码任务输入参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 视频转码模板 ID。
        :type Definition: int
        :param RawParameter: 视频转码自定义参数，当 Definition 填 0 时有效。
该参数用于高度定制场景，建议您优先使用 Definition 指定转码参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RawParameter: :class:`tencentcloud.mps.v20190612.models.RawTranscodeParameter`
        :param OverrideParameter: 视频转码自定义参数，当 Definition 不填 0 时有效。
当填写了该结构中的部分转码参数时，将使用填写的参数覆盖转码模板中的参数。
该参数用于高度定制场景，建议您仅使用 Definition 指定转码参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OverrideParameter: :class:`tencentcloud.mps.v20190612.models.OverrideTranscodeParameter`
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        :param MosaicSet: 马赛克列表，最大可支持 10 张。
        :type MosaicSet: list of MosaicInput
        :param StartTimeOffset: 转码后的视频的起始时间偏移，单位：秒。
<li>不填或填0，表示转码后的视频从原始视频的起始位置开始；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频从原始视频的第 n 秒位置开始；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频从原始视频结束 n 秒前的位置开始。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 转码后视频的终止时间偏移，单位：秒。
<li>不填或填0，表示转码后的视频持续到原始视频的末尾终止；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频持续到原始视频第 n 秒时终止；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频持续到原始视频结束 n 秒前终止。</li>
        :type EndTimeOffset: float
        :param OutputStorage: 转码后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 转码后主文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_transcode_{definition}.{format}`。
        :type OutputObjectPath: str
        :param SegmentObjectName: 转码后分片文件的输出路径（转码 HLS 时 ts 的路径），只能为相对路径。如果不填，则默认为：`{inputName}_transcode_{definition}_{number}.{format}`。
        :type SegmentObjectName: str
        :param ObjectNumberFormat: 转码后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        :param HeadTailParameter: 片头片尾参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadTailParameter: :class:`tencentcloud.mps.v20190612.models.HeadTailParameter`
        """
        self.Definition = None
        self.RawParameter = None
        self.OverrideParameter = None
        self.WatermarkSet = None
        self.MosaicSet = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.SegmentObjectName = None
        self.ObjectNumberFormat = None
        self.HeadTailParameter = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("RawParameter") is not None:
            self.RawParameter = RawTranscodeParameter()
            self.RawParameter._deserialize(params.get("RawParameter"))
        if params.get("OverrideParameter") is not None:
            self.OverrideParameter = OverrideTranscodeParameter()
            self.OverrideParameter._deserialize(params.get("OverrideParameter"))
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("MosaicSet") is not None:
            self.MosaicSet = []
            for item in params.get("MosaicSet"):
                obj = MosaicInput()
                obj._deserialize(item)
                self.MosaicSet.append(obj)
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.SegmentObjectName = params.get("SegmentObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        if params.get("HeadTailParameter") is not None:
            self.HeadTailParameter = HeadTailParameter()
            self.HeadTailParameter._deserialize(params.get("HeadTailParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTemplate(AbstractModel):
    """转码模板详情

    """

    def __init__(self):
        r"""
        :param Definition: 转码模板唯一标识。
        :type Definition: str
        :param Container: 封装格式，取值：mp4、flv、hls、mp3、flac、ogg。
        :type Container: str
        :param Name: 转码模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param Type: 模板类型，取值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param RemoveVideo: 是否去除视频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数，仅当 RemoveVideo 为 0，该字段有效。
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: 音频流配置参数，仅当 RemoveAudio 为 0，该字段有效 。
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: 极速高清转码参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`
        :param ContainerType: 封装格式过滤条件，可选值：
<li>Video：视频格式，可以同时包含视频流和音频流的封装格式；</li>
<li>PureAudio：纯音频格式，只能包含音频流的封装格式板。</li>
        :type ContainerType: str
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param EnhanceConfig: 音视频增强配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnhanceConfig: :class:`tencentcloud.mps.v20190612.models.EnhanceConfig`
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.Type = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.ContainerType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.EnhanceConfig = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Type = params.get("Type")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        self.ContainerType = params.get("ContainerType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("EnhanceConfig") is not None:
            self.EnhanceConfig = EnhanceConfig()
            self.EnhanceConfig._deserialize(params.get("EnhanceConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlInputInfo(AbstractModel):
    """媒体处理 URL 对象信息。

    """

    def __init__(self):
        r"""
        :param Url: 视频的 URL。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineAsrTextReviewTemplateInfo(AbstractModel):
    """用户自定义语音审核任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 用户自定语音审核任务开关，可选值：
<li>ON：开启自定义语音审核任务；</li>
<li>OFF：关闭自定义语音审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义语音过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义语音关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineAsrTextReviewTemplateInfoForUpdate(AbstractModel):
    """用户自定义语音审核任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 用户自定语音审核任务开关，可选值：
<li>ON：开启自定义语音审核任务；</li>
<li>OFF：关闭自定义语音审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义语音过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义语音关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineConfigureInfo(AbstractModel):
    """用户自定义审核任务控制参数

    """

    def __init__(self):
        r"""
        :param FaceReviewInfo: 用户自定义人物审核控制参数。
        :type FaceReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineFaceReviewTemplateInfo`
        :param AsrReviewInfo: 用户自定义语音审核控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineAsrTextReviewTemplateInfo`
        :param OcrReviewInfo: 用户自定义文本审核控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineOcrTextReviewTemplateInfo`
        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfo()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineConfigureInfoForUpdate(AbstractModel):
    """用户自定义审核任务控制参数。

    """

    def __init__(self):
        r"""
        :param FaceReviewInfo: 用户自定义人物审核控制参数。
        :type FaceReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineFaceReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 用户自定义语音审核控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineAsrTextReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 用户自定义文本审核控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineOcrTextReviewTemplateInfoForUpdate`
        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfoForUpdate()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineFaceReviewTemplateInfo(AbstractModel):
    """用户自定义人物审核任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 用户自定义人物审核任务开关，可选值：
<li>ON：开启自定义人物审核任务；</li>
<li>OFF：关闭自定义人物审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义人物过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义人物库的时，需要添加对应人物标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 97 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 95 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineFaceReviewTemplateInfoForUpdate(AbstractModel):
    """用户自定义人物审核任务控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 用户自定义人物审核任务开关，可选值：
<li>ON：开启自定义人物审核任务；</li>
<li>OFF：关闭自定义人物审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义人物过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义人物库的时，需要添加对应人物标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineOcrTextReviewTemplateInfo(AbstractModel):
    """用户自定义文本审核任务控制参数

    """

    def __init__(self):
        r"""
        :param Switch: 用户自定文本审核任务开关，可选值：
<li>ON：开启自定义文本审核任务；</li>
<li>OFF：关闭自定义文本审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义文本过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义文本关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineOcrTextReviewTemplateInfoForUpdate(AbstractModel):
    """用户自定义文本审核任务控制参数。

    """

    def __init__(self):
        r"""
        :param Switch: 用户自定文本审核任务开关，可选值：
<li>ON：开启自定义文本审核任务；</li>
<li>OFF：关闭自定义文本审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义文本过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义文本关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoDenoiseConfig(AbstractModel):
    """视频降噪配置

    """

    def __init__(self):
        r"""
        :param Switch: 能力配置开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>
默认值：ON。
        :type Switch: str
        :param Type: 类型，可选值：
<li>weak</li>
<li>strong</li>
默认值：weak。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Switch = None
        self.Type = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEnhanceConfig(AbstractModel):
    """视频增强配置

    """

    def __init__(self):
        r"""
        :param FrameRate: 插帧帧率配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameRate: :class:`tencentcloud.mps.v20190612.models.FrameRateConfig`
        :param SuperResolution: 超分配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SuperResolution: :class:`tencentcloud.mps.v20190612.models.SuperResolutionConfig`
        :param Hdr: HDR配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Hdr: :class:`tencentcloud.mps.v20190612.models.HdrConfig`
        :param Denoise: 视频降噪配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Denoise: :class:`tencentcloud.mps.v20190612.models.VideoDenoiseConfig`
        :param ImageQualityEnhance: 综合增强配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageQualityEnhance: :class:`tencentcloud.mps.v20190612.models.ImageQualityEnhanceConfig`
        :param ColorEnhance: 色彩增强配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ColorEnhance: :class:`tencentcloud.mps.v20190612.models.ColorEnhanceConfig`
        :param SharpEnhance: 细节增强配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SharpEnhance: :class:`tencentcloud.mps.v20190612.models.SharpEnhanceConfig`
        :param FaceEnhance: 人脸增强配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceEnhance: :class:`tencentcloud.mps.v20190612.models.FaceEnhanceConfig`
        :param LowLightEnhance: 低光照增强配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LowLightEnhance: :class:`tencentcloud.mps.v20190612.models.LowLightEnhanceConfig`
        :param ScratchRepair: 去划痕配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScratchRepair: :class:`tencentcloud.mps.v20190612.models.ScratchRepairConfig`
        :param ArtifactRepair: 去伪影（毛刺）配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ArtifactRepair: :class:`tencentcloud.mps.v20190612.models.ArtifactRepairConfig`
        """
        self.FrameRate = None
        self.SuperResolution = None
        self.Hdr = None
        self.Denoise = None
        self.ImageQualityEnhance = None
        self.ColorEnhance = None
        self.SharpEnhance = None
        self.FaceEnhance = None
        self.LowLightEnhance = None
        self.ScratchRepair = None
        self.ArtifactRepair = None


    def _deserialize(self, params):
        if params.get("FrameRate") is not None:
            self.FrameRate = FrameRateConfig()
            self.FrameRate._deserialize(params.get("FrameRate"))
        if params.get("SuperResolution") is not None:
            self.SuperResolution = SuperResolutionConfig()
            self.SuperResolution._deserialize(params.get("SuperResolution"))
        if params.get("Hdr") is not None:
            self.Hdr = HdrConfig()
            self.Hdr._deserialize(params.get("Hdr"))
        if params.get("Denoise") is not None:
            self.Denoise = VideoDenoiseConfig()
            self.Denoise._deserialize(params.get("Denoise"))
        if params.get("ImageQualityEnhance") is not None:
            self.ImageQualityEnhance = ImageQualityEnhanceConfig()
            self.ImageQualityEnhance._deserialize(params.get("ImageQualityEnhance"))
        if params.get("ColorEnhance") is not None:
            self.ColorEnhance = ColorEnhanceConfig()
            self.ColorEnhance._deserialize(params.get("ColorEnhance"))
        if params.get("SharpEnhance") is not None:
            self.SharpEnhance = SharpEnhanceConfig()
            self.SharpEnhance._deserialize(params.get("SharpEnhance"))
        if params.get("FaceEnhance") is not None:
            self.FaceEnhance = FaceEnhanceConfig()
            self.FaceEnhance._deserialize(params.get("FaceEnhance"))
        if params.get("LowLightEnhance") is not None:
            self.LowLightEnhance = LowLightEnhanceConfig()
            self.LowLightEnhance._deserialize(params.get("LowLightEnhance"))
        if params.get("ScratchRepair") is not None:
            self.ScratchRepair = ScratchRepairConfig()
            self.ScratchRepair._deserialize(params.get("ScratchRepair"))
        if params.get("ArtifactRepair") is not None:
            self.ArtifactRepair = ArtifactRepairConfig()
            self.ArtifactRepair._deserialize(params.get("ArtifactRepair"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfo(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        r"""
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
<li>av1：AOMedia Video 1 编码</li>
注意：目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。
注意：av1 编码容器目前只支持 mp4 。
        :type Codec: str
        :param Fps: 视频帧率，取值范围：[0, 100]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。
注意：自适应码率时取值范围是 [0, 60]
        :type Fps: int
        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
注意：自适应模式时，Width不能小于Height。
        :type ResolutionAdaptive: str
        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param Gop: 关键帧 I 帧之间的间隔，取值范围：0 和 [1, 100000]，单位：帧数。
当填 0 或不填时，系统将自动设置 gop 长度。
        :type Gop: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊填充。</li>
默认值：black 。
注意：自适应码流只支持 stretch、black。
        :type FillType: str
        :param Vcrf: 视频恒定码率控制因子，取值范围为[1, 51]。
如果指定该参数，将使用 CRF 的码率控制方式做转码（视频码率将不再生效）。
如果没有特殊需求，不建议指定该参数。
        :type Vcrf: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.Gop = None
        self.FillType = None
        self.Vcrf = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Gop = params.get("Gop")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfoForUpdate(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        r"""
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
<li>av1：AOMedia Video 1 编码</li>
注意：目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。
注意：av1 编码容器目前只支持 mp4 。
        :type Codec: str
        :param Fps: 视频帧率，取值范围：[0, 100]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。
        :type Fps: int
        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
注意：自适应模式时，Width不能小于Height。
        :type ResolutionAdaptive: str
        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
        :type Height: int
        :param Gop: 关键帧 I 帧之间的间隔，取值范围：0 和 [1, 100000]，单位：帧数。当填 0 时，系统将自动设置 gop 长度。
        :type Gop: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊填充。</li>
        :type FillType: str
        :param Vcrf: 视频恒定码率控制因子。取值范围为[0, 51]，填0表示禁用该参数。
如果没有特殊需求，不建议指定该参数。
        :type Vcrf: int
        :param ContentAdaptStream: 内容自适应编码。可选值：
<li>0：不开启</li>
<li>1：开启</li>
默认值: 0.   当开启该参数时，将会自适应生成多个不同分辨率，不同码率的码流， 其中VideoTemplate的宽和高为多个码流中的最大分辨率，VideoTemplate中的码率为多个码流中的最高码率， VideoTemplate中的vcrf为多个码流中的最高质量。 当不设置分辨率、码率和vcrf时， ContentAdaptStream 参数生成的最高分辨率为视频源的分辨率，视频质量为接近vmaf95分。 若要开启该参数或了解计费细节, 请联系您的腾讯云商务。
        :type ContentAdaptStream: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.Gop = None
        self.FillType = None
        self.Vcrf = None
        self.ContentAdaptStream = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Gop = params.get("Gop")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        self.ContentAdaptStream = params.get("ContentAdaptStream")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkInput(AbstractModel):
    """媒体处理任务中的水印参数类型

    """

    def __init__(self):
        r"""
        :param Definition: 水印模板 ID。
        :type Definition: int
        :param RawParameter: 水印自定义参数，当 Definition 填 0 时有效。
该参数用于高度定制场景，建议您优先使用 Definition 指定水印参数。
水印自定义参数不支持截图打水印。
        :type RawParameter: :class:`tencentcloud.mps.v20190612.models.RawWatermarkParameter`
        :param TextContent: 文字内容，长度不超过100个字符。仅当水印类型为文字水印时填写。
文字水印不支持截图打水印。
        :type TextContent: str
        :param SvgContent: SVG 内容。长度不超过 2000000 个字符。仅当水印类型为 SVG 水印时填写。
SVG 水印不支持截图打水印。
        :type SvgContent: str
        :param StartTimeOffset: 水印的起始时间偏移，单位：秒。不填或填0，表示水印从画面出现时开始显现。
<li>不填或填0，表示水印从画面开始就出现；</li>
<li>当数值大于0时（假设为 n），表示水印从画面开始的第 n 秒出现；</li>
<li>当数值小于0时（假设为 -n），表示水印从离画面结束 n 秒前开始出现。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 水印的结束时间偏移，单位：秒。
<li>不填或填0，表示水印持续到画面结束；</li>
<li>当数值大于0时（假设为 n），表示水印持续到第 n 秒时消失；</li>
<li>当数值小于0时（假设为 -n），表示水印持续到离画面结束 n 秒前消失。</li>
        :type EndTimeOffset: float
        """
        self.Definition = None
        self.RawParameter = None
        self.TextContent = None
        self.SvgContent = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("RawParameter") is not None:
            self.RawParameter = RawWatermarkParameter()
            self.RawParameter._deserialize(params.get("RawParameter"))
        self.TextContent = params.get("TextContent")
        self.SvgContent = params.get("SvgContent")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkTemplate(AbstractModel):
    """水印模板详情

    """

    def __init__(self):
        r"""
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param Type: 水印类型，取值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>
        :type Type: str
        :param Name: 水印模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param XPos: 水印图片原点距离视频图像原点的水平位置。
<li>当字符串以 % 结尾，表示水印 Left 为视频宽度指定百分比的位置，如 10% 表示 Left 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Left 为视频宽度指定像素的位置，如 100px 表示 Left 为 100 像素。</li>
        :type XPos: str
        :param YPos: 水印图片原点距离视频图像原点的垂直位置。
<li>当字符串以 % 结尾，表示水印 Top 为视频高度指定百分比的位置，如 10% 表示 Top 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Top 为视频高度指定像素的位置，如 100px 表示 Top 为 100 像素。</li>
        :type YPos: str
        :param ImageTemplate: 图片水印模板，仅当 Type 为 image，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkTemplate`
        :param TextTemplate: 文字水印模板，仅当 Type 为 text，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG 水印模板，当 Type 为 svg，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInput`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param CoordinateOrigin: 原点位置，可选值：
<li>topLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>topRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>bottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>bottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下。；</li>
        :type CoordinateOrigin: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CoordinateOrigin = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkTemplate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowInfo(AbstractModel):
    """工作流信息详情。

    """

    def __init__(self):
        r"""
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        :param WorkflowName: 工作流名称。
        :type WorkflowName: str
        :param Status: 工作流状态，取值范围：
<li>Enabled：已启用，</li>
<li>Disabled：已禁用。</li>
        :type Status: str
        :param Trigger: 工作流绑定的输入规则，当上传视频命中该规则到该对象时即触发工作流。
        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: 媒体处理的文件输出存储位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param MediaProcessTask: 媒体处理类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 视频内容审核类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 视频内容分析类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 视频内容识别类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TaskPriority: 任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TaskPriority: int
        :param OutputDir: 媒体处理生成的文件输出的目标目录，如`/movie/201907/`。
        :type OutputDir: str
        :param CreateTime: 工作流创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 工作流最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Status = None
        self.Trigger = None
        self.OutputStorage = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None
        self.OutputDir = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        self.Status = params.get("Status")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")
        self.OutputDir = params.get("OutputDir")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTask(AbstractModel):
    """媒体处理任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 媒体处理任务 ID。
        :type TaskId: str
        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 源异常时返回非0错误码，返回0 时请使用各个具体任务的 ErrCode。
        :type ErrCode: int
        :param Message: 源异常时返回对应异常Message，否则请使用各个具体任务的 Message。
        :type Message: str
        :param InputInfo: 媒体处理的目标文件信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param MetaData: 原始视频的元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.mps.v20190612.models.MediaMetaData`
        :param MediaProcessResultSet: 媒体处理任务的执行状态与结果。
        :type MediaProcessResultSet: list of MediaProcessTaskResult
        :param AiContentReviewResultSet: 视频内容审核任务的执行状态与结果。
        :type AiContentReviewResultSet: list of AiContentReviewResult
        :param AiAnalysisResultSet: 视频内容分析任务的执行状态与结果。
        :type AiAnalysisResultSet: list of AiAnalysisResult
        :param AiRecognitionResultSet: 视频内容识别任务的执行状态与结果。
        :type AiRecognitionResultSet: list of AiRecognitionResult
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.InputInfo = None
        self.MetaData = None
        self.MediaProcessResultSet = None
        self.AiContentReviewResultSet = None
        self.AiAnalysisResultSet = None
        self.AiRecognitionResultSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("MediaProcessResultSet") is not None:
            self.MediaProcessResultSet = []
            for item in params.get("MediaProcessResultSet"):
                obj = MediaProcessTaskResult()
                obj._deserialize(item)
                self.MediaProcessResultSet.append(obj)
        if params.get("AiContentReviewResultSet") is not None:
            self.AiContentReviewResultSet = []
            for item in params.get("AiContentReviewResultSet"):
                obj = AiContentReviewResult()
                obj._deserialize(item)
                self.AiContentReviewResultSet.append(obj)
        if params.get("AiAnalysisResultSet") is not None:
            self.AiAnalysisResultSet = []
            for item in params.get("AiAnalysisResultSet"):
                obj = AiAnalysisResult()
                obj._deserialize(item)
                self.AiAnalysisResultSet.append(obj)
        if params.get("AiRecognitionResultSet") is not None:
            self.AiRecognitionResultSet = []
            for item in params.get("AiRecognitionResultSet"):
                obj = AiRecognitionResult()
                obj._deserialize(item)
                self.AiRecognitionResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTrigger(AbstractModel):
    """输入规则，当上传视频命中该规则时，即触发工作流。

    """

    def __init__(self):
        r"""
        :param Type: 触发器的类型，目前仅支持 CosFileUpload。
        :type Type: str
        :param CosFileUploadTrigger: 当 Type 为 CosFileUpload 时必填且有效，为 COS 触发规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosFileUploadTrigger: :class:`tencentcloud.mps.v20190612.models.CosFileUploadTrigger`
        """
        self.Type = None
        self.CosFileUploadTrigger = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosFileUploadTrigger") is not None:
            self.CosFileUploadTrigger = CosFileUploadTrigger()
            self.CosFileUploadTrigger._deserialize(params.get("CosFileUploadTrigger"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        