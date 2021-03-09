import requests

req = requests.get("http://216.10.245.166/Library/GetBook.php",
                   params={"AuthorName": "Ruben Gadi"})
print(req.content)


