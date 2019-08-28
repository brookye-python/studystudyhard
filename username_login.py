import re
import os
import json
import requests
# https://github.com/pig6/login_taobao/commit/52f462cda6cc0ca50830773d585f2625519d665c#diff-39316d8793d0ddb286229f8667b9f78dR40


s = requests.Session()
#cookies序列化文件
COOKIES_FILE_PATH = 'taobao_login_cookies.txt'

class UsernameLogin: