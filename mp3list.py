import os, fnmatch
import playmp3
import media


def find():
    #results = []
    songlist = []
    for root, dirs, files in os.walk("/home/mostwanted"):
        for name in files:
            if fnmatch.fnmatch(name, '*.mp3'):
                #result.append(os.path.join(root, name))
                location = root + "/" + name
                objname = name
                objname = media.mp3(name, location)
                songlist.append(objname)
	        
                #for song in songlist:
                    #new = song.location
                    #print new
    #print songlist
    print "finished complying all mp3s"
    playmp3.open_mp3_page(songlist)
    print "Done!!"
    

find()
            


