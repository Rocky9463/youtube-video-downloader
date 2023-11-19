try:
    import pytube 
    print("The library was imported successfully!")
except ImportError:
    print("The library could not be imported.")


link = "https://youtu.be/vEQ8CXFWLZU?si=tvFETuz7YLn44flR"
print(link)
yt_video = pytube.YouTube(link)
#print("Title : ", yt.title)
print(f"""
Title: {yt_video.title}
Length: {yt_video.length/60} minutes
Date Published: {yt_video.publish_date}
Views: {yt_video.views}
""")

streams = set()

for stream in yt_video.streams.filter(type="video"):
    streams.add(stream.resolution)
print("Availabel formats : ", streams)

for stream in yt_video.streams.filter(resolution="1440p"):
    print(stream)
    #stream.download()



# WORK IN PROGRESS