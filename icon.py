import os
import sys
import win32ui
import win32gui

f1 = 'E:\\Users\\tigerlyb\\Documents\\CSCI8260Project\\malware\\ff0eee6a9fafaf69c569df1b6007d18e.exe'
f2 = 'E:\\Users\\tigerlyb\\Documents\\CSCI8260Project\\malware\\febcdd9280379f41b576f0f9db40f6e5.exe'

icon1 = win32gui.ExtractIconEx(f1, 0)
icon2 = win32gui.ExtractIconEx(f2, 0)

print icon1
print icon2
print icon1[0]
print icon2[0]

        
