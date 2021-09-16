import requests
import base64
import json
import sys


def ToBase64(file):
    with open(file, 'rb') as fileObj:
        data = fileObj.read()
        base64_data = base64.b64encode(data).decode('utf-8')
        return base64_data

# 上传文件
def upload_file(file_name):
    
    token = "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"
    url = "https://api.github.com/repos/wongJG/imgBed/contents/file/"+file_name
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

    # print(data)

    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    re_data = json.loads(req.text)
    
    # print(re_data)
    # print(re_data['content']['sha'])
    print("https://cdn.jsdelivr.net/gh/wongJG/imgBed/file/"+file_name)


if __name__ == '__main__':

    upload_file(sys.argv[1])