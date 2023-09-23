import os.path
import os
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

def main():
    appData = os.environ['APPDATA']
    packageDir = os.path.join(appData, 'Sublime Text', 'Installed Packages')
    packagePath = os.path.join(packageDir, 'HLSL 2021 Syntax.sublime-package')
    srcDir = os.path.dirname(os.path.abspath(__file__))

    print('Packaging %s in %s' % (srcDir, packagePath))

    with ZipFile(packagePath, 'w', compression=ZIP_DEFLATED) as zipObject:
        for folderName, subFolders, fileNames in os.walk(srcDir):
            if folderName.find('.git') != -1:
                continue

            for fileName in fileNames:
                # Create filepath of files in directory
                filePath = os.path.join(folderName, fileName)
                # Add files to zip file
                zipObject.write(filePath, os.path.relpath(filePath, srcDir))

if __name__ == "__main__":
    main()