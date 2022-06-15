# ## 
# ## not done codes are coreect files not showing

def readFile(filename):
    try:
        with open(filename, "r"): as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile(pr44_1.txt)
readFile(pr45_2.txt)
readFile(pr46_3.txt)
