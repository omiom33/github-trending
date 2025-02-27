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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.dcdb.v20180411 import models


class DcdbClient(AbstractClient):
    _apiVersion = '2018-04-11'
    _endpoint = 'dcdb.tencentcloudapi.com'
    _service = 'dcdb'


    def ActiveHourDCDBInstance(self, request):
        """解隔离DCDB后付费实例

        :param request: Request instance for ActiveHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ActiveHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ActiveHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActiveHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ActiveHourDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateSecurityGroups(self, request):
        """本接口 (AssociateSecurityGroups) 用于安全组批量绑定云资源。

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelDcnJob(self, request):
        """取消DCN同步

        :param request: Request instance for CancelDcnJob.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CancelDcnJobRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CancelDcnJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelDcnJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelDcnJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloneAccount(self, request):
        """本接口（CloneAccount）用于克隆实例账户。

        :param request: Request instance for CloneAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneAccount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloneAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseDBExtranetAccess(self, request):
        """本接口(CloseDBExtranetAccess)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问，查询实例列表接口将不返回对应实例的外网域名和端口信息。

        :param request: Request instance for CloseDBExtranetAccess.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseDBExtranetAccessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CopyAccountPrivileges(self, request):
        """本接口（CopyAccountPrivileges）用于复制云数据库账号的权限。
        注意：相同用户名，不同Host是不同的账号，Readonly属性相同的账号之间才能复制权限。

        :param request: Request instance for CopyAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyAccountPrivilegesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAccount(self, request):
        """本接口（CreateAccount）用于创建云数据库账号。一个实例可以创建多个不同的账号，相同的用户名+不同的host是不同的账号。

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDCDBInstance(self, request):
        """本接口（CreateDCDBInstance）用于创建包年包月的云数据库实例，可通过传入实例规格、数据库版本号、购买时长等信息创建云数据库实例。

        :param request: Request instance for CreateDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDCDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHourDCDBInstance(self, request):
        """创建DCDB后付费实例

        :param request: Request instance for CreateHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHourDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAccount(self, request):
        """本接口（DeleteAccount）用于删除云数据库账号。用户名+host唯一确定一个账号。

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccountPrivileges(self, request):
        """本接口（DescribeAccountPrivileges）用于查询云数据库账号权限。
        注意：注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountPrivilegesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccounts(self, request):
        """本接口（DescribeAccounts）用于查询指定云数据库实例的账号列表。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBLogFiles(self, request):
        """本接口(DescribeDBLogFiles)用于获取数据库的各种日志列表，包括冷备、binlog、errlog和slowlog。

        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBLogFiles", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBLogFilesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBParameters(self, request):
        """本接口(DescribeDBParameters)用于获取数据库的当前参数设置。

        :param request: Request instance for DescribeDBParameters.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBParameters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBParametersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBSecurityGroups(self, request):
        """本接口（DescribeDBSecurityGroups）用于查询实例安全组信息

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBSlowLogs(self, request):
        """本接口(DescribeDBSlowLogs)用于查询慢查询日志列表。

        :param request: Request instance for DescribeDBSlowLogs.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSlowLogsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSlowLogs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSlowLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBSyncMode(self, request):
        """本接口（DescribeDBSyncMode）用于查询云数据库实例的同步模式。

        :param request: Request instance for DescribeDBSyncMode.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSyncMode", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSyncModeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBInstanceNodeInfo(self, request):
        """本接口（DescribeDCDBInstanceNodeInfo）用于获取实例节点信息

        :param request: Request instance for DescribeDCDBInstanceNodeInfo.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBInstanceNodeInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBInstances(self, request):
        """查询云数据库实例列表，支持通过项目ID、实例ID、内网地址、实例名称等来筛选实例。
        如果不指定任何筛选条件，则默认返回10条实例记录，单次请求最多支持返回100条实例记录。

        :param request: Request instance for DescribeDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBPrice(self, request):
        """本接口（DescribeDCDBPrice）用于在购买实例前，查询实例的价格。

        :param request: Request instance for DescribeDCDBPrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBPrice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBPriceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBRenewalPrice(self, request):
        """本接口（DescribeDCDBRenewalPrice）用于在续费分布式数据库实例时，查询续费的价格。

        :param request: Request instance for DescribeDCDBRenewalPrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBRenewalPriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBRenewalPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBRenewalPrice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBRenewalPriceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBSaleInfo(self, request):
        """本接口(DescribeDCDBSaleInfo)用于查询分布式数据库可售卖的地域和可用区信息。

        :param request: Request instance for DescribeDCDBSaleInfo.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBSaleInfoRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBSaleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBSaleInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBSaleInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBShards(self, request):
        """本接口（DescribeDCDBShards）用于查询云数据库实例的分片信息。

        :param request: Request instance for DescribeDCDBShards.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBShards", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBShardsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBUpgradePrice(self, request):
        """本接口（DescribeDCDBUpgradePrice）用于查询变配分布式数据库实例价格。

        :param request: Request instance for DescribeDCDBUpgradePrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBUpgradePriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBUpgradePriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBUpgradePrice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBUpgradePriceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabaseObjects(self, request):
        """本接口（DescribeDatabaseObjects）用于查询云数据库实例的数据库中的对象列表，包含表、存储过程、视图和函数。

        :param request: Request instance for DescribeDatabaseObjects.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseObjects", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseObjectsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabaseTable(self, request):
        """本接口（DescribeDatabaseTable）用于查询云数据库实例的表信息。

        :param request: Request instance for DescribeDatabaseTable.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseTable", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseTableResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabases(self, request):
        """本接口（DescribeDatabases）用于查询云数据库实例的数据库列表。

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabases", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabasesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDcnDetail(self, request):
        """获取实例灾备详情

        :param request: Request instance for DescribeDcnDetail.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDcnDetailRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDcnDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDcnDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDcnDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFileDownloadUrl(self, request):
        """本接口(DescribeFileDownloadUrl)用于获取数据库指定备份或日志文件的下载连接。

        :param request: Request instance for DescribeFileDownloadUrl.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeFileDownloadUrlRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeFileDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileDownloadUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileDownloadUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlow(self, request):
        """本接口（DescribeFlow）用于查询流程状态

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlow", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOrders(self, request):
        """本接口（DescribeOrders）用于查询分布式数据库订单信息。传入订单ID来查询订单关联的分布式数据库实例，和对应的任务流程ID。

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrders", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrdersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjectSecurityGroups(self, request):
        """本接口（DescribeProjectSecurityGroups）用于查询项目安全组信息

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjects(self, request):
        """本接口（DescribeProjects）用于查询项目列表

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeShardSpec(self, request):
        """查询可创建的分布式数据库可售卖的分片规格配置。

        :param request: Request instance for DescribeShardSpec.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeShardSpecRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeShardSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShardSpec", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShardSpecResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSqlLogs(self, request):
        """本接口（DescribeSqlLogs）用于获取实例SQL日志。

        :param request: Request instance for DescribeSqlLogs.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeSqlLogsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeSqlLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSqlLogs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSqlLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserTasks(self, request):
        """本接口（DescribeUserTasks）用于拉取用户任务列表

        :param request: Request instance for DescribeUserTasks.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeUserTasksRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeUserTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyDCDBInstance(self, request):
        """本接口(DestroyDCDBInstance)用于销毁已隔离的包年包月实例。

        :param request: Request instance for DestroyDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DestroyDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DestroyDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyDCDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyHourDCDBInstance(self, request):
        """本接口（DestroyHourDCDBInstance）用于销毁按量计费实例。

        :param request: Request instance for DestroyHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DestroyHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DestroyHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyHourDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateSecurityGroups(self, request):
        """本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FlushBinlog(self, request):
        """相当于在所有分片的mysqld中执行flush logs，完成切分的binlog将展示在各个分片控制台binlog列表里。

        :param request: Request instance for FlushBinlog.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.FlushBinlogRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.FlushBinlogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FlushBinlog", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FlushBinlogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GrantAccountPrivileges(self, request):
        """本接口（GrantAccountPrivileges）用于给云数据库账号赋权。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for GrantAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GrantAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GrantAccountPrivilegesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InitDCDBInstances(self, request):
        """本接口(InitDCDBInstances)用于初始化云数据库实例，包括设置默认字符集、表名大小写敏感等。

        :param request: Request instance for InitDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitDCDBInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDCDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateDedicatedDBInstance(self, request):
        """本接口（IsolateDedicatedDBInstance）用于隔离独享云数据库实例。

        :param request: Request instance for IsolateDedicatedDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.IsolateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.IsolateDedicatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDedicatedDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateDedicatedDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateHourDCDBInstance(self, request):
        """隔离DCDB后付费实例

        :param request: Request instance for IsolateHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.IsolateHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.IsolateHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateHourDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def KillSession(self, request):
        """本接口（KillSession）用于杀死指定会话。

        :param request: Request instance for KillSession.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.KillSessionRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.KillSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillSession", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.KillSessionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccountDescription(self, request):
        """本接口（ModifyAccountDescription）用于修改云数据库账号备注。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountDescription", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountDescriptionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceName(self, request):
        """本接口（ModifyDBInstanceName）用于修改实例名字

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口（ModifyDBInstanceSecurityGroups）用于修改云数据库安全组

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstancesProject(self, request):
        """本接口（ModifyDBInstancesProject）用于修改云数据库实例所属项目。

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstancesProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstancesProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBParameters(self, request):
        """本接口(ModifyDBParameters)用于修改数据库参数。

        :param request: Request instance for ModifyDBParameters.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBParameters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBParametersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBSyncMode(self, request):
        """本接口（ModifyDBSyncMode）用于修改云数据库实例的同步模式。

        :param request: Request instance for ModifyDBSyncMode.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBSyncMode", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBSyncModeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstanceNetwork(self, request):
        """本接口（ModifyInstanceNetwork）用于修改实例所属网络。

        :param request: Request instance for ModifyInstanceNetwork.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceNetworkRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceNetwork", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceNetworkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstanceVip(self, request):
        """本接口（ModifyInstanceVip）用于修改实例Vip

        :param request: Request instance for ModifyInstanceVip.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVipRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceVip", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceVipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstanceVport(self, request):
        """本接口（ModifyInstanceVport）用于修改实例VPORT

        :param request: Request instance for ModifyInstanceVport.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVportRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceVport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceVportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRealServerAccessStrategy(self, request):
        """本接口(ModifyRealServerAccessStrategy)用于修改云数据库的VPCGW到RS的访问策略。

        **注意**
        - 修改策略后只对新建立的连接生效，老连接不受影响
        - 就近访问只针对实例是跨可用区部署有用，单可用区部署实例就近与否并无作用
        - DB每个Node对应一个proxy，如果开启就近访问，将会把连接集中到对应可用区的proxy上，可能造成热点问题，这种情况下如果是线上业务，请务必根据自己的业务请求量测试符合预期后再进行就近策略变更

        :param request: Request instance for ModifyRealServerAccessStrategy.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyRealServerAccessStrategyRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyRealServerAccessStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRealServerAccessStrategy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRealServerAccessStrategyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OpenDBExtranetAccess(self, request):
        """本接口（OpenDBExtranetAccess）用于开通云数据库实例的外网访问。开通外网访问后，您可通过外网域名和端口访问实例，可使用查询实例列表接口获取外网域名和端口信息。

        :param request: Request instance for OpenDBExtranetAccess.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenDBExtranetAccessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewDCDBInstance(self, request):
        """本接口（RenewDCDBInstance）用于续费分布式数据库实例。

        :param request: Request instance for RenewDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.RenewDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.RenewDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDCDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetAccountPassword(self, request):
        """本接口（ResetAccountPassword）用于重置云数据库账号的密码。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAccountPassword", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAccountPasswordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SwitchDBInstanceHA(self, request):
        """本接口(SwitchDBInstanceHA)用于实例主备切换。

        :param request: Request instance for SwitchDBInstanceHA.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.SwitchDBInstanceHARequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.SwitchDBInstanceHAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDBInstanceHA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchDBInstanceHAResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateDedicatedDBInstance(self, request):
        """本接口（TerminateDedicatedDBInstance）用于销毁已隔离的独享分布式数据库实例。

        :param request: Request instance for TerminateDedicatedDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.TerminateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.TerminateDedicatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDedicatedDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateDedicatedDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeDCDBInstance(self, request):
        """本接口（UpgradeDCDBInstance）用于升级分布式数据库实例。本接口完成下单和支付两个动作，如果发生支付失败的错误，调用用户账户相关接口中的支付订单接口（PayDeals）重新支付即可。

        :param request: Request instance for UpgradeDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDCDBInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)