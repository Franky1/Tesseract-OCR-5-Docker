# only test file

import hashlib
import os

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

print(hashlib.sha256(GITHUB_TOKEN.encode()).hexdigest())
