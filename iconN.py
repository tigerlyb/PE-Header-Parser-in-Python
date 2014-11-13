import os
import sys
import win32ui
import win32gui
from PyQt4 import QtGui

class extractIcon():
    def __init__(self):
        iconEmbededN = 0
        numberOfFilesN = 0
        
        fileListN = self.dir_list('YourDirectory\\normal\\')
        
        for f in fileListN:
            numberOfFilesN = numberOfFilesN + 1            
            print "File Number(NormalFile): ", numberOfFilesN
            print f
            if win32gui.ExtractIconEx(f, -1):
                print "Icon Embedded(NormalFile)."                    
                iconEmbededN = iconEmbededN + 1                
                large, small = win32gui.ExtractIconEx(f, 0)
                print large[0], small[0]
                print win32gui.ExtractIconEx(f, 0)
                win32gui.DestroyIcon(small[0])                    
                self.pixmap = QtGui.QPixmap.fromWinHBITMAP(self.bitmapFromHIcon(large[0]), 2)
                dest = "YourDirectory\\iconN\\" + f[42:len(f)-4] + ".ico"
                self.pixmap.save(dest)
                print ""
            else:
                print "No Icon Embedded(NormalFile)."
                print ""       
                        
        print ""        
        print "Total Number Of Files Embedded Icon(NormalFile): ", iconEmbededN
        
    def bitmapFromHIcon(self, hIcon):
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 32, 32)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0, 0), hIcon)
        hdc.DeleteDC()
        return hbmp.GetHandle()
    
    def dir_list(self, dir_name, *args):
        fileList = []
        for file in os.listdir(dir_name):
            dirfile = os.path.join(dir_name, file)
            if os.path.isfile(dirfile):
                if len(args) == 0:
                    fileList.append(dirfile)
                else:
                    if os.path.splitext(dirfile)[1][1:] in args:
                        fileList.append(dirfile)
        return fileList 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    icon = extractIcon()
