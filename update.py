import urllib.request
import os
from zipfile import ZipFile
import shutil

with urllib.request.urlopen("https://github.com/finnaminope/Python-RAT-ScriptsAndPlugins/archive/refs/heads/beta.zip") as upd:
    with open("upd.zip", "wb+") as f:
        f.write(upd.read())

# loading the temp.zip and creating a zip object
with ZipFile("upd.zip", 'r') as zObject:

	# Extracting specific file in the zip
	# into a specific location.
	zObject.extractall(
            path="./upd")
zObject.close()

for file_name in os.listdir("./upd/Python-RAT-ScriptsAndPlugins-beta"):
    # construct full file path
    source = "./upd/Python-RAT-ScriptsAndPlugins-beta" + file_name
    destination = "./" + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
