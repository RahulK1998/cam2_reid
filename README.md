# cam2_reid

## segment.py ## 
Python file to segment input images from the gt_bbox file into top, middle, and bottom. 

### Running the script ###
python segment.py -f <input_folder_address> -s <output_folder_address>  
if -f or -s are not specified, the current working directory is used.   
  
### Outputs ###
The script produces 3 image outputs for every input with the naming convention <image_name>_TOP.<ext>, <image_name>_MID.<ext>, and <image_name>_BOT.<ext> representing the Top, middle and botttom portions of the image.   
It is recommended to specify -s, the output address.   
The script currently does not create a new folder if the folder specified (in -f or -s) does not exist.   
