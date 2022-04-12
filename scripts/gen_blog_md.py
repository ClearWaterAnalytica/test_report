import glob
import os
import time
import s3fs

from auth import *

# git@github.com:ClearWaterAnalytica/oradell_reports.git

lake_name = 'nj_oradell_reservoir'

# Get dates
date = time.strftime("%Y-%m-%d")
abb_date = time.strftime("%b %d, %Y")
shrink_date = time.strftime("%Y%m%d")

# Generate folders
os.system(f"mkdir Figs")
os.system(f"mkdir ../assets/images/{shrink_date}/")

# Download zip and unzip
repo_dir = f"/home/ubuntu/dashboard_{lake_name}"
zip_dir = f"clw-us/{lake_name}/misc/dashboard_zip/{lake_name}_dashboard.zip"
zip_file = zip_dir.split("/")[-1]
zip_folder = zip_dir.split("/")[-1].replace(".zip","")

# Download zip file
s3 = s3fs.S3FileSystem(anon=False, key=AWS_ACCESS_KEY, secret=AWS_SECRET)
s3.download(zip_dir, "/tmp/")
os.system(f"unzip -o /tmp/{zip_file} -d /tmp/")


# Run scripts
import plot_climatology
import plot_hotspots
import plot_nowcast
import plot_weather

# Copy figures to assets folder




# Get previous file index num
last_post = sorted(glob.glob("../_posts/*.md"))[-1]
last_num = int(last_post.split("-")[-1].replace("blog", "").replace(".md", ""))
new_num = str(last_num + 1).zfill(3)

# Copy skel_post.md to _post
os.system(f"cp skel_post.md ../_posts/{date}-blog{new_num}.md")

# Replace dates and folder directories
# Read in the file
with open(f"../_posts/{date}-blog{new_num}.md", 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace("{abb_date}", abb_date)
filedata = filedata.replace("{shrink_date}", shrink_date)

# Write the file out again
with open(f"../_posts/{date}-blog{new_num}.md", 'w') as file:
  file.write(filedata)


with open("test.txt", "w") as w:
  w.write(text)


os.system(f"rm -rfv Figs/")
os.system(f"rm /tmp/{zip_file}")
os.system(f"rm -rfv /tmp/{lake_name}_dashboard")