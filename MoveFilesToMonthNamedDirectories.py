#Author: Dharmesh Kishore
#Created: 30 Oct 2020
#What does it do:
#  Takes Path that it needs to work with, as the first argument
#  Checks for all files in the Path directory
#  Checks for Created Date for each file, extracts month and year of creation and uses it as targeted_dir with pattern MM_YYYY
#  Moves each file into the respective targeted_dir
#
#Example:
#      C:\>python MoveFilesToDirectories.py "<path for the folder>"
#      Output
#      Received Argument Path <path for the folder>
#      For given path:  <path for the folder>  Total Files Moved to Named Month Directories: 1000

import sys
import pathlib
from pathlib import Path
import datetime

path = Path(sys.argv[1])
print("Received Argument Path", path)


count = 0
for file in path.glob('*.*'):

    created_time = datetime.datetime.fromtimestamp(file.stat().st_ctime) 
    targeted_dir = str(created_time.month) + '_' + str(created_time.year)

#    Check if the targeted_dir is already available, if not create one
    target_path = path.joinpath(targeted_dir)
    pathlib.Path(target_path).mkdir(parents=True,exist_ok=True)
    file_path = path.joinpath(file)

#    Crude Way (WORKING)
    Path(file_path).rename(Path(file_path).parents[0] / targeted_dir / Path(file_path).name)
    
    count+=1
    
print("For given path: ",path," Total Files Moved to Named Month Directories: ", count)
