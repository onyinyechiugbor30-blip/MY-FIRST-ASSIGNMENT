'''Question 5:
list your 10 favorite songs as tuples:
(title, artist, duration_seconds, genre)
find total duration in hh:mm:ss, 
all unique genres as a set
the longest and shortest track,
songs over 3 minutes
and how many songs each artist appear in'''

#This is a list containing information about my favorite songs. each tuple stores(song title,artist, duration, and genre)
my_fav_songs = [("King of eternity", "Loveworld singers", 415, "Gospel"),
("Head 2 core", "Anendlessocean", 147, "Afro Gospel",),
("You are the Lord","Loveworld singers", 460, "Gospel",),
("People in prison", "Tru South", 276, "Rap",),
("I Don't Chase I attract", "Sweetmamazurum", 170, "Pop",),
("Divinity", "Loveworld singers", 333, "Gospel"),
("You do this one", "Mercy Chinwo", 226, "Afro Gospel",),
("Omekannaya", "Mercy Chinwo", 478, "Gospel",),
("Three in one", "Buchi Atuonwu", 258, "Reggae",), 
("No end", "Loveworld singers", 341, "Gospel")]

#total playlist duration
#let's start with zero seconds
total_duration = 0
#visit each song and add its duration
for songs in my_fav_songs:
    total_duration += songs[2]
print(f"The total duration of all my favourite songs is {total_duration} seconds")
#convert total seconds into hours minutes and seconds
#the floor division is used for hour because only the whole number is required
hours = total_duration// 3600
#% modulus is first used because we require the remainder from 3600/total duration
#// is used next because we need only the remainder from (total duration% 3600) // 60
minutes = (total_duration % 3600) // 60
seconds = total_duration % 60
print(hours, "h", minutes, "m", seconds,"s")

#FIND UNIQUE GENRES
#a set automatically removes duplicates
genres = set()
#add each song's genre to the set
for song in my_fav_songs:
    #song[3] is used because the position of genre is index 3 in the tuple
    genres.add(song[3])
print("The unique genres in my favorite songs are:" , genres)

#FIND THE LONGEST SONG
#we'll assume the first song is the longest song
longest_song = my_fav_songs[0]
#compare every song picked with the current longest, till we arrive at the final longest song
for song in my_fav_songs:
    #the song[2] is used because the position of duration is index 2 in the tuple
    if song [2] > longest_song [2]:
        longest_song = song
print("The longest song is:", longest_song)

#FIND THE SHORTEST SONG
#we'll also assume that the first song is the shortest,
shortest_track = my_fav_songs[0]
# then compare the next picked song with the current shortest song till we get the shortest song among all
for song in my_fav_songs:
    if song[2] < shortest_track [2]:
        shortest_track = song
print("The shortest song is:", shortest_track)

#SONGS LOWER THAN 3 MINUTES
#convert three minutes to seconds
three_mins = 3 * 60
three_mins = 180
#the duration is in the index 2 position. Check through for every song that is under 180 seconds
for song in my_fav_songs:
    if song[2]> 180:
        #song[0] gets the first item from the variable which happens to be the song title
        print("song over three minutes: ", song[0])
#create a set of unique artist and removes duplicates
artists = set()
#loop through each unique artist in the artists set
for song in my_fav_songs:
    artists.add(song[1])
print("Artist appearances:")
for artist in artists:
    #start a counter for each artist that will count how many song belong to each artist
    count = 0
    #go through every song in the playlist of my favorite songs
    for song in my_fav_songs:
        #check if the artist of the current song matches the artist we are currently counting
        if song[1] == artist:
            #if it matches, increase the counter by one
            count += 1
            #after checking through all the songs, print how many times the artist appears
    print(artist, "appears in", count, "song(s)")