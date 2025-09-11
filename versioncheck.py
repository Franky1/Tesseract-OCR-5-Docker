"""
Check upstream tesseract-ocr/tesseract for new default-branch commits or
stable 5.x releases, write MAIN.json/RELEASE.json, and update/commit VERSION.ini
in this repo via the GitHub API. Requires a GITHUB_TOKEN in the environment.
"""

import json
import os
from configparser import ConfigParser

from github import Github


# read github token from os env
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# check if token is set
assert GITHUB_TOKEN, "GITHUB_TOKEN could not be loaded from env"

# get github repo object from remote and local repo
g = Github(GITHUB_TOKEN)
remote_repo = g.get_repo("tesseract-ocr/tesseract")
own_repo = g.get_repo("Franky1/Tesseract-OCR-5-Docker")

# Get the configparser object
config_object = ConfigParser()

ini_file_name = "VERSION.ini"
ini_file_exists = False

try:
    ini_file_contents = own_repo.get_contents(ini_file_name)
    decoded_contents = ini_file_contents.decoded_content.decode("utf-8")
except Exception as e:
    print(e)
    print(f"Could not find file {ini_file_name} in the repository")
    ini_file_exists = False
else:
    config_object.read_string(decoded_contents)
    ini_file_exists = True

# check for valid content in ini file
if config_object.has_section("VERSION"):
    version = config_object["VERSION"]
else:
    version = dict()

latest_release = remote_repo.get_latest_release()
default_branch = remote_repo.get_branch(remote_repo.default_branch)

update = False
main_data = dict()
release_data = dict()
main_data["version"] = "None"
release_data["version"] = "None"

# get version for default main branch
if version.get("main") != default_branch.commit.sha:
    print("New main commit available:", default_branch.commit.sha)
    update = True
    main_data["tag"] = "latest"
    main_data["version"] = default_branch.name
    main_data["url"] = remote_repo.url + "/tarball/" + default_branch.name

# get version for latest relase
if version.get("release") != latest_release.tag_name:
    if not latest_release.prerelease:
        if not latest_release.draft:
            if latest_release.tag_name.startswith("5."):
                if "rc" not in latest_release.tag_name.lower():
                    print("New release found:", latest_release.tag_name)
                    update = True
                    release_data["tag"] = latest_release.tag_name
                    release_data["version"] = latest_release.tag_name
                    release_data["url"] = latest_release.tarball_url

with open("MAIN.json", "w", encoding="utf-8") as f:
    json.dump(main_data, f, indent=4)

with open("RELEASE.json", "w", encoding="utf-8") as f:
    json.dump(release_data, f, indent=4)

if update:
    print("Update necessary - New Version(s) found")
    config_object["VERSION"] = {
        "release": remote_repo.get_latest_release().tag_name,
        "main": default_branch.commit.sha,
        "updated_at": remote_repo.updated_at,
        "pushed_at": remote_repo.pushed_at,
    }
    with open(ini_file_name, "w", encoding="utf-8") as conf:
        config_object.write(conf)
    with open(ini_file_name, encoding="utf-8") as f:
        content = f.read()
    if ini_file_exists:
        # update file in repo
        own_repo.update_file(
            path=ini_file_name,
            message=f"Auto Update of {ini_file_name}",
            content=content,
            sha=ini_file_contents.sha,
        )
    else:
        # create file if it not exists in repo
        own_repo.create_file(
            path=ini_file_name,
            message=f"Auto Creation of {ini_file_name}",
            content=content,
        )
else:
    print("Update NOT necessary")
