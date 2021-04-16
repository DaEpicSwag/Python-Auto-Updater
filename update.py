import os
try:
  import requests
 except:
  os.system("pip install requests")
from zipfile import ZipFile
import time
try:
  import progressbar
except:
  os.system("pip install progressbar2")

print("Downloading Latest Release...")
with progressbar.ProgressBar(max_value=10) as bar:
    for i in range(10):
        time.sleep(2)
        bar.update(i)

url = 'http://software2life.com/zip/sonicFTP/update.zip'


r = requests.get(url, stream=True)
handle = open("update.zip", "wb")
for chunk in r.iter_content(chunk_size=512):
    if chunk:  # filter out keep-alive new chunks
        handle.write(chunk)
handle.close()
os.system("del main.py")
with ZipFile('update.zip', 'r') as zipObj:
   zipObj.extractall('')
   
os.system("del update.zip")
print("Successfully updated to the newest build!")
