from PyInstaller.utils.hooks import collect_data_files

hiddenimports = ['gi._gobject']

datas = collect_data_files('gi')

print("gi girdi")
