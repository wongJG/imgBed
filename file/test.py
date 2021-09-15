import requests
import base64
import json

import sys


# Encode the file to base64 coding
def ToBase64(file):
    with open(file, 'rb') as fileObj:
        data = fileObj.read()
        base64_data = base64.b64encode(data).decode('utf-8')
        return base64_data

# upload
def upload_file(file_name):
    
    token = "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"
    url = "https://api.github.com/repos/wongjg/imgBed/contents/file/"+file_name
    headers = {"Authorization": "token " + token}
    
    content = ToBase64(file_name)
    
    data = {
        "message": "message",
        "committer": {
            "name": "wongJG",
            "email": "jerome20132@hotmail.com"
        },
        "content": content
    }

    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    re_data = json.loads(req.text)

    # print(re_data)
    # print(re_data['content']['sha'])
    print("https://cdn.jsdelivr.net/gh/wongjg/imgBed/file/"+file_name)
    # 在国内默认的down_url可能会无法访问，因此使用CDN访问


if __name__ == '__main__':

    upload_file(sys.argv[0])