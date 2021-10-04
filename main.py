import requests
data = {
    'api_token': '4e67559d640f055fdc9add5c7b68988b',
    'return': 'apple_music,spotify',
}
files = {
    'file': open('test.mp3', 'rb'),
}
result = requests.post('https://api.audd.io/', data=data, files=files)
print(result.text)