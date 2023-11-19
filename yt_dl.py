try:
    import pytube 
    print("The library was imported successfully!")
except ImportError:
    print("The library could not be imported.")


link = input("Enter link of youtube video : ")
print("You entered  : ", link)
yt_video = pytube.YouTube(link)

print(f"""
Title: {yt_video.title}
Length: {round(yt_video.length/60, 2)} minutes
Date Published: {yt_video.publish_date}
Views: {yt_video.views}
""")

streams = set()

for stream in yt_video.streams.filter(type="video"):
    streams.add(stream.resolution)

streams = list(streams)
streams.sort()
print("___ AVAILABLE RESOLUTIONS ___")
for i in range(len(streams)):
    print(i+1, ". ", streams[i])

while True:
    choice = input("Enter choice : ")
    if choice in streams:
        print(choice)
        final_choice = choice
        break
    elif int(choice) <= i+1 and streams[int(choice)-1] in streams:
        print(streams[int(choice)-1])
        final_choice = streams[int(choice)-1]
        break
    else:
        print("invalid input")

for stream in yt_video.streams.filter(resolution=final_choice):
    print("Download size : ", round(stream.filesize/1048576, 2), "MB")
    print("Do you want to download (y/n) : ", end="")
    confirmation = input()
    if confirmation == 'y':
        stream.download()
    else:
        print("BYE")
        exit()
    print("Downloading......")
    break


# WORK IN PROGRESS
