# Read a file

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# with open("file.txt") as f:
#     print(f.read())

# 1.
f = open("files-IO/poem.txt")
content = f.read()
f.close()
if("twinkle" in content):
    print("The word twinkle is present in the file")
else:
    print("The word twinkle is not present in the file")