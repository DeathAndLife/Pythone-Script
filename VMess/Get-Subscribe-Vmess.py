import requests
import sys

url = "http://tool.chacuo.net/cryptaes"

data = {
    "data": requests.get(sys.argv[3]).text,
    "type": "aes",
    "arg": "m=cbc_pad=zero_block=128_p=" + sys.argv[1] + "_i=" + sys.argv[2] + "_o=0_s=utf-8_t=1"
}

response = requests.post(url, data).json().get('data')[0]

print(response)