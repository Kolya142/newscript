@echo off
pyinstaller --noconfirm --onefile --console  "C:/Users/nicks/PycharmProjects/new-script/ns.py"
pyinstaller --noconfirm --onefile --console "C:/Users/nicks/PycharmProjects/new-script/nsload.py"
copy dist\* .