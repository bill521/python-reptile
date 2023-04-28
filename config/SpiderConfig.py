

class SpiderConfig:

    def __init__(self, cookie, user_agent, folder_path, chrome_path):
        self.cookie = cookie
        self.user_agent = user_agent
        self.folder_path = folder_path
        self.chrome_path = chrome_path

    def default_harder(self):
        self.cookie = 'ttwid=1|vq3bQKabBPIYjLK8bAVvBZEpw_yAphmkeTWiekC1S34|1682081459|cbf97f128722a15fd24d221b87a08f1c3510f327a866a9eaed454eddbfb62a88; passport_csrf_token=eee741fcbc2c0dd239e72a452cc2e96d; passport_csrf_token_default=eee741fcbc2c0dd239e72a452cc2e96d; s_v_web_id=verify_lgqjveur_KOHdkJfY_ErwI_4SKI_8QTk_iUhmE1o58Lv2; ttcid=bc49c1ae9e9b44c6ae68f7f6715d7ba429; n_mh=KgcapNbrq_JKERZw2x5pw2cMWKLjD96_rA-R4G47NPM; sso_uid_tt=e510bda952f0a21b898936e2af7a09e7; sso_uid_tt_ss=e510bda952f0a21b898936e2af7a09e7; toutiao_sso_user=70131ba66a6b5613339a91b28d59692d; toutiao_sso_user_ss=70131ba66a6b5613339a91b28d59692d; passport_auth_status=1c4dceb1c62007fa4fd07a0bc5bb5a46,; passport_auth_status_ss=1c4dceb1c62007fa4fd07a0bc5bb5a46,; uid_tt=2b1db88c612e7fbcef3b13e71ef48b29; uid_tt_ss=2b1db88c612e7fbcef3b13e71ef48b29; sid_tt=ac800cd7b440b3416df3f2d5f17b3690; sessionid=ac800cd7b440b3416df3f2d5f17b3690; sessionid_ss=ac800cd7b440b3416df3f2d5f17b3690; odin_tt=330ba8c9115c82b2781b7a20fc6f3ee3663646d1465cb2373749a7a2d4dc0f00b7b299b5a7bc133caa0ee5bd8e07476a; passport_assist_user=CjyvV1TFpmugmW4QauZdmu03Gd9-7pQJj8p_D9Yt9yWu5B-oU8zQsT8QwOBMdf2L73TqTrC8BvZe_MN5DJoaSAo8BtIThkuvrwP4POZ4s5J3i8cB8DAc766RMnc0XZtC-E0anm9l8TVo0Bcg6zBY8-zPQz4nxw8wa5Bva6uREL6Krw0Yia_WVCIBAzcPm7Y=; sid_ucp_sso_v1=1.0.0-KDI2NWY4ZjczOGFkN2M3MTJhNDYwNzk0YTRiZTBlYjBiNzIwOTQ2YmUKHQjOlvWE5AIQro6KogYY7zEgDDDI_rTVBTgGQPQHGgJsZiIgNzAxMzFiYTY2YTZiNTYxMzMzOWE5MWIyOGQ1OTY5MmQ; ssid_ucp_sso_v1=1.0.0-KDI2NWY4ZjczOGFkN2M3MTJhNDYwNzk0YTRiZTBlYjBiNzIwOTQ2YmUKHQjOlvWE5AIQro6KogYY7zEgDDDI_rTVBTgGQPQHGgJsZiIgNzAxMzFiYTY2YTZiNTYxMzMzOWE5MWIyOGQ1OTY5MmQ; publish_badge_show_info="0,0,0,1682081584341"; LOGIN_STATUS=1; store-region=cn-sh; store-region-src=uid; sid_guard=ac800cd7b440b3416df3f2d5f17b3690|1682081586|5183996|Tue,+20-Jun-2023+12:53:02+GMT; sid_ucp_v1=1.0.0-KDEyNDk4NTUxM2E2MTNhMTBhNGUwZWYzYTRkMTExM2YxOTNjZTE3MzQKGQjOlvWE5AIQso6KogYY7zEgDDgGQPQHSAQaAmxmIiBhYzgwMGNkN2I0NDBiMzQxNmRmM2YyZDVmMTdiMzY5MA; ssid_ucp_v1=1.0.0-KDEyNDk4NTUxM2E2MTNhMTBhNGUwZWYzYTRkMTExM2YxOTNjZTE3MzQKGQjOlvWE5AIQso6KogYY7zEgDDgGQPQHSAQaAmxmIiBhYzgwMGNkN2I0NDBiMzQxNmRmM2YyZDVmMTdiMzY5MA; my_rd=1; pwa2="2|1"; download_guide="3/20230423"; _tea_utm_cache_2018=undefined; douyin.com; strategyABtestKey="1682486448.212"; csrf_session_id=35aa8870cd71fd00d299f6034f4e2f82; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNlcnQiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFLS0tLS1cbk1JSUNGRENDQWJxZ0F3SUJBZ0lVQXN1RVc0YmJSRCtIaklZTkYxZjBTVURvN01Zd0NnWUlLb1pJemowRUF3SXdcbk1URUxNQWtHQTFVRUJoTUNRMDR4SWpBZ0JnTlZCQU1NR1hScFkydGxkRjluZFdGeVpGOWpZVjlsWTJSellWOHlcbk5UWXdIaGNOTWpNd05ESXhNVEkxTXpBeFdoY05Nek13TkRJeE1qQTFNekF4V2pBbk1Rc3dDUVlEVlFRR0V3SkRcblRqRVlNQllHQTFVRUF3d1BZbVJmZEdsamEyVjBYMmQxWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERcbkFRY0RRZ0FFVTV3dndLaGt0aTBkcFlHdWNlTWZXYUpudDVCMFNuUi9yK0F0SHY1TFFGOW1oUHFvWXdNZi9TTWRcbmllMmdPMHYxcDNpQ2dpcUhmcitVU1JrTVppOTJkYU9CdVRDQnRqQU9CZ05WSFE4QkFmOEVCQU1DQmFBd01RWURcblZSMGxCQ293S0FZSUt3WUJCUVVIQXdFR0NDc0dBUVVGQndNQ0JnZ3JCZ0VGQlFjREF3WUlLd1lCQlFVSEF3UXdcbktRWURWUjBPQkNJRUlLcndneEdrR24vUmJQdkRWc0JqVlpsYVJxaWl3Z2Q2QXNrODE4d1lRVEpuTUNzR0ExVWRcbkl3UWtNQ0tBSURLbForcU9aRWdTamN4T1RVQjdjeFNiUjIxVGVxVFJnTmQ1bEpkN0lrZURNQmtHQTFVZEVRUVNcbk1CQ0NEbmQzZHk1a2IzVjVhVzR1WTI5dE1Bb0dDQ3FHU000OUJBTUNBMGdBTUVVQ0lRRHRLNDB5SWhlNzRuU0dcbkFCdlVNU1pQNEkrZ0dDU0NMTks0S1NpbVpuUFBjd0lnUnhUNk1pZUFZT0pJRkRsTEJqdGRyTGV3SmZORTdYV0lcblBzcGtNb3JHV3ZnPVxuLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLVxuIn0=; SEARCH_RESULT_LIST_TYPE="single"; VIDEO_FILTER_MEMO_SELECT={"expireTime":1683092470630,"type":1}; __ac_nonce=06448c16000537ac5e6f7; __ac_signature=_02B4Z6wo00f01bHpEYwAAIDBMevrzfxIdwmxyRUAAAgzSdpp5c-7JJ2m0o6aeGu-OLcYmQxUNeK8Zeg9p0HLCSl2yrF8agU8H9NIvWXS6YF8g5QrMPkJrlynARLBWRt6vw6aKOHpOJXRRShV1d; FOLLOW_LIVE_POINT_INFO="MS4wLjABAAAAqhkqpo3WDmbcqJVSbdlBntVxy1FCt1YSAE9o1EwtrNI/1682524800000/0/0/1682491671076"; FOLLOW_NUMBER_YELLOW_POINT_INFO="MS4wLjABAAAAqhkqpo3WDmbcqJVSbdlBntVxy1FCt1YSAE9o1EwtrNI/1682524800000/0/0/1682492271077"; msToken=1gPfENFkaM9KVdOUU9phx9P_PeDX0NfG_AbRWyclFCdSs6Rx4cd9s8nqdvk-DMLMRp71ppdWC1bFz4qEN0gjAz4o-2DgKjr2g8zrRTuXPwVCo0Owagrki-Jy2TU5ImM=; passport_fe_beating_status=true; home_can_add_dy_2_desktop="1"; msToken=u4dK4l7iq16NMiKyKJDXKnmBhzUZtMCKPCXcZo5DSIxKgzMew714Dm_d1OVpVqMacHH7BuKaoWcDm-JE1V7P0hkVSzFYEpoJKYKxOFNd5OFVLjT0eHeItjcZA8eO4v0=; tt_scid=JkIZTLVzjjPJfsEg1n3qvDruT7kCfreIFnWOSXRxB-8awa4WXzYq3KJO1DfQMxRe4f36'

        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

        self.folder_path = None

        self.chrome_path = None

        return self

    def default_selenium_harder(self):
        self.cookie = "ttwid=1%7CvTO_uJ7LmaveRIOE8nlIwh0MF9NA5UKrFYGNozKNQKM%7C1682424504"
        "%7C182d57cf452d8ec06cebbdfab649f8a7251a58db51307e7c24f07f4314e6e675; home_can_add_dy_2_desktop=%220%22; "
        "strategyABtestKey=%221682424506.261%22; passport_csrf_token=4517be9174294276aef4a0270de60b9d; "
        "passport_csrf_token_default=4517be9174294276aef4a0270de60b9d; "
        "msToken"
        "=XEm0LWG1_Txdm0MaoS3m4O6eELy4jdlcNg943sZbis_0EemVNRJM3nBOOsGXk03pQbP99vEXufu5hUrBhTH5RAzOvdQIJV2h3OvlSnEkXUo=; "
        "__ac_nonce=06447c2cb00b1be795f84; __ac_signature=_02B4Z6wo00f01JB.4VwAAIDAEH0bHpBBnDCQT-XAAEBc4f; "
        "__ac_referer=__ac_blank"

        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

        self.folder_path = None

        self.chrome_path = "exe"

        return self
