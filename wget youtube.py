'''Program to download max res thumbnail from Youtube video.
Pls input link to the video without any playlists, mixes, etc'''
import wget

outfolder = 'C:/Users/lenovo/Downloads/'    #change this to your output folder

print('Download Youtube video thumbnails at max resolution. Code by Julian Cheung.')
print()
def dl():
    videoID = str(input('Enter Youtube video URL: '))[-11:]
    print('Video ID:', videoID)
    print()
    url = 'https://img.youtube.com/vi/' + videoID + '/maxresdefault.jpg'
    print('Download URL:', url)
    print('Downloading...')
    print()
    outfile = outfolder + 'thumbnail_' + videoID + '.jpg'
    wget.download(url, outfile)
    print('Done! Thumbnail is at:', outfile)
    print()
    print('Type dl() to download another thumbnail')

dl()
