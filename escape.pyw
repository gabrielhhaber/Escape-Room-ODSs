from pythonBgt import *
#Global variables
intro=loadSound("sounds/intro.ogg")
def main():
	showWindow("Escape Room ODSs")
	intro.playLogo()
	begin()

def begin():
	message("Boas vindas ao jogo Escape Room dos Objetivos de Desenvolvimento Sustentável (ODSs)! Neste jogo você deverá passar por diversas salas, cada uma com um jogo representando um ODS específico. Cada sala será um nível separado do jogo, e você deve completar cada nível para escapar da sala e ir para a próxima, até chegar ao final! Pressione enter para começar a aventura.")
	playGame1()

#Game1 structure
game1Base="sounds/game_1/"
mapSize=40
moveTime=200
trashCollide=loadSound(game1Base+"trash_collide.ogg")
class Player:
	def __init__(self, x, stepSound):
		self.x=x
		self.stepSound=loadSound(stepSound)
		self.moveTimer=Timer(paused=False)
	def move(self, dir):
		if not self.moveTimer.elapsed>=moveTime:
			return
		self.moveTimer.start()
		if dir=="left":
			if self.x>0:
				self.x-=1
				self.stepSound.play()
			else:
				trashCollide.play()
		elif dir=="right":
			if self.x<mapSize:
				self.x+=1
				self.stepSound.play()
			else:
				trashCollide.play()
class TrashCan:
	def __init__(self, x, type):
		self.x=x
		self.type=type
		self.sound=loadSound(game1Base+"trash_can.ogg")

def playGame1():
	def updateSounds():
		for trashCan in trashCans:
			positionSound1d(trashCan.sound, player.x, trashCan.x)

	player=Player(20, game1Base+"step.ogg")
	organicTrash=TrashCan(0, "organic")
	inorganicTrash=TrashCan(mapSize, "inorganic")
	inorganicTrash.sound.pitch-=15
	trashCans=[]
	trashCans.append(organicTrash)
	trashCans.append(inorganicTrash)
	for trashCan in trashCans:
		trashCan.sound.playLooped()
		wait(5)
	updateSounds()
	while True:
		updateSounds()
		if keyDown(K_LEFT):
			player.move("left")
		elif keyDown(K_RIGHT):
			player.move("right")
		elif keyPressed(K_RETURN):
			player.interact()
		wait(5)


main()