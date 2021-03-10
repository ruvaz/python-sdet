import requests
import json

res = requests.get("http://216.10.245.166/Library/GetBook.php",
                   params={"AuthorName": "Rahul"})
print(res.text)
print(res)  # <Response [200]>
print(type(res))  # <class 'requests.models.Response'>
print(type(res.text))  # <class 'str'>

dic_json = json.loads(res.text)
print(dic_json)
print(dic_json[0])
# {'book_name': 'Learn Appium Automation with Java', 'isbn': 'bcde6334', 'aisle': '227'}
print(dic_json[0]['isbn'])
print(res.status_code)
assert res.status_code == 200

print(res.headers)

assert res.headers['Content-Type'] == 'application/json;charset=UTF-8'
