movie = 'False'
file= open('com.txt','w')
file.write(movie)
file.close()
file= open('variables.txt','w')
file.write("0,0,0,0,2")
file.write("\n")
file.write("0,0,0,0,0")
file.close()
variable = ''
import tkinter as tk
from PIL import ImageTk,Image
import time
import math

root = tk.Tk()

root.title("Translate")
corhand1 = 0
clicks = 0
once= 1
wait = 0 
uph1 = 1
uph2 = 1
sidh1 = 2 
sidh2 = 2
anglh1 = 0
anglh2 = 0
autocorrect = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
finalword = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
word1 = ""
word2 = ""
word3 = ""

def clear():
    global wordcount,finalword
    finalword = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    w.itemconfigure(thetext4, text="")
    w.itemconfigure(thetext5, text="")
    w.itemconfigure(thetext6, text="")
    w.itemconfigure(thetext7, text="")
    w.itemconfigure(thetext8, text="")
    w.itemconfigure(thetext9, text="")
    wordcount = 0
    

def auto():
    global word1,word2,word3
    print(autocorrect)
    correctauto = str(autocorrect[0])
    ranking = []
    score = 0
    counter = 0
    ans = []
    for i in autocorrect[1::]:
        correctauto = correctauto+str(i)
    for i in numbers:
        for k in i:
            if i[counter] == correctauto[counter]:
                score += 2
            elif int(i[counter])==int(correctauto[counter])-1 or int(i[counter])==int(correctauto[counter])+1:
                score += 1
            counter += 1
        counter = 0
        ranking.append(score)
        score = 0
    for i in range(0,3):
        maxi = max(ranking)
        position = ranking.index(maxi)
        ans.append(words[position])
        ranking.remove(maxi)
        ranking.insert(position,0)
    t.itemconfigure(thetext1, text=ans[0])
    t.itemconfigure(thetext2, text=ans[1])
    t.itemconfigure(thetext3, text=ans[2])
    t.update()
    word1 = ans[0]
    word2 = ans[1]
    word3 = ans[2]

def displaytext():
    if x<412/3 and y<60:
        word = word1
    elif x<824/3 and y<60:
        word = word2
    elif x>824/3 and y<60:
        word = word3
    else:
        word = ""
    if word != "":
        wordcount = 0
        for i in finalword:
            if i != "":
                wordcount += 1
        if wordcount > 14:
            w.itemconfigure(thetext9, text="No more input allowed.")
        else:
            finalword[wordcount] = word
            wordcount += 1
            if wordcount <= 3:
                w.itemconfigure(thetext4, text=(finalword[0]+" "+finalword[1]+" "+finalword[2]))
            if wordcount <= 6:
                w.itemconfigure(thetext5, text=(finalword[3]+" "+finalword[4]+" "+finalword[5]))
            if wordcount <= 9:
                w.itemconfigure(thetext6, text=(finalword[6]+" "+finalword[7]+" "+finalword[8]))
            if wordcount <= 12:
                w.itemconfigure(thetext7, text=(finalword[9]+" "+finalword[10]+" "+finalword[11]))
            if wordcount <= 15:
                w.itemconfigure(thetext8, text=(finalword[12]+" "+finalword[13]+" "+finalword[14]))

words = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Abandon','About','Above','Accept','Act','Add to:','Address','Advertise','Advise','Afraid','Africa','After','Afternoon','Again','Against','Agree','Ahead','Air Conditioner','Airplane','Alarm','Alcohol','All','Everywhere','All right','Allergy','Alligator','Allow','Almost','Alone','Alternate','Always','Amazed','Ambulance','And','Angry','Announce','Answer','Anxious','Any','Anyone','Anyway','Appear','Applaud','Art','Article','Artificial','Ashamed','Ask','Assign','Assistant','Associate with','Apple','Attend','Attitude','Fascinated','Audience','Aunt','Avoid','Awkward','Baby','Bad','Bake','Balance','Banana','Barely','Baseball','Basement','Basic','Basketball','Bear','Because','Become','Bed','Beer','Before','Beg','Believe','Bell','less then','Benefit','Best','Bet','Better','Between','Bicycle','Big']
numbers = ['0000000000001200041','5555000000001200041','1111000000001100041','1115000000001200041','1111000000001200041','5551000000001200041','0005000000011200041','0055000000011200041','5000000000001200041','5000000000001200041','0055010000000000041','0005020000000000041','0003000000000000041','0003000000000000041','0044010000000000041','0045000000000100041','0005020000000100041','0055000000000000041','0000000000000000041','0000000000000000041','0055000000000000041','0555000000000000041','0004000000000000041','5000020000000000041','0005000000000000041',
           '5555020000001042111','0005100000001021122','3333110000001102122','5555021111001122112','0000010000001102122','5555021111001332111','0000021000001022122','0000100000001111122','3333010000101312123','5555021111021002112','3333010000101212122','5555020000001122123','5555020000001312123','3333010000001112112','5555021000001012112','0005100000001002123','0000021000001112122','0000010000001202112','5005100000000102112','0005100000001212122','5005100000001012123','5555020000001210132','5555021111001322122','5555020000021112122','0005100000001012123','5555021111001322132','5555020000001142111','3333110000001111122','0005100000001002112','0005021000001112112','0005100000001012122','0000100000001112112','5555020000001202113','5555021111001012132','4444111111001012122','0005100000001012123','0005100000001202123','5535021111001010122','0000021000001012122','0000021000001012122','5555021000001010122','0005100000001122131','5000100000001012133','0004010000001012133','0005100000001102113','3333110000001002113','0005100000001212122','0000021000001112122','5555021111001012133','0004100000001212123','0005100000001212122','0000010000001112122','5555020000001112123','5555020000001322121','0000010000001202123','5555020000001110122','0000021000001012132','0055021100001302113','5555020000001422123','5555020000001012123','5555020000001422121','3333110000001102112','3333010000101112133','5554111111101102123','0000100000001100113','0000021000001022121','5555020000001322121','0055021100001122112','4444111111001012132','0005021000001002123','5555020000001312132','5555020000001102113','5555020000001202123','3333110000001410132','5555021111001412132','0005100000001202123','3333110000002302112','3333110000001112122','5554111111101112122','5555020000001012123','5555020000001122112','5555020000001012123','5555020000001112122','0000100000001312122','0001021000001112112']

def changeimage(x,or2):
    pilImage0 = Image.open("0.png")
    pilImage0 = pilImage0.resize((10, 17), Image.ANTIALIAS)
    image0 = ImageTk.PhotoImage(pilImage0)

    pilImage1 = Image.open("1.png")
    pilImage1 = pilImage1.resize((10, 17), Image.ANTIALIAS)  
    image1 = ImageTk.PhotoImage(pilImage1)  #yaxisup

    pilImage3 = Image.open("3.png")
    pilImage3 = pilImage3.resize((10, 17), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(pilImage3) 

    pilImage4 = Image.open("4.png")
    pilImage4 = pilImage4.resize((10, 17), Image.ANTIALIAS)
    image4 = ImageTk.PhotoImage(pilImage4) 

    pilImage5 = Image.open("5.png")
    pilImage5 = pilImage5.resize((10, 40), Image.ANTIALIAS)
    image5 = ImageTk.PhotoImage(pilImage5) 
    diction = {0:image0,1:image1,2:image1,3:image3,4:image4,5:image5}
    if or2 == 0:
        for key,value in diction.items():
            if x[0] == key:
                e.itemconfigure(finger1hand1, image = value)
                e.imagefh1 = value
            if x[1] == key:
                e.itemconfigure(finger2hand1, image = value)
                e.imagef1h1 = value
            if x[2] == key:
                e.itemconfigure(finger3hand1, image = value)
                e.imagef2h1 = value
            if x[3] == key:
                e.itemconfigure(finger4hand1, image = value)
                e.imagef3h1 = value
    else:
        for key,value in diction.items():
            if x[0] == key:
                e.itemconfigure(finger1hand2, image = value)
                e.imagefh2 = value
            if x[1] == key:
                e.itemconfigure(finger2hand2, image = value)
                e.imagef1h2 = value
            if x[2] == key:
                e.itemconfigure(finger3hand2, image = value)
                e.imagef2h2 = value
            if x[3] == key:
                e.itemconfigure(finger4hand2, image = value)
                e.imagef3h2 = value
    e.update()


#when click on screen::
def getorigin(eventorigin):
    global x,y,clicks,objekt,cord,corhand1,corhand2,clicked,once,movie,e,arminimage1,arminimage2,armrot,autocorrect
    file = open('com.txt','r')
    movie = file.read()
    file.close()
    file = open('change.txt','r')
    changetext = file.read()
    file.close()
    #toplevel -> to provide 2 buttons that determine if the user wants to move/change position of the hands
    def toplevel():
        #moo stands for move
        def moo():
            movie = 'True'
            file= open('com.txt','w')
            file.write(movie)
            file.close()
            file = open('com.txt','r')
            movie = file.read()
            file.close()
        #cha stands for change
        def cha():
            changetext = 'True'
            file= open('change.txt','w')
            file.write(changetext)
            file.close()
            file = open('change.txt','r')
            movie = file.read()
            file.close()
        #stops all the user from changing/moving the hands
        def stop():
            movie = 'False'
            file= open('com.txt','w')
            file.write(movie)
            file.close()
            file = open('com.txt','r')
            movie = file.read()
            file.close()
            changetext = 'False'
            file= open('change.txt','w')
            file.write(changetext)
            file.close()
            file = open('change.txt','r')
            movie = file.read()
            file.close()
        def create_window():
            global window
            window = tk.Toplevel(root)
            window.title("CHANGER")
            corhand1 = 0
            def wrist():
                wristroot = tk.Toplevel(root)
                wristroot.configure(bg = "white")
                wristroot.title("Translate")

                def up():
                    global uph1
                    uph1 += 1
                    if uph1 == 3:
                        uph1 = 0
                    changeimagesonwrist()
                def angl():
                    global anglh1
                    anglh1 += 1
                    if anglh1 == 2:
                        anglh1 = 0
                    changeimagesonwrist()
                def sid():
                    global sidh1
                    sidh1 += 1
                    if sidh1 == 3:
                        sidh1 = 0
                    changeimagesonwrist()
                def up2():
                    global uph2
                    uph2 += 1
                    if uph2 == 3:
                        uph2 = 0
                    changeimagesonwrist2()
                def angl2():
                    global anglh2
                    anglh2 += 1
                    if anglh2 == 2:
                        anglh2 = 0
                    changeimagesonwrist2()
                def sid2():
                    global sidh2
                    sidh2 += 1
                    if sidh2 == 3:
                        sidh2 = 0
                    changeimagesonwrist2()

                def changeimagesonwrist():
                    if uph1 == 0 and sidh1 == 1 and anglh1 == 0:
                        canvwrtis.itemconfigure(wrist1, image = image3041)
                    elif uph1 == 0 and sidh1 == 2 and anglh1 == 0:
                        canvwrtis.itemconfigure(wrist1, image = image3042)
                    elif sidh1 == 1 and uph1 == 1 and anglh1 == 0:
                        canvwrtis.itemconfigure(wrist1, image = image3141)
                    elif uph1 == 1 and sidh1 == 0 and anglh1 == 0:
                        canvwrtis.itemconfigure(wrist1, image = image3140)
                    elif uph1 == 2 and sidh1 == 1 and anglh1 == 1:
                        canvwrtis.itemconfigure(wrist1, image = image3241)
                    elif uph1 == 2 and sidh1 == 2 and anglh1 == 0:
                        canvwrtis.itemconfigure(wrist1, image = image3242)
                    elif uph1 == 2 and sidh1 == 2 and anglh1 == 1:
                        canvwrtis.itemconfigure(wrist1, image = image3241)
                    elif (uph1 == 2 and sidh1 == 0) or (uph1 == 0 and sidh1 == 0):
                        pass
                    elif uph1 == 1 and sidh1 == 2 and anglh1 == 0:
                        canvwrtis.itemconfigure(wrist1, image = image120)
                    elif anglh1 == 1 and sidh1 == 0:
                        canvwrtis.itemconfigure(wrist1, image = image2140)
                    elif anglh1 == 1 and sidh1 == 1:
                        canvwrtis.itemconfigure(wrist1, image = image2141)
                    elif anglh1 == 1 and uph1 == 0:
                        canvwrtis.itemconfigure(wrist1, image = image2141)
                    elif anglh1 == 1 and uph1 == 1:
                        canvwrtis.itemconfigure(wrist1, image = image2142)
                    elif anglh1 == 1 and uph1 == 2:
                        pass
                    autocorrect[11] = anglh1
                    autocorrect[12] = uph1
                    autocorrect[13] = sidh1
                    auto()

                def changeimagesonwrist2():
                    if uph2 == 0 and sidh2 == 1 and anglh2 == 0:
                        canvwrtis.itemconfigure(wrist2, image = image3041)
                    elif uph2 == 0 and sidh2 == 2 and anglh2 == 0:
                        canvwrtis.itemconfigure(wrist2, image = image3042)
                    elif sidh2 == 1 and uph2 == 1 and anglh2 == 0:
                        canvwrtis.itemconfigure(wrist2, image = image3141)
                    elif uph2 == 1 and sidh2 == 0 and anglh2 == 0:
                        canvwrtis.itemconfigure(wrist2, image = image3140)
                    elif uph2 == 2 and sidh2 == 1 and anglh2 == 1:
                        canvwrtis.itemconfigure(wrist2, image = image3241)
                    elif uph2 == 2 and sidh2 == 2 and anglh2 == 0:
                        canvwrtis.itemconfigure(wrist2, image = image3242)
                    elif uph2 == 2 and sidh2 == 2 and anglh2 == 1:
                        canvwrtis.itemconfigure(wrist2, image = image3241)
                    elif (uph2 == 2 and sidh2 == 0) or (uph2 == 0 and sidh2 == 0):
                        pass
                    elif uph2 == 1 and sidh2 == 2 and anglh2 == 0:
                        canvwrtis.itemconfigure(wrist2, image = image120)
                    elif anglh2 == 1 and sidh2 == 0:
                        canvwrtis.itemconfigure(wrist2, image = image2140)
                    elif anglh2 == 1 and sidh2 == 1:
                        canvwrtis.itemconfigure(wrist2, image = image2141)
                    elif anglh2 == 1 and uph2 == 0:
                        canvwrtis.itemconfigure(wrist2, image = image2141)
                    elif anglh2 == 1 and uph2 == 1:
                        canvwrtis.itemconfigure(wrist2, image = image2142)
                    elif anglh2 == 1 and uph2 == 2:
                        pass
                #actual app framework
                frame = tk.Frame(bd=0)
                frame.grid()

                wristroot.minsize(660,525)
                wristroot.maxsize(660,525)
                #person
                canvwrtis = tk.Canvas(wristroot,bg = "white",height=450,width = 412,bd=0,highlightthickness=0)
                canvwrtis.grid(column = 1,row = 0)
                uprot = tk.Button(wristroot, text = "Vertical rotation", command = up)
                anglrot = tk.Button(wristroot, text = "Angular rotation", command = angl)
                sidrot = tk.Button(wristroot, text = "Sideways rotation", command = sid)
                uprot.grid(column= 0,row = 1)
                anglrot.grid(column= 0,row =2)
                sidrot.grid(column= 0,row = 3)
                uprot2 = tk.Button(wristroot, text = "Vertical rotation", command = up2)
                anglrot2 = tk.Button(wristroot, text = "Angular rotation", command = angl2)
                sidrot2 = tk.Button(wristroot, text = "Sideways rotation", command = sid2)
                uprot2.grid(column= 2,row = 1)
                anglrot2.grid(column= 2,row =2)
                sidrot2.grid(column= 2,row = 3)
                g = tk.Label(wristroot,text = "Right")
                g.grid(column= 0,row = 0)
                r = tk.Label(wristroot,text = "Left")
                r.grid(column= 2,row = 0)
                #412,77,206,338.5


                wrist1 = canvwrtis.create_image(128,225,image=image120)
                wrist2 = canvwrtis.create_image(325,225,image=image120)


            def finger():
                global image0,image1,image3,image4,image5,image6,image7
                fingertop = tk.Toplevel(root)
                def getnextorigin(event):
                    global rotation,whatchanged,imagechange,special,wait
                    x = event.x
                    y = event.y
                    if wait == 0:
                        wait = 1
                        file = open('variables.txt','r')
                        rotation,special = file.read().split()
                        file.close()
                        rotation = list(rotation.split(","))
                        special = list(special.split(","))
                        for i in range(0, len(rotation)): 
                            rotation[i] = int(rotation[i]) 
                        for i in range(0, len(special)): 
                            special[i] = int(special[i]) 
                        if x < coordinates_of_all[0][0]+10 and x > coordinates_of_all[0][0]-10 and y < coordinates_of_all[0][1]+16 and y > coordinates_of_all[0][1]-16:
                            objectr = finger1
                            acnum = 0
                            if rotation[0] ==5:
                                rotation[0] = 0
                            else:
                                rotation[0] = rotation[0]+1
                            whatchanged = 0
                        elif x < coordinates_of_all[1][0]+10 and x > coordinates_of_all[1][0]-10 and y < coordinates_of_all[1][1]+16 and y > coordinates_of_all[1][1]-16:
                            objectr = finger2
                            acnum = 1
                            if rotation[1] ==5:
                                rotation[1] = 0
                            else:
                                rotation[1] = rotation[1]+1
                            whatchanged = 1
                        elif x < coordinates_of_all[2][0]+10 and x > coordinates_of_all[2][0]-10 and y < coordinates_of_all[2][1]+16 and y > coordinates_of_all[2][1]-16:
                            objectr = finger3
                            acnum = 2
                            if rotation[2] ==5:
                                rotation[2] = 0
                            else:
                                rotation[2] = rotation[2]+1
                            whatchanged = 2
                        elif x < coordinates_of_all[3][0]+10 and x > coordinates_of_all[3][0]-10 and y < coordinates_of_all[3][1]+16 and y > coordinates_of_all[3][1]-16:
                            objectr = finger4
                            acnum = 3
                            if rotation[3] ==5:
                                rotation[3] = 0
                            else:
                                rotation[3] = rotation[3]+1
                            whatchanged = 3
                        elif x > coordinates_of_all[4][0]-32 and x < coordinates_of_all[4][0]-10 and y < coordinates_of_all[4][1]+10 and y > coordinates_of_all[4][1]-10:
                            objectr = finger5
                            acnum = 4
                            if rotation[4] ==2:
                                rotation[4] = 0
                            else:
                                rotation[4] = rotation[4]+1

                            whatchanged =4
                            autocorrect[5] = rotation[4]
                        elif x < coordinates_of_all[5][0]+10 and x > coordinates_of_all[5][0]-10 and y < coordinates_of_all[5][1]+16 and y > coordinates_of_all[5][1]-16:
                            objectr = finger1h2
                            acnum = 0
                            if special[0] ==5:
                                special[0] = 0
                            else:
                                special[0] = special[0]+1
                            whatchanged = 5
                        elif x < coordinates_of_all[6][0]+10 and x > coordinates_of_all[6][0]-10 and y < coordinates_of_all[6][1]+16 and y > coordinates_of_all[6][1]-16:
                            objectr = finger2h2
                            acnum = 1
                            if special[1] ==5:
                                special[1] = 0
                            else:
                                special[1] = special[1]+1
                            whatchanged = 6
                        elif x < coordinates_of_all[7][0]+10 and x > coordinates_of_all[7][0]-10 and y < coordinates_of_all[7][1]+16 and y > coordinates_of_all[7][1]-16:
                            objectr = finger3h2
                            acnum = 2
                            if special[2] ==5:
                                special[2] = 0
                            else:
                                special[2] = special[2]+1
                            whatchanged = 7
                        elif x < coordinates_of_all[8][0]+10 and x > coordinates_of_all[8][0]-10 and y < coordinates_of_all[8][1]+16 and y > coordinates_of_all[8][1]-16:
                            objectr = finger4h2
                            acnum = 3
                            if special[3] ==5:
                                special[3] = 0
                            else:
                                special[3] = special[3]+1
                            whatchanged = 8
                        elif x > coordinates_of_all[9][0]-32 and x < coordinates_of_all[9][0]-10 and y < coordinates_of_all[9][1]+10 and y > coordinates_of_all[9][1]-10:
                            objectr = finger5h2
                            acnum = 4
                            if special[4] ==2:
                                special[4] = 0
                            else:
                                special[4] = special[4]+1
                            whatchanged =9
                            autocorrect[5] = rotation[4]
                        else:
                            objectr = 0
                            acnum = 0
                            
                        if not(objectr ==0) and not(objectr == finger5) and whatchanged < 5:
                            if rotation[whatchanged] ==  0:
                                imagechange = image0
                                autocorrect[acnum] = 0
                            elif rotation[whatchanged] == 1:
                                imagechange = image1
                                autocorrect[acnum] = 1
                            elif rotation[whatchanged] == 2:
                                imagechange = image1
                                autocorrect[acnum] = 2
                            elif rotation[whatchanged] == 3:
                                imagechange = image3
                                autocorrect[acnum] = 3
                            elif rotation[whatchanged] == 4:
                                imagechange = image4
                                autocorrect[acnum] = 4
                            elif rotation[whatchanged] == 5:
                                imagechange = image5
                                autocorrect[acnum] = 5
                            ee.itemconfigure(objectr, image = imagechange)
                            ee.update()
                            changeimage(rotation,0)

                        if not(objectr ==0) and not(objectr == finger5h2) and whatchanged >= 5:
                            whatchanged -= 5
                            if special[whatchanged] ==  0:
                                imagechange = image0
                                autocorrect[acnum] = 0
                            elif special[whatchanged] == 1:
                                imagechange = image1
                                autocorrect[acnum] = 1
                            elif special[whatchanged] == 2:
                                imagechange = image1
                                autocorrect[acnum] = 2
                            elif special[whatchanged] == 3:
                                imagechange = image3
                                autocorrect[acnum] = 3
                            elif special[whatchanged] == 4:
                                imagechange = image4
                                autocorrect[acnum] = 4
                            elif special[whatchanged] == 5:
                                imagechange = image5
                                autocorrect[acnum] = 5
                            ee.itemconfigure(objectr, image = imagechange)
                            ee.update()
                            changeimage(special,1)
                        if objectr == finger5:
                            if rotation[whatchanged] ==  1:
                                ee.move(objectr,5,0) #move object
                                coordinates_of_all[4][0] = 155+41+5
                                coordinates_of_all[4][1] = 150+25
                            elif rotation[whatchanged] == 0:
                                ee.move(objectr,-10,0)
                                coordinates_of_all[4][0] = 155+41-5
                                coordinates_of_all[4][1] = 150+25
                            elif rotation[whatchanged] == 2:
                                ee.move(objectr,5,0)
                                coordinates_of_all[4][0] = 155+41
                                coordinates_of_all[4][1] = 150+25
                        try:
                            whatchanged-=5
                        except:
                            pass
                        if objectr == finger5h2:
                            if special[whatchanged] ==  1:
                                ee.move(objectr,5,0) #move object
                                coordinates_of_all[9][0] = 455+41+5
                                coordinates_of_all[9][1] = 150+25
                            elif special[whatchanged] == 0:
                                ee.move(objectr,-10,0)
                                coordinates_of_all[9][0] = 455+41-5
                                coordinates_of_all[9][1] = 150+25
                            elif special[whatchanged] == 2:
                                ee.move(objectr,5,0)
                                coordinates_of_all[9][0] = 455+41
                                coordinates_of_all[9][1] = 150+25
                        auto()
                        

                        file= open('variables.txt','w')
                        sep = ','
                        for i in rotation:
                            rotation[rotation.index(i)] = str(i)
                        rotation = sep.join(rotation)
                        file.write(rotation)
                        for i in special:
                            special[special.index(i)] = str(i)
                        special = sep.join(special)
                        file.write("\n")
                        file.write(special)
                        file.close()
                        wait = 0
                
                def getother(event):
                    global special
                    x = event.x
                    y = event.y
                    file = open('variables.txt','r')
                    rotation,special = file.read().split()
                    file.close()
                    rotation = list(rotation.split(","))
                    special = list(special.split(","))
                    for i in range(0, len(rotation)): 
                        rotation[i] = int(rotation[i]) 
                    for i in range(0, len(special)): 
                        special[i] = int(special[i])
                    if x < coordinates_of_all[0][0]+10 and x > coordinates_of_all[0][0]-10 and y < coordinates_of_all[0][1]+16 and y > coordinates_of_all[0][1]-16:
                        objectr = finger1
                        acnum = 0
                        if special[0] ==1:
                            special[0] = 0
                        else:
                            special[0] = special[0]+1
                        whatchanged = 0
                    elif x < coordinates_of_all[1][0]+10 and x > coordinates_of_all[1][0]-10 and y < coordinates_of_all[1][1]+16 and y > coordinates_of_all[1][1]-16:
                        objectr = finger2
                        acnum = 1
                        if special[1] ==1:
                            special[1] = 0
                        else:
                            special[1] = special[1]+1
                        whatchanged = 1
                    elif x < coordinates_of_all[2][0]+10 and x > coordinates_of_all[2][0]-10 and y < coordinates_of_all[2][1]+16 and y > coordinates_of_all[2][1]-16:
                        objectr = finger3
                        acnum = 2
                        if special[2] ==1:
                            special[2] = 0
                        else:
                            special[2] = special[2]+1
                        whatchanged = 2
                    elif x < coordinates_of_all[3][0]+10 and x > coordinates_of_all[3][0]-10 and y < coordinates_of_all[3][1]+16 and y > coordinates_of_all[3][1]-16:
                        objectr = finger4
                        acnum = 3
                        if special[3] ==1:
                            special[3] = 0
                        else:
                            special[3] = special[3]+1
                        whatchanged = 3
                    elif x < coordinates_of_all[4][0]+16 and x > coordinates_of_all[4][0]-16 and y < coordinates_of_all[4][1]+10 and y > coordinates_of_all[4][1]-10:
                        whatchanged = 4
                        objectr = finger5
                        acnum = 4
                        if special[4] ==3:
                            special[4] = 0
                        else:
                            special[4] = special[4]+1

                    file= open('variables.txt','w')
                    sep = ','
                    for i in rotation:
                        rotation[rotation.index(i)] = str(i)
                    rotation = sep.join(rotation)
                    file.write(rotation)
                    for i in special:
                        special[special.index(i)] = str(i)
                    special = sep.join(special)
                    file.write("\n")
                    file.write(special)
                    file.close()


                rotation = [0,0,0,0,2]
                special = [0,0,0,0,0]
                coordinates_of_all= [[150-24,150+10],[150-9,150+7],[150+6,150+6],[150+21,150+6],[155+41+5,150+25],[450-24,150+10],[450-9,150+7],[450+6,150+6],[450+21,150+6],[455+41+5,150+25]]
                fingertop.bind("<Button 1>",getnextorigin)
                fingertop.bind("<Button 2>",getother)

                fingertop.maxsize(width=600, height=300)
                fingertop.minsize(width=600, height=300)
                #actual app framework
                frame = tk.Frame(bd=0)
                frame.grid()

                ee = tk.Canvas(fingertop,bg = "green",bd=0,highlightthickness=0,height=300,width = 600)
                ee.grid()
                pilImage0 = Image.open("0.png")
                pilImage1 = Image.open("1.png")
                pilImage3 = Image.open("3.png")
                pilImage4 = Image.open("4.png")
                pilImage5 = Image.open("5.png")
                pilImage6 = Image.open("thumb.png")
                pilImage7 = Image.open("wrist.png")
                pilImage0 = pilImage0.resize((20, 33), Image.ANTIALIAS)
                pilImage1 = pilImage1.resize((20, 33), Image.ANTIALIAS)  
                pilImage3 = pilImage3.resize((20, 33), Image.ANTIALIAS)
                pilImage4 = pilImage4.resize((20, 33), Image.ANTIALIAS)
                pilImage5 = pilImage5.resize((20, 60), Image.ANTIALIAS)
                pilImage6 = pilImage6.resize((33,20), Image.ANTIALIAS)
                pilImage7 = pilImage7.resize((69, 51), Image.ANTIALIAS)
                image0= ImageTk.PhotoImage(pilImage0)
                image1= ImageTk.PhotoImage(pilImage1)
                image3= ImageTk.PhotoImage(pilImage3)
                image4= ImageTk.PhotoImage(pilImage4)
                image5= ImageTk.PhotoImage(pilImage5)
                image6= ImageTk.PhotoImage(pilImage6)
                image7= ImageTk.PhotoImage(pilImage7)


                finger6 = ee.create_image(150,150+40,image=image7)
                finger1 = ee.create_image(150-24,150+10,image=image0)
                finger2 = ee.create_image(150-9,150+7,image=image0)
                finger3 = ee.create_image(150+6,150+6,image=image0)
                finger4 = ee.create_image(150+21,150+6,image=image0)
                finger5 = ee.create_image(155+21+5,150+25,image=image6)

                finger6h2 = ee.create_image(450,150+40,image=image7)
                finger1h2 = ee.create_image(450-24,150+10,image=image0)
                finger2h2 = ee.create_image(450-9,150+7,image=image0)
                finger3h2 = ee.create_image(450+6,150+6,image=image0)
                finger4h2 = ee.create_image(450+21,150+6,image=image0)
                finger5h2 = ee.create_image(455+21+5,150+25,image=image6)
                """
                """


            button = tk.Button(window, text="finger", command=finger)
            button.grid(row = 1,column = 0) 
            button = tk.Button(window, text="wrist", command=wrist)
            button.grid(row = 2,column = 0) 
            #button = tk.Button(window, text="arm", command=arm)
            #button.grid(row = 3,column = 0) 
                
            
        def close():
            window.destroy()
        global top,opened,change
        top = tk.Toplevel() #initialising top level
        opened = True #opened the toplevel == true
        top.title("EDITOR") 
        msg = tk.Message(top, text="oh") #placeholder for text
        msg.grid(row = 0,column = 1)  
        button = tk.Button(top, text="move", command=moo)
        button.grid(row = 1,column = 0) 
        button = tk.Button(top, text="change", command=create_window)
        button.grid(row = 2,column = 0)
        button = tk.Button(top, text="stop", command=stop)
        button.grid(row = 1,column = 2)
        button = tk.Button(top, text="stop", command=stop and close)
        button.grid(row = 2,column = 2)
        root.wait_window(top)  #waits for the toplevel to close, then runs the code below
        opened = False #toplevel closed
    x = eventorigin.x
    y = eventorigin.y
    displaytext()
    
        

        
    if once == 1:    #this piece of code is supposed to run once to define it within the function
        once = 2
        #move = False
        clicked = False
        toplevel() # runs toplevel() function upon a click

    if not(opened == True) and not(once == 2): #checks if toplevel closed
        toplevel()
    else:
        once = 0 
        #what happens if once == 2 meaning 1st instance toplevel() is open
    
    clicks += 1 #count clicks for movement purposes

    #checking if click is withtin cordinates of 1st hand
    if x>=corhand1[0] and x <=corhand1[2] and y >=corhand1[1] and y <= corhand1[3] and clicked == False and movie == 'True':
        clicked = True
        objekt =  "hand1"
        cord = corhand1 #cord stands for coordinates
        clicks = 1

    #checking if click is withtin cordinates of 2nd hand
    elif x>=corhand2[0] and x <=corhand2[2] and y >=corhand2[1] and y <= corhand2[3] and clicked == False and movie == 'True':
        clicked = True
        objekt = "hand2"
        cord = corhand2 #cord stands for coordinates
        clicks = 1

    #e.itemconfigure(hand1, image = image2)  

    #my code knows you want to move object
    if clicks >= 2 and clicked == True and movie == 'True' and y<300:
        if objekt == "hand1":
            e.move(objekt,x-cord[4],y-cord[5])
            e.move(fingerhand1,x-cord[4],y-cord[5])
            e.move(finger1hand1,x-cord[4],y-cord[5])
            e.move(finger2hand1,x-cord[4],y-cord[5])
            e.move(finger3hand1,x-cord[4],y-cord[5])
            e.move(finger4hand1,x-cord[4],y-cord[5])
            e.move(finger5hand1,x-cord[4],y-cord[5]) #move object
        else:
            e.move(objekt,x-cord[4],y-cord[5])
            e.move(fingerhand2,x-cord[4],y-cord[5])
            e.move(finger1hand2,x-cord[4],y-cord[5])
            e.move(finger2hand2,x-cord[4],y-cord[5])
            e.move(finger3hand2,x-cord[4],y-cord[5])
            e.move(finger4hand2,x-cord[4],y-cord[5])
            e.move(finger5hand2,x-cord[4],y-cord[5])
        e.move(objekt,x-cord[4],y-cord[5]) #move object
        e.update()
        #amount_of_move = [x-cord[4],y-cord[5]]
        #uses global at the top of getorigin()
        if objekt == "hand1":
            var = int(((300-y)**2 + (129-x)**2)**(1/2))
            pilImagearm1 = Image.open("150.png")
            try:
                angle1 = 90-math.degrees(math.atan((300-y)/abs(129-x)))
            except:
                angle1 = 0
            if x > 129:
                angle1 = -angle1
            pilImagearm1= pilImagearm1.resize((25,abs(var)), Image.ANTIALIAS)
            pilImagearm1 = pilImagearm1.rotate(angle1, Image.NEAREST, expand = 1)
            imagearm1 = ImageTk.PhotoImage(pilImagearm1)
            arminimage1 = e.create_image(129-((129-x)/2),310-((300-y)/2),image=imagearm1)
            
            e.image1 = imagearm1
            e.update()
        else:

            var = int(((300-y)**2 + (283-x)**2)**(1/2))

            pilImagearm2= Image.open("150.png")
            try:
                angle2 = 90-math.degrees(math.atan((300-y)/abs(283-x)))
            except:
                angle2 = 0
            if x > 283:
                angle2 = -angle2
            pilImagearm2 = pilImagearm2.resize((25,abs(var)), Image.ANTIALIAS)

            pilImagearm2 = pilImagearm2.rotate(angle2, Image.NEAREST, expand = 1)
            imagearm2 = ImageTk.PhotoImage(pilImagearm2)
            arminimage2 = e.create_image(283-((283-x)/2),310-((300-y)/2),image=imagearm2)
            e.image2 = imagearm2
            e.update()

        finalcoordx = []
        finalcoordy = []
        xcoord = [0,206/3,412/3,206,824/3,1030/3,412]
        ycoord = [300,225,150,75,0]
        for i in xcoord:
            if x < i:
                finalcoordx.append(xcoord.index(i)-1)
        for i in ycoord:
            if y > i:
                finalcoordy.append(ycoord.index(i)-1)
        if finalcoordx == []:
            finalcoordx.append("0")
        if finalcoordy == []:
            finalcoordy.append("0")
        if objekt == "hand1":
            if angle1 > -20 and angle1 < 15:
                armrot = 0
            elif angle1 > 15 and angle1 < 45:
                armrot = 1
            elif angle1 > 55 and angle1 < 90:
                armrot = 2
            else:
                armrot =0
        else:
            if angle2 > -20 and angle2 < 15:
                armrot = 0
            elif angle2 > 15 and angle2 < 45:
                armrot = 1
            elif angle2 > 55 and angle2 < 90:
                armrot = 2
            else:
                armrot =0
        autocorrect[17] = finalcoordx[0]
        autocorrect[18] = finalcoordy[0]
        autocorrect[14] = armrot
        finalcoordx = []
        finalcoordy = []
        auto()
        cord = [x-25,y-25,x+25,y+25,x,y] #update coordinates
        if objekt == "hand1":
            corhand1=cord
        elif objekt == "hand2":
            corhand2=cord
        clicks = 0 #reset clicks
        clicked = False #reset clicks


#pilImage10 = pilImage10.rotate(90, Image.NEAREST, expand = 1)
        #283,338.5
        

            
        

"""
        def coox():
            xcoord = [0,206/3,412/3,206,824/3,1030/3]
            for i in xcoord:
                if i < x:
                    return(xcoord.index(i))
                    break
        def cooy():
            ycoord = [300,225,150,75]
            for i in ycoord:
                if i < y:
                    return(ycoord.index(i))
                    break
"""
    #changing
    #if changetext == 'True':
        
    

root.bind("<Button 1>",getorigin)

#actual app framework
frame = tk.Frame(bg = "black",bd=0)
frame.grid()

root.minsize(412,732)
root.maxsize(412,732)

#text edit
w = tk.Canvas(root,bg = "black",height=290,width = 412,bd=0,highlightthickness=0)
w.grid(row = 0)
thetext4 = w.create_text(210,50,fill="white",font="Times 20 italic bold",text="")
thetext5 = w.create_text(210,90,fill="white",font="Times 20 italic bold",text="")
thetext6 = w.create_text(210,130,fill="white",font="Times 20 italic bold",text="")
thetext7 = w.create_text(210,170,fill="white",font="Times 20 italic bold",text="")
thetext8 = w.create_text(210,210,fill="white",font="Times 20 italic bold",text="")
thetext9 = w.create_text(210,250,fill="white",font="Times 20 italic bold",text="")

pilImagebtn = Image.open("button.png")
pilImagebtn = pilImagebtn.resize((80, 50), Image.ANTIALIAS)
imagebtn = ImageTk.PhotoImage(pilImagebtn)
clearb = tk.Button(w,command=clear)
clearb.configure(image=imagebtn, fg="blue",bd=0)
clearb_window=w.create_window(350, 250, window=clearb)

#entry1 = tk.Entry (root) 
#canvas1.create_window(200, 140, window=entry1)
#thetext4 = w.create_text(73,30,fill="white",font="Times 20 italic bold",text="")
#autocorrect
t = tk.Canvas(root,bg = "blue",height=65,width = 412,bd=0,highlightthickness=0)
t.grid(row = 1)
thetext1 = t.create_text(73,30,fill="white",font="Times 20 italic bold",text="")
thetext2 = t.create_text(210,30,fill="white",font="Times 20 italic bold",text="")
thetext3 = t.create_text(345,30,fill="white",font="Times 20 italic bold",text="")

#thetext1 = t.create_text(73,30,fill="white",font="Times 20 italic bold",text="")
#thetext2 = t.create_text(210,30,fill="white",font="Times 20 italic bold",text="")
#thetext3 = t.create_text(345,30,fill="white",font="Times 20 italic bold",text="")


#person
e = tk.Canvas(root,bg = "brown",height=377,width = 412,bd=0,highlightthickness=0)
e.grid(row = 2)

#412,77,206,338.5

'''
#Grid
zerozero = e.create_rectangle(0,300,206/3,225, fill='cyan')
zeroone = e.create_rectangle(0,225,206/3,150, fill='purple')
zerotwo = e.create_rectangle(0,150,206/3,75, fill = 'cyan')
zerothree = e.create_rectangle(0,75,206/3,0, fill='purple')
onezero = e.create_rectangle(206/3,300,412/3,225, fill='purple')
oneone = e.create_rectangle(206/3,225,412/3,150, fill='cyan')
onetwo = e.create_rectangle(206/3,150,412/3,75, fill = 'purple')
onethree = e.create_rectangle(206/3,75,412/3,0, fill='cyan')
twozero = e.create_rectangle(412/3,300,206,225, fill='cyan')
twoone = e.create_rectangle(412/3,225,206,150, fill='purple')
twotwo = e.create_rectangle(412/3,150,206,75, fill='cyan')
twothree = e.create_rectangle(412/3,75,206,0, fill='purple')
threezero = e.create_rectangle(206,300,824/3,225, fill='purple')
threeone = e.create_rectangle(206,225,824/3,150, fill='cyan')
threetwo = e.create_rectangle(206,150,824/3,75, fill='purple')
threethree = e.create_rectangle(206,75,824/3,0, fill='cyan')
fourzero = e.create_rectangle(824/3,300,1030/3,225, fill='cyan')
fourone = e.create_rectangle(824/3,225,1030/3,150, fill='purple')
fourtwo = e.create_rectangle(824/3,150,1030/3,75, fill='cyan')
fourthree = e.create_rectangle(824/3,75,1030/3,0, fill='purple')
fivezero = e.create_rectangle(1030/3,300,412,225, fill='purple')
fivezero = e.create_rectangle(1030/3,225,412,150, fill='cyan')
fivezero = e.create_rectangle(1030/3,150,412,75, fill='purple')
fivezero = e.create_rectangle(1030/3,75,412,0, fill='cyan')
'''

pilImage0 = Image.open("0.png")
pilImage0 = pilImage0.resize((10, 17), Image.ANTIALIAS)
image0 = ImageTk.PhotoImage(pilImage0)

pilImage1 = Image.open("1.png")
pilImage1 = pilImage1.resize((10, 17), Image.ANTIALIAS)  
image1 = ImageTk.PhotoImage(pilImage1)  #yaxisup

pilImage3 = Image.open("3.png")
pilImage3 = pilImage3.resize((10, 17), Image.ANTIALIAS)
image3 = ImageTk.PhotoImage(pilImage3) 

pilImage4 = Image.open("4.png")
pilImage4 = pilImage4.resize((10, 17), Image.ANTIALIAS)
image4 = ImageTk.PhotoImage(pilImage4) 

pilImage5 = Image.open("5.png")
pilImage5 = pilImage5.resize((10, 30), Image.ANTIALIAS)
image5 = ImageTk.PhotoImage(pilImage5)

pilImage6 = Image.open("thumb.png")
pilImage6 = pilImage6.resize((17,10), Image.ANTIALIAS)
image6= ImageTk.PhotoImage(pilImage6)

pilImage7 = Image.open("wrist.png")
pilImage7 = pilImage7.resize((34, 25), Image.ANTIALIAS)
image7= ImageTk.PhotoImage(pilImage7)

pilImagegirl = Image.open("girl.png")
pilImagegirl = pilImagegirl.resize((400, 377), Image.ANTIALIAS)
imagegirl = ImageTk.PhotoImage(pilImagegirl)

pilImage120 = Image.open("120.png")
pilImage120 = pilImage120.resize((200, 200), Image.ANTIALIAS)
image120 = ImageTk.PhotoImage(pilImage120)

pilImage150 = Image.open("150.png")
pilImage150 = pilImage150.resize((111,200), Image.ANTIALIAS)
image150 = ImageTk.PhotoImage(pilImage150)

pilImage2140 = Image.open("121140.png")
pilImage2140 = pilImage2140.resize((200, 200), Image.ANTIALIAS)
image2140 = ImageTk.PhotoImage(pilImage2140)

pilImage3041 = Image.open("130141.png")
pilImage3041 = pilImage3041.resize((200, 200), Image.ANTIALIAS)
image3041 = ImageTk.PhotoImage(pilImage3041)

pilImage3042 = Image.open("130142.png")
pilImage3042 = pilImage3042.resize((200, 200), Image.ANTIALIAS)
image3042 = ImageTk.PhotoImage(pilImage3042)

pilImage3140 = Image.open("131140.png")
pilImage3140 = pilImage3140.resize((200, 200), Image.ANTIALIAS)
image3140 = ImageTk.PhotoImage(pilImage3140)

pilImage3241 = Image.open("132141.png")
pilImage3241 = pilImage3241.resize((200, 200), Image.ANTIALIAS)
image3241 = ImageTk.PhotoImage(pilImage3241)

pilImage3242 = Image.open("132142.png")
pilImage3242 = pilImage3242.resize((200, 200), Image.ANTIALIAS)
image3242 = ImageTk.PhotoImage(pilImage3242)

pilImage3141 = Image.open("131141.png")
pilImage3141 = pilImage3141.resize((200, 200), Image.ANTIALIAS)
image3141 = ImageTk.PhotoImage(pilImage3141)

pilImage2142 = Image.open("121142.png")
pilImage2142 = pilImage2142.resize((200, 200), Image.ANTIALIAS)
image2142 = ImageTk.PhotoImage(pilImage2142)

pilImage2141 = Image.open("121141.png")
pilImage2141 = pilImage2141.resize((200, 200), Image.ANTIALIAS)
image2141 = ImageTk.PhotoImage(pilImage2141)

pilImageback = Image.open("piback.png")
pilImageback = pilImageback.resize((412, 377), Image.ANTIALIAS)
imageback = ImageTk.PhotoImage(pilImageback)

#pilImage10 = pilImage10.rotate(90, Image.NEAREST, expand = 1)


#pilImage10 = pilImage10.rotate(90, Image.NEAREST, expand = 1)

#button1 = tk.Button(w, image = image, command = root.quit)
#button1.configure(highlightbackground='',bd=0)
#button1_window = w.create_window(200, 200, window=button1)
back = e.create_image(206,188.5,image=imageback)
girl = e.create_image(206,188.5,image=imagegirl)
#a = e.create_rectangle(0,300,412,377, fill='red', alpha=.5)
fingerhand1 = e.create_image(129,318.5+25,image=image7)
finger1hand1 = e.create_image(129-12,318.5+10,image=image0)
finger2hand1 = e.create_image(129-4,318.5+7,image=image0)
finger3hand1 = e.create_image(129+3,318.5+6,image=image0)
finger4hand1 = e.create_image(129+10,318.5+6,image=image0)
finger5hand1 = e.create_image(129+8,318.5+15,image=image6)

e.fingerhand1 = image7
e.finger1hand1 = image0
e.finger2hand1 = image0
e.finger3hand1 = image0
e.finger4hand1 = image0
e.finger5hand1 = image6

fingerhand2 = e.create_image(283,318.5+25,image=image7)
finger1hand2 = e.create_image(283-11,318.5+10,image=image0)
finger2hand2 = e.create_image(283-4,318.5+7,image=image0)
finger3hand2 = e.create_image(283+3,318.5+6,image=image0)
finger4hand2 = e.create_image(283+10,318.5+6,image=image0)
finger5hand2 = e.create_image(283+8,318.5+15,image=image6)

e.fingerhand2 = image7
e.finger1hand2 = image0
e.finger2hand2 = image0
e.finger3hand2 = image0
e.finger4hand2 = image0
e.finger5hand2 = image6

corhand1 = [104,313.5,154,363.5,129,338.5] #min x,min y, max x,max y , mid x, mid y
corhand2 = [258,313.5,308,363.5,283,338.5]

root.mainloop()
movie = 'False'
file= open('com.txt','w')
file.write(movie)
file.close()
file= open('variables.txt','w')
file.write("0,0,0,0,2")
file.write("\n")
file.write("0,0,0,0,0")
file.close()
