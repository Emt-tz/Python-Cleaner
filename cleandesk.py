 
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime

from time import gmtime, strftime

class user:
	def username():
		return os.getlogin()
		
#For linux users this works well:
class FolderCheck:
	def makedirectories():

		direc = f'/home/{user.username()}/Desktop/organized'

		directory = f'/home/{user.username()}/Desktop/organized/'
		for f in os.listdir(f'/home/{user.username()}/Desktop'):
			try:
				os.mkdir(f'/home/{user.username()}/Desktop/organized')
			except:
				pass

		for n in os.listdir(directory):
			try:
				os.mkdir(f'{directory}Media')
				os.mkdir(f'{directory}Other')
				os.mkdir(f'{directory}Programming')
				os.mkdir(f'{directory}Text')
			except:
				pass

		for x in os.listdir(f'{directory}Media'):
			try:
				os.mkdir(f'{directory}Media/Audio')
				os.mkdir(f'{directory}Media/Images')
				os.mkdir(f'{directory}Media/Video')
			except:
				pass

		for y in os.listdir(f'{directory}Other'):
			try:
				os.mkdir(f'{directory}Other/Internet')
				os.mkdir(f'{directory}Other/Uncategorized')
				os.mkdir(f'{directory}Other/Compressed')
				os.mkdir(f'{directory}Other/Disc')
				os.mkdir(f'{directory}Other/Executables')
			except:
				pass

		for i in os.listdir(f'{directory}Programming'):
			try:
				os.mkdir(f'{directory}Programming/C&C++')
				os.mkdir(f'{directory}Programming/Python')
				os.mkdir(f'{directory}Programming/Dart')
				os.mkdir(f'{directory}Programming/Shell')
				os.mkdir(f'{directory}Programming/Java')
				os.mkdir(f'{directory}Programming/Swift')
			except:
				pass

		for j in os.listdir(f'{directory}Text'):
			try:
				os.mkdir(f'{directory}Text/Other')
				os.mkdir(f'{directory}Text/Presentations')
				os.mkdir(f'{directory}Text/PDF')
				os.mkdir(f'{directory}Text/Microsoft')
				os.mkdir(f'{directory}Text/TextFiles')
			except:
				pass

		for k in os.listdir(f'{directory}Text/Microsoft'):
			try:
				os.mkdir(f'{directory}Text/Microsoft/Word')
				os.mkdir(f'{directory}Text/Microsoft/Excel')
			except:
				pass

		for l in os.listdir(f'{directory}Text/Other'):
			try:
				os.mkdir(f'{directory}Text/Other/System')
			except:
				pass

FolderCheck.makedirectories()

class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(folder_to_track):
			i = 1
			if filename != 'organized':
				# try:
					new_name = filename
					extension = 'noname'
					try:
						extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
						path = extensions_folders[extension]
					except Exception:
						extension = 'noname'

					now = datetime.now()
					year = now.strftime("%Y")
					month = now.strftime("%m")

					folder_destination_path = extensions_folders[extension]
					
					year_exists = False
					month_exists = False
					for folder_name in os.listdir(extensions_folders[extension]):
						if folder_name == year:
							folder_destination_path = extensions_folders[extension] + "/" +year
							year_exists = True
							for folder_month in os.listdir(folder_destination_path):
								if month == folder_month:
									folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
									month_exists = True
					if not year_exists:
						os.mkdir(extensions_folders[extension] + "/" + year)
						folder_destination_path = extensions_folders[extension] + "/" + year
					if not month_exists:
						os.mkdir(folder_destination_path + "/" + month)
						folder_destination_path = folder_destination_path + "/" + month


					file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
					while file_exists:
						i += 1
						new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
						new_name = new_name.split("/")[4]
						file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
					src = folder_to_track + "/" + filename

					new_name = folder_destination_path + "/" + new_name
					os.rename(src, new_name)
				# except Exception:
				#     print(filename)
#extensions
extensions_folders = {
#No name
	'noname' : f'/home/{user.username()}/Desktop/organized/Other/Uncategorized',
#Audio
	'.aif' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.cda' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.mid' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.midi' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.mp3' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.mpa' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.ogg' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.wav' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.wma' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.wpl' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
	'.m3u' : f'/home/{user.username()}/Desktop/organized/Media/Audio',
#Text
	'.txt' : f'/home/{user.username()}/Desktop/organized/Text/TextFiles',
	'.doc' : f'/home/{user.username()}/Desktop/organized/Text/Microsoft/Word',
	'.docx' : f'/home/{user.username()}/Desktop/organized/Text/Microsoft/Word',
	'.odt ' : f'/home/{user.username()}/Desktop/organized/Text/TextFiles',
	'.pdf': f'/home/{user.username()}/Desktop/organized/Text/PDF',
	'.rtf': f'/home/{user.username()}/Desktop/organized/Text/TextFiles',
	'.tex': f'/home/{user.username()}/Desktop/organized/Text/TextFiles',
	'.wks ': f'/home/{user.username()}/Desktop/organized/Text/TextFiles',
	'.wps': f'/home/{user.username()}/Desktop/organized/Text/TextFiles',
	'.wpd': f'/home/{user.username()}/Desktop/organized/Text/TextFiles',
#Video
	'.3g2': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.3gp': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.avi': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.flv': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.h264': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.m4v': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.mkv': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.mov': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.mp4': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.mpg': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.mpeg': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.rm': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.swf': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.vob': f'/home/{user.username()}/Desktop/organized/Media/Video',
	'.wmv': f'/home/{user.username()}/Desktop/organized/Media/Video',
#Images
	'.ai': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.bmp': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.gif': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.ico': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.jpg': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.jpeg': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.png': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.ps': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.psd': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.svg': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.tif': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.tiff': f'/home/{user.username()}/Desktop/organized/Media/Images',
	'.CR2': f'/home/{user.username()}/Desktop/organized/Media/Images',
#Internet
	'.asp': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.aspx': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.cer': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.cfm': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.cgi': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.pl': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.css': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.htm': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.js': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.jsp': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.part': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.php': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.rss': f'/home/{user.username()}/Desktop/organized/Other/Internet',
	'.xhtml': f'/home/{user.username()}/Desktop/organized/Other/Internet',
#Compressed
	'.7z': f'/home/{user.username()}/Desktop/organized/Other/Compressed',
	'.arj': f'/home/{user.username()}/Desktop/organized/Other/Compressed',
	'.deb': f'/home/{user.username()}/Desktop/organized/Other/Compressed',
	'.pkg': f'/home/{user.username()}/Desktop/organized/Other/Compressed',
	'.rar': f'/home/{user.username()}/Desktop/organized/Other/Compressed',
	'.rpm': f'/home/{user.username()}/Desktop/organized/Other/Compressed',
	'.tar.gz': f'/home/{user.username()}/Desktop/organized/Other/Compressed',
	'.z': f'/home/{user.username()}/Desktop/organized/Other/Compressed',
	'.zip': f'/home/{user.username()}/Desktop/organized/Other/Compressed',
#Disc
	'.bin': f'/home/{user.username()}/Desktop/organized/Other/Disc',
	'.dmg': f'/home/{user.username()}/Desktop/organized/Other/Disc',
	'.iso': f'/home/{user.username()}/Desktop/organized/Other/Disc',
	'.toast': f'/home/{user.username()}/Desktop/organized/Other/Disc',
	'.vcd': f'/home/{user.username()}/Desktop/organized/Other/Disc',
#Data
	'.csv': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.dat': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.db': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.dbf': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.log': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.mdb': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.sav': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.sql': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.tar': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.xml': f'/home/{user.username()}/Desktop/organized/Programming/Database',
	'.json': f'/home/{user.username()}/Desktop/organized/Programming/Database',
#Executables
	'.apk': f'/home/{user.username()}/Desktop/organized/Other/Executables',
	'.bat': f'/home/{user.username()}/Desktop/organized/Other/Executables',
	'.com': f'/home/{user.username()}/Desktop/organized/Other/Executables',
	'.exe': f'/home/{user.username()}/Desktop/organized/Other/Executables',
	'.gadget': f'/home/{user.username()}/Desktop/organized/Other/Executables',
	'.jar': f'/home/{user.username()}/Desktop/organized/Other/Executables',
	'.wsf': f'/home/{user.username()}/Desktop/organized/Other/Executables',
#Fonts
	'.fnt': f'/home/{user.username()}/Desktop/organized/Other/Fonts',
	'.fon': f'/home/{user.username()}/Desktop/organized/Other/Fonts',
	'.otf': f'/home/{user.username()}/Desktop/organized/Other/Fonts',
	'.ttf': f'/home/{user.username()}/Desktop/organized/Other/Fonts',
#Presentations
	'.key': f'/home/{user.username()}/Desktop/organized/Text/Presentations',
	'.odp': f'/home/{user.username()}/Desktop/organized/Text/Presentations',
	'.pps': f'/home/{user.username()}/Desktop/organized/Text/Presentations',
	'.ppt': f'/home/{user.username()}/Desktop/organized/Text/Presentations',
	'.pptx': f'/home/{user.username()}/Desktop/organized/Text/Presentations',
#Programming
	'.c': f'/home/{user.username()}/Desktop/organized/Programming/C&C++',
	'.class': f'/home/{user.username()}/Desktop/organized/Programming/Java',
	'.dart': f'/home/{user.username()}/Desktop/organized/Programming/Dart',
	'.py': f'/home/{user.username()}/Desktop/organized/Programming/Python',
	'.sh': f'/home/{user.username()}/Desktop/organized/Programming/Shell',
	'.swift': f'/home/{user.username()}/Desktop/organized/Programming/Swift',
	'.html': f'/home/{user.username()}/Desktop/organized/Programming/C&C++',
	'.h': f'/home/{user.username()}/Desktop/organized/Programming/C&C++',
#Spreadsheets
	'.ods' : f'/home/{user.username()}/Desktop/organized/Text/Microsoft/Excel',
	'.xlr' : f'/home/{user.username()}/Desktop/organized/Text/Microsoft/Excel',
	'.xls' : f'/home/{user.username()}/Desktop/organized/Text/Microsoft/Excel',
	'.xlsx' : f'/home/{user.username()}/Desktop/organized/Text/Microsoft/Excel',
#System
	'.bak' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.cab' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.cfg' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.cpl' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.cur' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.dll' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.dmp' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.drv' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.icns' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.ico' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.ini' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.lnk' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.msi' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.sys' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
	'.tmp' : f'/home/{user.username()}/Desktop/organized/Text/Other/System',
}

folder_to_track = f'/home/{user.username()}/Desktop'
folder_destination = f'/home/{user.username()}/Desktop/organized'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
	while True:           
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()
