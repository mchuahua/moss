# Description
The core of this is the MOSS submission script: `moss.pl`. The scripts I provide are hacked up and are almost certain to contain bugs but it worked for my specific/current use-case. You will likely find it easier to write your own parsing scripts.

# Notes
- There is a submission limit of 100/userid/day. 
- Each submission you send should contain at least one particular file of interest (ie. all tetris.c files)
- Another userid you can use is 834099981 (edit this in the perl script). I made two accounts, but it should be unlikely this limit is saturated during normal use
- As long as there is a `Query submitted. Waiting for server's response`, anything afterwards that isn't a html link means their server is down. This includes errors such as `no files uploaded`. Try again the next day, hopefully their server is up again. 

# Example usage:
`perl moss.pl -l c -b base/template_file -d students/*/submission_file`

- `-l c`: language = c. There's a variety of languages supported and you should change it depending on the file language
- `-b base/template_file`: set the filepath for a base file template to reduce false positives
- `-d`: specify to split the reports to individual student directory rather than file
- Everything else afterwards is the file path to file submissions. Wildcard `*` is supported.


# Steps:
- Download submissions off of canvas. For each assignment, there should be a button that downloads all submissions at once into a single zip file.
- Download template off of canvas and unzip into base folder.
- This single zip file extracts into multiple zip files each corresponding to a single student. I extracted this into the students folder
- Unzip each zip file and make sure the folder it extracts to preserves their name/student number, otherwise you won't know who is who
- I did some quick parsing to extract files of interest to each student's folder's top-level. This made it easier for me to switch between files. 
- Call the perl script. 
- A html link is returned. Make sure to save this because it'll get auto deleted in 2 weeks.

# Saving
` wget --recursive --no-clobber --page-requisites \
  --html-extension --convert-links \
  --restrict-file-names=windows \
  --domains moss.stanford.edu \
  --no-parent \
  -e robots=off \
  http://moss.stanford.edu/results/1/XXXXXXXXXX/`
