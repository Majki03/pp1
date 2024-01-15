class MusicPieces():
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    def __str__(self):
        return (f"Performer:    {self.artist}\n"
                f"Song:         {self.track_title}\n"
                f"Album:        {self.album}\n"
                f"Year:         {self.year}\n")

music1 = MusicPieces("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
music2 = MusicPieces("Adele", "Hello", "25", 2015)

print(music1)
print(music2)