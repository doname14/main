import requests
import json

def test_langflow():
    url = "http://localhost:7860/api/v1/run"
    headers = {"Content-Type": "application/json"}
    data = {"input": "Hello, how are you?"}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_langflow() 