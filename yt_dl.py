try:
    import pytube 
    print("The library was imported successfully!")
except ImportError:
    print("The library could not be imported.")


link = "https://youtu.be/vEQ8CXFWLZU?si=tvFETuz7YLn44flR"
print(link)
yt = pytube.YouTube(link)
print("Title : ", yt.title)
            

