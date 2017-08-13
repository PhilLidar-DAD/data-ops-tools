__version__ = "0.2"
__author__ = "Jok Laurente"
__email__ = "jmelaurente@gmail.com"
__description__ = "Script for batch transferring laz files"

import os
import csv
import subprocess

# parameters
csv_path = "luzon_area.csv"
dst_folder = "/mnt/pl2-storage/FREXLS/DATA_FROM_DAD/Extension/_tempLuzon"
adjusted_las_folder = "/mnt/pmsat-nas_geostorage/DPC/TERRA/Adjusted_LAZ_Tiles"
las_folder = "/mnt/pmsat-nas_geostorage/DPC/TERRA/LAS_Tiles"

with open(csv_path, 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		try:
			print "Finding matches for %s" % row
			adjusted = False
			block = str(row).replace("[","").replace("]","").replace("'","")
			area = block.split("_Blk")[0]
			wc_block = block + "_20"

			print "Finding matches in adjusted folder"
			for path, dirs, files in os.walk(adjusted_las_folder, topdown=False):
				for d in dirs:
					if wc_block in d:
						adjusted = True
						src = os.path.join(path,d)
						print src
						dst = os.path.join(dst_folder, "Adjusted")
						cmd = "rsync -aiPS --exclude 'ground' {0} {1}".format(src, dst)
						subprocess.call(cmd, shell=True)
						break

			print "Finding matches in unadjusted folder"
			if not adjusted:
				top_directory = os.path.join(las_folder,area)
				for path, dirs, files in os.walk(top_directory):
					for d in dirs:
						if wc_block in d:
							src = os.path.join(path,d)
							print src
							dst = os.path.join(dst_folder, "Unadjusted")
							cmd = "rsync -aiPS --exclude 'ASCII' --exclude 'MKP' --exclude '*.las' {0} {1}".format(src, dst)
							subprocess.call(cmd, shell=True)
							break
					break
		except Exception, e:
			print "Error in transferring"
