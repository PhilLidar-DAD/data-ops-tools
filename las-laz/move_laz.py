__version__ = "0.1"
__author__ = "Jok Laurente"
__email__ = "jmelaurente@gmail.com"
__description__ = "Script for moving LAZ files"

import os
import shutil

cwd = os.getcwd()

for path, dirs, files in os.walk(cwd):
	for d in dirs:
		if d.endswith("LAZ"):
			src = os.path.join(path,d)
			dst = os.path.join(path.replace("LAS_FILES","LAZ"))
			print "OLD: " + path
			print "SRC: " + src
			print "DST: " + dst
			try:
				shutil.move(src,dst)
				shutil.rmtree(path)
			except Exception, e:
				print "Error in copying"
