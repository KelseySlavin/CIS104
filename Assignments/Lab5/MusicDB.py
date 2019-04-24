songs=[] #my list of songs

def addsong(title, artist, album, track, year, genre):
    song=dict(Title=title, Artist=artist, Album=album, Track=track, Year=year, Genre=genre)
    songs.append(song) #add to the list 

def getsongnumber(number):
    try:
        int(number) #make sure that the number is  a number and not a string
    except:
        return None
    if(number <1):
        return None
    if((number // 1) > songs.count): 
        return None 
    else:
        return songs[(number // 1) - 1] #-1 the song because it starts at 0

