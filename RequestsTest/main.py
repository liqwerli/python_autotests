import requests

response = requests.post('https://petstore.swagger.io/v2/pet', json = {
  "id": 700,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "neko",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


response = requests.put('https://petstore.swagger.io/v2/pet', json = {
  "id": 600,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "terry",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


response = requests.get('https://petstore.swagger.io/v2/pet/700')
print(response.text)