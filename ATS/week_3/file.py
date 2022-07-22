
# to read a file after creating it

with open('star_poem.txt', "r") as rf:
    pass
    #print(rf.read())

# to read the file in line by line
with open('star_poem.txt', "r") as rf:
    read_in_line = rf.readline()
    #print(read_in_line)

# to read multiple lines, but the output will be in form of list
with open('star_poem.txt', "r") as rf:
    read_multline = rf.readlines()
    #print(read_multline)

    # you can loop over it so as to get the content printed normal
    for line in read_multline:
        #for loop returns the file contents with in between spaces,
        #to deal with this use end=" "
        print(line, end=" ")

# You may want to copy from already created file to a new  one using nexted with
with open("star_poem.txt", "r") as rf:
    with open("text_copied.txt", "w") as wf:
        for line in rf:
            wf.write(line)

#you might even want to read specific size of the file


#to read and copy a picture using context manager

with open("pic.png","rb") as rf:
    with open("pic_copied.png", "wb") as wb:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            #to avoid infinite loop
            rf_chunk = rf.read(chunk_size)



