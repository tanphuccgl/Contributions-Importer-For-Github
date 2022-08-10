# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("/Users/levi2k/Desktop/imagelocal/wile")
# Your mock repo
mock_repo = git.Repo("/Users/levi2k/Working/Contributions-Importer-For-Github")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['phamnguyentanphucgl@gmail.com', 'tanphuc@cooldev.vn',])
importer.import_repository()
# pip3 install gitpython
# pip3 install pathlib 
# run ✗ python3 run_script.py
