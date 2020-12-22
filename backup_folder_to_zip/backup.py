#! python3
# Copies an entire folder and its contains into
# a zip file whose filename increments. 

import zipfile, os, sys

folderToZip = ''
folderDestination = ''

# Red the terminal
helpMenssage = 'Write the folder to backup in zip, and opcional the destination \
        folder to the zip file (example: main.py "user/myfoldertobackup" "user/folderdestination")'
if len(sys.argv) == 1: 
    print ('The program need more arguments. ' + helpMenssage)
    sys.exit()
elif len(sys.argv) == 2:  
    folderToZip = sys.argv[1]
    folderDestination = os.path.dirname(folderToZip)
elif len(sys.argv) == 3:  
    folderToZip = sys.argv[1]
    folderDestination = sys.argv[2]
else: 
    print ('To much argument. ' + helpMenssage)
    sys.exit()

def backupToZip (folder, destination):
    """ Backup the antire contents of "folder" into a ZIP file """

    # Verify the paths
    if not os.path.exists (folderToZip) or not os.path.exists (folderDestination): 
        print ('Check your paths')
        sys.exit()
        
    folder =  folder

    # Figure out the filename this code should use based on 
    # what files already exist
    number = 1
    while True: 
        os.chdir (destination)
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    
    #Create the zip file
    print ('Creating %s...' % (zipFilename))
    #os.chdir('/home/dari/develop/learning/programación/python/ejercicios/automate_the_boring_stuff_with_python_new/9_organicing_files')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    #Walk the entire folder tree and compress the files in each folder.
    os.chdir (folder)
    for foldername, subfolders, filesnames in os.walk('.'):
        print ('Adding files in %s...' %(foldername))
        # Add the current folder to the zip file
        backupZip.write(foldername)
        # Add all files in this folder, to the Zip file
        for filename in filesnames: 
            newBase = os.path.basename(folder) + '_' #Checks the starts of the file
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # Dont backup the backup zip files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print ('Done.')

backupToZip(folderToZip, folderDestination)

