# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo -  pwd    
# grammarcheck-release
# obd-ii
# castcar
# CastCarPlay
repo = git.Repo("/Users/levi2k/Working/CastCarPlay")
# Your mock repo
mock_repo = git.Repo("/Users/levi2k/Working/Bitbucket-Contributions")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['phamnguyentanphucgl@gmail.com', 'tanphuc@cooldev.vn','silas.truong.goldenowl@gmail.com','levi.pham.goldenowl@gmail.com'])
importer.import_repository()
# pip3 install gitpython
# pip3 install pathlib 
# run ✗ python3 run_script.py