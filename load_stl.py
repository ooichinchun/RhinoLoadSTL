# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2019. 


import rhinoscriptsyntax as rs
import os

### Commands to open Files from specific folders

#path = '"C:\\IHPC\\Projects\\blk271.d3m"'
#rs.DocumentModified(False)
#rs.Command('_-Open {} _Enter'.format(path))

### Function to loop through all stl files in a folder and import into single Rhino file
def load_stl():
    fol = rs.BrowseForFolder()
    listing  = os.listdir(fol)
    #rFiles = []
    for file in listing:
        rs.DocumentModified(False)
        rs.Command('_-Import {} _Enter'.format(file))

        print os.path.splitext(file)[1]
        #if os.path.splitext(file)[1] == ".stl":
        #    rFiles.append(fol + "/" +file)  
    
    #if len(rFiles) == 0: return 
    #for rFile in rFiles:
        # extra commands
        
load_stl()