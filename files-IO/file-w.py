st = "Hello everyone welcome in IIT Delhi Webinar,First of all How are you all"
f = open("files-IO/myfile.txt", "w")
f.write(st)
f.close()

# Q4. Replace a word with # in a file
word = "Donkey"
with open("files-IO/file.txt", "r") as f:
    content = f.read()
    contentNew = content.replace(word, "#####")

with open("files-IO/file.txt", "w") as f:
    f.write(contentNew)

# Q5. Replace multiple words with # in a file
words = ["Donkey", "Mango", "Apple"]
with open("files-IO/file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("files-IO/file.txt", "w") as f:
    f.write(content)

# To wipe the file, you can use the following code:
# with open("file.txt", "w") as f:
#     f.write("")