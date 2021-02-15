import base64

with open('tes.mp3', 'rb') as f:
    a = base64.b64decode(f.read())

with open('tes2.mp3', 'wb') as f:
    f.write(a)
