#########################################################################
# resutil.py - The Resolve utilities script
# ------------------------------
#
# Be sure your paths are set correctly in ENV!!!
# 
#
# Requires from pip:
#   pyyaml: python pip install pyyaml
#
#
# Follow meh somewhere or subscribes yo.
#
# emailz: pressresetshow@gmail.com
# githubub: github.com/pressreset
# youtubez: youtube.com/pressreset
# tweeterz: @pressreset
# instaface: @pressreset
#
# Code is copyright: Preston Allen
#
# This code is released as GPLv2 License
#
# "Resolve", "Fusion" and "DaVinci Resolve"
#   are copyright Blackmagic Design Pty. Ltd.
#
#
#              ███████  ███████
#          ████▓▓▓▓▓▓████░░░░░██
#        ██▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░██
#      ██▓▓▓▓▓▓████████████░░░░██
#    ██▓▓▓▓▓▓████████████████░██
#    ██▓▓████░░░░░░░░░░░░██████     /----------------------------------\
#  ████████░░░░░░██░░██░░██▓▓▓▓██   | Helooo! It's-a me! Watch out!     |
#  ██░░████░░░░░░██░░██░░██▓▓▓▓██   |  API could-a change-a and break   |
#██░░░░██████░░░░░░░░░░░░░░██▓▓██   |  you code! You no gonna be happy! |
#██░░░░░░██░░░░██░░░░░░░░░░██▓▓██   /  Use-a da githubs checkouts.      |
#  ██░░░░░░░░░███████░░░░██████    |  Don't-a make-a da copy pasta.     |
#    ████░░░░░░░███████████▓▓██    | Nobody like-a da copy pasta...     |
#      ██████░░░░░░░░░░██▓▓▓▓██   /  only Luigi and nobody like-a Luigi.|
#    ██▓▓▓▓██████████████▓▓██     --------------------------------------/
#  ██▓▓▓▓▓▓▓▓████░░░░░░████
#████▓▓▓▓▓▓▓▓██░░░░░░░░░░██
#████▓▓▓▓▓▓▓▓██░░░░░░░░░░██
#██████▓▓▓▓▓▓▓▓██░░░░░░████████
#  ██████▓▓▓▓▓▓████████████████
#    ██████████████████████▓▓▓▓██
#  ██▓▓▓▓████████████████▓▓▓▓▓▓██
#████▓▓██████████████████▓▓▓▓▓▓██
#██▓▓▓▓██████████████████▓▓▓▓▓▓██
#██▓▓▓▓██████████      ██▓▓▓▓████
#██▓▓▓▓████              ██████ 
#  ████
#
#
# Feel free to:
#   Fork this code and play with it.
#   Scratch your butt and smell your finger. You're a weirdo, but do you.
#   Open a pull request if you want improvements merged.
#   Eat pineapple on pizza. Nobody puts baby in a corner. Nobody.
#
#    Please share your changes and source code.
#       There aren't many working script examples for Resolve out there.
#       More examples helps people learn and get their stuff done.
#
#########################################################################


# Built in python imports
import sys
import os

# Imports from pip.
# Be sure to install them, else you will pizza when you should have french fried.
import yaml

# Import the DaVinciResolve script
# This MUST be set up in your ENV & paths OR YOU'RE GONNA HAVE A BAD TIME
import DaVinciResolveScript as GetResolve

# Open config file and set up the vars
with open('config.yml', 'r') as config:
    cfg = yaml.load(config, Loader=yaml.FullLoader)

# TODO:
# Variable names should just be auto built from the yaml config

# Filesystem Variables
storagePath = cfg['file']['storagePath']
directories = cfg['file']['directories']
binsOnly = cfg['file']['binsOnly']

# Resolve Variables
projectName = cfg['resolve']['project']['name']
frameRate = cfg['resolve']['project']['frameRate']
timelineName = cfg['resolve']['project']['timeline']['timelineName']
width = cfg['resolve']['project']['width']
height = cfg['resolve']['project']['height']
buildTimeline = cfg['resolve']['buildTimeline']
masterFolder = cfg['resolve']['masterFolder']
openPage = cfg['resolve']['openPage']
mediaPath = storagePath + projectName

# Check if there are vars on the command line script
# If no vars on command line stop
if len(sys.argv) == 1:
    print("Type help if you need help.")
    sys.exit()

# Set command line args to var
# Leaving this here for later in case an array needs to be built because FU that's why
var = sys.argv[1]

# Init Filesystem
def filesystemInit():
    
    # Init the filesystem for project structure
    # TODO: Figure out last project number on filesystem,
    #   increment by 1 and append to project name.

    # Inform user filesystem structure build process is starting
    print("---Building Filesystem structures at: " + storagePath + projectName)

    # Check if we can make the directory
    try:
        os.mkdir(storagePath + projectName)
        print("--Added directory " + storagePath + projectName)

    # Hey muchaho, we can't do it. Inform user and quit.
    except OSError:
        print ("--Can't create directory check paths! " + storagePath + projectName)
        sys.exit()

    # We're good, add directories and inform user they are created
    else:
        for i in directories:
            os.mkdir(storagePath + projectName + '\\' + i)
            print("--Added directory " + storagePath + projectName + "\\" + i)

        # Inform user directory creation process complete
        print ("---Created storage path at: " + storagePath + projectName)

# Init Resolve
def resolveInit():
    
    # Set up GetResolve
    resolve = GetResolve.scriptapp("Resolve")
    
    # Get the projectManager
    projectManager = resolve.GetProjectManager()

    # TODO:
    # Check if we are updating a current project via command line
    # If yes:
    # project = projectManager.GetCurrentProject()
    # If no, it's a new Init so make a project
    #
    # PA: Python is a meaniepants stupidhead dumbface language and I hate it

    # Create a project
    project = projectManager.CreateProject(projectName)

    # If the project can't be created exit
    if not project:
        print("Unable to create project " + projectName)
        sys.exit()

    # TODO:
    # Check if settings values exist in config.yaml
    # If no, skip and use defaults
    # If yes, apply each config value for project/timeline
    #
    # PA: What jerk decided Python should be white space delimited?

    # Set setting values for project/timeline
    # Any other timeline related settings or project related settings go here   
    project.SetSetting("timelineFrameRate", str(frameRate))
    project.SetSetting("timelineResolutionWidth", str(width))
    project.SetSetting("timelineResolutionHeight", str(height))

    # Inform user we are setting up the media storage and do it
    print("--Setting up media storage")
    mediaStorage = resolve.GetMediaStorage()

    # Inform user we are setting up the media pool and do it
    print("--Instantiate Media Pool")
    mediaPool = project.GetMediaPool()

    # Get the root folder of the mediapool 'Master'
    rootFolder = mediaPool.GetRootFolder()

    # Inform user and start bin creation process
    print("--Creating Media Bins and Adding Media")

    # Loop through the config and get the directory structure and bin names to create
    #
    # PA: Python also has no line endings, come on

    # Get the directories that exist for the mediaPath
    dirs = next(os.walk(mediaPath))

    # Loop through directories
    for d in dirs[1]:

        # Change to the rootFolder, just in case we aren't there
        mediaPool.SetCurrentFolder(rootFolder)

        # Add a folder/bin for the first directory we see 
        mediaPool.AddSubFolder(mediaPool.GetCurrentFolder(), d)

        # Save the current folder as a variable just in case we need it
        currentFolder = mediaPool.GetCurrentFolder()
        print("----Added folder " + d) # Hey look, we need it.

        
        # We got subdirectories then...
        subdirs = next(os.walk(mediaPath + '\\' + d))

        # loop through those too...
        for s in subdirs[1]:
            
            # Change to the bin where we need to be before adding
            mediaPool.SetCurrentFolder(currentFolder)
            print("----Set folder to " + d + s)
            
            # Add folder to media pool as bin
            mediaPool.AddSubFolder(mediaPool.GetCurrentFolder(), s)
            print("----Added folder as Bin: " + s)

            # Add items in the folder to media pool
            mediaStorage.AddItemsToMediaPool(mediaPath + '\\' + d + '\\' + s)

            # Tell the user we added the file to media pool
            for f in next(os.walk(mediaPath + '\\' + d + '\\' + s))[2]:
                print("------Added file to media pool: " + f)

            # If we are in the masterFolder AND we are building the timline, DO IT.
            if s == masterFolder and buildTimeline == 'Y':
                
                # Building the master timeline LET'S DO IT
                print("------Building master timeline")
                aRollFolder = mediaPool.GetCurrentFolder()
                
                # Hold up while we warp to root folder
                mediaPool.SetCurrentFolder(rootFolder)

                # Entered warp zone take 3rd pipe
                mediaPool.CreateTimelineFromClips(timelineName, aRollFolder.GetClips())
                print("------Created timeline: " + timelineName)

                # Exiting warp zone entering water level (cue music)
                mediaPool.SetCurrentFolder(aRollFolder)

                # Tell user what media we added to the timeline
                for f in next(os.walk(mediaPath + '\\' + d + '\\' + s))[2]:
                    print("--------Added clip to timeline: " + f)
                    
                print("------Added Camera A clips to Master Timeline")

    # Create the bins from config that don't exist on filesystem            
    for b in binsOnly:
        mediaPool.SetCurrentFolder(rootFolder)
        mediaPool.AddSubFolder(rootFolder, b)
                          
        # Inform the user we made the bin
        print("----Created Bin: " + b)
        
    # Inform user process is complete
    #
    # PA: Python uses white space to break its statements, which is stupid 
    print("--Created Media Bins and Added Media")

    mediaPool.SetCurrentFolder(rootFolder)
    print("--Set folder to root")

    # Open to selected page
    resolve.OpenPage(openPage)
    print("--Opened the " + openPage + " page")

    # Save the project just to be sure
    projectManager.SaveProject()
    print("--Saved project")

def exportProject():
    # nada
    print('export')
    
def render():
    #nada also
    print('render')

# Define main: PA: ...because Python is a buttface    
def main(var):

    # Check if we are doing a Filesystem Init process
    if var == 'fileinit':
        filesystemInit()
        print("\nThanks for playing... I'm done building the Filesystem Structure.")

    # So are we doing a Resolve Init process?
    elif var == 'resolveinit':
        resolveInit()
        print("\nThanks for playing... I'm done building the Resolve Project.")

    # Uh, are we doing a complete Init?
    elif var == 'fullinit':
        filesystemInit()
        resolveInit()
        print("\nThanks for playing... Init Finished.")

    # Are we exporting a project then?
    elif var == 'export':
        exportProject()
        print("\nHey! I said this function doesn't work yet!")

    # So are we rendering a project?
    elif var == 'render':
        render()
        print("\nFriend. This function doesn't work yet. It's not added.")

    elif var == 'biff':
        print("What are you lookin at?... butthead.")
        
    # Guess there is nothing we know how to do here. Print useless help doc placeholder.
    else:
        print("\nalmost HELPful MENU\n"
              "------\n\n"
              "Run the script with: \n>python resutil.py <option>\n\n"
              "Current options are:\n\n"
              "fileinit:     Build filesystem project structures.\n"
              "              [Do this first, then add your files into the folders.]\n\n"
              "resolveinit:  Build a Resolve project (Resolve must be running!)\n"
              "              [Run this next, and the files will be ingested into Resolve bins.]\n\n"
              "fullinit:     Do both fileinit and resolveinit.\n"
              "              [Do this if you just need a blank project with file structures/bins.]\n\n"
              "To be added:\n"
              "clone    - Offload footage from a card or other media to project folder and auto ingest.\n"
              "export   - Export a specific project #/current project.\n"
              "archive  - Archive a specific project #/current project.\n"
              "render   - Render a project # or submit it to render server in various formats.\n"
              "proxy    - Render proxies for project #, local or remote and organize them.\n"
              "normal   - Normalize all audio tracks to input gain individually.\n"
              "average  - Normalize all audio tracks input averaged.\n"
              "buff     - Normalize, place compressor and limit tracks.\n"
              "abnormal - Undo normalize on all audio tracks.\n"
              "delorean - Takes a project to a specific version, re-opens at that version.\n"
              "docbrown - Takes a project back to first version.\n"
              "marty    - Takes a project to the newest version.\n"
              "biff     - Doesn't actually do anything, just in the way.\n"
              "camshow  - Auto build multicam clip sequences for all your clips, make timeline.\n"
              "shadow   - Shadow a timeline to another project.\n"
              "bumpit   - Insert your bumpers/leaders/motion graphics automatically.\n"
              "mumps    - Same as bumpit, but only motion graphics, and all on new track.\n"
              "reducio  - Archive a project by #, and bundle a zip for internet transfer.\n"
              "presto   - Imports archive, submits render automatically then removes project from database.\n"
              "changeo  - Imports archive, cleans white space, dead clips, cut-throughs etc, re-archives.\n"
              "correcto - Apply auto-correct to all clips on a timeline.\n"
              "7of9     - Apply a specific REC709 lut to everything automatically.\n"
              "ventura  - Apply an ACE tranformation automatically.\n"
              "crayola  - Batch color your clips based on bins/metadata.\n"
              "config   - Change any config variable for whatever project from here.\n"
              "att      - Connect to a remote machine and run this script.\n"
              "shazam   - Run a whole batch of commands in sequence from the config file.\n"
              "\n")
        

# PA: I hate python, this is necessary for future expansion later so it's here...
if __name__ == "__main__":
    main(var)    
