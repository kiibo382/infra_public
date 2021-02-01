# import json

# with open("sample.json") as f:
#     # print(f.read())
#     data_dict = json.load(f)

# for i in data_dict["KeyPhrases"]:
#     print(i["Text"])
a = "0123456789"
print(a[:-3])
b = a[5:-4] + "-transcribe.json"
c = b[:-16] + "-comprehend.json"
print(b)
print(c)