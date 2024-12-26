import os, re

def search_file(file):
    f = open(file, "r")
    contents = f.read()
    pattern = r"(\d{3})-(\d{3})-(\d{4})"
    re.search(pattern, contents)
    if re.search(pattern, contents) != None:
        print(re.search(pattern, contents).group())

for folder, subfolders, files in os.walk(".\\extracted_content"):
    for file in files:
        full_path = folder+"\\"+file
        search_file(full_path)