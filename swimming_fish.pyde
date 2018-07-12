xCoordinate=50
speed=5
FishSize=50 


def setup():
    size(400,400)
    background(0,255,255)
    fish(100,200,60,40)
    fish(random(0,400),random(0,400),random(10,100),random(10,100))
    
def fish(xCoordinate,yCoordinate,fishWidth,fishHeight):
    fill(random(250), random(250),random(250))
    ellipse(xCoordinate,yCoordinate,fishWidth,fishHeight)
    triangle(xCoordinate+fishWidth/2,yCoordinate,xCoordinate+fishWidth,yCoordinate+fishHeight/2,xCoordinate+fishWidth,yCoordinate-fishHeight/2)
    fill(250,250,250)
    ellipse(xCoordinate-15,yCoordinate-2,5,5)
    
def draw():
    background(0,255,255)
    global xCoordinate,yCoordinate,speed, FishSize
    xCoordinate += speed
    leftBoundary = FishSize / 2
    rightBoundary = 400 - FishSize / 2
    if xCoordinate >rightBoundary or xCoordinate <=leftBoundary:
        speed = -speed
    fill(255,5,250)
    fish(50,xCoordinate,50,50)    
    fish(xCoordinate,50,50,50)  
