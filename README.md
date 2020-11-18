# MoveFilesToNameMonthDirectories
Small Python Utility to help you move files into Named Month Folders based on created date of each file

What does it do:

  Takes Path that it needs to work with, as the first argument
  
  Checks for all files in the Path directory
  
  Checks for Created Date for each file, extracts month and year of creation and uses it as targeted_dir with pattern MM_YYYY
  
  Moves each file into the respective targeted_dir

Example:
      C:\>python MoveFilesToDirectories.py " < path for the folder > "
      
      Output
      
      Received Argument Path <path for the folder>
      
      For given path:  <path for the folder>  Total Files Moved to Named Month Directories: 1000
