import json
import os
from configparser import ConfigParser

from github import Github


# read github token from os env
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

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
    print(f'Could not find file {ini_file_name} in the repository')
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

# get version for latest relase
if version.get("release") != latest_release.tag_name:
    if latest_release.prerelease == False:
        if latest_release.draft == False:
            if latest_release.tag_name.startswith("5."):
                if 'rc' not in latest_release.tag_name.lower():
                        print("New release found:", latest_release.tag_name)
                        update = True
                        data = dict()  # write url and tag to json file
                        data["tag"] = latest_release.tag_name
                        data["version"] = latest_release.tag_name
                        data["url"] = latest_release.tarball_url
                        with open("RELEASE.json", "w") as f:
                            json.dump(data, f, indent=4)

# get version for default main branch
if version.get("main") != default_branch.commit.sha:
    print("New main commit available:", default_branch.commit.sha)
    update = True
    data = dict()  # write url and tag to json file
    data["tag"] = "latest"
    data["version"] = default_branch.name
    data["url"] = remote_repo.url + "/tarball/" + default_branch.name
    with open("MAIN.json", "w") as f:
        json.dump(data, f, indent=4)

if update:
    print("Update necessary - New Version(s) found")
    config_object["VERSION"] = {
        "release": remote_repo.get_latest_release().tag_name,
        "main": default_branch.commit.sha,
        "updated_at": remote_repo.updated_at,
        "pushed_at": remote_repo.pushed_at,
    }
    with open(ini_file_name, 'w') as conf:
        config_object.write(conf)
    with open(ini_file_name) as f:
        content = f.read()
    if ini_file_exists:
        # update file in repo
        own_repo.update_file(path=ini_file_name, message=f'Auto Update of {ini_file_name}', content=content, sha=ini_file_contents.sha)
    else:
        # create file if it not exists in repo
        own_repo.create_file(path=ini_file_name, message=f'Auto Creation of {ini_file_name}', content=content)
else:
    print("Update NOT necessary")
