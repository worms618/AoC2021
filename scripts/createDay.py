# Decide which day
# Check if day already exists
# If exists, stop
# If not exists:
# copy _days# and content towards day# where # will be changed with day number
import os
import sys

if len(sys.argv) < 3:
    raise ValueError('No root directory and day number given')

daysRootDir = sys.argv[1]
day=int(sys.argv[2])

replaceWithDayNumberChar = '$'

# Days template directory with content
daysTemplateDirName = '_day' + replaceWithDayNumberChar
daysTemplateDirPath = os.path.join(daysRootDir, daysTemplateDirName)

dayDirName = daysTemplateDirName.replace('_', '').replace(replaceWithDayNumberChar, str(day))
dayDirPath = os.path.join(daysRootDir, dayDirName)

# Create the day directory, when not exists
if not os.path.isdir(dayDirPath):
    os.mkdir(dayDirPath)

dayTemplateFileNames = os.listdir(daysTemplateDirPath)

# Copy the template files and
# Replace replaceWithDayNumberChar with the day number in either file name and file content
for dayTemplateFileName in dayTemplateFileNames:
    # New file name and path for day directory
    dayFileName = dayTemplateFileName.replace(replaceWithDayNumberChar, str(day))
    dayFilePath = os.path.join(dayDirPath, dayFileName)

    # Create new file for day, if not exists
    if not os.path.isfile(dayFilePath):
        dayTemplateFilePath = os.path.join(daysTemplateDirPath, dayTemplateFileName)

        # Read template file content
        dayTemplateFileContent = ''
        with open(dayTemplateFilePath) as f:
            dayTemplateFileContent = f.read()

        # Set the day number where needed in the file content
        dayTemplateFileContent = dayTemplateFileContent.replace(replaceWithDayNumberChar, str(day))

        # Create new file for day
        with open(dayFilePath, mode="w") as f:
            f.write(dayTemplateFileContent)
