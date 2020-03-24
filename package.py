#!/usr/bin/env python3

import json
from zipfile import ZipFile

modFiles = [
	"info.json",
	"changelog.txt",
	"thumbnail.png",

	"data-updates.lua",
]

with open("info.json") as file:
	modInfo = json.load(file)

zipName = "{}_{}".format(modInfo["name"], modInfo["version"])

with ZipFile("{}.zip".format(zipName), 'w') as modZip:
	for file in modFiles:
		modZip.write(file, arcname="{}/{}".format(zipName, file))
