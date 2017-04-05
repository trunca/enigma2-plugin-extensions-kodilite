import os, re
from urllib2 import urlopen
from twisted.web.client import getPage, downloadPage

THISPLUG = "/usr/lib/enigma2/python/Plugins/Extensions/KodiLite"
HOSTS = ["allvid", "cloudy", "daclips", "exashare", "filebox", "filehoot", "filenuke", "flashx", "nosvideo", "streamcloud", "streaminto", "thevideo", "uploadc", "uptobox", "vidbull", "videomega", "vidhog", "vidlockers", "vidspot", "vidto", "vidx", "vidzi", "vodlocker", "youwatch"]

latest = " "

print "Starting Update-py"

def findmax(match = []):
                A = []
                B = []
                C = []
                D = []
                E = []
                imax = 0
                for item in match:
                        item = item.replace("%7E", "~")
                        x = item.split(".")
                        print "In findmax x =", x
                        A.append(int(x[0]))
#                        A.append((x[0]))
                lx = len(x)        
                Amax = max(A) 
                print "In findmax Amax =", Amax
                i1 = 0
                for a in A:
                      if a == Amax:
                             imax = i1
                             break
                      i1 = i1+1                
#                maxitem = str(Amax)
                print "In findnax imax A=", imax
                if lx > 1:
                    for item in match:        
                        x = item.split(".")
                        if int(x[0]) == int(Amax):
                                B.append(int(x[1]))
                        else:
#                                continue  
                                B.append(int('0'))       
                    Bmax = max(B) 
                    print "In findnax Bmax =", Bmax
                    i2 = 0
                    for b in B:
                         if b == Bmax:
                                imax = i2
                                break
                         i2 = i2+1                    
#                    maxitem = str(Amax) + "." + str(Bmax)
                    print "In findnax imax B=", imax
                    if lx > 2:
                      for item in match:        
                        x = item.split(".")
                        if (int(x[0]) == int(Amax)) and (int(x[1]) == int(Bmax)):
                                C.append(int(x[2]))
                        else:        
                                C.append(int('0'))
                      Cmax = max(C)
                      print "In findnax Cmax =", Cmax
                      i3 = 0
                      for c in C:
                            if c == Cmax:
                                   imax = i3
                                   break
                            i3 = i3+1
#                      maxitem = str(Amax) + "." + str(Bmax) + "." + str(Cmax)
                      print "In findnax imax C=", imax  
                print "In findnax imax final =", imax                              
                maxitem = match[imax]
                print "maxitem =", maxitem
                return maxitem        


def updstart():
######################################## 
                tfile = THISPLUG + "/scripts/script.module.urlresolver/addon.xml"
                if not os.path.exists(tfile):
                       upd_done1()
                url2 = "https://offshoregit.com/tvaresolvers/tva-common-repository/raw/master/addons.xml"
                print "In Update-py checkvers3 url2 2=", url2
#                fpage = urlopen(url2).read()
                xdest = "/tmp/down.txt"
                downloadPage(url2, xdest).addCallback(getdown1).addErrback(showError1)

def getdown1(fplug):                
                fpage = open("/tmp/down.txt", "r").read()
#                print "In checkvers3 fpage =", fpage
                rx = 'addon id="script.module.urlresolver".*?version="(.*?)"'
                match = re.compile(rx,re.DOTALL).findall(fpage)
                newvers = match[0]
                print "In updstart urlresolver new version= ", newvers
                tfile = THISPLUG + "/scripts/script.module.urlresolver/addon.xml"
                f = open(tfile, "r")       
                txt = f.read()
                print "In main txt = ", txt
                n1 = txt.find('<addon', 0)
                n11 = txt.find('id', n1)
                n2 = txt.find("version", n11)
                n3 = txt.find('"', n2)
                n4 = txt.find('"', (n3+2))
                version = txt[(n3+1):n4]
                f.close()
                print "In updstart urlresolver version= ", version 
                if newvers == " ":
                       upd_done1()                      
                if newvers != version:
                       plug = "urlresolver.zip"
                       fdest = THISPLUG + "/scripts"
                       dest = "/tmp/urlresolver.zip"
                       xfile = "https://offshoregit.com/tvaresolvers/tva-common-repository/raw/master/zips/script.module.urlresolver/script.module.urlresolver-" + newvers + ".zip" 
                       print "updstart xfile =", xfile
                       downloadPage(xfile, dest).addCallback(uresolv).addErrback(showError1)
                else:       
                       upd_done1()        

def showError1(error):
                print "ERROR :", error
                upd_done1()

def uresolv(fplug): 
                       tfile = THISPLUG + "/scripts/script.module.urlresolver"
                       cmd1 = "rm -rf " + tfile
                       fdest = THISPLUG + "/scripts"
                       cmd2 = "unzip -o -q '/tmp/urlresolver.zip' -d " + fdest
                       print "In main cmd urlresolver=", cmd2
                       title = _("Installing script urlresolver")
                       cmd = cmd1 + " && " + cmd2
                       os.system(cmd)
                       upd_done1()
                       #################

##############################################################################                       
def upd_done1():
        tfile = THISPLUG + "/scripts/script.module.youtube.dl/lib/youtube_dl/version.py"
        if not os.path.exists(tfile):
                upd_done3()
        else:
                url2 = "https://rg3.github.io/youtube-dl/download.html"
                print "In Update-py checkvers url2 =", url2
                #fpage = urlopen(url2).read()
                xdest = "/tmp/down.txt"
                downloadPage(url2, xdest).addCallback(getdown2).addErrback(showError2)

def getdown2(fplug):                
                fpage = open("/tmp/down.txt", "r").read()
#                print "In checkvers fpage =", fpage
                txt = fpage
                n1 = txt.find('<h2><a href=', 0)
                n11 = txt.find('"', (n1+2))
                n2 = txt.find('">', (n11+2))
                n3 = txt.find('</a>', (n2+4))
                latest = txt[(n2+2):n3]
                print  "checkvers latest =", latest
                tfile = THISPLUG + "/scripts/script.module.youtube.dl/lib/youtube_dl/version.py"
                f = open(tfile, "r")       
                txt = f.read()
                print "In upd_done1 txt = ", txt
                n1 = txt.find('__version__ = ', 0)
                n2 = txt.find("'", (n1+18))
                
                version = txt[(n1+15):n2]
                f.close()
                print "In upd_done1 version youtube.dl= ", version
                newvers = latest
                print "In upd_done1 newvers youtube.dl= ", newvers
                if newvers == " ":
                       upd_done3()
                elif newvers != version:
#                       fdest = THISPLUG + "/scripts//script.module.youtube.dl/lib"
                       dest = "/tmp/youtube-dl.zip"
                       xfile = "https://yt-dl.org/downloads/" + newvers + "/youtube-dl" 
#                       xfile = "https://yt-dl.org/downloads/latest/youtube-dl"
                       downloadPage(xfile, dest).addCallback(ytdl).addErrback(showError2)
                else:       
                       upd_done3()        

def showError2(error):
                print "ERROR :", error
                upd_done3()

def ytdl(fplug):
        try:
                fdest = THISPLUG + "/scripts/script.module.youtube.dl/lib/"
                import zipfile
                zip_ref = zipfile.ZipFile('/tmp/youtube-dl.zip', 'r')
                zip_ref.extractall(fdest)
                zip_ref.close()
#                cmd = "mv '/tmp/youtube-dl' '/tmp/youtube_dl' && cp -rf '/tmp/youtube_dl' " + fdest
#                print "In ytdl cmd =", cmd
#                os.system(cmd)
                upd_done3()
        except:
                upd_done3()               
########################################   

def upd_done3():
        tfile = THISPLUG + "/scripts/script.module.liveresolver/addon.xml"
        if not os.path.exists(tfile):
                upd_done5()
        else:
#                name = "script.module.urlresolver"
                url2 = "https://offshoregit.com/natko1412/addons.xml"
                print "In Update-py newvers url2 3=", url2
#                fpage = urlopen(url2).read()
                xdest = "/tmp/down.txt"
                downloadPage(url2, xdest).addCallback(getdown4).addErrback(showError4)

def getdown4(fplug):                
                fpage = open("/tmp/down.txt", "r").read()
#                print "In checkvers4 fpage =", fpage
                rx = 'addon id="script.module.liveresolver".*?version="(.*?)"'
                print "In checkvers4 rx =", rx
                match = re.compile(rx,re.DOTALL).findall(fpage)
                print "In checkvers4 match =", match
                latest = match[0]
                tfile = THISPLUG + "/scripts/script.module.liveresolver/addon.xml"
                f = open(tfile, "r")       
                txt = f.read()
                print "In main txt = ", txt
                n1 = txt.find('<addon', 0)
                n11 = txt.find('id', n1)
                n2 = txt.find("version", n11)
                n3 = txt.find('"', n2)
                n4 = txt.find('"', (n3+2))
                version = txt[(n3+1):n4]
                f.close()
                print "In main version liveresolver= ", version
                newvers = latest
                if newvers == " ":
                       upd_done5()
                elif newvers != version:
                       plug = "liveresolver.zip"
                       fdest = THISPLUG + "/scripts"
                       dest = "/tmp/liveresolver.zip"
                       xfile = "https://offshoregit.com/natko1412/zips/script.module.liveresolver/script.module.liveresolver-" + newvers + ".zip" 
                       downloadPage(xfile, dest).addCallback(upd_done4).addErrback(showError4)
                else:       
                       upd_done5()   

def showError4(error):
                print "ERROR :", error
                upd_done5()

def upd_done4(fplug): 
                       tfile = THISPLUG + "/scripts/script.module.liveresolver"
                       cmd1 = "rm -rf " + tfile
                       fdest = THISPLUG + "/scripts"
                       cmd2 = "unzip -o -q '/tmp/liveresolver.zip' -d " + fdest
                       print "In main cmd liveresolver=", cmd2
                       title = _("Installing script liveresolver")
                       cmd = cmd1 + " && " + cmd2
                       os.system(cmd)
                       upd_done5()

########################
def upd_done5():
        tfile = THISPLUG + "/scripts/script.mrknow.urlresolver/addon.xml"
        if not os.path.exists(tfile):
                upd_done()
        else:
#                name = "script.module.urlresolver"
                url2 = "http://kodi.filmkodi.com/script.mrknow.urlresolver/addon.xml"
                print "In Update-py checkvers5 url2 3=", url2
#                fpage = urlopen(url2).read()
                xdest = "/tmp/down.txt"
                downloadPage(url2, xdest).addCallback(getdown5).addErrback(showError5)

def getdown5(fplug):                
                fpage = open("/tmp/down.txt", "r").read()

#                print "In checkvers5 fpage =", fpage
                rx = 'addon id="script.mrknow.urlresolver".*?version="(.*?)"'
                print "In checkvers5 rx =", rx
                match = re.compile(rx,re.DOTALL).findall(fpage)
                print "In checkvers5 match =", match
                latest = match[0]
                print  "latest =", latest
                tfile = THISPLUG + "/scripts/script.mrknow.urlresolver/addon.xml"
                f = open(tfile, "r")       
                txt = f.read()
                print "In main txt = ", txt
                n1 = txt.find('<addon', 0)
                n11 = txt.find('id', n1)
                n2 = txt.find("version", n11)
                n3 = txt.find('"', n2)
                n4 = txt.find('"', (n3+2))
                version = txt[(n3+1):n4]
                f.close()
                print "In main version mrknow resolver version = ", version
                newvers = latest
                print "In main version mrknow newvers= ", newvers
                if newvers == " ":
                       upd_done()
                elif newvers != version:
                       plug = "mkresolver.zip"
                       fdest = THISPLUG + "/scripts"
                       dest = "/tmp/mkresolver.zip"
                       xfile = "http://kodi.filmkodi.com/script.mrknow.urlresolver/script.mrknow.urlresolver-" + newvers + ".zip" 
                       print "In main version mrknow xfile= ", xfile
                       downloadPage(xfile, dest).addCallback(upd_done6).addErrback(showError5)
                else:       
                       upd_done()   

def showError5(error):
                print "ERROR :", error
                upd_done()

def upd_done6(fplug): 
                       print "In mupd_done6"
                       tfile = THISPLUG + "/scripts/script.mrknow.urlresolver"
                       cmd1 = "rm -rf " + tfile
                       fdest = THISPLUG + "/scripts"
                       cmd2 = "unzip -o -q '/tmp/mkresolver.zip' -d " + fdest
                       print "In main cmd mkeresolver=", cmd2
                       title = _("Installing script mrknow resolver")
                       cmd = cmd1 + " && " + cmd2
                       os.system(cmd)
                       upd_done()

def upd_done():        
        #################
        print "In upd_done"
        #################
        fdest = THISPLUG + "/scripts/script.module.youtube.dl/lib/youtube_dl/extractor"
        dest = "/tmp/extractors.zip"
        xfile = "http://www.turk-dreamworld.com/bayraklar/Receiverler/Dreambox/TDW/e2/addons/KodiDirect/Fix/extractors-py.zip" 
        cmd1 = "wget -O '" + dest + "' '" + xfile + "'"
        cmd2 = "unzip -o -q '/tmp/extractors.zip' -d " + fdest
        cmd = cmd1 + " && " + cmd2
        os.system(cmd)
        #################
        fdest = THISPLUG
        dest = "/tmp/adlist.zip"
        xfile = "http://www.turk-dreamworld.com/bayraklar/Receiverler/Dreambox/TDW/e2/addons/KodiDirect/Fix/adlist-txt.zip" 
        cmd1 = "wget -O '" + dest + "' '" + xfile + "'"
        cmd2 = "unzip -o -q '/tmp/adlist.zip' -d " + fdest
        cmd = cmd1 + " && " + cmd2
        os.system(cmd)
        ####################
        
        if not os.path.exists("/usr/lib/python2.7/site-packages/requests"):
               cmd = "opkg install python-requests"
               os.system(cmd)
        if not os.path.exists("/usr/lib/python2.7/site-packages/Crypto"):
               cmd = "opkg install python-pycrypto"
               os.system(cmd)
        if not os.path.exists("/usr/lib/python2.7/lib-dynload/mmap.so"):
               cmd = "opkg install python-mmap"
               os.system(cmd)
        if not os.path.exists("/usr/lib/python2.7/sqlite3"):
               cmd = "opkg install python-sqlite3"
               os.system(cmd)

        print "In upd_done 2"
        ####################

#updstart()










              