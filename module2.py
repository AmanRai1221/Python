# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello, Everyone in the world i am Aman Rai's build AI Agent")
# engine.runAndWait()


import os

# Get the current working directory
current_directory = os.getcwd()

# List all files and directories in the current directory
contents = os.listdir(current_directory)

# Print the contents
print(f"Contents of the directory '{current_directory}':")
for item in contents:
    print(item)

# Content of Directory
import os

directory_path = '/'
directory_contents = os.listdir(directory_path)

# Print the contents of the specified directory
print(f"Contents of the directory '{directory_path}':")
for item in directory_contents:
    print(item)