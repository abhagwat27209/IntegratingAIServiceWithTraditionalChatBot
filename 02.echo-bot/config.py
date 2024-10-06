#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    # Set ENDPOINT_URI and API_KEY directly here
    ENDPOINT_URI = "https://t6languageservice27209.cognitiveservices.azure.com/"
    API_KEY = "2f1a5878f879405d9f3d1185592ae89d"

    # Fallback to environment variables if not set above
    ENDPOINT_URI = ENDPOINT_URI or os.environ.get("MicrosoftAIServiceEndpoint", "")
    API_KEY = API_KEY or os.environ.get("MicrosoftAPIKey", "")

    if ENDPOINT_URI and API_KEY:
        text_analytics_client = TextAnalyticsClient(endpoint=ENDPOINT_URI, credential=AzureKeyCredential(API_KEY))
        print(f"TextAnalyticsClient initialized with ENDPOINT_URI = {ENDPOINT_URI}")
    else:
        print("Error: ENDPOINT_URI or API_KEY is not set")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId", "")
