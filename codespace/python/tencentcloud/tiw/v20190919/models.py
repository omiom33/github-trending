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


class AuthParam(AbstractModel):
    """鉴权参数

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param UserId: 用户ID
        :type UserId: str
        :param UserSig: 用户ID对应的签名
        :type UserSig: str
        """
        self.SdkAppId = None
        self.UserId = None
        self.UserSig = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        self.UserSig = params.get("UserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Canvas(AbstractModel):
    """混流画布参数

    """

    def __init__(self):
        r"""
        :param LayoutParams: 混流画布宽高配置
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param BackgroundColor: 背景颜色，默认为黑色，格式为RGB格式，如红色为"#FF0000"
        :type BackgroundColor: str
        """
        self.LayoutParams = None
        self.BackgroundColor = None


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        self.BackgroundColor = params.get("BackgroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Concat(AbstractModel):
    """实时录制视频拼接参数

    """

    def __init__(self):
        r"""
        :param Enabled: 是否开启拼接功能
在开启了视频拼接功能的情况下，实时录制服务会把同一个用户因为暂停导致的多段视频拼接成一个视频
        :type Enabled: bool
        :param Image: 视频拼接时使用的垫片图片下载地址，不填默认用全黑的图片进行视频垫片
        :type Image: str
        """
        self.Enabled = None
        self.Image = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotTaskRequest(AbstractModel):
    """CreateSnapshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Whiteboard: 白板相关参数
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.SnapshotWhiteboard`
        :param SdkAppId: 白板房间 `SdkAppId`
        :type SdkAppId: int
        :param RoomId: 白板房间号
        :type RoomId: int
        :param CallbackURL: 白板板书生成结果通知回调地址
        :type CallbackURL: str
        :param COS: 白板板书文件 `COS` 存储参数， 不填默认存储在公共存储桶，公共存储桶的数据仅保存3天
        :type COS: :class:`tencentcloud.tiw.v20190919.models.SnapshotCOS`
        :param SnapshotMode: 白板板书生成模式，默认为 `AllMarks`。取值说明如下：

`AllMarks` - 全量模式，即对于客户端每一次调用 `addSnapshotMark` 接口打上的白板板书生成标志全部都会生成对应的白板板书图片。

`LatestMarksOnly` - 单页去重模式，即对于客户端在同一页白板上多次调用 `addSnapshotMark` 打上的白板板书生成标志仅保留最新一次标志来生成对应白板页的白板板书图片。

（**注意：`LatestMarksOnly` 模式只有客户端使用v2.6.8及以上版本的白板SDK调用 `addSnapshotMark` 时才生效，否则即使在调用本API是指定了 `LatestMarksOnly` 模式，服务后台会使用默认的 `AllMarks` 模式生成白板板书**）
        :type SnapshotMode: str
        """
        self.Whiteboard = None
        self.SdkAppId = None
        self.RoomId = None
        self.CallbackURL = None
        self.COS = None
        self.SnapshotMode = None


    def _deserialize(self, params):
        if params.get("Whiteboard") is not None:
            self.Whiteboard = SnapshotWhiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.CallbackURL = params.get("CallbackURL")
        if params.get("COS") is not None:
            self.COS = SnapshotCOS()
            self.COS._deserialize(params.get("COS"))
        self.SnapshotMode = params.get("SnapshotMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotTaskResponse(AbstractModel):
    """CreateSnapshotTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 白板板书生成任务ID，只有任务创建成功的时候才会返回此字段
        :type TaskID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class CreateTranscodeRequest(AbstractModel):
    """CreateTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Url: 经过URL编码后的转码文件地址。URL 编码会将字符转换为可通过因特网传输的格式，比如文档地址为http://example.com/测试.pdf，经过URL编码之后为http://example.com/%E6%B5%8B%E8%AF%95.pdf。为了提高URL解析的成功率，请对URL进行编码。
        :type Url: str
        :param IsStaticPPT: 是否为静态PPT，默认为False；
如果IsStaticPPT为False，后缀名为.ppt或.pptx的文档会动态转码成HTML5页面，其他格式的文档会静态转码成图片；如果IsStaticPPT为True，所有格式的文档会静态转码成图片；
        :type IsStaticPPT: bool
        :param MinResolution: 注意: 该参数已废弃, 请使用最新的 [云API SDK](https://cloud.tencent.com/document/api/1137/40060#SDK) ，使用 MinScaleResolution字段传递分辨率

转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率

示例：1280x720，注意分辨率宽高中间为英文字母"xyz"的"x"
        :type MinResolution: str
        :param ThumbnailResolution: 动态PPT转码可以为文件生成该分辨率的缩略图，不传、传空字符串或分辨率格式错误则不生成缩略图，分辨率格式同MinResolution
        :type ThumbnailResolution: str
        :param CompressFileType: 转码文件压缩格式，不传、传空字符串或不是指定的格式则不生成压缩文件，目前支持如下压缩格式：

zip： 生成`.zip`压缩包
tar.gz： 生成`.tar.gz`压缩包
        :type CompressFileType: str
        :param ExtraData: 内部参数
        :type ExtraData: str
        :param Priority: 文档转码优先级， 只有对于PPT动态转码生效，支持填入以下值：<br/>
- low: 低优先级转码，对于动态转码，能支持500MB（下载超时时间10分钟）以及2000页文档，但资源有限可能会有比较长时间的排队，请酌情使用该功能。<br/>
- 不填表示正常优先级转码，支持200MB文件（下载超时时间2分钟），500页以内的文档进行转码
<br/>
注意：对于PDF等静态文件转码，无论是正常优先级或者低优先级，最大只能支持200MB
        :type Priority: str
        :param MinScaleResolution: 转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率。
分辨率越高，效果越清晰，转出来的图片资源体积会越大，课件加载耗时会变长，请根据实际使用场景配置此参数。

示例：1280x720，注意分辨率宽高中间为英文字母"xyz"的"x"
        :type MinScaleResolution: str
        """
        self.SdkAppId = None
        self.Url = None
        self.IsStaticPPT = None
        self.MinResolution = None
        self.ThumbnailResolution = None
        self.CompressFileType = None
        self.ExtraData = None
        self.Priority = None
        self.MinScaleResolution = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Url = params.get("Url")
        self.IsStaticPPT = params.get("IsStaticPPT")
        self.MinResolution = params.get("MinResolution")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileType = params.get("CompressFileType")
        self.ExtraData = params.get("ExtraData")
        self.Priority = params.get("Priority")
        self.MinScaleResolution = params.get("MinScaleResolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeResponse(AbstractModel):
    """CreateTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 文档转码任务的唯一标识Id，用于查询该任务的进度以及转码结果
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateVideoGenerationTaskRequest(AbstractModel):
    """CreateVideoGenerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param OnlineRecordTaskId: 录制任务的TaskId
        :type OnlineRecordTaskId: str
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Whiteboard: 视频生成的白板参数，例如白板宽高等。

此参数与开始录制接口提供的Whiteboard参数互斥，在本接口与开始录制接口都提供了Whiteboard参数时，优先使用本接口指定的Whiteboard参数进行视频生成，否则使用开始录制接口提供的Whiteboard参数进行视频生成。
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param Concat: 视频拼接参数

此参数与开始录制接口提供的Concat参数互斥，在本接口与开始录制接口都提供了Concat参数时，优先使用本接口指定的Concat参数进行视频拼接，否则使用开始录制接口提供的Concat参数进行视频拼接。
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param MixStream: 视频生成混流参数

此参数与开始录制接口提供的MixStream参数互斥，在本接口与开始录制接口都提供了MixStream参数时，优先使用本接口指定的MixStream参数进行视频混流，否则使用开始录制接口提供的MixStream参数进行视频拼混流。
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param RecordControl: 视频生成控制参数，用于更精细地指定需要生成哪些流，某一路流是否禁用音频，是否只录制小画面等

此参数与开始录制接口提供的RecordControl参数互斥，在本接口与开始录制接口都提供了RecordControl参数时，优先使用本接口指定的RecordControl参数进行视频生成控制，否则使用开始录制接口提供的RecordControl参数进行视频拼生成控制。
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        :param ExtraData: 内部参数
        :type ExtraData: str
        """
        self.OnlineRecordTaskId = None
        self.SdkAppId = None
        self.Whiteboard = None
        self.Concat = None
        self.MixStream = None
        self.RecordControl = None
        self.ExtraData = None


    def _deserialize(self, params):
        self.OnlineRecordTaskId = params.get("OnlineRecordTaskId")
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("Concat") is not None:
            self.Concat = Concat()
            self.Concat._deserialize(params.get("Concat"))
        if params.get("MixStream") is not None:
            self.MixStream = MixStream()
            self.MixStream._deserialize(params.get("MixStream"))
        if params.get("RecordControl") is not None:
            self.RecordControl = RecordControl()
            self.RecordControl._deserialize(params.get("RecordControl"))
        self.ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoGenerationTaskResponse(AbstractModel):
    """CreateVideoGenerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 视频生成的任务Id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CustomLayout(AbstractModel):
    """自定义混流布局参数

    """

    def __init__(self):
        r"""
        :param Canvas: 混流画布参数
        :type Canvas: :class:`tencentcloud.tiw.v20190919.models.Canvas`
        :param InputStreamList: 流布局参数，每路流的布局不能超出画布区域
        :type InputStreamList: list of StreamLayout
        """
        self.Canvas = None
        self.InputStreamList = None


    def _deserialize(self, params):
        if params.get("Canvas") is not None:
            self.Canvas = Canvas()
            self.Canvas._deserialize(params.get("Canvas"))
        if params.get("InputStreamList") is not None:
            self.InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = StreamLayout()
                obj._deserialize(item)
                self.InputStreamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordCallbackRequest(AbstractModel):
    """DescribeOnlineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordCallbackResponse(AbstractModel):
    """DescribeOnlineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 实时录制事件回调地址，如果未设置回调地址，该字段为空字符串
        :type Callback: str
        :param CallbackKey: 实时录制回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeOnlineRecordRequest(AbstractModel):
    """DescribeOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 实时录制任务Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordResponse(AbstractModel):
    """DescribeOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param FinishReason: 录制结束原因，
- AUTO: 房间内长时间没有音视频上行及白板操作导致自动停止录制
- USER_CALL: 主动调用了停止录制接口
- EXCEPTION: 录制异常结束
- FORCE_STOP: 强制停止录制，一般是因为暂停超过90分钟或者录制总时长超过24小时。
        :type FinishReason: str
        :param TaskId: 需要查询结果的录制任务Id
        :type TaskId: str
        :param Status: 录制任务状态
- PREPARED: 表示录制正在准备中（进房/启动录制服务等操作）
- RECORDING: 表示录制已开始
- PAUSED: 表示录制已暂停
- STOPPED: 表示录制已停止，正在处理并上传视频
- FINISHED: 表示视频处理并上传完成，成功生成录制结果
        :type Status: str
        :param RoomId: 房间号
        :type RoomId: int
        :param GroupId: 白板的群组 Id
        :type GroupId: str
        :param RecordUserId: 录制用户Id
        :type RecordUserId: str
        :param RecordStartTime: 实际开始录制时间，Unix 时间戳，单位秒
        :type RecordStartTime: int
        :param RecordStopTime: 实际停止录制时间，Unix 时间戳，单位秒
        :type RecordStopTime: int
        :param TotalTime: 回放视频总时长（单位：毫秒）
        :type TotalTime: int
        :param ExceptionCnt: 录制过程中出现异常的次数
        :type ExceptionCnt: int
        :param OmittedDurations: 拼接视频中被忽略的时间段，只有开启视频拼接功能的时候，这个参数才是有效的
        :type OmittedDurations: list of OmittedDuration
        :param VideoInfos: 录制视频列表
        :type VideoInfos: list of VideoInfo
        :param ReplayUrl: 回放URL，需配合信令播放器使用。此字段仅适用于`视频生成模式`
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplayUrl: str
        :param Interrupts: 视频流在录制过程中断流次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Interrupts: list of Interrupt
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FinishReason = None
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.GroupId = None
        self.RecordUserId = None
        self.RecordStartTime = None
        self.RecordStopTime = None
        self.TotalTime = None
        self.ExceptionCnt = None
        self.OmittedDurations = None
        self.VideoInfos = None
        self.ReplayUrl = None
        self.Interrupts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.RecordUserId = params.get("RecordUserId")
        self.RecordStartTime = params.get("RecordStartTime")
        self.RecordStopTime = params.get("RecordStopTime")
        self.TotalTime = params.get("TotalTime")
        self.ExceptionCnt = params.get("ExceptionCnt")
        if params.get("OmittedDurations") is not None:
            self.OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self.OmittedDurations.append(obj)
        if params.get("VideoInfos") is not None:
            self.VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self.VideoInfos.append(obj)
        self.ReplayUrl = params.get("ReplayUrl")
        if params.get("Interrupts") is not None:
            self.Interrupts = []
            for item in params.get("Interrupts"):
                obj = Interrupt()
                obj._deserialize(item)
                self.Interrupts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQualityMetricsRequest(AbstractModel):
    """DescribeQualityMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param StartTime: 开始时间，Unix时间戳，单位秒，时间跨度不能超过7天
        :type StartTime: int
        :param EndTime: 结束时间，Unix时间戳，单位秒，时间跨度不能超过7天
        :type EndTime: int
        :param Metric: 查询的指标，目前支持以下值
  - image_load_total_count: 图片加载总数（单位，次）
  - image_load_fail_count: 图片加载失败数量（单位，次）
  - image_load_success_rate: 图片加载成功率（百分比）
  - ppt_load_total_count: PPT加载总数（单位，次）
  - ppt_load_fail_count: PPT加载失败总数（单位，次）
  - ppt_load_success_rate: PPT加载成功率（单位，百分比）
  - verify_sdk_total_count: 白板鉴权总次数（单位，次）
  - verify_sdk_fail_count: 白板鉴权失败次数（单位，次）
  - verify_sdk_success_rate: 白板鉴权成功率（单位，百分比）
  - verify_sdk_in_one_second_rate: 白板鉴权秒开率（单位，百分比）
  - verify_sdk_cost_avg: 白板鉴权耗时平均时间（单位，毫秒）
        :type Metric: str
        :param Interval: 聚合的时间维度，目前只支持1小时，输入值为"1h"
        :type Interval: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Interval = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQualityMetricsResponse(AbstractModel):
    """DescribeQualityMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Metric: 输入的查询指标
        :type Metric: str
        :param Content: 时间序列
        :type Content: list of TimeValue
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Metric = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotTaskRequest(AbstractModel):
    """DescribeSnapshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 查询任务ID
        :type TaskID: str
        :param SdkAppId: 任务SdkAppId
        :type SdkAppId: int
        """
        self.TaskID = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotTaskResponse(AbstractModel):
    """DescribeSnapshotTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskID: str
        :param Status: 任务状态
Running - 任务执行中
Finished - 任务已结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param CreateTime: 任务创建时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param FinishTime: 任务完成时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: int
        :param Result: 任务结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tiw.v20190919.models.SnapshotResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskID = None
        self.Status = None
        self.CreateTime = None
        self.FinishTime = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("Result") is not None:
            self.Result = SnapshotResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTIWDailyUsageRequest(AbstractModel):
    """DescribeTIWDailyUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 互动白板应用SdkAppId
        :type SdkAppId: int
        :param SubProduct: 需要查询的子产品用量，支持传入以下值
- sp_tiw_board: 互动白板时长，单位为分钟
- sp_tiw_dt: 动态转码页数，单位页
- sp_tiw_st: 静态转码页数，单位页
- sp_tiw_ric: 实时录制时长，单位分钟

注意：动态转码以1:8的比例计算文档转码页数，静态转码以1:1的比例计算文档转码页数
        :type SubProduct: str
        :param StartTime: 开始时间，格式YYYY-MM-DD，查询结果里包括该天数据
        :type StartTime: str
        :param EndTime: 结束时间，格式YYYY-MM-DD，查询结果里包括该天数据，单次查询统计区间最多不能超过31天。
        :type EndTime: str
        """
        self.SdkAppId = None
        self.SubProduct = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTIWDailyUsageResponse(AbstractModel):
    """DescribeTIWDailyUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Usages: 指定区间指定产品的用量汇总
        :type Usages: list of UsageDataItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Usages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = UsageDataItem()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTranscodeCallbackRequest(AbstractModel):
    """DescribeTranscodeCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeCallbackResponse(AbstractModel):
    """DescribeTranscodeCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 文档转码回调地址
        :type Callback: str
        :param CallbackKey: 文档转码回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeRequest(AbstractModel):
    """DescribeTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 文档转码任务的唯一标识Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeResponse(AbstractModel):
    """DescribeTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param Pages: 文档的总页数
        :type Pages: int
        :param Progress: 转码的当前进度,取值范围为0~100
        :type Progress: int
        :param Resolution: 文档的分辨率
        :type Resolution: str
        :param ResultUrl: 转码完成后结果的URL
动态转码：PPT转动态H5的链接
静态转码：文档每一页的图片URL前缀，比如，该URL前缀为`http://example.com/g0jb42ps49vtebjshilb/`，那么文档第1页的图片URL为
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`，其它页以此类推
        :type ResultUrl: str
        :param Status: 任务的当前状态
- QUEUED: 正在排队等待转换
- PROCESSING: 转换中
- FINISHED: 转换完成
        :type Status: str
        :param TaskId: 转码任务的唯一标识Id
        :type TaskId: str
        :param Title: 文档的文件名
        :type Title: str
        :param ThumbnailUrl: 缩略图URL前缀，比如，该URL前缀为`http://example.com/g0jb42ps49vtebjshilb/ `，那么动态PPT第1页的缩略图URL为
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`，其它页以此类推

如果发起文档转码请求参数中带了ThumbnailResolution参数，并且转码类型为动态转码，该参数不为空，其余情况该参数为空字符串
        :type ThumbnailUrl: str
        :param ThumbnailResolution: 动态转码缩略图生成分辨率
        :type ThumbnailResolution: str
        :param CompressFileUrl: 转码压缩文件下载的URL，如果发起文档转码请求参数中`CompressFileType`为空或者不是支持的压缩格式，该参数为空字符串
        :type CompressFileUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Pages = None
        self.Progress = None
        self.Resolution = None
        self.ResultUrl = None
        self.Status = None
        self.TaskId = None
        self.Title = None
        self.ThumbnailUrl = None
        self.ThumbnailResolution = None
        self.CompressFileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Pages = params.get("Pages")
        self.Progress = params.get("Progress")
        self.Resolution = params.get("Resolution")
        self.ResultUrl = params.get("ResultUrl")
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        self.Title = params.get("Title")
        self.ThumbnailUrl = params.get("ThumbnailUrl")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileUrl = params.get("CompressFileUrl")
        self.RequestId = params.get("RequestId")


class DescribeVideoGenerationTaskCallbackRequest(AbstractModel):
    """DescribeVideoGenerationTaskCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoGenerationTaskCallbackResponse(AbstractModel):
    """DescribeVideoGenerationTaskCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 录制视频生成回调地址
        :type Callback: str
        :param CallbackKey: 录制视频生成回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeVideoGenerationTaskRequest(AbstractModel):
    """DescribeVideoGenerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 录制视频生成的任务Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoGenerationTaskResponse(AbstractModel):
    """DescribeVideoGenerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 任务对应的群组Id
        :type GroupId: str
        :param RoomId: 任务对应的房间号
        :type RoomId: int
        :param TaskId: 任务的Id
        :type TaskId: str
        :param Progress: 已废弃
        :type Progress: int
        :param Status: 录制视频生成任务状态
- QUEUED: 正在排队
- PROCESSING: 正在生成视频
- FINISHED: 生成视频结束（成功完成或失败结束，可以通过错误码和错误信息进一步判断）
        :type Status: str
        :param TotalTime: 回放视频总时长,单位：毫秒
        :type TotalTime: int
        :param VideoInfos: 已废弃，请使用`VideoInfoList`参数
        :type VideoInfos: :class:`tencentcloud.tiw.v20190919.models.VideoInfo`
        :param VideoInfoList: 录制视频生成视频列表
        :type VideoInfoList: list of VideoInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RoomId = None
        self.TaskId = None
        self.Progress = None
        self.Status = None
        self.TotalTime = None
        self.VideoInfos = None
        self.VideoInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RoomId = params.get("RoomId")
        self.TaskId = params.get("TaskId")
        self.Progress = params.get("Progress")
        self.Status = params.get("Status")
        self.TotalTime = params.get("TotalTime")
        if params.get("VideoInfos") is not None:
            self.VideoInfos = VideoInfo()
            self.VideoInfos._deserialize(params.get("VideoInfos"))
        if params.get("VideoInfoList") is not None:
            self.VideoInfoList = []
            for item in params.get("VideoInfoList"):
                obj = VideoInfo()
                obj._deserialize(item)
                self.VideoInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardPushCallbackRequest(AbstractModel):
    """DescribeWhiteboardPushCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardPushCallbackResponse(AbstractModel):
    """DescribeWhiteboardPushCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 白板推流事件回调地址，如果未设置回调地址，该字段为空字符串
        :type Callback: str
        :param CallbackKey: 白板推流回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardPushRequest(AbstractModel):
    """DescribeWhiteboardPush请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 白板推流任务Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardPushResponse(AbstractModel):
    """DescribeWhiteboardPush返回参数结构体

    """

    def __init__(self):
        r"""
        :param FinishReason: 推流结束原因，
- AUTO: 房间内长时间没有音视频上行及白板操作导致自动停止推流
- USER_CALL: 主动调用了停止推流接口
- EXCEPTION: 推流异常结束
        :type FinishReason: str
        :param TaskId: 需要查询结果的白板推流任务Id
        :type TaskId: str
        :param Status: 推流任务状态
- PREPARED: 表示推流正在准备中（进房/启动推流服务等操作）
- PUSHING: 表示推流已开始
- STOPPED: 表示推流已停止
        :type Status: str
        :param RoomId: 房间号
        :type RoomId: int
        :param GroupId: 白板的群组 Id
        :type GroupId: str
        :param PushUserId: 推流用户Id
        :type PushUserId: str
        :param PushStartTime: 实际开始推流时间，Unix 时间戳，单位秒
        :type PushStartTime: int
        :param PushStopTime: 实际停止推流时间，Unix 时间戳，单位秒
        :type PushStopTime: int
        :param ExceptionCnt: 推流过程中出现异常的次数
        :type ExceptionCnt: int
        :param IMSyncTime: 白板推流首帧对应的IM时间戳，可用于录制回放时IM聊天消息与白板推流视频进行同步对时。
        :type IMSyncTime: int
        :param Backup: 备份推流任务结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FinishReason = None
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.GroupId = None
        self.PushUserId = None
        self.PushStartTime = None
        self.PushStopTime = None
        self.ExceptionCnt = None
        self.IMSyncTime = None
        self.Backup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.PushUserId = params.get("PushUserId")
        self.PushStartTime = params.get("PushStartTime")
        self.PushStopTime = params.get("PushStopTime")
        self.ExceptionCnt = params.get("ExceptionCnt")
        self.IMSyncTime = params.get("IMSyncTime")
        self.Backup = params.get("Backup")
        self.RequestId = params.get("RequestId")


class Interrupt(AbstractModel):
    """实时录制中出现的用户视频流断流次数统计

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param Count: 视频流断流次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.UserId = None
        self.Count = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayoutParams(AbstractModel):
    """自定义混流配置布局参数

    """

    def __init__(self):
        r"""
        :param Width: 流画面宽，取值范围[2,3000]
        :type Width: int
        :param Height: 流画面高，取值范围[2,3000]
        :type Height: int
        :param X: 当前画面左上角顶点相对于Canvas左上角顶点的x轴偏移量，默认为0，取值范围[0,3000]
        :type X: int
        :param Y: 当前画面左上角顶点相对于Canvas左上角顶点的y轴偏移量，默认为0， 取值范围[0,3000]
        :type Y: int
        :param ZOrder: 画面z轴位置，默认为0
z轴确定了重叠画面的遮盖顺序，z轴值大的画面处于顶层
        :type ZOrder: int
        """
        self.Width = None
        self.Height = None
        self.X = None
        self.Y = None
        self.ZOrder = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.ZOrder = params.get("ZOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixStream(AbstractModel):
    """混流配置

    """

    def __init__(self):
        r"""
        :param Enabled: 是否开启混流
        :type Enabled: bool
        :param DisableAudio: 是否禁用音频混流
        :type DisableAudio: bool
        :param ModelId: 内置混流布局模板ID, 取值 [1, 2], 区别见内置混流布局模板样式示例说明
在没有填Custom字段时候，ModelId是必填的
        :type ModelId: int
        :param TeacherId: 老师用户ID
此字段只有在ModelId填了的情况下生效
填写TeacherId的效果是把指定为TeacherId的用户视频流显示在内置模板的第一个小画面中
        :type TeacherId: str
        :param Custom: 自定义混流布局参数
当此字段存在时，ModelId 及 TeacherId 字段将被忽略
        :type Custom: :class:`tencentcloud.tiw.v20190919.models.CustomLayout`
        """
        self.Enabled = None
        self.DisableAudio = None
        self.ModelId = None
        self.TeacherId = None
        self.Custom = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.DisableAudio = params.get("DisableAudio")
        self.ModelId = params.get("ModelId")
        self.TeacherId = params.get("TeacherId")
        if params.get("Custom") is not None:
            self.Custom = CustomLayout()
            self.Custom._deserialize(params.get("Custom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OmittedDuration(AbstractModel):
    """拼接视频中被忽略的时间段

    """

    def __init__(self):
        r"""
        :param VideoTime: 录制暂停时间戳对应的视频播放时间(单位: 毫秒)
        :type VideoTime: int
        :param PauseTime: 录制暂停时间戳(单位: 毫秒)
        :type PauseTime: int
        :param ResumeTime: 录制恢复时间戳(单位: 毫秒)
        :type ResumeTime: int
        """
        self.VideoTime = None
        self.PauseTime = None
        self.ResumeTime = None


    def _deserialize(self, params):
        self.VideoTime = params.get("VideoTime")
        self.PauseTime = params.get("PauseTime")
        self.ResumeTime = params.get("ResumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordRequest(AbstractModel):
    """PauseOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 实时录制任务 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordResponse(AbstractModel):
    """PauseOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RecordControl(AbstractModel):
    """录制控制参数， 用于指定全局录制控制及具体流录制控制参数，比如设置需要对哪些流进行录制，是否只录制小画面等

    """

    def __init__(self):
        r"""
        :param Enabled: 设置是否开启录制控制参数，只有设置为true的时候，录制控制参数才生效。
        :type Enabled: bool
        :param DisableRecord: 设置是否禁用录制的全局控制参数。一般与`StreamControls`参数配合使用。

true - 所有流都不录制。
false - 所有流都录制。默认为false。

这里的设置对所有流都生效，如果同时在 `StreamControls` 列表中针对指定流设置了控制参数，则优先采用`StreamControls`中设置的控制参数。
        :type DisableRecord: bool
        :param DisableAudio: 设置是否禁用所有流的音频录制的全局控制参数。一般与`StreamControls`参数配合使用。

true - 所有流的录制都不对音频进行录制。
false - 所有流的录制都需要对音频进行录制。默认为false。

这里的设置对所有流都生效，如果同时在 `StreamControls` 列表中针对指定流设置了控制参数，则优先采用`StreamControls`中设置的控制参数。
        :type DisableAudio: bool
        :param PullSmallVideo: 设置是否所有流都只录制小画面的全局控制参数。一般与`StreamControls`参数配合使用。

true - 所有流都只录制小画面。设置为true时，请确保上行端在推流的时候同时上行了小画面，否则录制视频可能是黑屏。
false - 所有流都录制大画面，默认为false。

这里的设置对所有流都生效，如果同时在 `StreamControls` 列表中针对指定流设置了控制参数，则优先采用`StreamControls`中设置的控制参数。
        :type PullSmallVideo: bool
        :param StreamControls: 针对具体流指定控制参数，如果列表为空，则所有流采用全局配置的控制参数进行录制。列表不为空，则列表中指定的流将优先按此列表指定的控制参数进行录制。
        :type StreamControls: list of StreamControl
        """
        self.Enabled = None
        self.DisableRecord = None
        self.DisableAudio = None
        self.PullSmallVideo = None
        self.StreamControls = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.DisableRecord = params.get("DisableRecord")
        self.DisableAudio = params.get("DisableAudio")
        self.PullSmallVideo = params.get("PullSmallVideo")
        if params.get("StreamControls") is not None:
            self.StreamControls = []
            for item in params.get("StreamControls"):
                obj = StreamControl()
                obj._deserialize(item)
                self.StreamControls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordRequest(AbstractModel):
    """ResumeOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 恢复录制的实时录制任务 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordResponse(AbstractModel):
    """ResumeOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetOnlineRecordCallbackKeyRequest(AbstractModel):
    """SetOnlineRecordCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param CallbackKey: 设置实时录制回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥。回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackKeyResponse(AbstractModel):
    """SetOnlineRecordCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetOnlineRecordCallbackRequest(AbstractModel):
    """SetOnlineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 实时录制任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头。回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40258
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackResponse(AbstractModel):
    """SetOnlineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetTranscodeCallbackKeyRequest(AbstractModel):
    """SetTranscodeCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param CallbackKey: 设置文档转码回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackKeyResponse(AbstractModel):
    """SetTranscodeCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetTranscodeCallbackRequest(AbstractModel):
    """SetTranscodeCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 文档转码进度回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持http或https协议，即回调地址以http://或https://开头。
回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackResponse(AbstractModel):
    """SetTranscodeCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetVideoGenerationTaskCallbackKeyRequest(AbstractModel):
    """SetVideoGenerationTaskCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param CallbackKey: 设置视频生成回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVideoGenerationTaskCallbackKeyResponse(AbstractModel):
    """SetVideoGenerationTaskCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetVideoGenerationTaskCallbackRequest(AbstractModel):
    """SetVideoGenerationTaskCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 课后录制任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVideoGenerationTaskCallbackResponse(AbstractModel):
    """SetVideoGenerationTaskCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetWhiteboardPushCallbackKeyRequest(AbstractModel):
    """SetWhiteboardPushCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param CallbackKey: 设置白板推流回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥。回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWhiteboardPushCallbackKeyResponse(AbstractModel):
    """SetWhiteboardPushCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetWhiteboardPushCallbackRequest(AbstractModel):
    """SetWhiteboardPushCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 白板推流任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头。回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWhiteboardPushCallbackResponse(AbstractModel):
    """SetWhiteboardPushCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SnapshotCOS(AbstractModel):
    """板书文件存储cos参数

    """

    def __init__(self):
        r"""
        :param Uin: cos所在腾讯云帐号uin
        :type Uin: int
        :param Region: cos所在地区
        :type Region: str
        :param Bucket: cos存储桶名称
        :type Bucket: str
        :param TargetDir: 板书文件存储根目录
        :type TargetDir: str
        :param Domain: CDN加速域名
        :type Domain: str
        """
        self.Uin = None
        self.Region = None
        self.Bucket = None
        self.TargetDir = None
        self.Domain = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.TargetDir = params.get("TargetDir")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotResult(AbstractModel):
    """白板板书结果

    """

    def __init__(self):
        r"""
        :param ErrorCode: 任务执行错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param ErrorMessage: 任务执行错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param Total: 快照生成图片总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Snapshots: 快照图片链接列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Snapshots: list of str
        """
        self.ErrorCode = None
        self.ErrorMessage = None
        self.Total = None
        self.Snapshots = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        self.Total = params.get("Total")
        self.Snapshots = params.get("Snapshots")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotWhiteboard(AbstractModel):
    """生成白板板书时的白板参数，例如白板宽高等

    """

    def __init__(self):
        r"""
        :param Width: 白板宽度大小，默认为1280，有效取值范围[0，2560]
        :type Width: int
        :param Height: 白板高度大小，默认为720，有效取值范围[0，2560]
        :type Height: int
        :param InitParams: 白板初始化参数的JSON转义字符串，透传到白板 SDK
        :type InitParams: str
        """
        self.Width = None
        self.Height = None
        self.InitParams = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.InitParams = params.get("InitParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordRequest(AbstractModel):
    """StartOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param RoomId: 需要录制的房间号，取值范围: (1, 4294967295)
        :type RoomId: int
        :param RecordUserId: 用于录制服务进房的用户ID，最大长度不能大于60个字节，格式为`tic_record_user_${RoomId}_${Random}`，其中 `${RoomId} `与录制房间号对应，`${Random}`为一个随机字符串。
该ID必须是一个单独的未在SDK中使用的ID，录制服务使用这个用户ID进入房间进行音视频与白板录制，若该ID和SDK中使用的ID重复，会导致SDK和录制服务互踢，影响正常录制。
        :type RecordUserId: str
        :param RecordUserSig: 与RecordUserId对应的签名
        :type RecordUserSig: str
        :param GroupId: （已废弃，设置无效）白板的 IM 群组 Id，默认同房间号
        :type GroupId: str
        :param Concat: 录制视频拼接参数
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param Whiteboard: 录制白板参数，例如白板宽高等
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param MixStream: 录制混流参数
特别说明：
1. 混流功能需要根据额外开通， 请联系腾讯云互动白板客服人员
2. 使用混流功能，必须提供 Extras 参数，且 Extras 参数中必须包含 "MIX_STREAM"
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param Extras: 使用到的高级功能列表
可以选值列表：
MIX_STREAM - 混流功能
        :type Extras: list of str
        :param AudioFileNeeded: 是否需要在结果回调中返回各路流的纯音频录制文件，文件格式为mp3
        :type AudioFileNeeded: bool
        :param RecordControl: 录制控制参数，用于更精细地指定需要录制哪些流，某一路流是否禁用音频，是否只录制小画面等
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        :param RecordMode: 录制模式

REALTIME_MODE - 实时录制模式（默认）
VIDEO_GENERATION_MODE - 视频生成模式（内测中，需邮件申请开通）
        :type RecordMode: str
        :param ChatGroupId: 聊天群组ID，此字段仅适用于`视频生成模式`

在`视频生成模式`下，默认会记录白板群组内的非白板信令消息，如果指定了`ChatGroupId`，则会记录指定群ID的聊天消息。
        :type ChatGroupId: str
        :param AutoStopTimeout: 自动停止录制超时时间，单位秒，取值范围[300, 86400], 默认值为300秒。

当超过设定时间房间内没有音视频上行且没有白板操作的时候，录制服务会自动停止当前录制任务。
        :type AutoStopTimeout: int
        :param ExtraData: 内部参数，可忽略
        :type ExtraData: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.RecordUserId = None
        self.RecordUserSig = None
        self.GroupId = None
        self.Concat = None
        self.Whiteboard = None
        self.MixStream = None
        self.Extras = None
        self.AudioFileNeeded = None
        self.RecordControl = None
        self.RecordMode = None
        self.ChatGroupId = None
        self.AutoStopTimeout = None
        self.ExtraData = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.RecordUserId = params.get("RecordUserId")
        self.RecordUserSig = params.get("RecordUserSig")
        self.GroupId = params.get("GroupId")
        if params.get("Concat") is not None:
            self.Concat = Concat()
            self.Concat._deserialize(params.get("Concat"))
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("MixStream") is not None:
            self.MixStream = MixStream()
            self.MixStream._deserialize(params.get("MixStream"))
        self.Extras = params.get("Extras")
        self.AudioFileNeeded = params.get("AudioFileNeeded")
        if params.get("RecordControl") is not None:
            self.RecordControl = RecordControl()
            self.RecordControl._deserialize(params.get("RecordControl"))
        self.RecordMode = params.get("RecordMode")
        self.ChatGroupId = params.get("ChatGroupId")
        self.AutoStopTimeout = params.get("AutoStopTimeout")
        self.ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordResponse(AbstractModel):
    """StartOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 录制任务Id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class StartWhiteboardPushRequest(AbstractModel):
    """StartWhiteboardPush请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param RoomId: 需要推流的白板房间号，取值范围: (1, 4294967295)。

在没有指定TRTCRoomId和TRTCRoomIdStr的情况下，默认会以RoomId作为白板流进行推流的TRTC房间号。
        :type RoomId: int
        :param PushUserId: 用于白板推流服务进入白板房间的用户ID。在没有进行额外指定的情况下，这个用户ID同时会用于IM登录、IM加群、TRTC进房推流等操作。
用户ID最大长度不能大于60个字节，该ID必须是一个单独的未在SDK中使用的ID，白板推流服务使用这个用户ID进入房间进行白板音视频推流，若该ID和SDK中使用的ID重复，会导致SDK和白板推流服务互踢，影响正常推流。
        :type PushUserId: str
        :param PushUserSig: 与PushUserId对应的签名
        :type PushUserSig: str
        :param Whiteboard: 白板参数，例如白板宽高、背景颜色等
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param AutoStopTimeout: 自动停止推流超时时间，单位秒，取值范围[300, 259200], 默认值为1800秒。

当白板超过设定时间没有操作的时候，白板推流服务会自动停止白板推流。
        :type AutoStopTimeout: int
        :param AutoManageBackup: 对主白板推流任务进行操作时，是否同时同步操作备份任务
        :type AutoManageBackup: bool
        :param Backup: 备份白板推流相关参数。

指定了备份参数的情况下，白板推流服务会在房间内新增一路白板画面视频流，即同一个房间内会有两路白板画面推流。
        :type Backup: :class:`tencentcloud.tiw.v20190919.models.WhiteboardPushBackupParam`
        :param PrivateMapKey: TRTC高级权限控制参数，如果在实时音视频开启了高级权限控制功能，必须提供PrivateMapKey才能保证正常推流。
        :type PrivateMapKey: str
        :param VideoFPS: 白板推流视频帧率，取值范围[0, 30]，默认20fps
        :type VideoFPS: int
        :param VideoBitrate: 白板推流码率， 取值范围[0, 2000]，默认1200kbps。

这里的码率设置是一个参考值，实际推流的时候使用的是动态码率，所以真实码率不会固定为指定值，会在指定值附近波动。
        :type VideoBitrate: int
        :param AutoRecord: 在实时音视频云端录制模式选择为 `指定用户录制` 模式的时候是否自动录制白板推流。

默认在实时音视频的云端录制模式选择为 `指定用户录制` 模式的情况下，不会自动进行白板推流录制，如果希望进行白板推流录制，请将此参数设置为true。

如果实时音视频的云端录制模式选择为 `全局自动录制` 模式，可忽略此参数。
        :type AutoRecord: bool
        :param UserDefinedRecordId: 指定白板推流录制的RecordID，指定的RecordID会用于填充实时音视频云端录制完成后的回调消息中的 "userdefinerecordid" 字段内容，便于您更方便的识别录制回调，以及在点播媒体资源管理中查找相应的录制视频文件。

限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线和连词符。

此字段设置后，不管`AutoRecord`字段取值如何，都将自动进行白板推流录制。

默认RecordId生成规则如下：
urlencode(SdkAppID_RoomID_PushUserID)

例如：
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
那么：RecordId = 12345678_12345_push_user_1
        :type UserDefinedRecordId: str
        :param AutoPublish: 在实时音视频旁路推流模式选择为`指定用户旁路`模式的时候，是否自动旁路白板推流。

默认在实时音视频的旁路推流模式选择为 `指定用户旁路` 模式的情况下，不会自动旁路白板推流，如果希望旁路白板推流，请将此参数设置为true。

如果实时音视频的旁路推流模式选择为 `全局自动旁路` 模式，可忽略此参数。
        :type AutoPublish: bool
        :param UserDefinedStreamId: 指定实时音视频在旁路白板推流时的StreamID，设置之后，您就可以在腾讯云直播 CDN 上通过标准直播方案（FLV或HLS）播放该用户的音视频流。

限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线和连词符。

此字段设置后，不管`AutoPublish`字段取值如何，都将自动旁路白板推流。

默认StreamID生成规则如下：
urlencode(SdkAppID_RoomID_PushUserID_main)

例如：
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
那么：StreamID = 12345678_12345_push_user_1_main
        :type UserDefinedStreamId: str
        :param ExtraData: 内部参数，不需要关注此参数
        :type ExtraData: str
        :param TRTCRoomId: TRTC数字类型房间号，取值范围: (1, 4294967295)。

在同时指定了RoomId与TRTCRoomId的情况下，优先使用TRTCRoomId作为白板流进行推流的TRTC房间号。

当指定了TRTCRoomIdStr的情况下，此字段将被忽略。
        :type TRTCRoomId: int
        :param TRTCRoomIdStr: TRTC字符串类型房间号。

在指定了TRTCRoomIdStr的情况下，会优先使用TRTCRoomIdStr作为白板流进行推流的TRTC房间号。
        :type TRTCRoomIdStr: str
        :param IMAuthParam: 内测参数，需开通白名单进行体验。

IM鉴权信息参数，用于IM鉴权。
当白板信令所使用的IM应用与白板应用的SdkAppId不一致时，可以通过此参数提供对应IM应用鉴权信息。

如果提供了此参数，白板推流服务会优先使用此参数指定的SdkAppId作为白板信令的传输通道，否则使用公共参数中的SdkAppId作为白板信令的传输通道。
        :type IMAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        :param TRTCAuthParam: 内测参数，需开通白名单进行体验。

TRTC鉴权信息参数，用于TRTC进房推流鉴权。
当需要推流到的TRTC房间所对应的TRTC应用与白板应用的SdkAppId不一致时，可以通过此参数提供对应的TRTC应用鉴权信息。

如果提供了此参数，白板推流服务会优先使用此参数指定的SdkAppId作为白板推流的目标TRTC应用，否则使用公共参数中的SdkAppId作为白板推流的目标TRTC应用。
        :type TRTCAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        """
        self.SdkAppId = None
        self.RoomId = None
        self.PushUserId = None
        self.PushUserSig = None
        self.Whiteboard = None
        self.AutoStopTimeout = None
        self.AutoManageBackup = None
        self.Backup = None
        self.PrivateMapKey = None
        self.VideoFPS = None
        self.VideoBitrate = None
        self.AutoRecord = None
        self.UserDefinedRecordId = None
        self.AutoPublish = None
        self.UserDefinedStreamId = None
        self.ExtraData = None
        self.TRTCRoomId = None
        self.TRTCRoomIdStr = None
        self.IMAuthParam = None
        self.TRTCAuthParam = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.PushUserId = params.get("PushUserId")
        self.PushUserSig = params.get("PushUserSig")
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        self.AutoStopTimeout = params.get("AutoStopTimeout")
        self.AutoManageBackup = params.get("AutoManageBackup")
        if params.get("Backup") is not None:
            self.Backup = WhiteboardPushBackupParam()
            self.Backup._deserialize(params.get("Backup"))
        self.PrivateMapKey = params.get("PrivateMapKey")
        self.VideoFPS = params.get("VideoFPS")
        self.VideoBitrate = params.get("VideoBitrate")
        self.AutoRecord = params.get("AutoRecord")
        self.UserDefinedRecordId = params.get("UserDefinedRecordId")
        self.AutoPublish = params.get("AutoPublish")
        self.UserDefinedStreamId = params.get("UserDefinedStreamId")
        self.ExtraData = params.get("ExtraData")
        self.TRTCRoomId = params.get("TRTCRoomId")
        self.TRTCRoomIdStr = params.get("TRTCRoomIdStr")
        if params.get("IMAuthParam") is not None:
            self.IMAuthParam = AuthParam()
            self.IMAuthParam._deserialize(params.get("IMAuthParam"))
        if params.get("TRTCAuthParam") is not None:
            self.TRTCAuthParam = AuthParam()
            self.TRTCAuthParam._deserialize(params.get("TRTCAuthParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartWhiteboardPushResponse(AbstractModel):
    """StartWhiteboardPush返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 推流任务Id
        :type TaskId: str
        :param Backup: 备份任务结果参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Backup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Backup = params.get("Backup")
        self.RequestId = params.get("RequestId")


class StopOnlineRecordRequest(AbstractModel):
    """StopOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 需要停止录制的任务 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopOnlineRecordResponse(AbstractModel):
    """StopOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopWhiteboardPushRequest(AbstractModel):
    """StopWhiteboardPush请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 需要停止的白板推流任务 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWhiteboardPushResponse(AbstractModel):
    """StopWhiteboardPush返回参数结构体

    """

    def __init__(self):
        r"""
        :param Backup: 备份任务相关参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Backup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Backup = params.get("Backup")
        self.RequestId = params.get("RequestId")


class StreamControl(AbstractModel):
    """指定流录制的控制参数，比如是否禁用音频、视频是录制大画面还是录制小画面等

    """

    def __init__(self):
        r"""
        :param StreamId: 视频流ID
视频流ID的取值含义如下：
1. tic_record_user - 表示白板视频流
2. tic_substream - 表示辅路视频流
3. 特定用户ID - 表示指定用户的视频流

在实际录制过程中，视频流ID的匹配规则为前缀匹配，只要真实流ID的前缀与指定的流ID一致就认为匹配成功。
        :type StreamId: str
        :param DisableRecord: 设置是否对此路流开启录制。

true - 表示不对这路流进行录制，录制结果将不包含这路流的视频。
false - 表示需要对这路流进行录制，录制结果会包含这路流的视频。

默认为 false。
        :type DisableRecord: bool
        :param DisableAudio: 设置是否禁用这路流的音频录制。

true - 表示不对这路流的音频进行录制，录制结果里这路流的视频将会没有声音。
false - 录制视频会保留音频，如果设置为true，则录制视频会丢弃这路流的音频。

默认为 false。
        :type DisableAudio: bool
        :param PullSmallVideo: 设置当前流录制视频是否只录制小画面。

true - 录制小画面。设置为true时，请确保上行端同时上行了小画面，否则录制视频可能是黑屏。
false - 录制大画面。

默认为 false。
        :type PullSmallVideo: bool
        """
        self.StreamId = None
        self.DisableRecord = None
        self.DisableAudio = None
        self.PullSmallVideo = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.DisableRecord = params.get("DisableRecord")
        self.DisableAudio = params.get("DisableAudio")
        self.PullSmallVideo = params.get("PullSmallVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLayout(AbstractModel):
    """流布局参数

    """

    def __init__(self):
        r"""
        :param LayoutParams: 流布局配置参数
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param InputStreamId: 视频流ID
流ID的取值含义如下：
1. tic_record_user - 表示当前画面用于显示白板视频流
2. tic_substream - 表示当前画面用于显示辅路视频流
3. 特定用户ID - 表示当前画面用于显示指定用户的视频流
4. 不填 - 表示当前画面用于备选，当有新的视频流加入时，会从这些备选的空位中选择一个没有被占用的位置来显示新的视频流画面
        :type InputStreamId: str
        :param BackgroundColor: 背景颜色，默认为黑色，格式为RGB格式，如红色为"#FF0000"
        :type BackgroundColor: str
        :param FillMode: 视频画面填充模式。

0 - 自适应模式，对视频画面进行等比例缩放，在指定区域内显示完整的画面。此模式可能存在黑边。
1 - 全屏模式，对视频画面进行等比例缩放，让画面填充满整个指定区域。此模式不会存在黑边，但会将超出区域的那一部分画面裁剪掉。
        :type FillMode: int
        """
        self.LayoutParams = None
        self.InputStreamId = None
        self.BackgroundColor = None
        self.FillMode = None


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        self.InputStreamId = params.get("InputStreamId")
        self.BackgroundColor = params.get("BackgroundColor")
        self.FillMode = params.get("FillMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeValue(AbstractModel):
    """查询指标返回的时间序列

    """

    def __init__(self):
        r"""
        :param Time: Unix时间戳，单位秒
        :type Time: int
        :param Value: 查询指标对应当前时间的值
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDataItem(AbstractModel):
    """互动白板用量信息

    """

    def __init__(self):
        r"""
        :param Time: 日期，格式为YYYY-MM-DD
        :type Time: str
        :param SdkAppId: 白板应用SDKAppID
        :type SdkAppId: int
        :param SubProduct: 互动白板子产品，请求参数传入的一致
- sp_tiw_board: 互动白板时长
- sp_tiw_dt: 动态转码页数
- sp_tiw_st: 静态转码页数
- sp_tiw_ric: 实时录制时长
        :type SubProduct: str
        :param Value: 用量值
- 静态转码、动态转码单位为页
- 白板时长、实时录制时长单位为分钟
        :type Value: float
        """
        self.Time = None
        self.SdkAppId = None
        self.SubProduct = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoInfo(AbstractModel):
    """视频信息

    """

    def __init__(self):
        r"""
        :param VideoPlayTime: 视频开始播放的时间（单位：毫秒）
        :type VideoPlayTime: int
        :param VideoSize: 视频大小（字节）
        :type VideoSize: int
        :param VideoFormat: 视频格式
        :type VideoFormat: str
        :param VideoDuration: 视频播放时长（单位：毫秒）
        :type VideoDuration: int
        :param VideoUrl: 视频文件URL
        :type VideoUrl: str
        :param VideoId: 视频文件Id
        :type VideoId: str
        :param VideoType: 视频流类型 
- 0：摄像头视频 
- 1：屏幕分享视频
- 2：白板视频 
- 3：混流视频
- 4：纯音频（mp3)
        :type VideoType: int
        :param UserId: 摄像头/屏幕分享视频所属用户的 Id（白板视频为空、混流视频tic_mixstream_房间号_混流布局类型、辅路视频tic_substream_用户Id）
        :type UserId: str
        :param Width: 视频分辨率的宽
        :type Width: int
        :param Height: 视频分辨率的高
        :type Height: int
        """
        self.VideoPlayTime = None
        self.VideoSize = None
        self.VideoFormat = None
        self.VideoDuration = None
        self.VideoUrl = None
        self.VideoId = None
        self.VideoType = None
        self.UserId = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.VideoPlayTime = params.get("VideoPlayTime")
        self.VideoSize = params.get("VideoSize")
        self.VideoFormat = params.get("VideoFormat")
        self.VideoDuration = params.get("VideoDuration")
        self.VideoUrl = params.get("VideoUrl")
        self.VideoId = params.get("VideoId")
        self.VideoType = params.get("VideoType")
        self.UserId = params.get("UserId")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Whiteboard(AbstractModel):
    """实时录制白板参数，例如白板宽高等

    """

    def __init__(self):
        r"""
        :param Width: 实时录制结果里白板视频宽，取值必须大于等于2，默认为1280
        :type Width: int
        :param Height: 实时录制结果里白板视频高，取值必须大于等于2，默认为960
        :type Height: int
        :param InitParam: 白板初始化参数，透传到白板 SDK
        :type InitParam: str
        """
        self.Width = None
        self.Height = None
        self.InitParam = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.InitParam = params.get("InitParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushBackupParam(AbstractModel):
    """白板推流备份相关请求参数

    """

    def __init__(self):
        r"""
        :param PushUserId: 用于白板推流服务进房的用户ID，
该ID必须是一个单独的未在SDK中使用的ID，白板推流服务将使用这个用户ID进入房间进行白板推流，若该ID和SDK中使用的ID重复，会导致SDK和录制服务互踢，影响正常推流。
        :type PushUserId: str
        :param PushUserSig: 与PushUserId对应的签名
        :type PushUserSig: str
        """
        self.PushUserId = None
        self.PushUserSig = None


    def _deserialize(self, params):
        self.PushUserId = params.get("PushUserId")
        self.PushUserSig = params.get("PushUserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        