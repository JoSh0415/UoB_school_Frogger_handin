from pygame import *
init()

# define global variables
width = 800
height = 600
screen = display.set_mode((width, height))

timeLeft = 200

# frog globals
froggerImage = image.load("frog.png")
froggerImage = transform.scale(froggerImage,(40,40))
frog = Rect(380, 505, froggerImage.get_width(), froggerImage.get_height())
px = 0
onLog = 0
onTurtle = False

# car globals
carImage1 = image.load("car1.png")
carImage1 = transform.scale(carImage1,(50,40))
carImage2 = image.load("car2.png")
carImage2 = transform.scale(carImage2,(50,40))
carImage3 = image.load("car3.png")
carImage3 = transform.scale(carImage3,(50,40))
carImage4 = image.load("car4.png")
carImage4 = transform.scale(carImage4,(50,40))
carList = []
class carRecord():
	carRect = None
	carSpeed = 0
	carImage = None
car1 = carRecord()
car1x = carRecord()
car2 = carRecord()
car2x = carRecord()
car3 = carRecord()
car3x = carRecord()
car4 = carRecord()
car4x = carRecord()
car4xx = carRecord()

# cars 
car1.carRect = Rect(720,455,carImage1.get_width(), carImage1.get_height())
car1.carSpeed = -3
car1.carImage = carImage1
car1x.carRect = Rect(320,455,carImage1.get_width(), carImage1.get_height())
car1x.carSpeed = -3
car1x.carImage = carImage1
car2.carRect = Rect(250,405,carImage4.get_width(), carImage4.get_height())
car2.carSpeed = -2 
car2.carImage = carImage4
car2x.carRect = Rect(400,405,carImage4.get_width(), carImage4.get_height())
car2x.carSpeed = -2 
car2x.carImage = carImage4
car3.carRect = Rect(520,355,carImage2.get_width(), carImage2.get_height())
car3.carSpeed = 3 
car3.carImage = carImage2
car3x.carRect = Rect(120,355,carImage2.get_width(), carImage2.get_height())
car3x.carSpeed = 3 
car3x.carImage = carImage2
car4.carRect = Rect(620,305,carImage3.get_width(), carImage3.get_height())
car4.carSpeed = 2 
car4.carImage = carImage3
car4x.carRect = Rect(220,305,carImage3.get_width(), carImage3.get_height())
car4x.carSpeed = 2 
car4x.carImage = carImage3
car4xx.carRect = Rect(120,305,carImage3.get_width(), carImage3.get_height())
car4xx.carSpeed = 2 
car4xx.carImage = carImage3

carList = [car1,car2,car3,car4,car1x,car2x,car3x,car4x,car4xx]

#logs
class logRecord():
	logRect = None
	logSpeed = 0
	logLength = None
logImage = image.load("log.png")

log1 = logRecord()
log1x = logRecord()
log1xx = logRecord()
log2 = logRecord()
log2x = logRecord()
log2xx = logRecord()

log1.logRect = Rect(50,155,logImage.get_width(), logImage.get_height())
log1.logSpeed = -1
log1.logLength = 150
log1x.logRect = Rect(400,155,logImage.get_width(), logImage.get_height())
log1x.logSpeed = -1
log1x.logLength = 150
log1xx.logRect = Rect(560,155,logImage.get_width(), logImage.get_height())
log1xx.logSpeed = -1
log1xx.logLength = 150
log2.logRect = Rect(50,105,logImage.get_width(), logImage.get_height())
log2.logSpeed = 1
log2.logLength = 200
log2x.logRect = Rect(400,105,logImage.get_width(), logImage.get_height())
log2x.logSpeed = 1
log2x.logLength = 200
log2xx.logRect = Rect(700,105,logImage.get_width(), logImage.get_height())
log2xx.logSpeed = 1
log2xx.logLength = 200

logList = [log1,log1x,log1xx,log2,log2x,log2xx]

turtleImage = image.load("turtle.png")
turtleImage = transform.scale(turtleImage,(45,45))

turtle1 = Rect(52,202,45,45)
turtle2 = Rect(102,202,45,45)
turtle3 = Rect(402,202,45,45)
turtle4 = Rect(452,202,45,45)
turtle5 = Rect(502,202,45,45)
turtle6 = Rect(352,52,45,45)
turtle7 = Rect(402,52,45,45)
turtle8 = Rect(502,52,45,45)
turtle9 = Rect(152,52,45,45)
turtle10 = Rect(202,52,45,45)

turtleList = [turtle1,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7,turtle8,turtle9,turtle10]

font1 = font.Font("ARCADE_N.ttf",80)

gameOver = False
game = True

# define functions
def drawBackground():
	global screen, timeLeft
	screen.fill((0,0,0))
	draw.rect(screen,(200,35,255),(0,500,800,50))
	draw.rect(screen,(200,35,255),(0,250,800,50))
	draw.rect(screen,(0,200,10),(0,0,800,50))
	draw.rect(screen,(0,110,255),(0,50,800,200))
	draw.rect(screen,(0,200,10),(round(timeLeft),560,600,20))

def drawPlayer():
	global screen, frog, froggerImage
	screen.blit(froggerImage, frog)

def moveFrog():
	global px, frog
	frog.move_ip(px,0)

def drawCars():
	global screen, carList, carImage
	for cars in carList:
		screen.blit(cars.carImage, cars.carRect)

def drawLogs():
	global screen, logList, logImage, turtleList, turtleImage
	for logs in logList:
		logImage1 = transform.scale(logImage,(logs.logLength,40))
		screen.blit(logImage1, logs.logRect)
	for turtles in turtleList:
		screen.blit(turtleImage, turtles)

def moveCars():
	global screen, carList
	for cars in carList:
		cars.carRect[0] += cars.carSpeed
		if cars.carSpeed < 0:
			if cars.carRect[0] <= -60:
				cars.carRect[0] = 800
		if cars.carSpeed > 0:
			if cars.carRect[0] >= 860:
				cars.carRect[0] = -60
def moveLogs():
	global screen, logList
	for logs in logList:
		logs.logRect[0] += logs.logSpeed
		if logs.logSpeed < 0:
			if logs.logRect[0] <= -200:
				logs.logRect[0] = 800
		if logs.logSpeed > 0:
			if logs.logRect[0] >= 1000:
				logs.logRect[0] = -200


while game:
	frog[0] += onLog
	timeLeft += 1/4
	for e in event.get():
		if e.type == QUIT: 
			game = False
		elif e.type == KEYDOWN:
			if e.key == K_LEFT:
				px = -3
			if e.key == K_RIGHT:
				px = 3
			if e.key == K_UP:
				frog[1] -= 50
				onLog = 0
				onTurtle = False
			if e.key == K_DOWN:
				frog[1] += 50
				onLog = 0
				onTurtle = False
		elif e.type == KEYUP:
			onLog = 0
			onTurtle = False
			if e.key == K_LEFT or e.key == K_RIGHT:
				px = 0

	# movement
	moveCars()
	moveLogs()
	moveFrog()
	# game mechanics
	for cars in carList:
		if cars.carRect.colliderect(frog):
			gameOver = True
	for logs in logList:
		if frog[0] >= logs.logRect[0] and frog[0] <= logs.logRect[0] + logs.logLength and frog[1] >= logs.logRect[1] and frog[1] <= logs.logRect[1] + 40:
			onLog = logs.logSpeed
	for turtles in turtleList:
		if frog.colliderect(turtles):
			onTurtle = True
	if frog[1] >= 50 and frog[1] < 250 and onLog == 0 and onTurtle == False:
		gameOver = True
	if timeLeft >= 800:
		gameOver = True
	# drawing
	drawBackground()
	drawLogs()
	drawPlayer()
	drawCars()
	if frog[1] < 50:
		text = font1.render('You Win',True,(255,255,255))
		screen.blit(text,(100,252))
		gameOver = False
	if gameOver == True:
		screen.fill((0,0,0))
		text = font1.render('Game Over',True,(255,255,255))
		screen.blit(text,(50,252))
	
	# show the newly drawn screen (double buffering)
	display.flip()
	# short delay to slow down animation.
	time.delay(5)
