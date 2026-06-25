import urllib.request
import json

url = "http://localhost:8000/api/book"
data = {
    "name": "Test Client",
    "email": "tchuekrostand@gmail.com",
    "product": "Tchuekam Agent",
    "notes": "Testing integration from products page.",
    "date": "June 25, 2026",
    "time": "10:30 AM"
}

req = urllib.request.Request(
    url, 
    data=json.dumps(data).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req) as response:
        status_code = response.getcode()
        body = response.read().decode('utf-8')
        print(f"Status Code: {status_code}")
        print("Response Body:")
        print(json.dumps(json.loads(body), indent=2))
except Exception as e:
    print(f"Error occurred: {e}")
