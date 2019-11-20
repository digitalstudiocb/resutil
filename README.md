# resutil
Python Utility Script for DaVinci Resolve

Will add more to this document soon.
I just spit out this code. It works, but it's BETA.
Use are your own peril.

Currently here is what it can do:

Run the script with:
>python resutil.py <option>

Current options are:

fileinit:     Build filesystem project structures.
              [Do this first, then add your files into the folders.]

resolveinit:  Build a Resolve project (Resolve must be running!)
              [Run this next, and the files will be ingested into Resolve bins.]

fullinit:     Do both fileinit and resolveinit.
              [Do this if you just need a blank project with file structures/bins.]

To be added:
clone    - Offload footage from a card or other media to project folder and auto ingest.
export   - Export a specific project #/current project.
archive  - Archive a specific project #/current project.
render   - Render a project # or submit it to render server in various formats.
proxy    - Render proxies for project #, local or remote and organize them.
normal   - Normalize all audio tracks to input gain individually.
average  - Normalize all audio tracks input averaged.
buff     - Normalize, place compressor and limit tracks.
abnormal - Undo normalize on all audio tracks.
delorean - Takes a project to a specific version, re-opens at that version.
docbrown - Takes a project back to first version.
marty    - Takes a project to the newest version.
biff     - Doesn't actually do anything, just in the way.
camshow  - Auto build multicam clip sequences for all your clips, make timeline.
shadow   - Shadow a timeline to another project.
bumpit   - Insert your bumpers/leaders/motion graphics automatically.
mumps    - Same as bumpit, but only motion graphics, and all on new track.
reducio  - Archive a project by #, and bundle a zip for internet transfer.
presto   - Imports archive, submits render automatically then removes project from database.
changeo  - Imports archive, cleans white space, dead clips, cut-throughs etc, re-archives.
correcto - Apply auto-correct to all clips on a timeline.
7of9     - Apply a specific REC709 lut to everything automatically.
ventura  - Apply an ACE tranformation automatically.
crayola  - Batch color your clips based on bins/metadata.
config   - Change any config variable for whatever project from here.
att      - Connect to a remote machine and run this script.
shazam   - Run a whole batch of commands in sequence from the config file.
