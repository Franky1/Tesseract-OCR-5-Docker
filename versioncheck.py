# only test file

import hashlib
import os
from pathlib import Path

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

print(hashlib.sha256(GITHUB_TOKEN.encode()).hexdigest())

Path("UPDATE_MAIN").touch()
Path("UPDATE_RELEASE").touch()
