# Distribution Tools for Orthophotos

## batch_copy_ortho.py
### *Script for copying orthophotos using AOI as basis*

Requirements
* terminal
* text file listing all block names that intersects with AOI
* AOI shapefile

1. List all the missions that intersect with the area of interest, and save it as textfile. The filename of the text file should be the name of the folder where the mission was located.
The text should not contain white spaces. 

1. Open terminal, then SSH to salad.prd.dream.upd.edu.ph using your username and password. 

1. Change directory to `/mnt/geostorage/DAD/Working/Operation/scripts/data-ops-tools/orthos` 

1. Run this command to see the options for the script: ./batchCopy_ortho.py -h
  * Input Shapefile - This shapefile will be used as the area of interest. It should contain only 1 feature and it has to be polygon or multipolygon.
  * Text file - The text file where the missions were listed.
  * Output Folder - The location of each output raster.

  Sample run: `./batchCopy_ortho.py -i AOI/Jalaur_AOI.shp -t Jalaur.txt -o /mnt/geostorage/FTP/`

  `./batchCopy_ortho.py -i UPM_Talomo.shp -t Davao.txt -o /mnt/geostorage/FTP/PL1/upm-user/DL/DAD/Compressed/`

Ref: https://docs.google.com/document/d/11a9KGoDbai5lrZKRmpeGvdLSCarQ9gBeyEB5P80Z_p8/edit
