from datetime import datetime
print("python artifact demo")

with open("result.txt", "w") as file:
    file.write("hello from GitHub\n")
    file.write("this file is created in GitHub\n")
    file.write(f"Genaretd Time:{datetime.now()}\n")

print ("result.txt file is created successfully")