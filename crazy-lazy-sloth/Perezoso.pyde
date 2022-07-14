def setup():
    size (600, 600)

def draw():
    for i in range(10) :
        background(random(255),random(255),random(255))
        noLoop()
        
        solveChooseBackgrounds()
        solveChooseStructure()
            
        #Draw circle
        noFill()
        stroke (random(255),random(255),random(255))
        x = 400
        for j in range(15):
            circle (300,300,x)
            x = x-1
        
        createImage(i)


####### Methonds to create the images #########
def solveChooseBackgrounds():
    # Choose Background
    chooseBackgrounds = int(random(0, 30))
    randomBackgound = [4,1,2,1,5,4,1,5,1,3,10,6,3,1,2,1,5,1,1,2,1,1,7,1,6,1,9,1,1,8]
    
    if randomBackgound[chooseBackgrounds] == 1:
        backgroudColors()
    elif randomBackgound[chooseBackgrounds] == 2:
        backgroudHappyFaceses()
    elif randomBackgound[chooseBackgrounds] == 3:
        backgroudSuftTable()
    elif randomBackgound[chooseBackgrounds] == 4:
        backgroudMath()
    elif randomBackgound[chooseBackgrounds] == 5:
        backgroudCircles()
    elif randomBackgound[chooseBackgrounds] == 6:
        backgroudForest()
    elif randomBackgound[chooseBackgrounds] == 7:
        backgroudForest2()
    elif randomBackgound[chooseBackgrounds] == 8:
        backgroudPokeBall()
    else:
        backgroudUniverse()
        
        
def solveChooseStructure():
    # Choose Sloth Skin 
    chooseStructure = int(random(0, 40))
    structureRandom = [1,1,2,1,1,1,1,1,1,3,1,1,1,1,2,1,1,1,1,1,1,1,3,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,4]
    
    if structureRandom[chooseStructure] == 1:
        createNormalStructureBody()
    elif structureRandom[chooseStructure] == 2:
        createZombieStructureBody()
    elif structureRandom[chooseStructure] == 3:
        createZebraStructureBody()
    else:
        createGoldStructureBody()
        

##### Create Images #####  
def createImage(i):
    save("Sloth"+ str(i) +".png")
    
########################## Backgrounds ##########################

####### Happy Facesses ########
def backgroudHappyFaceses():
    #Draw circle
    fill(172, 194, 227)
    noStroke()
    circle (300,300,400)
    
    # Face 1
    fill(255, 255, 0)
    stroke(0)
    
    circle (190, 200, 50)
    
    fill(0)
    ellipse (180, 192, 4, 7)
    ellipse (200, 192, 4, 7)
    
    noFill()
    bezier (175, 200, 180, 220, 200, 220, 205, 200)
    line (174, 201, 177, 200)
    line (204, 200, 207, 201)
    
    # Face 2
    fill(255, 255, 0)
    stroke(0)
    
    circle (450, 290, 50)
    
    fill(0)
    ellipse (440, 282, 4, 7)
    ellipse (460, 282, 4, 7)
    
    noFill()
    bezier (435, 290, 440, 310, 460, 310, 465, 290)
    line (434, 291, 437, 290)
    line (464, 290, 467, 291)
    
    # Face 3
    fill(255, 255, 0)
    stroke(0)
    
    circle (140, 300, 50)
    
    fill(0)
    ellipse (130, 292, 4, 7)
    ellipse (150, 292, 4, 7)
    
    noFill()
    bezier (125,300, 130, 320, 150, 320, 155, 300)
    line (124, 301, 127, 300)
    line (154, 300, 157, 301)


####### Color Background ########
def backgroudColors():
    #Draw circle
    fill(random(255),random(255),random(255))
    noStroke()
    circle (300,300,400)
    
####### Surf Table Background ########
def backgroudSuftTable():
    #Draw circle
    fill(108, 190, 250)
    noStroke()
    circle (300,300,400)
    
    fill(231, 201, 30)
    stroke(231, 201, 30)
    circle (190, 170, 50)
    
    fill (7, 101, 170)
    stroke (7, 101, 170)
    bezier (100, 300, 150, 565, 450, 565 , 500, 300)
    
    stroke (255)
    line (200, 310, 250, 310)
    line (350, 310, 400, 310)
    line (250, 320, 300, 320)
    line (100, 320, 230, 320)
    line (420, 320, 480, 320)
    
    stroke (0)
    line (220, 140, 230, 150)
    line (230, 150, 240, 140)
    line (250, 130, 260, 140)
    line (260, 140, 270, 130)
    
    r = random(255)
    g = random(255)
    b = random(255)
    fill(r, g, b)
    ellipse (380, 300, 150, 345)
    fill(255)
    ellipse (380, 300, 130, 340)
    fill(r, g, b)
    rect (375, 130, 10, 340)
    
    
####### Universe Background ########
def backgroudUniverse():
    #Draw circle
    fill(42, 37, 37)
    noStroke()
    circle (300,300,400)
    
    noFill()
    stroke(255)
    ellipse (170, 200, 40, 10)
    circle (170,200, 30)
    
    circle (320,140, 30)
    fill(255)
    ellipse (310, 140, 10, 20)
    ellipse (450, 300, 5, 5)
    ellipse (400, 190, 5, 5)
    ellipse (130, 360, 5, 5)
    
    line (140, 300, 150, 310)
    line (140, 310, 150, 300)
    
    line (250, 150, 260, 160)
    line (250, 160, 260, 150)
    

####### Math Background ########
def backgroudMath():
    #Draw circle
    fill(42, 255, 37)
    noStroke()
    circle (300,300,400)
    
    stroke(255)
    line (120, 300, 140, 320)
    line (120, 320, 140, 300)
    
    line (450, 350, 470, 370)
    line (450, 370, 470, 350)
    
    line (400, 180, 400, 200)
    line (390, 190, 410, 190)
    
    line (150, 250, 150, 270)
    line (140, 260, 160, 260)
    
    line (440, 250, 460, 250)
    
    line (170, 170, 190, 170)
    
####### Forest Background ########
def backgroudForest():
    #Draw circle
    fill(250)
    noStroke()
    circle (300,300,400)

    fill(0, 255, 0)
    ellipse (170, 190, 30, 65)
    stroke(255)
    line (170, 160, 170, 222)
    line (160, 180, 170, 190)
    line (170, 200, 180, 190)
    line (160, 200, 170, 210)
    
    ellipse (270, 135, 30, 65)
    line (270, 105, 270, 167)
    line (260, 125, 270, 135)
    line (270, 145, 280, 135)
    line (260, 145, 270, 155)
    
    ellipse (480, 335, 30, 65)
    line (480, 305, 480, 367)
    line (470, 325, 480, 335)
    line (480, 345, 490, 335)
    line (470, 345, 480, 355)
    
    fill(93, 165, 79 )
    triangle (440, 160, 470, 200, 360, 300)
    triangle (185, 140, 220, 120, 260, 190)
    triangle (420, 140, 440, 160, 360, 190)
    triangle (360, 110, 380, 120, 360, 190)
    triangle (110, 340, 120, 380, 180, 290)
    triangle (110, 260, 105, 290, 180, 295)
    

####### Forest Background ########
def backgroudForest2():
    #Draw circle
    fill(135, 145, 180)
    noStroke()
    circle (300,300,400)
    
    stroke(255)
    ### Rigt Forest ####
    fill(80, 97, 76)
    rect (438, 288, 5, 15)
    triangle (430, 290, 450, 290, 440, 260)
    
    fill(80, 97, 76)
    rect (478, 288, 5, 15)
    triangle (470, 290, 490, 290, 480, 260)
    triangle (470, 275, 490, 275, 480, 240)
    
    fill(80, 97, 76)
    rect (458, 288, 5, 15)
    triangle (450, 290, 470, 290, 460, 260)
    triangle (450, 275, 470, 275, 460, 240)
    triangle (450, 260, 470, 260, 460, 220)
    
    fill(80, 97, 76)
    rect (468, 288, 5, 15)
    triangle (460, 290, 480, 290, 470, 260)
    triangle (460, 275, 480, 275, 470, 240)
    
    ### Left Forest ####
    fill(80, 97, 76)
    rect (158, 288, 5, 15)
    triangle (150, 290, 170, 290, 160, 260)
    
    fill(80, 97, 76)
    rect (118, 288, 5, 15)
    triangle (110, 290, 130, 290, 120, 260)
    triangle (110, 275, 130, 275, 120, 240)
    
    fill(80, 97, 76)
    rect (138, 288, 5, 15)
    triangle (130, 290, 150, 290, 140, 260)
    triangle (130, 275, 150, 275, 140, 240)
    triangle (130, 260, 150, 260, 140, 220)
    
    fill(80, 97, 76)
    rect (128, 288, 5, 15)
    triangle (120, 290, 140, 290, 130, 260)
    triangle (120, 275, 140, 275, 130, 240)
    
    fill (26, 48, 21)
    stroke (26, 48, 21)
    bezier (100, 300, 150, 565, 450, 565 , 500, 300)
    
    fill(240)
    noStroke()
    circle (360, 150, 40)
    circle (200, 170, 7)
    circle (430, 200, 7)
    
####### Pokeball Background ########
def backgroudPokeBall():
    #Draw circle
    fill(255, 0, 0)
    noStroke()
    circle (300,300,400)
    
    fill (255)
    bezier (100, 300, 140, 565, 460, 565 , 500, 300)
    
    fill (50, 50, 50)
    rect (101, 280, 397, 40)
    
    circle (300,300,230)


####### Circles Background ########
def backgroudCircles():
    #Draw circle
    noStroke()
    x = 400
    for i in range (6):
        fill(random(255),random(255),random(255))
        circle (300,300,x)
        x = x -40
    
    
########################## Normal Skin ##########################

###### Normal Head ######
def createNormalHead():
    # Draw head
    fill (129,92,0)
    stroke (129,92,0)
    ellipse (300,280, 240,190)
    triangle (300, 190, 310, 190, 300, 170)
    triangle (290, 190, 300, 190, 290, 170)
    fill (248,237,210)
    stroke (248,237,210)
    ellipse (301, 310, 215, 100)
    bezier(198, 330, 231, 392, 370, 392, 405, 329)
    
    stroke (248,237,210)
    fill (248,237,210)
    bezier(182, 290, 202, 240, 250, 190, 300, 260)
                
    bezier(300, 260, 342, 190, 370, 230, 420, 290) 
    
##### draw Normal Eyes #####    
def createNormalEyes():
    #Draw Eyes
    #left eye
    fill (189,189,189)
    stroke (189,189,189)
    bezier(185, 310, 202, 250, 270, 210, 280, 285)
                
    fill (0)
    ellipse (260, 270, 15, 30)
    fill (255)
    circle (260, 270,7)
        
    #rigth eye
    fill (189,189,189)
    stroke (189,189,189)
    bezier(320, 280, 330, 210, 398, 250, 415, 310)
        
    fill (0)
    ellipse (340,270, 15, 30)
    fill (255)
    circle (340, 270,7)
    
####### Create Color Body #######
def createNormalBody():
    fill (129,92,0)
    stroke (129,92,0)
    ellipse (305, 400, 270, 190)
    ellipse (200, 340, 15, 20)
    
def createNormalNose():
    #Draw nose
    stroke(189,189,189)
    fill (189,189,189)
    ellipse (300, 300, 45,25)
    fill (0)
    ellipse (285, 300, 15,12)
    fill (0)
    ellipse (315, 300, 15,12)
    stroke (0)    
    
##### Create Normal Mouse #####
def createNormalMouse():
    #Draw mouse
    noFill ()
    stroke (0)
    curve(265, 300, 275, 320, 320, 320, 330, 300)
        
    fill (255,0,0)
    stroke (0)
    bezier(285, 323, 295, 333, 305, 333, 315, 323)
    
####### Create Normal Structure Body #######
def createNormalStructureBody():
    
    createNormalBody()

    createNormalHead()
    
    createNormalNose()
    
    #Draw Body
    fill(129,92,0)
    stroke (0)
    #left hand
    bezier(197, 330, 197, 330, 150, 400, 170, 450)
    bezier(220, 380, 210, 400, 200, 430, 220, 480)
    
    #right hand
    bezier(402, 329, 412, 329, 460, 390, 455, 420)
    bezier(390, 380, 400, 400, 420, 430, 410, 460)
    
    #stomage
    fill(248,237,210)
    stroke (0)
    bezier(230, 410, 260, 375, 360, 375, 390, 410)
    stroke (248,237,210)
    ellipse (310, 440, 185, 110)
    
    createNormalEyes()

    solveMouseElements()
    
    n = int(random(2,5))
    listElements = []
    print(n)
    
    for i in range (n):    
        elementsNumber = int(random(1, 5))
        
        
        while (elementsNumber in listElements):
            elementsNumber = int(random(1,5))

        listElements.append(elementsNumber)
        
        if elementsNumber == 1:
            solveTieElements()
            
        elif elementsNumber == 2:
            solverGlassesAndEyes()
            
        elif elementsNumber == 3:
            solverHad()
        
        elif elementsNumber == 4:
            solverEarring()

    
    
################## Zebra Skin ###################

###### Zebra Head ######
def createZebraHead():
    # Draw head    
    fill (0)
    stroke (0)
    ellipse (300,280, 240,190)
    triangle (300, 190, 310, 190, 300, 170)
    triangle (290, 190, 300, 190, 290, 170)
    
    fill (255)
    stroke (255)
    triangle (280, 185, 320, 185, 300, 230)
    
    triangle (250, 193, 260, 190, 290, 220)
    triangle (350, 193, 340, 190, 310, 220)
    
    triangle (230, 201, 240, 196, 290, 230)
    triangle (370, 201, 360, 196, 310, 230)
    
    triangle (218, 211, 225, 206, 300, 240)
    triangle (382, 211, 375, 206, 300, 240)
    
    triangle (218, 211, 225, 206, 300, 240)
    triangle (382, 211, 375, 206, 300, 240)
    
    triangle (206, 221, 210, 216, 300, 250)
    triangle (394, 221, 390, 216, 300, 250)
    
    triangle (196, 231, 198, 226, 300, 260)
    triangle (404, 231, 402, 226, 300, 260)
    
    triangle (182, 261, 187, 246, 300, 270)
    triangle (418, 261, 412, 246, 300, 270)
    
    fill (0)
    stroke (0)
    triangle (190, 350, 194, 340, 300, 430)
    triangle (418, 350, 412, 340, 300, 430)
    
    triangle (190, 340, 194, 330, 300, 400)
    triangle (418, 340, 408, 330, 300, 400)
    
    triangle (180, 360, 187, 350, 300, 440)
    triangle (430, 360, 420, 350, 300, 440)

    triangle (180, 380, 182, 370, 300, 440)
    triangle (440, 380, 430, 370, 300, 440)
    
    triangle (180, 400, 182, 390, 300, 440)
    triangle (450, 400, 440, 390, 300, 440)
    
    triangle (170, 420, 172, 410, 300, 450)
    
    stroke (0)
    fill (248,237,210)
    stroke (248,237,210)
    ellipse (301, 310, 215, 100)
    bezier(198, 330, 231, 392, 370, 392, 405, 329)
    
    stroke (248,237,210)
    fill (248,237,210)
    bezier(182, 290, 202, 240, 250, 190, 300, 260)
                
    bezier(300, 260, 342, 190, 370, 230, 420, 290) 
    
##### Zebra Eyes #####    
def createZebraEyes():
    #Draw Eyes
    #left eye
    fill (255)
    stroke (255)
    bezier(185, 310, 202, 250, 270, 210, 280, 285)
                
    fill (0)
    ellipse (260, 270, 15, 30)
    fill (255)
    circle (260, 270,7)
        
    #rigth eye
    fill (255)
    stroke (255)
    bezier(320, 280, 330, 210, 398, 250, 415, 310)
        
    fill (0)
    ellipse (340,270, 15, 30)
    fill (255)
    circle (340, 270,7)
    
####### Create Zebra Body #######
def createZebraBody():
    fill (255)
    stroke (255)
    ellipse (305, 400, 270, 190)
    ellipse (200, 340, 15, 20)
    
def createZebraNose():
    #Draw nose
    stroke(0)
    fill (0)
    ellipse (300, 300, 45,25)
    fill (255)
    ellipse (285, 300, 15,12)
    fill (255)
    ellipse (315, 300, 15,12)   
    
##### Create Zebra Mouse #####
def createZebraMouse():
    #Draw mouse
    noFill ()
    stroke (0)
    curve(265, 300, 275, 320, 320, 320, 330, 300)
        
    fill (255,0,0)
    stroke (0)
    bezier(285, 323, 295, 333, 305, 333, 315, 323)
    
####### Create Zebra Structure Body #######
def createZebraStructureBody():
    
    createZebraBody()

    createZebraHead()
    
    createZebraNose()

    #Draw Body
    fill(0)
    stroke (0)
    #left hand
    bezier(197, 330, 197, 330, 150, 400, 170, 450)
    bezier(220, 380, 210, 400, 200, 430, 220, 480)
    
    #right hand
    bezier(402, 329, 412, 329, 460, 390, 455, 420)
    bezier(390, 380, 400, 400, 420, 430, 410, 460)
    
    #stomage
    fill (0)
    stroke (0)
    bezier(230, 405, 260, 370, 360, 370, 390, 405)
    fill (132, 137,132)
    noStroke ()
    ellipse (310, 440, 185, 110)
    
    createZebraEyes()
    
    createZebraMouse()
    
    n = int(random(2,5))
    listElements = []
    print(n)
    
    for i in range (n):    
        elementsNumber = int(random(1, 5))
        
        
        while (elementsNumber in listElements):
            elementsNumber = int(random(1,5))

        listElements.append(elementsNumber)
        
        if elementsNumber == 1:
            solveTieElements()
            
        elif elementsNumber == 2:
            solverGlassesAndEyes()
            
        elif elementsNumber == 3:
            solverHad()
        
        elif elementsNumber == 4:
            solverEarring()
            
            

########################### Zombie Skin ###########################

####### Create Zombie Body #######        
def createZombieBody():
    fill (108,157,108)
    stroke (108,157,108)
    ellipse (305, 400, 270, 190)
    ellipse (200, 340, 15, 20)
    
####### Create Zombie Mouse #######    
def createZombieMouse():
    #Draw mouse
    fill (255,0,0)
    stroke (255,0,0)
    ellipse (300, 335, 80, 40)
    
    noFill ()
    stroke (0)
    ellipse (300, 335, 80, 40)
    
    fill (224, 248, 204)
    stroke (224, 248, 204)
    rect (275, 316, 10, 10)
    rect (310, 316, 10, 10)
    
    rect (295, 345, 10, 10)
    rect (320, 342, 10, 10)
    rect (270, 342, 10, 10)
    
####### Create Zombie Eyes #######    
def createZombieEyes():
    #Draw Eyes
    #left eye
    fill (122,128,118)
    stroke (122,128,118)
    bezier(185, 310, 202, 250, 270, 210, 280, 285)
                
    fill (255, 0,0)
    ellipse (260, 270, 15, 30)
    fill (0)
    stroke (0)
    circle (260, 270,10)
        
    #rigth eye
    fill (122,128,118)
    stroke (122,128,118)
    bezier(320, 280, 330, 210, 398, 250, 415, 310)
        
    fill (255, 0,0)
    ellipse (340,270, 15, 30)
    fill (0)
    stroke (0)
    circle (340, 270,7)
    
###### Normal Head Zombre ######
def createZombieHead():
    # Draw head
    fill (108,157,108)
    stroke (108,157,108)
    ellipse (300,280, 240,190)
    triangle (300, 190, 310, 190, 300, 170)
    triangle (290, 190, 300, 190, 290, 170)
    fill (248,237,210)
    stroke (248,237,210)
    ellipse (301, 310, 215, 100)
    bezier(198, 330, 231, 392, 370, 392, 405, 329)
    
    stroke (248,237,210)
    fill (248,237,210)
    bezier(182, 290, 202, 240, 250, 190, 300, 260)
                
    bezier(300, 260, 342, 190, 370, 230, 420, 290) 

######## Create Zombie Nose ########
def createZombieNose():
    #Draw nose
    stroke (122,128,118)
    fill (122,128,118)
    ellipse (300, 300, 45,25)
    fill (0)
    ellipse (285, 300, 15,12)
    fill (0)
    ellipse (315, 300, 15,12)
    stroke (0) 

    
####### Create Zombie Structure Body #######    
def createZombieStructureBody():
    
    createZombieBody()

    createZombieHead()
    
    createZombieNose()
    
    #Draw Body
    fill (88,130,89)
    stroke (0)
    #left hand
    bezier(197, 330, 197, 330, 150, 400, 170, 450)
    bezier(220, 380, 210, 400, 200, 430, 220, 480)
    
    #right hand
    bezier(402, 329, 412, 329, 460, 390, 455, 420)
    bezier(390, 380, 400, 400, 420, 430, 410, 460)
    
    #stomage
    fill(255,0, 0)
    stroke (0)
    bezier(230, 410, 260, 375, 360, 375, 390, 410)
    stroke (255,0,0)
    ellipse (310, 440, 185, 110)
    
    ellipse (250, 320, 10, 6)
    ellipse (400, 320, 10, 6)
    ellipse (350, 350, 10, 12)
    ellipse (250, 380, 12, 5)
    
    createZombieEyes()
    
    createZombieMouse()
    
    n = int(random(2,5))
    listElements = []
    print(n)
    
    for i in range (n):    
        elementsNumber = int(random(1, 5))
        
        
        while (elementsNumber in listElements):
            elementsNumber = int(random(1,5))

        listElements.append(elementsNumber)
        
        if elementsNumber == 1:
            solveTieElements()
            
        elif elementsNumber == 2:
            solverGlasses()
            
        elif elementsNumber == 3:
            solverHad()
        
        elif elementsNumber == 4:
            solverEarring()
    
    
    
########################### Gold Skin ###########################

####### Create Gold Body #######        
def createGoldBody():
    fill (236,187,4)
    stroke (236,187,4)
    ellipse (305, 400, 270, 190)
    ellipse (200, 340, 15, 20)
    
####### Create Gold Mouse #######    
def createGoldMouse():
    #Draw mouse
    noFill ()
    stroke (0)
    curve(265, 290, 275, 318, 320, 320, 330, 300)
        
    fill (255,0,0)
    stroke (0)
    bezier(280, 320, 295, 333, 305, 333, 320, 320)
    
####### Create Gold Eyes #######    
def createGoldEyes():
    #Draw Eyes
    #left eye
    fill (204,203,200)
    stroke (204,203,200)
    bezier(185, 310, 202, 250, 270, 210, 280, 285)
                
    fill (0)
    ellipse (260, 270, 15, 30)
    fill (175, 138, 2)
    stroke (175, 138, 2)
    circle (260, 270, 8)
    fill (255)
    stroke (255)
    circle (260, 270,3)
    
    #rigth eye
    fill (204,203,200)
    stroke (204,203,200)
    bezier(320, 280, 330, 210, 398, 250, 415, 310)
        
    fill (0)
    ellipse (340,270, 15, 30)
    fill (175, 138, 2)
    stroke (175, 138, 2)
    circle (340, 270, 8)
    fill (255)
    stroke (255)
    circle (340, 270,3)
    
    
###### Gold Head  ######
def createGoldHead():
    # Draw head
    fill (236,187,4)
    stroke (236,187,4)
    ellipse (300,280, 240,190)
    triangle (300, 190, 310, 190, 300, 170)
    triangle (290, 190, 300, 190, 290, 170)
    
    fill (248,237,210)
    stroke (248,237,210)
    ellipse (301, 310, 215, 100)
    bezier(198, 330, 231, 392, 370, 392, 405, 329)
    
    fill (175, 138, 2)
    stroke (175, 138, 2)
    bezier(182, 285, 202, 235, 250, 185, 302, 255)        
    bezier(298, 255, 342, 185, 370, 225, 420, 285) 
    
    fill (248,237,210)
    stroke (248,237,210)
    bezier(182, 290, 202, 240, 250, 190, 300, 260)        
    bezier(300, 260, 342, 190, 370, 230, 420, 290)

######## Create Gold Nose ########
def createGoldNose():
    #Draw nose
    stroke (236,187,4)
    fill (236,187,4)
    ellipse (300, 300, 45,25)
    
    fill (175, 138, 2)
    ellipse (285, 300, 15,12)
    ellipse (315, 300, 15,12)

    
####### Create Gold Structure Body #######    
def createGoldStructureBody():
    
    createGoldBody()

    createGoldHead()
    
    createGoldNose()
    
    #Draw Body
    fill (175, 138, 2)
    stroke (0)
    
    #left hand
    bezier(197, 330, 197, 330, 150, 400, 170, 450)
    bezier(220, 380, 210, 400, 200, 430, 220, 480)
    
    #right hand
    bezier(402, 329, 412, 329, 460, 390, 455, 420)
    bezier(390, 380, 400, 400, 420, 430, 410, 460)
    
    #stomage
    fill (175, 138, 2)
    stroke (236,187,4)
    bezier(230, 405, 260, 370, 360, 370, 390, 405)
    fill (204,203,200)
    noStroke ()
    ellipse (310, 440, 185, 110)
    
    createGoldEyes()
    
    createGoldMouse()
    
    n = int(random(2,5))
    listElements = []
    print(n)
    
    for i in range (n):    
        elementsNumber = int(random(1, 5))
        
        
        while (elementsNumber in listElements):
            elementsNumber = int(random(1,5))

        listElements.append(elementsNumber)
        
        if elementsNumber == 1:
            solveTieElements()
            
        elif elementsNumber == 2:
            solverGlassesAndEyes()
            
        elif elementsNumber == 3:
            solverHad()
        
        elif elementsNumber == 4:
            solverEarring()

    
    
####################### Mouse #######################
    
##### Create Left Mouse #####
def createLeftMouse():
    #Draw mouse
    noFill ()
    stroke (0)
    bezier (300, 314, 285, 320, 285, 325, 300, 330)
    bezier (300, 330, 285, 335, 285, 340, 300, 345)
    

##### Create Right Mouse #####
def createRightMouse():
    #Draw mouse
    noFill ()
    stroke (0)
    bezier (300, 314, 315, 320, 315, 325, 300, 330)
    bezier (300, 330, 315, 335, 315, 340, 300, 345)


####################### Elements ####################### 

##### Create Beard #####  
def createBeard():
    fill(189,189,189)
    stroke (189,189,189)
    triangle (270, 370, 330, 370, 300, 450)
    
####################### Hads ####################### 

##### Create Had #####      
def createMagicHad():

    fill(0,255, 0)
    stroke (0,255,0)
    ellipse (300, 220, 210,30)
    rect (220, 125, 160, 80)
    
    fill(133,133,133)
    stroke (133,133,133)
    rect (220, 200, 160, 15)
    
    noFill()
    stroke (255,255,0)
    
    x = 280
    y = 195
    z = 40
    m = 25
    for i in range(5):
        rect (x, y, z, m)
        x = x +1
        y = y +1
        z = z -2
        m = m -2
    
    fill(255,255,0)
    stroke (255,255,0)
    rect (295, 195, 10, 8)
    rect (295, 212, 10, 8)
    
    
##### Create Sport Had #####      
def createSportHad():
    
    x = random (255)
    y = random (255)
    z = random (255)
    fill (x,y,z)
    stroke (x,y,z)
    rect (210, 210, 180, 20)
    ellipse (210, 220, 15, 20)
    ellipse (390, 220, 15, 20)
    
    fill(255)
    stroke (255)
    ellipse (300, 220, 10,10)
    
    
##### Create Angel Had #####      
def createAngelHad():
    
    noFill()
    stroke (255)
    z = 140
    m = 20
    for i in range (10):
        ellipse (300, 155, z, m)
        z = z -1
        m = m -1
    
            
##### Create Party Had #####      
def createPartyHad():
    
    r = random(255)
    g = random(255)
    b = random(255)
    fill(r,g,b)
    stroke (r,g,b)
    ellipse (300, 205, 150,40)
    
    r1 = random(255)
    g1 = random(255)
    b1 = random(255)
    fill(r1,g1,b1)
    stroke (r1,g1,b1)
    ellipse (300, 205, 140,30)
    triangle (230, 205, 370, 205, 300, 110)

    fill(r,g,b)
    stroke (r,g,b)
    ellipse (300, 130, 15, 15)
    ellipse (285, 160, 20, 20)
    ellipse (315, 150, 15, 15)
    ellipse (335, 170, 5, 5)
    ellipse (265, 195, 15, 15)
    ellipse (300, 190, 5, 5)
    ellipse (330, 200, 15, 15)
    ellipse (350, 195, 7, 7)
    

##### Create Constructor Had #####      
def createConstructorHad():
    
    #central 
    fill(255, 250, 0)
    stroke (255, 250, 0)
    rect (210, 160, 180, 80)
    rect (390, 180, 10, 50)
    rect (260, 150, 40,10)
    rect (310, 150, 40,10)
    
    fill(208, 163, 23)
    stroke (208, 163, 23)
    rect (210, 240, 180, 10)
    rect (390, 230, 30, 10)
    rect (180, 230, 30, 10)
    rect (200, 180, 10, 50)
    
    rect (250, 160, 10, 40)
    rect (300, 160, 10, 55)
    rect (350, 160, 10, 40)

##### Create Crown #####      
def createCrownHad():
    
    #central 
    fill(255, 250, 0)
    stroke (255, 250, 0)
    rect (200, 170, 200, 70)
    rect (200, 130, 20, 40)
    rect (220, 160, 20, 10)
    rect (380, 130, 20, 40)
    rect (360, 160, 20, 10)
    rect (270, 160, 60, 10)
    rect (290, 140, 20, 30)
    
    rect (190, 180, 10, 60)
    rect (180, 230, 10, 10)
    
    rect (400, 180, 10, 60)
    rect (410, 230, 10, 10)
    
    #Jewels
    fill(255, 0, 0)
    stroke (255, 0, 0)
    rect (210, 210, 10, 10)
    rect (380, 210, 10, 10)
    
    fill(0, 255, 0)
    stroke (0, 255, 0)
    rect (240, 210, 10, 10)
    rect (350, 210, 10, 10)
        
    fill(94, 188, 238)
    stroke(94, 188, 238)
    rect (270, 210, 60, 10)
    rect (290, 200, 20, 10)
    
    
##### Create Viking Had #####      
def createVikingHad():
    
    fill(255)
    stroke (255)
    triangle (190, 150, 190, 235, 220, 200)
    triangle (410, 150, 410, 235, 380, 200)
    
    #central 
    fill(141, 152, 153)
    stroke (141, 152, 153)
    bezier(195, 230, 240, 125, 360, 125, 405, 230)
    
    fill(255)
    stroke (255)
    rect (185, 230 ,230, 20)
    rect (290, 150, 20, 80)
    
    fill(0)
    stroke (0)
    x = 195
    for i in range(22):
        ellipse (x, 240, 5, 5)
        x = x + 10
                    
##### Create Luffy Had #####      
def createLuffyHad():
    
    fill (241, 177, 39)
    stroke (241, 177, 39)
    ellipse (300, 205, 220, 22)
    
    bezier(210, 210, 230, 100, 370, 100, 390, 210)
    
    fill (255, 0, 0)
    stroke (255, 0, 0)
    rect (210, 190, 180, 10)

    stroke (0)
    line (210, 190, 390, 190)
    line (210, 200, 390, 200)
    
    stroke (100,100,100)
    line (240, 170, 260, 170)
    line (240, 177, 260, 177)
    line (245, 165, 245, 185)
    line (255, 165, 255, 185)
    
    
##### Create Cowboy Had #####      
def createCowboyHad():
    
    fill (241, 177, 39)
    stroke (241, 177, 39)
    rect (190, 205, 220, 30)
    
    rect (230, 150, 140, 70)
    rect (240, 140, 40, 10)
    rect (320, 140, 40, 10)
    
    #left part
    rect (220, 160, 10, 40)
    rect (210, 180, 10, 20)
    rect (170, 205, 20, 20)
    rect (150, 195, 20, 20)
    
    #right part
    rect (370, 160, 10, 40)
    rect (380, 180, 10, 20)
    rect (410, 205, 20, 20)
    rect (420, 195, 20, 20)
    
    fill (138, 94, 0)
    stroke (138, 94, 0)
    rect (210, 195, 180, 10)
   
##### Create HeadPhones #####      
def createHeadPhones():
    
    fill(0)
    stroke (0)
    ellipse (180, 273, 25, 70)
    ellipse (420, 273, 25, 70)
    
    r1 = random(255)
    g1 = random(255)
    b1 = random(255)
    fill(r1,g1,b1)
    stroke (0)
    ellipse (175, 273, 15, 70)
    ellipse (425, 273, 15, 70)
    
    noFill()
    x = 181
    y = 150
    z =419
    for i in range(5):
        bezier(x, 240, 200, y, 400, y, z, 240)
        x = x -1
        y = y -1
        z = z +1
        
##### Create HeadPhones #####      
def createHeadPhones2():
    
    fill(0)
    stroke (0)
    ellipse (180, 273, 25, 70)
    ellipse (420, 273, 25, 70)
        
    r1 = random(255)
    g1 = random(255)
    b1 = random(255)
    fill(r1,g1,b1)
    stroke (0)
    ellipse (175, 273, 15, 70)
    ellipse (425, 273, 15, 70)
    
    noFill()
    x = 181
    y = 160
    z =419
    for i in range(5):
        bezier(x, 240, 200, y, 400, y, z, 240)
        x = x -1
        y = y -1
        z = z +1
    
    fill(0)    
    ellipse(291, 352, 20,7)
    
    noFill()
    x = 181
    y = 340
    z = 360
    for i in range(5):
        bezier(x, 305, 190, y, 250, z, 300, 350)
        x = x -1
        y = y +1
        z = z +1


####################### Glasses ####################### 

##### Rectangular Glases #####  
def createRectGlasses():
    stroke (random(255),random(255),random(255))
    fill (random(255),random(255),random(255))
    x = 210
    y = 250
    z = 70
    m = 40
    for i in range(4): 
        rect (x, y, z, m)
        x = x + 1
        y = y + 1
        z = z - 2
        m = m - 2
     
    x = 320
    y = 250
    z = 70
    m = 40   
    for i in range(4): 
        rect (x, y, z, m)
        x = x + 1
        y = y + 1
        z = z - 2
        m = m - 2
        
    y = 270
    for i in range(4):    
        line (280, y, 320, y)
        y = y + 1
        
    x = 185
    for i in range(4):    
        line (x, 250, x+25, 260)
        x = x + 1
        
    x = 387
    for i in range(4):    
        line (x, 260, x+25, 250)
        x = x + 1

##### Oval glasses #####  
def createOvalGlasses():
    stroke (random(255),random(255),random(255))
    fill (random(255),random(255),random(255))

    m = 70
    for i in range(5): 
        circle (245, 270, m)
        m = m - 2
     
    m = 70   
    for i in range(5): 
        circle (355, 270, m)
        m = m - 2
        
    y = 270
    for i in range(4):    
        line (280, y, 320, y)
        y = y + 1
        
    x = 185
    for i in range(4):    
        line (x, 250, x+25, 260)
        x = x + 1
        
    x = 387
    for i in range(4):    
        line (x, 260, x+25, 250)
        x = x + 1
    

##### Turn Down for What Glasses #####      
def createTDFWGlasses():
    stroke (0)
    fill (0)

    y = 250
    for i in range(6):    
        line (210, y, 390, y)
        y = y + 1
        
    bezier(210, 250, 230, 300, 280, 300, 290, 250)
    
    bezier(310, 250, 330, 300, 380, 300, 390, 250)
    
    stroke (255)
    fill (255)
    # left
    rect (225, 260, 7,7)
    rect (235, 260, 7,7)
    rect (230, 270, 7,7)
    rect (240, 270, 7,7)
    
    # left
    stroke (0)
    fill (0)
    rect (215, 260, 10,10)
    rect (220, 270, 10,10)
    x = 230
    for i in range(5):
        rect (x, 280, 9,9)
        x = x+9
    rect (277, 260, 10,10)
    rect (272, 270, 10,10)
    
    #rigth
    stroke (0)
    fill (0)
    rect (315, 260, 10,10)
    rect (320, 270, 10,10)
    
    x = 330
    for i in range(5):
        rect (x, 280, 9,9)
        x = x+9
    rect (377, 260, 10,10)
    rect (372, 270, 10,10)
    
    stroke (255)
    fill (255)
    rect (325, 260, 7,7)
    rect (335, 260, 7,7)
    rect (330, 270, 7,7)
    rect (340, 270, 7,7)
    
##### Heart Glases #####  
def createHeartGlasses():
    stroke (random(255),random(255),random(255))
    fill (180, 10, 10)

    y = 270
    for i in range(4):    
        line (270, y, 325, y)
        y = y + 1
    
    x = 185
    for i in range(4):    
        line (x, 240, x+31, 250)
        x = x + 1
        
    x = 380
    for i in range(4):    
        line (x, 250, x+25, 240)
        x = x + 1
        
    #left 
    bezier(250, 300, 170, 250, 250, 220, 250, 255)
    bezier(250, 300, 325, 250, 250, 220, 250, 255)    
    # bezier(390, 380, 400, 400, 420, 430, 410, 460)
    
    #rigth 
    bezier(350, 300, 270, 250, 350, 220, 350, 255)
    bezier(350, 300, 430, 250, 350, 220, 350, 255)
    
           
##### 3D Glases #####                  
def create3DGlasses():
    stroke (255)
    fill (0,0,250)
    x = 210
    y = 250
    z = 70
    m = 40
    for i in range(4): 
        rect (x, y, z, m)
        x = x + 1
        y = y + 1
        z = z - 2
        m = m - 2
     
    fill (250,0,0)
    x = 320
    y = 250
    z = 70
    m = 40   
    for i in range(4): 
        rect (x, y, z, m)
        x = x + 1
        y = y + 1
        z = z - 2
        m = m - 2
        
    y = 270
    for i in range(4):    
        line (280, y, 320, y)
        y = y + 1
        
    x = 185
    for i in range(4):    
        line (x, 250, x+25, 260)
        x = x + 1
        
    x = 387
    for i in range(4):    
        line (x, 260, x+25, 250)
        x = x + 1    
 
               
##### One glass #####                  
def createOneGlass():
    stroke (255)

    fill(0, 240, 0)
    x = 210
    y = 250
    z = 180
    m = 40   
    for i in range(7): 
        rect (x, y, z, m)
        x = x + 1
        y = y + 1
        z = z - 2
        m = m - 2
        
    y = 263
    for i in range(13):    
        line (177, y, 210, y)
        y = y + 1
        
    y = 263
    for i in range(13):    
        line (387, y, 420, y)
        y = y + 1    


##### Eye Patch #####                  
def createEyePatch():
    stroke (0)
    fill (0)

    y = 250
    for i in range(6):    
        line (200, y, 280, y)
        y = y + 1
        
    bezier(200, 250, 220, 310, 280, 310, 290, 250)
    
    y = 251
    for i in range(4):    
        line (185, y, 210, y)
        y = y + 1
        
    y = 251
    for i in range(4):    
        line (285, y, 397, 220)
        y = y + 1
    
    stroke (255)    
    line (230, 260, 260, 280)
    line (230, 280, 260, 260)  


##### draw Cripto Eyes #####    
def createCriptoEyes():
    #Draw Eyes
    #left eye
    fill (189,189,189)
    stroke (189,189,189)
    bezier(185, 310, 202, 250, 270, 210, 280, 285)
                
    fill (0)
    ellipse (260, 270, 15, 30)
    fill (250,0,0)
    stroke(250,0,0)
    circle (260, 270, 15)
    stroke(250,0,0)
    triangle (258, 270, 258, 272, 250, 278)
    triangle (260, 272, 262, 272, 260, 280)
    triangle (259, 267, 260, 267, 260, 250)
    triangle (258, 268, 259, 268, 250, 260)
    triangle (262, 268, 262, 269, 268, 260)
    triangle (262, 270, 262, 271, 270, 270)
    triangle (258, 270, 258, 272, 240, 278)
    triangle (262, 268, 262, 269, 268, 240)
    triangle (262, 270, 262, 271, 270, 280)
    fill (255, 195, 0 )
    circle (260, 270, 10)
            
    #rigth eye
    fill (189,189,189)
    stroke (189,189,189)
    bezier(320, 280, 330, 210, 398, 250, 415, 310)
        
    fill (0)
    ellipse (340,270, 15, 30)
    fill (250,0,0)
    stroke(250,0,0)
    circle (340, 270,15)
    stroke(250,0,0)
    triangle (338, 270, 338, 272, 330, 278)
    triangle (340, 272, 342, 272, 340, 290)
    triangle (339, 267, 340, 267, 340, 250)
    triangle (338, 268, 338, 268, 330, 250)
    triangle (342, 268, 342, 269, 348, 260)
    triangle (342, 270, 342, 271, 350, 270)
    triangle (338, 270, 338, 272, 340, 275)
    triangle (342, 268, 342, 269, 348, 255)
    triangle (342, 270, 342, 271, 350, 280)
    fill (255, 195, 0)
    circle (340, 270, 10)
    
    
##### draw Green Eyes #####    
def createGreenEyes():
    #Draw Eyes
    #left eye
    fill (189,189,189)
    stroke (189,189,189)
    bezier(185, 310, 202, 250, 270, 210, 280, 285)
                
    fill (0)
    ellipse (260, 270, 15, 30)
    fill (0,255,0)
    stroke (0,255,0)
    circle (260, 270,7)
        
    #rigth eye
    fill (189,189,189)
    stroke (189,189,189)
    bezier(320, 280, 330, 210, 398, 250, 415, 310)
        
    fill (0)
    ellipse (340,270, 15, 30)
    fill (0,255,0)
    stroke (0,255,0)
    circle (340, 270,7)

    
##### Create Earring #####      
def createEarring():

    stroke (100,100,100)
    noFill()
    x = 285
    y = 325
    z = 315
    for i in range(5):
        bezier(x, 305, 290, y, 310, y, z, 305)
        x = x -1
        y = y -1
        z = z +1
        
        
####################### Cigars #######################

##### Create Cigar Pipe #####  
def createCigarPipe():
    fill (241, 177, 39)
    stroke (0)
    rect (230, 325, 20, 15)
    bezier (230, 340, 250, 370, 270, 350, 278, 328)
    noStroke()
    ellipse (286, 330, 22, 8)
    
    fill (0)
    ellipse (240, 325, 18, 5)
    
    stroke(0)
    line (276, 333, 292, 333)
    
    stroke (255)
    line (230, 330, 250, 330)
    line (230, 333, 250, 333)
    line (252, 335, 255, 355)
    line (256, 333, 259, 354)
    
    stroke (0)
    line (230, 310, 231, 320)
    line (235, 310, 236, 320)
    line (230, 300, 231, 312)
    line (235, 300, 236, 312)
    

##### Create Cigar #####  
def createCigar():
    fill (241, 177, 39)
    stroke (0)
    rect (301, 326, 15, 5)
    
    fill(255)
    stroke(0)
    rect (316, 326, 30, 5)
    
    fill(255, 0, 0)
    stroke(0)
    ellipse (345, 329, 6, 5)
    
    line (347, 310, 345, 320)
    line (349, 305, 350, 315)
    
##### Create Habano #####  
def createHabano():
    fill (190, 140, 34)
    stroke (190, 140, 34)
    ellipse (332, 327,75,10)
    rect (301, 327, 70, 5)
    
    fill(0)
    stroke(0)
    ellipse (370, 329, 5, 7)
    
    line (372, 310, 370, 320)
    line (375, 305, 376, 315)
    
    fill (255, 0, 0)
    stroke (255, 0, 0)
    rect (316, 323, 10, 9)
    
    stroke(255)
    line (315, 323, 315, 332)
    line (325, 323, 325, 332)
    
    
##### Create Tie #####  
def createTie():
    
    fill (0)
    stroke (0)
    triangle (270, 377, 330, 377, 300, 410)
    bezier (265, 375, 275, 377, 320, 377, 335, 375)
    rect (288, 380, 24, 20)
    
    r = random (255)
    g = random (255)
    b = random (255)    
    fill (r, g, b)
    stroke (r, g, b)
    triangle (265, 450, 335, 450, 300, 380)
    triangle (265, 450, 335, 450, 300, 490)
    
    r = random (255)
    g = random (255)
    b = random (255)
    fill (r, g, b)
    stroke (r, g, b)
    rect (276, 425, 50, 2)
    rect (270, 455, 60, 2)
    rect (295, 483, 10, 2)
    
    r = random (255)
    g = random (255)
    b = random (255)
    fill (r, g, b)
    stroke (r, g, b)
    rect (283, 410, 35, 3)
    rect (269, 440, 62, 3)
    rect (283, 470, 34, 3)
    
    fill (0)
    stroke (0)
    rect (288, 380, 24, 20)
    
    
##### Create Circle Tie #####  
def createCircleTie():
    
    fill (0)
    stroke (0)
    triangle (270, 377, 330, 377, 300, 410)
    bezier (265, 375, 275, 377, 320, 377, 335, 375)
    rect (288, 380, 24, 20)
    
    r = random (255)
    g = random (255)
    b = random (255)    
    fill (r, g, b)
    stroke (r, g, b)
    triangle (265, 450, 335, 450, 300, 380)
    triangle (265, 450, 335, 450, 300, 490)
    
    r = random (255)
    g = random (255)
    b = random (255)
    fill (r, g, b)
    stroke (r, g, b)
    ellipse (290, 425, 10, 10)
    ellipse (310, 445, 10, 10)
    ellipse (300, 483, 6, 6)
    
    r = random (255)
    g = random (255)
    b = random (255)
    fill (r, g, b)
    stroke (r, g, b)
    ellipse (307, 410, 10, 10)
    ellipse (285, 450, 8, 8)
    ellipse (312, 470, 10, 10)
    
    fill (0)
    stroke (0)
    rect (288, 380, 24, 20)
    
    
def solveTieElements():
    
    element = int(random(10))
    arrayElements = [4,2,1,3,3,4,2,1,2,3]
    
    if arrayElements[element] == 1:
        createBeard()
    elif arrayElements[element] == 2:
        createTie()
    elif arrayElements[element] == 3:
        createCircleTie()
    else:
        return;
    
def solveMouseElements():
    
    element = int(random(10))
    arrayElements = [1,1,1,1,1,1,2,1,2,5]
    if arrayElements[element] == 1:
        createNormalMouse()
    elif arrayElements[element] == 2:
        createRightMouse()
        solverRightMouse()
    else:
        createLeftMouse()
        createCigarPipe()
        
        
def solverRightMouse():
    element = int(random(10))
    arrayElements = [1,2,1,1,2,1,2,1,2,1]
    
    if arrayElements[element] == 1:
        createCigar()
    else :
        createHabano()
        
        
def solverGlassesAndEyes():
    element = int(random(40))
    arrayElements = [1,1,2,1,1,6,1,8,1,3,1,2,5,1,1,8,1,1,1,7,1,1,1,1,6,1,1,8,1,3,1,1,1,8,1,1,1,1,1,4]
    
    if arrayElements[element] == 1:
        return
    elif arrayElements[element] == 2:
        createRectGlasses()
    elif arrayElements[element] == 3:
        createOvalGlasses()
    elif arrayElements[element] == 4:
        createTDFWGlasses()
    elif arrayElements[element] == 5:
        createHeartGlasses()
    elif arrayElements[element] == 6:
        create3DGlasses()
    elif arrayElements[element] == 7:
        createOneGlass()
    elif arrayElements[element] == 8:
        solveEyes()

def solveEyes():
    element = int(random(10))
    arrayElements = [2,1,2,3,1,3,2,3,1,3]
    
    if arrayElements[element] == 1:
        createEyePatch
    elif arrayElements[element] == 2:
        createCriptoEyes()
    elif arrayElements[element] == 3:
        createGreenEyes()
        
def solverHad():
    element = int(random(40))
    arrayElements = [1,1,2,1,1,1,1,1,11,3,1,2,5,1,12,8,1,1,1,7,1,10,1,1,6,1,1,5,1,3,1,1,1,1,1,1,1,9,1,4]
    
    if arrayElements[element] == 1:
        return
    elif arrayElements[element] == 2:
        createMagicHad()
    elif arrayElements[element] == 3:
        createSportHad()
    elif arrayElements[element] == 4:
        createAngelHad()
    elif arrayElements[element] == 5:
        createPartyHad()
    elif arrayElements[element] == 6:
        createConstructorHad()
    elif arrayElements[element] == 7:
        createCrownHad()
    elif arrayElements[element] == 8:
        createVikingHad()
    elif arrayElements[element] == 9:
        createLuffyHad()
    elif arrayElements[element] == 10:
        createCowboyHad()
    elif arrayElements[element] == 11:
        createHeadPhones()
    elif arrayElements[element] == 12:
        createHeadPhones2()


def solverEarring():
    element = int(random(10))
    arrayElements = [1,1,2,1,1,1,1,1,1,1]
    
    if arrayElements[element] == 1:
        return
    elif arrayElements[element] == 2:
        createEarring()
        
def solverGlasses():
    element = int(random(40))
    arrayElements = [1,1,2,1,1,6,1,1,1,3,1,2,5,1,1,1,1,1,1,7,1,1,1,1,6,1,1,1,1,3,1,1,1,8,1,1,1,1,1,4]
    
    if arrayElements[element] == 1:
        return
    elif arrayElements[element] == 2:
        createRectGlasses()
    elif arrayElements[element] == 3:
        createOvalGlasses()
    elif arrayElements[element] == 4:
        createTDFWGlasses()
    elif arrayElements[element] == 5:
        createHeartGlasses()
    elif arrayElements[element] == 6:
        create3DGlasses()
    elif arrayElements[element] == 7:
        createOneGlass()
    
