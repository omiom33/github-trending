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
from tencentcloud.irp.v20220805 import models


class IrpClient(AbstractClient):
    _apiVersion = '2022-08-05'
    _endpoint = 'irp.tencentcloudapi.com'
    _service = 'irp'


    def FeedRecommend(self, request):
        """获取信息流推荐结果

        :param request: Request instance for FeedRecommend.
        :type request: :class:`tencentcloud.irp.v20220805.models.FeedRecommendRequest`
        :rtype: :class:`tencentcloud.irp.v20220805.models.FeedRecommendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FeedRecommend", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FeedRecommendResponse()
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


    def ReportFeedBehavior(self, request):
        """上报信息流场景内的行为数据，随着数据的积累，模型的效果会逐渐稳定。

        :param request: Request instance for ReportFeedBehavior.
        :type request: :class:`tencentcloud.irp.v20220805.models.ReportFeedBehaviorRequest`
        :rtype: :class:`tencentcloud.irp.v20220805.models.ReportFeedBehaviorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportFeedBehavior", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReportFeedBehaviorResponse()
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


    def ReportFeedItem(self, request):
        """上报被用于推荐的信息流内容信息

        :param request: Request instance for ReportFeedItem.
        :type request: :class:`tencentcloud.irp.v20220805.models.ReportFeedItemRequest`
        :rtype: :class:`tencentcloud.irp.v20220805.models.ReportFeedItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportFeedItem", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReportFeedItemResponse()
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


    def ReportFeedUser(self, request):
        """上报信息流用户信息，请务必确认用户的唯一性，并在请求推荐结果时指定用户的唯一标识信息（UserId），否则将无法进行千人千面的推荐

        :param request: Request instance for ReportFeedUser.
        :type request: :class:`tencentcloud.irp.v20220805.models.ReportFeedUserRequest`
        :rtype: :class:`tencentcloud.irp.v20220805.models.ReportFeedUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportFeedUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReportFeedUserResponse()
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