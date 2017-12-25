import zipfile
zp=zipfile.ZipFile("Armored Advance.musicloop")
print(zp.infolist())
print(zp.getinfo('Part.mid'))
zp.extract("Part.mid")