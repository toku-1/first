ufoX = 0
ufoY = 0
dufoX = 0
dufoY = 0
ufoH = 25.0
ufoW = 12.5
wallW = 20
destX = 0
ddestX = 0
destW = 80
life = 5
missileX = -100
missileY = -100


ufoX2 = 0
ufoY2 = 0
dufoX2 = 0
dufoY2 = 0
ufoH2 = 25.0
ufoW2 = 12.5
wallW2 = 20
life2 = 5
missileX2 = -100
missileY2 = -100





gameTime = 0
timeCount = 0

winColor = (255,255,255)

keyPressing = [False,False,False,False,False,False] #a,d,LEFT,RIGHT,ENTER," "

startFlag = False


def setup():
    noStroke()
    global  ufoX,ufoY,destX,ufoX2,ufoY2,destX2,startFlag    , dufoX,dufoY, dufoX2,dufoY2  
    global life,life2,timeCount,gameTime

    startFlag = False
    #size(1600,900)
    fullScreen()
    frameRate(120)
    textSize(64)
    textAlign(CENTER,CENTER)
    background(255)
    strokeWeight(3)
    dufoX  =  0
    dufoY  =  0
    dufoX2 =  0
    dufoY2 =  0
    
    
    
    ufoX = width * 6/8
    ufoY = height/2
    destX = width/2
    ufoX2 = width *  2/8
    ufoY2 = height/2
    destX2 = width/2
    
    life = 5
    life2 = 5
    timeCount = (millis()//10)/100
    gameTime = 45
    
    #fill(0,0,255)
    #background(192)
   ########################################################################## 
#################################################################################################################


def draw():
    
    background(96)
    global  startFlag,winColor
    if startFlag == False:
        fill(winColor[0],winColor[1],winColor[2])
        
        text("PLZ SPASE",width/2,height/2)
        if keyPressed:
            if key == " ":
                timeCount = (millis()//10)/100
                startFlag = True
            else:
                return 
        else:
            return 
            
    
    global ufoX,ufoY,dufoX,dufoY,ufoH,ufoW,wallW,destX,ddestX,destW
    global ufoX2,ufoY2,dufoX2,dufoY2,ufoH2,ufoW2,wallW2,destX2,ddestX2,destW2
    global life,life2,timeCount,gameTime,missileX,missileY,missileX2,missileY2


################################################
#ミサイル関連










##################################
    #当たり判定の横移動
    
    if (destX - destW < wallW) or (destX + destW > width - wallW):
        ddestX *= -1
    destX += ddestX
    ddestX += ((mouseX - destX)/13000)
    ddestX = (ddestX) * 0.996
    
    #壁の描画
    fill(0,128,255)
    rect(wallW,wallW,width - wallW * 2,height - wallW *2)
#################################


#時間関連
    fill(255)
    text(str(  gameTime  -  (((millis()//10)/100)-timeCount)),width/2,wallW + 90)
    if (gameTime  -  (((millis()//10)/100)-timeCount)) <= 0:
        winColor =(255,255,0)
        setup()
    elif life <= 0 and life2 <= 0:
        winColor =(255,255,0)
        setup()

############################################################################################
#life表示
#fill()


    fill(255)
    text("LIFE",width/2,wallW + 32)

    fill(200,50,50)
    text(str(life),width/2+128,wallW + 32)

    fill(100,200,100)
    text(str(life2),width/2-128,wallW + 32)    

        
#####################################################################################################################################                
                        
                                        
    if keyPressed:
        if keyPressing[2]:
            dufoY -= 0.02
            if dufoY <= -2:
                dufoY = -2

#おされるだけでおきるやつ↑
            dufoX -= 0.02
            if dufoX < -2:
                dufoX = -2
                



        if keyPressing[3]:
            dufoY -= 0.02
            if dufoY <= -2:
                dufoY = -2
                
                
            dufoX += 0.02
            if dufoX > 2:
                dufoX = 2
                



        if keyPressing[4]:#ENTER
            fill(200,50,50)
            ellipse(ufoX,ufoY,ufoH * 8,ufoH*2)
            
    
    
    dufoY += 0.01
    if dufoY >= 2:
        0
        dufoY = 2
        
        
    dufoX *= 0.995
    
    ufoX += dufoX
    ufoY += dufoY
    
    


    
    fill(255,255,0)
    rect(destX - destW,height - wallW,destW * 2,wallW/2)
    
    
    fill(200,0,0)
    ellipse(ufoX,ufoY,ufoH * 2,ufoH * 2)
    
    fill(200,50,50)
    ellipse(ufoX,ufoY,ufoH * 4,ufoH)
    
    


    if (ufoY + ufoH >= height - wallW) and (ufoX > destX - destW) and (ufoX  < destX + destW):
        fill(255)
        text("Congratulations!",width/2,height/2)
        winColor = (200,50,50)
        setup() 
    elif (wallW > ufoX - ufoW *4) or (width - wallW < ufoX + ufoW*4) or (ufoY + ufoH > height - wallW) or (ufoY - ufoH < wallW):
        fill(255)
        #text("Game over",width/2,height/2)
        ufoX = width*6/8
        ufoY = height/2
        dufoX  =  0
        dufoY  =  0
        life -= 1
        if life < 1 :
            life = 0
            ufoX = 3000000
            ufoY = 3000000
            #winColor = (50,200,50)
            #setup()
    
        
        
                
#######################################################################################                
                                    

    
    

    if keyPressed:
        if keyPressing[0]:
            dufoY2 -= 0.02
            if dufoY2 <= -2:
                dufoY2 = -2

#おされるだけでおきるやつ↑
            dufoX2 -= 0.02
            if dufoX2 < -2:
                dufoX2 = -2
                


        if keyPressing[1]:
            dufoY2 -= 0.02
            if dufoY2 <= -2:
                dufoY2 = -2
                
                
            dufoX2 += 0.02
            if dufoX2 > 2:
                
                dufoX2 = 2
                
                
        if keyPressing[5]:#" "
            fill(50,200,50)
            ellipse(ufoX2,ufoY2,ufoH2 * 8,ufoH2*2)
            
    
    
    dufoY2 += 0.01
    if dufoY2 >= 2:
        
        dufoY2 = 2
        
        
    dufoX2 *= 0.995
    
    ufoX2 += dufoX2
    ufoY2 += dufoY2
    
    
    
#    fill(0,128,255)
 #   rect(wallW2,wallW2,width - wallW2 * 2,height - wallW2 *2)

    
  #  fill(255,255,0)
   # rect(destX2 - destW2,height - wallW2,destW2 * 2,wallW2/2) 

  
    fill(0,200,0)
    ellipse(ufoX2,ufoY2,ufoH2 * 2,ufoH2 * 2)
    
    fill(50,200,50)
    ellipse(ufoX2,ufoY2,ufoH2 * 4,ufoH2)
    
    #text("Congratulations!",width/2,height/2)
    
    


    if (ufoY2 + ufoH2 >= height - wallW2) and (ufoX2 > destX - destW) and (ufoX2  < destX + destW):
        fill(255)
        text("Congratulations!",width /2,height/2)
        winColor = (100,200,100)
        setup()
        
    elif (wallW2 > ufoX2 - ufoW2 *4) or (width - wallW2 < ufoX2 + ufoW2*4) or (ufoY2 + ufoH2 > height - wallW2) or (ufoY2 - ufoH2 < wallW2):
        fill(255)
        #text("Game over",width/2,height/2)
        ufoX2 = width*2/8
        ufoY2 = height/2
        dufoX2  =  0
        dufoY2  =  0
        life2 -= 1
        if life2 < 1 :
            life2 = 0
            ufoX2 = 3000000
            ufoY2 = 3000000
            #winColor = (200,50,50)
            #setup()

    
    
    
################################################################################

def keyPressed():
    global keyPressing
            
    if key == "a":
        keyPressing[0] = True
    elif key == "d":
        keyPressing[1] = True
    elif keyCode == LEFT:
        keyPressing[2] = True
    elif keyCode == RIGHT:
        keyPressing[3] = True
    elif key == ENTER:
        keyPressing[4] = True
    elif key == " ":
        keyPressing[5] = True

def keyReleased():
    global keyPressing
            
    if key == "a":
        keyPressing[0] = False
    elif key == "d":
        keyPressing[1] = False
    elif keyCode == LEFT:
        keyPressing[2] = False
    elif keyCode == RIGHT:
        keyPressing[3] = False
    elif key == ENTER:
        keyPressing[4] = False
    elif key == " ":
        keyPressing[5] = False
