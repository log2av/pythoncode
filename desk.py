import ctypes, time, os
SPI_SETDESKWALLPAPER = 20
path = "C:\\Users\\Ajju\\Desktop\sdfawef\\test_images"
for filename in os.listdir(path):
    print filename
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0 , path + '\\' + filename, 0)
    time.sleep(3)