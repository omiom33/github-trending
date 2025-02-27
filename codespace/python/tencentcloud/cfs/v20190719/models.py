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


class AutoSnapshotPolicyInfo(AbstractModel):
    """快照策略信息

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param PolicyName: 快照策略ID
        :type PolicyName: str
        :param CreationTime: 快照策略创建时间
        :type CreationTime: str
        :param FileSystemNums: 关联的文件系统个数
        :type FileSystemNums: int
        :param DayOfWeek: 快照定期备份在一星期哪一天
        :type DayOfWeek: str
        :param Hour: 快照定期备份在一天的哪一小时
        :type Hour: str
        :param IsActivated: 是否激活定期快照功能
        :type IsActivated: int
        :param NextActiveTime: 下一次触发快照时间
        :type NextActiveTime: str
        :param Status: 快照策略状态
        :type Status: str
        :param AppId: 帐号ID
        :type AppId: int
        :param AliveDays: 保留时间
        :type AliveDays: int
        :param RegionName: 地域
        :type RegionName: str
        :param FileSystems: 文件系统信息
        :type FileSystems: list of FileSystemByPolicy
        """
        self.AutoSnapshotPolicyId = None
        self.PolicyName = None
        self.CreationTime = None
        self.FileSystemNums = None
        self.DayOfWeek = None
        self.Hour = None
        self.IsActivated = None
        self.NextActiveTime = None
        self.Status = None
        self.AppId = None
        self.AliveDays = None
        self.RegionName = None
        self.FileSystems = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.PolicyName = params.get("PolicyName")
        self.CreationTime = params.get("CreationTime")
        self.FileSystemNums = params.get("FileSystemNums")
        self.DayOfWeek = params.get("DayOfWeek")
        self.Hour = params.get("Hour")
        self.IsActivated = params.get("IsActivated")
        self.NextActiveTime = params.get("NextActiveTime")
        self.Status = params.get("Status")
        self.AppId = params.get("AppId")
        self.AliveDays = params.get("AliveDays")
        self.RegionName = params.get("RegionName")
        if params.get("FileSystems") is not None:
            self.FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemByPolicy()
                obj._deserialize(item)
                self.FileSystems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableProtoStatus(AbstractModel):
    """版本控制-协议详情

    """

    def __init__(self):
        r"""
        :param SaleStatus: 售卖状态。可选值有 sale_out 售罄、saling可售、no_saling不可销售
        :type SaleStatus: str
        :param Protocol: 协议类型。可选值有 NFS、CIFS
        :type Protocol: str
        """
        self.SaleStatus = None
        self.Protocol = None


    def _deserialize(self, params):
        self.SaleStatus = params.get("SaleStatus")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableRegion(AbstractModel):
    """版本控制-区域数组

    """

    def __init__(self):
        r"""
        :param Region: 区域名称，如“ap-beijing”
        :type Region: str
        :param RegionName: 区域名称，如“bj”
        :type RegionName: str
        :param RegionStatus: 区域可用情况，当区域内至少有一个可用区处于可售状态时，取值为AVAILABLE，否则为UNAVAILABLE
        :type RegionStatus: str
        :param Zones: 可用区数组
        :type Zones: list of AvailableZone
        :param RegionCnName: 区域中文名称，如“广州”
        :type RegionCnName: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionStatus = None
        self.Zones = None
        self.RegionCnName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionStatus = params.get("RegionStatus")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = AvailableZone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RegionCnName = params.get("RegionCnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableType(AbstractModel):
    """版本控制-类型数组

    """

    def __init__(self):
        r"""
        :param Protocols: 协议与售卖详情
        :type Protocols: list of AvailableProtoStatus
        :param Type: 存储类型。返回值中 SD 为标准型存储、HP 为性能型存储
        :type Type: str
        :param Prepayment: 是否支持预付费。返回值中 true 为支持、false 为不支持
        :type Prepayment: bool
        """
        self.Protocols = None
        self.Type = None
        self.Prepayment = None


    def _deserialize(self, params):
        if params.get("Protocols") is not None:
            self.Protocols = []
            for item in params.get("Protocols"):
                obj = AvailableProtoStatus()
                obj._deserialize(item)
                self.Protocols.append(obj)
        self.Type = params.get("Type")
        self.Prepayment = params.get("Prepayment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableZone(AbstractModel):
    """版本控制-可用区数组

    """

    def __init__(self):
        r"""
        :param Zone: 可用区名称
        :type Zone: str
        :param ZoneId: 可用区ID
        :type ZoneId: int
        :param ZoneCnName: 可用区中文名称
        :type ZoneCnName: str
        :param Types: Type数组
        :type Types: list of AvailableType
        :param ZoneName: 可用区中英文名称
        :type ZoneName: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneCnName = None
        self.Types = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneCnName = params.get("ZoneCnName")
        if params.get("Types") is not None:
            self.Types = []
            for item in params.get("Types"):
                obj = AvailableType()
                obj._deserialize(item)
                self.Types.append(obj)
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoSnapshotPolicyRequest(AbstractModel):
    """BindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param FileSystemIds: 文件系统列表
        :type FileSystemIds: str
        """
        self.AutoSnapshotPolicyId = None
        self.FileSystemIds = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.FileSystemIds = params.get("FileSystemIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoSnapshotPolicyResponse(AbstractModel):
    """BindAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoSnapshotPolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.RequestId = params.get("RequestId")


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    """CreateAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param DayOfWeek: 快照重复日期，星期一到星期日
        :type DayOfWeek: str
        :param Hour: 快照重复时间点
        :type Hour: str
        :param PolicyName: 策略名称
        :type PolicyName: str
        :param AliveDays: 快照保留时长
        :type AliveDays: int
        """
        self.DayOfWeek = None
        self.Hour = None
        self.PolicyName = None
        self.AliveDays = None


    def _deserialize(self, params):
        self.DayOfWeek = params.get("DayOfWeek")
        self.Hour = params.get("Hour")
        self.PolicyName = params.get("PolicyName")
        self.AliveDays = params.get("AliveDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoSnapshotPolicyResponse(AbstractModel):
    """CreateAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoSnapshotPolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.RequestId = params.get("RequestId")


class CreateCfsFileSystemRequest(AbstractModel):
    """CreateCfsFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区名称，例如ap-beijing-1，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的地域与可用区列表
        :type Zone: str
        :param NetInterface: 网络类型，可选值为 VPC，BASIC，CCN；其中 VPC 为私有网络，BASIC 为基础网络, CCN 为云联网，Turbo系列当前必须选择云联网。目前基础网络已逐渐淘汰，不推荐使用。
        :type NetInterface: str
        :param PGroupId: 权限组 ID，通用标准型和性能型必填，turbo系列请填写pgroupbasic
        :type PGroupId: str
        :param Protocol: 文件系统协议类型， 值为 NFS、CIFS、TURBO ; 若留空则默认为 NFS协议，turbo系列必须选择turbo，不支持NFS、CIFS
        :type Protocol: str
        :param StorageType: 文件系统存储类型，默认值为 SD ；其中 SD 为通用标准型标准型存储， HP为通用性能型存储， TB为turbo标准型， TP 为turbo性能型。
        :type StorageType: str
        :param VpcId: 私有网络（VPC） ID，若网络类型选择的是VPC，该字段为必填。
        :type VpcId: str
        :param SubnetId: 子网 ID，若网络类型选择的是VPC，该字段为必填。
        :type SubnetId: str
        :param MountIP: 指定IP地址，仅VPC网络支持；若不填写、将在该子网下随机分配 IP，Turbo系列当前不支持指定
        :type MountIP: str
        :param FsName: 用户自定义文件系统名称
        :type FsName: str
        :param ResourceTags: 文件系统标签
        :type ResourceTags: list of TagInfo
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。用于保证请求幂等性的字符串失效时间为2小时。
        :type ClientToken: str
        :param CcnId: 云联网ID， 若网络类型选择的是CCN，该字段为必填
        :type CcnId: str
        :param CidrBlock: 云联网中CFS使用的网段， 若网络类型选择的是Ccn，该字段为必填，且不能和Ccn中已经绑定的网段冲突
        :type CidrBlock: str
        :param Capacity: 文件系统容量，turbo系列必填，单位为GiB。 turbo标准型单位GB，起售40TiB，即40960 GiB；扩容步长20TiB，即20480 GiB。turbo性能型起售20TiB，即20480 GiB；扩容步长10TiB，10240 GiB。
        :type Capacity: int
        """
        self.Zone = None
        self.NetInterface = None
        self.PGroupId = None
        self.Protocol = None
        self.StorageType = None
        self.VpcId = None
        self.SubnetId = None
        self.MountIP = None
        self.FsName = None
        self.ResourceTags = None
        self.ClientToken = None
        self.CcnId = None
        self.CidrBlock = None
        self.Capacity = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NetInterface = params.get("NetInterface")
        self.PGroupId = params.get("PGroupId")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.MountIP = params.get("MountIP")
        self.FsName = params.get("FsName")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.ClientToken = params.get("ClientToken")
        self.CcnId = params.get("CcnId")
        self.CidrBlock = params.get("CidrBlock")
        self.Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsFileSystemResponse(AbstractModel):
    """CreateCfsFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param CreationTime: 文件系统创建时间
        :type CreationTime: str
        :param CreationToken: 用户自定义文件系统名称
        :type CreationToken: str
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param LifeCycleState: 文件系统状态，可能出现状态包括：“creating”  创建中, “create_failed” 创建失败, “available” 可用, “unserviced” 不可用, “upgrading” 升级中， “deleting” 删除中。
        :type LifeCycleState: str
        :param SizeByte: 文件系统已使用容量大小，单位为 Byte
        :type SizeByte: int
        :param ZoneId: 可用区 ID
        :type ZoneId: int
        :param FsName: 用户自定义文件系统名称
        :type FsName: str
        :param Encrypted: 文件系统是否加密
        :type Encrypted: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CreationTime = None
        self.CreationToken = None
        self.FileSystemId = None
        self.LifeCycleState = None
        self.SizeByte = None
        self.ZoneId = None
        self.FsName = None
        self.Encrypted = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.LifeCycleState = params.get("LifeCycleState")
        self.SizeByte = params.get("SizeByte")
        self.ZoneId = params.get("ZoneId")
        self.FsName = params.get("FsName")
        self.Encrypted = params.get("Encrypted")
        self.RequestId = params.get("RequestId")


class CreateCfsPGroupRequest(AbstractModel):
    """CreateCfsPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线
        :type Name: str
        :param DescInfo: 权限组描述信息，1-255个字符
        :type DescInfo: str
        """
        self.Name = None
        self.DescInfo = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsPGroupResponse(AbstractModel):
    """CreateCfsPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param Name: 权限组名字
        :type Name: str
        :param DescInfo: 权限组描述信息
        :type DescInfo: str
        :param BindCfsNum: 已经与该权限组绑定的文件系统个数
        :type BindCfsNum: int
        :param CDate: 权限组创建时间
        :type CDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.BindCfsNum = None
        self.CDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.BindCfsNum = params.get("BindCfsNum")
        self.CDate = params.get("CDate")
        self.RequestId = params.get("RequestId")


class CreateCfsRuleRequest(AbstractModel):
    """CreateCfsRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param AuthClientIp: 可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :type AuthClientIp: str
        :param Priority: 规则优先级，参数范围1-100。 其中 1 为最高，100为最低
        :type Priority: int
        :param RWPermission: 读写权限, 值为 RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :type RWPermission: str
        :param UserPermission: 用户权限，值为 all_squash、no_all_squash、root_squash、no_root_squash。其中all_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash为将来访的root用户映射为匿名用户或用户组；no_root_squash为来访的root用户保持root帐号权限。不填默认为root_squash。
        :type UserPermission: str
        """
        self.PGroupId = None
        self.AuthClientIp = None
        self.Priority = None
        self.RWPermission = None
        self.UserPermission = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.Priority = params.get("Priority")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsRuleResponse(AbstractModel):
    """CreateCfsRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则 ID
        :type RuleId: str
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param AuthClientIp: 客户端 IP
        :type AuthClientIp: str
        :param RWPermission: 读写权限
        :type RWPermission: str
        :param UserPermission: 用户权限
        :type UserPermission: str
        :param Priority: 优先级
        :type Priority: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.PGroupId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.PGroupId = params.get("PGroupId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")


class CreateCfsSnapshotRequest(AbstractModel):
    """CreateCfsSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统id
        :type FileSystemId: str
        :param SnapshotName: 快照名称
        :type SnapshotName: str
        :param ResourceTags: 快照标签
        :type ResourceTags: list of TagInfo
        """
        self.FileSystemId = None
        self.SnapshotName = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.SnapshotName = params.get("SnapshotName")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsSnapshotResponse(AbstractModel):
    """CreateCfsSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 文件系统快照id
        :type SnapshotId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.RequestId = params.get("RequestId")


class DeleteAutoSnapshotPolicyRequest(AbstractModel):
    """DeleteAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        """
        self.AutoSnapshotPolicyId = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoSnapshotPolicyResponse(AbstractModel):
    """DeleteAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoSnapshotPolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.RequestId = params.get("RequestId")


class DeleteCfsFileSystemRequest(AbstractModel):
    """DeleteCfsFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID。说明，进行删除文件系统操作前需要先调用 DeleteMountTarget 接口删除该文件系统的挂载点，否则会删除失败。
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsFileSystemResponse(AbstractModel):
    """DeleteCfsFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCfsPGroupRequest(AbstractModel):
    """DeleteCfsPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        """
        self.PGroupId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsPGroupResponse(AbstractModel):
    """DeleteCfsPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param AppId: 用户 ID
        :type AppId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.AppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.AppId = params.get("AppId")
        self.RequestId = params.get("RequestId")


class DeleteCfsRuleRequest(AbstractModel):
    """DeleteCfsRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param RuleId: 规则 ID
        :type RuleId: str
        """
        self.PGroupId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsRuleResponse(AbstractModel):
    """DeleteCfsRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则 ID
        :type RuleId: str
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.PGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.PGroupId = params.get("PGroupId")
        self.RequestId = params.get("RequestId")


class DeleteCfsSnapshotRequest(AbstractModel):
    """DeleteCfsSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 文件系统快照id
        :type SnapshotId: str
        :param SnapshotIds: 需要删除的文件文件系统快照ID 列表，快照ID，跟ID列表至少填一项
        :type SnapshotIds: list of str
        """
        self.SnapshotId = None
        self.SnapshotIds = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsSnapshotResponse(AbstractModel):
    """DeleteCfsSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 文件系统ID
        :type SnapshotId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.RequestId = params.get("RequestId")


class DeleteMountTargetRequest(AbstractModel):
    """DeleteMountTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param MountTargetId: 挂载点 ID
        :type MountTargetId: str
        """
        self.FileSystemId = None
        self.MountTargetId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.MountTargetId = params.get("MountTargetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMountTargetResponse(AbstractModel):
    """DeleteMountTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserQuotaRequest(AbstractModel):
    """DeleteUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param UserType: 指定配额类型，包括Uid、Gid
        :type UserType: str
        :param UserId: UID/GID信息
        :type UserId: str
        """
        self.FileSystemId = None
        self.UserType = None
        self.UserId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.UserType = params.get("UserType")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserQuotaResponse(AbstractModel):
    """DeleteUserQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    """DescribeAutoSnapshotPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param Offset: 分页码
        :type Offset: int
        :param Limit: 页面长
        :type Limit: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Order: 升序，降序
        :type Order: str
        :param OrderField: 排序字段
        :type OrderField: str
        """
        self.AutoSnapshotPolicyId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoSnapshotPoliciesResponse(AbstractModel):
    """DescribeAutoSnapshotPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 快照策略总个数
        :type TotalCount: int
        :param AutoSnapshotPolicies: 快照策略信息
        :type AutoSnapshotPolicies: list of AutoSnapshotPolicyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AutoSnapshotPolicies = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicies") is not None:
            self.AutoSnapshotPolicies = []
            for item in params.get("AutoSnapshotPolicies"):
                obj = AutoSnapshotPolicyInfo()
                obj._deserialize(item)
                self.AutoSnapshotPolicies.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAvailableZoneInfoRequest(AbstractModel):
    """DescribeAvailableZoneInfo请求参数结构体

    """


class DescribeAvailableZoneInfoResponse(AbstractModel):
    """DescribeAvailableZoneInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegionZones: 各可用区的资源售卖情况以及支持的存储类型、存储协议等信息
        :type RegionZones: list of AvailableRegion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionZones = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionZones") is not None:
            self.RegionZones = []
            for item in params.get("RegionZones"):
                obj = AvailableRegion()
                obj._deserialize(item)
                self.RegionZones.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsFileSystemClientsRequest(AbstractModel):
    """DescribeCfsFileSystemClients请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID。
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsFileSystemClientsResponse(AbstractModel):
    """DescribeCfsFileSystemClients返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClientList: 客户端列表
        :type ClientList: list of FileSystemClient
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClientList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClientList") is not None:
            self.ClientList = []
            for item in params.get("ClientList"):
                obj = FileSystemClient()
                obj._deserialize(item)
                self.ClientList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsFileSystemsRequest(AbstractModel):
    """DescribeCfsFileSystems请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param VpcId: 私有网络（VPC） ID
        :type VpcId: str
        :param SubnetId: 子网 ID
        :type SubnetId: str
        """
        self.FileSystemId = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsFileSystemsResponse(AbstractModel):
    """DescribeCfsFileSystems返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystems: 文件系统信息
        :type FileSystems: list of FileSystemInfo
        :param TotalCount: 文件系统总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileSystems = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystems") is not None:
            self.FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemInfo()
                obj._deserialize(item)
                self.FileSystems.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCfsPGroupsRequest(AbstractModel):
    """DescribeCfsPGroups请求参数结构体

    """


class DescribeCfsPGroupsResponse(AbstractModel):
    """DescribeCfsPGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupList: 权限组信息列表
        :type PGroupList: list of PGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PGroupList") is not None:
            self.PGroupList = []
            for item in params.get("PGroupList"):
                obj = PGroupInfo()
                obj._deserialize(item)
                self.PGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsRulesRequest(AbstractModel):
    """DescribeCfsRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        """
        self.PGroupId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsRulesResponse(AbstractModel):
    """DescribeCfsRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleList: 权限组规则列表
        :type RuleList: list of PGroupRuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = PGroupRuleInfo()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsServiceStatusRequest(AbstractModel):
    """DescribeCfsServiceStatus请求参数结构体

    """


class DescribeCfsServiceStatusResponse(AbstractModel):
    """DescribeCfsServiceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param CfsServiceStatus: 该用户当前 CFS 服务的状态，none 为未开通，creating 为开通中，created 为已开通
        :type CfsServiceStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CfsServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfsServiceStatus = params.get("CfsServiceStatus")
        self.RequestId = params.get("RequestId")


class DescribeCfsSnapshotOverviewRequest(AbstractModel):
    """DescribeCfsSnapshotOverview请求参数结构体

    """


class DescribeCfsSnapshotOverviewResponse(AbstractModel):
    """DescribeCfsSnapshotOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param StatisticsList: 统计信息
        :type StatisticsList: list of SnapshotStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StatisticsList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatisticsList") is not None:
            self.StatisticsList = []
            for item in params.get("StatisticsList"):
                obj = SnapshotStatistics()
                obj._deserialize(item)
                self.StatisticsList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsSnapshotsRequest(AbstractModel):
    """DescribeCfsSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param SnapshotId: 快照ID
        :type SnapshotId: str
        :param Offset: 分页起始位置
        :type Offset: int
        :param Limit: 页面长度
        :type Limit: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param OrderField: 排序取值
        :type OrderField: str
        :param Order: 排序 升序或者降序
        :type Order: str
        """
        self.FileSystemId = None
        self.SnapshotId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.SnapshotId = params.get("SnapshotId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsSnapshotsResponse(AbstractModel):
    """DescribeCfsSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总个数
        :type TotalCount: int
        :param Snapshots: 快照信息描述
        :type Snapshots: list of SnapshotInfo
        :param TotalSize: 快照列表快照汇总
        :type TotalSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Snapshots = None
        self.TotalSize = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Snapshots") is not None:
            self.Snapshots = []
            for item in params.get("Snapshots"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self.Snapshots.append(obj)
        self.TotalSize = params.get("TotalSize")
        self.RequestId = params.get("RequestId")


class DescribeMountTargetsRequest(AbstractModel):
    """DescribeMountTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountTargetsResponse(AbstractModel):
    """DescribeMountTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param MountTargets: 挂载点详情
        :type MountTargets: list of MountInfo
        :param NumberOfMountTargets: 挂载点数量
        :type NumberOfMountTargets: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MountTargets = None
        self.NumberOfMountTargets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountTargets") is not None:
            self.MountTargets = []
            for item in params.get("MountTargets"):
                obj = MountInfo()
                obj._deserialize(item)
                self.MountTargets.append(obj)
        self.NumberOfMountTargets = params.get("NumberOfMountTargets")
        self.RequestId = params.get("RequestId")


class DescribeSnapshotOperationLogsRequest(AbstractModel):
    """DescribeSnapshotOperationLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 文件系统快照ID
        :type SnapshotId: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.SnapshotId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotOperationLogsResponse(AbstractModel):
    """DescribeSnapshotOperationLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 快照ID
        :type SnapshotId: str
        :param SnapshotOperates: 操作日志
        :type SnapshotOperates: list of SnapshotOperateLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotId = None
        self.SnapshotOperates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        if params.get("SnapshotOperates") is not None:
            self.SnapshotOperates = []
            for item in params.get("SnapshotOperates"):
                obj = SnapshotOperateLog()
                obj._deserialize(item)
                self.SnapshotOperates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserQuotaRequest(AbstractModel):
    """DescribeUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param Filters: 过滤条件。
<br><li>UserType - Array of String - 是否必填：否 -（过滤条件）按配额类型过滤。(Uid| Gid )
<br><li>UserId - Array of String - 是否必填：否 -（过滤条件）按UID/GID过滤。
        :type Filters: list of Filter
        :param Offset: Offset 分页码
        :type Offset: int
        :param Limit: Limit 页面大小
        :type Limit: int
        """
        self.FileSystemId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserQuotaResponse(AbstractModel):
    """DescribeUserQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: UserQuota条目总数
        :type TotalCount: int
        :param UserQuotaInfo: UserQuota条目
        :type UserQuotaInfo: list of UserQuota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserQuotaInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserQuotaInfo") is not None:
            self.UserQuotaInfo = []
            for item in params.get("UserQuotaInfo"):
                obj = UserQuota()
                obj._deserialize(item)
                self.UserQuotaInfo.append(obj)
        self.RequestId = params.get("RequestId")


class FileSystemByPolicy(AbstractModel):
    """绑定快照策略的文件系统信息

    """

    def __init__(self):
        r"""
        :param CreationToken: 文件系统名称
        :type CreationToken: str
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param SizeByte: 文件系统大小
        :type SizeByte: int
        :param StorageType: 存储类型
        :type StorageType: str
        :param TotalSnapshotSize: 快照总大小
        :type TotalSnapshotSize: int
        :param CreationTime: 文件系统创建时间
        :type CreationTime: str
        :param ZoneId: 文件系统所在区ID
        :type ZoneId: int
        """
        self.CreationToken = None
        self.FileSystemId = None
        self.SizeByte = None
        self.StorageType = None
        self.TotalSnapshotSize = None
        self.CreationTime = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.SizeByte = params.get("SizeByte")
        self.StorageType = params.get("StorageType")
        self.TotalSnapshotSize = params.get("TotalSnapshotSize")
        self.CreationTime = params.get("CreationTime")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemClient(AbstractModel):
    """文件系统客户端信息

    """

    def __init__(self):
        r"""
        :param CfsVip: 文件系统IP地址
        :type CfsVip: str
        :param ClientIp: 客户端IP地址
        :type ClientIp: str
        :param VpcId: 文件系统所属VPCID
        :type VpcId: str
        :param Zone: 可用区名称，例如ap-beijing-1，请参考 概览文档中的地域与可用区列表
        :type Zone: str
        :param ZoneName: 可用区中文名称
        :type ZoneName: str
        :param MountDirectory: 该文件系统被挂载到客户端上的路径信息
        :type MountDirectory: str
        """
        self.CfsVip = None
        self.ClientIp = None
        self.VpcId = None
        self.Zone = None
        self.ZoneName = None
        self.MountDirectory = None


    def _deserialize(self, params):
        self.CfsVip = params.get("CfsVip")
        self.ClientIp = params.get("ClientIp")
        self.VpcId = params.get("VpcId")
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.MountDirectory = params.get("MountDirectory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemInfo(AbstractModel):
    """文件系统基本信息

    """

    def __init__(self):
        r"""
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param CreationToken: 用户自定义名称
        :type CreationToken: str
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param LifeCycleState: 文件系统状态
        :type LifeCycleState: str
        :param SizeByte: 文件系统已使用容量
        :type SizeByte: int
        :param SizeLimit: 文件系统最大空间限制
        :type SizeLimit: int
        :param ZoneId: 区域 ID
        :type ZoneId: int
        :param Zone: 区域名称
        :type Zone: str
        :param Protocol: 文件系统协议类型
        :type Protocol: str
        :param StorageType: 文件系统存储类型
        :type StorageType: str
        :param StorageResourcePkg: 文件系统绑定的预付费存储包
        :type StorageResourcePkg: str
        :param BandwidthResourcePkg: 文件系统绑定的预付费带宽包（暂未支持）
        :type BandwidthResourcePkg: str
        :param PGroup: 文件系统绑定权限组信息
        :type PGroup: :class:`tencentcloud.cfs.v20190719.models.PGroup`
        :param FsName: 用户自定义名称
        :type FsName: str
        :param Encrypted: 文件系统是否加密
        :type Encrypted: bool
        :param KmsKeyId: 加密所使用的密钥，可以为密钥的 ID 或者 ARN
        :type KmsKeyId: str
        :param AppId: 应用ID
        :type AppId: int
        :param BandwidthLimit: 文件系统吞吐上限，吞吐上限是根据文件系统当前已使用存储量、绑定的存储资源包以及吞吐资源包一同确定
        :type BandwidthLimit: float
        :param Capacity: 文件系统总容量
        :type Capacity: int
        :param Tags: 文件系统标签列表
        :type Tags: list of TagInfo
        """
        self.CreationTime = None
        self.CreationToken = None
        self.FileSystemId = None
        self.LifeCycleState = None
        self.SizeByte = None
        self.SizeLimit = None
        self.ZoneId = None
        self.Zone = None
        self.Protocol = None
        self.StorageType = None
        self.StorageResourcePkg = None
        self.BandwidthResourcePkg = None
        self.PGroup = None
        self.FsName = None
        self.Encrypted = None
        self.KmsKeyId = None
        self.AppId = None
        self.BandwidthLimit = None
        self.Capacity = None
        self.Tags = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.LifeCycleState = params.get("LifeCycleState")
        self.SizeByte = params.get("SizeByte")
        self.SizeLimit = params.get("SizeLimit")
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        self.StorageResourcePkg = params.get("StorageResourcePkg")
        self.BandwidthResourcePkg = params.get("BandwidthResourcePkg")
        if params.get("PGroup") is not None:
            self.PGroup = PGroup()
            self.PGroup._deserialize(params.get("PGroup"))
        self.FsName = params.get("FsName")
        self.Encrypted = params.get("Encrypted")
        self.KmsKeyId = params.get("KmsKeyId")
        self.AppId = params.get("AppId")
        self.BandwidthLimit = params.get("BandwidthLimit")
        self.Capacity = params.get("Capacity")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """条件过滤

    """

    def __init__(self):
        r"""
        :param Values: 值
        :type Values: list of str
        :param Name: 名称
        :type Name: str
        """
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        self.Values = params.get("Values")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MountInfo(AbstractModel):
    """挂载点信息

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param MountTargetId: 挂载点 ID
        :type MountTargetId: str
        :param IpAddress: 挂载点 IP
        :type IpAddress: str
        :param FSID: 挂载根目录
        :type FSID: str
        :param LifeCycleState: 挂载点状态
        :type LifeCycleState: str
        :param NetworkInterface: 网络类型
        :type NetworkInterface: str
        :param VpcId: 私有网络 ID
        :type VpcId: str
        :param VpcName: 私有网络名称
        :type VpcName: str
        :param SubnetId: 子网 Id
        :type SubnetId: str
        :param SubnetName: 子网名称
        :type SubnetName: str
        :param CcnID: CFS Turbo使用的云联网ID
        :type CcnID: str
        :param CidrBlock: 云联网中CFS Turbo使用的网段
        :type CidrBlock: str
        """
        self.FileSystemId = None
        self.MountTargetId = None
        self.IpAddress = None
        self.FSID = None
        self.LifeCycleState = None
        self.NetworkInterface = None
        self.VpcId = None
        self.VpcName = None
        self.SubnetId = None
        self.SubnetName = None
        self.CcnID = None
        self.CidrBlock = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.MountTargetId = params.get("MountTargetId")
        self.IpAddress = params.get("IpAddress")
        self.FSID = params.get("FSID")
        self.LifeCycleState = params.get("LifeCycleState")
        self.NetworkInterface = params.get("NetworkInterface")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CcnID = params.get("CcnID")
        self.CidrBlock = params.get("CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroup(AbstractModel):
    """文件系统绑定权限组信息

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组ID
        :type PGroupId: str
        :param Name: 权限组名称
        :type Name: str
        """
        self.PGroupId = None
        self.Name = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroupInfo(AbstractModel):
    """权限组数组

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组ID
        :type PGroupId: str
        :param Name: 权限组名称
        :type Name: str
        :param DescInfo: 描述信息
        :type DescInfo: str
        :param CDate: 创建时间
        :type CDate: str
        :param BindCfsNum: 关联文件系统个数
        :type BindCfsNum: int
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.CDate = None
        self.BindCfsNum = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.CDate = params.get("CDate")
        self.BindCfsNum = params.get("BindCfsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroupRuleInfo(AbstractModel):
    """权限组规则列表

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param AuthClientIp: 允许访问的客户端IP
        :type AuthClientIp: str
        :param RWPermission: 读写权限, ro为只读，rw为读写
        :type RWPermission: str
        :param UserPermission: 用户权限。其中all_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash为将来访的root用户映射为匿名用户或用户组；no_root_squash为来访的root用户保持root帐号权限。
        :type UserPermission: str
        :param Priority: 规则优先级，1-100。 其中 1 为最高，100为最低
        :type Priority: int
        """
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetUserQuotaRequest(AbstractModel):
    """SetUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param UserType: 指定配额类型，包括Uid、Gid
        :type UserType: str
        :param UserId: UID/GID信息
        :type UserId: str
        :param CapacityHardLimit: 容量硬限制，单位GiB
        :type CapacityHardLimit: int
        :param FileHardLimit: 文件硬限制，单位个
        :type FileHardLimit: int
        """
        self.FileSystemId = None
        self.UserType = None
        self.UserId = None
        self.CapacityHardLimit = None
        self.FileHardLimit = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.UserType = params.get("UserType")
        self.UserId = params.get("UserId")
        self.CapacityHardLimit = params.get("CapacityHardLimit")
        self.FileHardLimit = params.get("FileHardLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetUserQuotaResponse(AbstractModel):
    """SetUserQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignUpCfsServiceRequest(AbstractModel):
    """SignUpCfsService请求参数结构体

    """


class SignUpCfsServiceResponse(AbstractModel):
    """SignUpCfsService返回参数结构体

    """

    def __init__(self):
        r"""
        :param CfsServiceStatus: 该用户当前 CFS 服务的状态，creating 是开通中，created 是已开通
        :type CfsServiceStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CfsServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfsServiceStatus = params.get("CfsServiceStatus")
        self.RequestId = params.get("RequestId")


class SnapshotInfo(AbstractModel):
    """快照信息

    """

    def __init__(self):
        r"""
        :param CreationTime: 创建快照时间
        :type CreationTime: str
        :param SnapshotName: 快照名称
        :type SnapshotName: str
        :param SnapshotId: 快照ID
        :type SnapshotId: str
        :param Status: 快照状态
        :type Status: str
        :param RegionName: 地域名称
        :type RegionName: str
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param Size: 快照大小
        :type Size: int
        :param AliveDay: 保留时长天
        :type AliveDay: int
        :param Percent: 快照进度
        :type Percent: int
        :param AppId: 帐号ID
        :type AppId: int
        :param DeleteTime: 快照删除时间
        :type DeleteTime: str
        :param FsName: 文件系统名称
        :type FsName: str
        :param Tags: 快照标签
        :type Tags: list of TagInfo
        """
        self.CreationTime = None
        self.SnapshotName = None
        self.SnapshotId = None
        self.Status = None
        self.RegionName = None
        self.FileSystemId = None
        self.Size = None
        self.AliveDay = None
        self.Percent = None
        self.AppId = None
        self.DeleteTime = None
        self.FsName = None
        self.Tags = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.SnapshotName = params.get("SnapshotName")
        self.SnapshotId = params.get("SnapshotId")
        self.Status = params.get("Status")
        self.RegionName = params.get("RegionName")
        self.FileSystemId = params.get("FileSystemId")
        self.Size = params.get("Size")
        self.AliveDay = params.get("AliveDay")
        self.Percent = params.get("Percent")
        self.AppId = params.get("AppId")
        self.DeleteTime = params.get("DeleteTime")
        self.FsName = params.get("FsName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotOperateLog(AbstractModel):
    """快照操作日志

    """

    def __init__(self):
        r"""
        :param Action: 操作类型
        :type Action: str
        :param ActionTime: 操作时间
        :type ActionTime: str
        :param ActionName: 操作名称
        :type ActionName: str
        :param Operator: 操作者
        :type Operator: str
        :param Result: 结果
        :type Result: int
        """
        self.Action = None
        self.ActionTime = None
        self.ActionName = None
        self.Operator = None
        self.Result = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.ActionTime = params.get("ActionTime")
        self.ActionName = params.get("ActionName")
        self.Operator = params.get("Operator")
        self.Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotStatistics(AbstractModel):
    """文件系统快照统计

    """

    def __init__(self):
        r"""
        :param Region: 地域
        :type Region: str
        :param SnapshotNumber: 快照总个数
        :type SnapshotNumber: int
        :param SnapshotSize: 快照总容量
        :type SnapshotSize: int
        """
        self.Region = None
        self.SnapshotNumber = None
        self.SnapshotSize = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.SnapshotNumber = params.get("SnapshotNumber")
        self.SnapshotSize = params.get("SnapshotSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Tag信息单元

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    """UnbindAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemIds: 需要解绑的文件系统ID列表，用"," 分割
        :type FileSystemIds: str
        :param AutoSnapshotPolicyId: 解绑的快照ID
        :type AutoSnapshotPolicyId: str
        """
        self.FileSystemIds = None
        self.AutoSnapshotPolicyId = None


    def _deserialize(self, params):
        self.FileSystemIds = params.get("FileSystemIds")
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyResponse(AbstractModel):
    """UnbindAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoSnapshotPolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.RequestId = params.get("RequestId")


class UpdateAutoSnapshotPolicyRequest(AbstractModel):
    """UpdateAutoSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param PolicyName: 快照策略名称
        :type PolicyName: str
        :param DayOfWeek: 快照定期备份在一星期哪一天
        :type DayOfWeek: str
        :param Hour: 快照定期备份在一天的哪一小时
        :type Hour: str
        :param AliveDays: 快照保留日期
        :type AliveDays: int
        :param IsActivated: 是否激活定期快照功能
        :type IsActivated: int
        """
        self.AutoSnapshotPolicyId = None
        self.PolicyName = None
        self.DayOfWeek = None
        self.Hour = None
        self.AliveDays = None
        self.IsActivated = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.PolicyName = params.get("PolicyName")
        self.DayOfWeek = params.get("DayOfWeek")
        self.Hour = params.get("Hour")
        self.AliveDays = params.get("AliveDays")
        self.IsActivated = params.get("IsActivated")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAutoSnapshotPolicyResponse(AbstractModel):
    """UpdateAutoSnapshotPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: 快照策略ID
        :type AutoSnapshotPolicyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoSnapshotPolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.RequestId = params.get("RequestId")


class UpdateCfsFileSystemNameRequest(AbstractModel):
    """UpdateCfsFileSystemName请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param FsName: 用户自定义文件系统名称
        :type FsName: str
        """
        self.FileSystemId = None
        self.FsName = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.FsName = params.get("FsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemNameResponse(AbstractModel):
    """UpdateCfsFileSystemName返回参数结构体

    """

    def __init__(self):
        r"""
        :param CreationToken: 用户自定义文件系统名称
        :type CreationToken: str
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param FsName: 用户自定义文件系统名称
        :type FsName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CreationToken = None
        self.FileSystemId = None
        self.FsName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.FsName = params.get("FsName")
        self.RequestId = params.get("RequestId")


class UpdateCfsFileSystemPGroupRequest(AbstractModel):
    """UpdateCfsFileSystemPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        """
        self.PGroupId = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemPGroupResponse(AbstractModel):
    """UpdateCfsFileSystemPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.FileSystemId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.FileSystemId = params.get("FileSystemId")
        self.RequestId = params.get("RequestId")


class UpdateCfsFileSystemSizeLimitRequest(AbstractModel):
    """UpdateCfsFileSystemSizeLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param FsLimit: 文件系统容量限制大小，输入范围0-1073741824, 单位为GB；其中输入值为0时，表示不限制文件系统容量。
        :type FsLimit: int
        :param FileSystemId: 文件系统ID，目前仅支持标准型文件系统。
        :type FileSystemId: str
        """
        self.FsLimit = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FsLimit = params.get("FsLimit")
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemSizeLimitResponse(AbstractModel):
    """UpdateCfsFileSystemSizeLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateCfsPGroupRequest(AbstractModel):
    """UpdateCfsPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param Name: 权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线
        :type Name: str
        :param DescInfo: 权限组描述信息，1-255个字符
        :type DescInfo: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsPGroupResponse(AbstractModel):
    """UpdateCfsPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组ID
        :type PGroupId: str
        :param Name: 权限组名称
        :type Name: str
        :param DescInfo: 描述信息
        :type DescInfo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.RequestId = params.get("RequestId")


class UpdateCfsRuleRequest(AbstractModel):
    """UpdateCfsRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param RuleId: 规则 ID
        :type RuleId: str
        :param AuthClientIp: 可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :type AuthClientIp: str
        :param RWPermission: 读写权限, 值为RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :type RWPermission: str
        :param UserPermission: 用户权限，值为all_squash、no_all_squash、root_squash、no_root_squash。其中all_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash为将来访的root用户映射为匿名用户或用户组；no_root_squash为来访的root用户保持root帐号权限。不填默认为root_squash。
        :type UserPermission: str
        :param Priority: 规则优先级，参数范围1-100。 其中 1 为最高，100为最低
        :type Priority: int
        """
        self.PGroupId = None
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsRuleResponse(AbstractModel):
    """UpdateCfsRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param RuleId: 规则 ID
        :type RuleId: str
        :param AuthClientIp: 允许访问的客户端 IP 或者 IP 段
        :type AuthClientIp: str
        :param RWPermission: 读写权限
        :type RWPermission: str
        :param UserPermission: 用户权限
        :type UserPermission: str
        :param Priority: 优先级
        :type Priority: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")


class UpdateCfsSnapshotAttributeRequest(AbstractModel):
    """UpdateCfsSnapshotAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 文件系统快照ID
        :type SnapshotId: str
        :param SnapshotName: 文件系统快照名称
        :type SnapshotName: str
        :param AliveDays: 文件系统快照保留天数
        :type AliveDays: int
        """
        self.SnapshotId = None
        self.SnapshotName = None
        self.AliveDays = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.SnapshotName = params.get("SnapshotName")
        self.AliveDays = params.get("AliveDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsSnapshotAttributeResponse(AbstractModel):
    """UpdateCfsSnapshotAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 文件系统快照ID
        :type SnapshotId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.RequestId = params.get("RequestId")


class UserQuota(AbstractModel):
    """文件系统配额信息

    """

    def __init__(self):
        r"""
        :param UserType: 指定配额类型，包括Uid、Gid
        :type UserType: str
        :param UserId: UID/GID信息
        :type UserId: str
        :param CapacityHardLimit: 容量硬限制，单位GiB
        :type CapacityHardLimit: int
        :param FileHardLimit: 文件硬限制，单位个
        :type FileHardLimit: int
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self.UserType = None
        self.UserId = None
        self.CapacityHardLimit = None
        self.FileHardLimit = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.UserType = params.get("UserType")
        self.UserId = params.get("UserId")
        self.CapacityHardLimit = params.get("CapacityHardLimit")
        self.FileHardLimit = params.get("FileHardLimit")
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        