#!/usr/bin/python3
import requests
import time
r = requests.session()
def falah():
   
   url = "https://zefoy.com/c2VuZC9mb2xsb3dlcnNfdGlrdG9V"
   payload = """



------WebKitFormBoundaryFOCX5zUap5r4lH74
Content-Disposition: form-data; name="343f6ac9eae3b523"

https://www.tiktok.com/@0xfff0800/video/6998544499710545154?sender_device=mobile&sender_web_id=7029722950002181633&is_from_webapp=v1&is_copy_url=0
------WebKitFormBoundaryFOCX5zUap5r4lH74--



"""
   headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryFOCX5zUap5r4lH74",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Accept": "*/*",
    "Cookie": "PHPSESSID=4on3qdihuduf2tvct3ru5sl532;",
    "Host": "zefoy.com",
    "Accept-Encoding": "gzip, deflate",
    "Origin":"https://zefoy.com",
    "CF-RAY":"6ad16544ba291786-FRA"
	
}
      

   response = r.post(url, data=payload , headers=headers).text
   print("ok تكرار العملية بعد 5 دقائق ")
   print("-"*15)


while True:
 start = falah()
 time.sleep(300)
