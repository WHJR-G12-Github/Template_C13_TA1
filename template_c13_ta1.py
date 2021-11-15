import pygame,random
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
images["invertedpipe"]=pygame.transform.flip(images["pipe"], False, True)
groundx=0
speed=0
# Create a variable 'score' and initialize it to 0

# Create a variable 'state' and assign the value "play" to it

# Create the font of style 'freesansbold.ttf' and size 20 and name it 'score_font'


class Bird:
    bird=pygame.Rect(100,250,30,30)
    

    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
    def moveup(self):
        global speed
        speed=speed-5
    def display(self):
        screen.blit(images["bird"],self.bird)

class Pipe:
    def __init__(self,x):
        self.height=random.randint(150,400)
        self.tpipe=pygame.Rect(x,self.height-400,40,300)
        self.bpipe=pygame.Rect(x,self.height+150,40,300)
    def display(self):
      screen.blit(images["pipe"],self.bpipe)
      screen.blit(images["invertedpipe"],self.tpipe)
    def move(self):
        self.tpipe.x-=2
        self.bpipe.x-=2
        # Check if 'self.tpipe.x' is less than -40
        
            # Assign a value greater than game screen width to 'self.tpipe.x'
           
            # Assign a value greater than game screen width to 'self.bpipe.x'
            
            # Assign a random value from 150 to 400 to 'self.height'
            
            # Assign 'self.height-400' to 'self.tpipe.y'
            
            # Assign 'self.height+150' to 'self.bpipe.y'
            
bird1=Bird()
pipe1=Pipe(250)
while True:  
  
  screen.blit(images["bg"],[0,0])
  # Create the text to be displayed for score using 'score_font' and naming it 'score_text'
  
  # Display 'score_text' at the location [10,10]
  
  # Move the following code inside the condition if state == "play":
  groundx-=5
  if groundx<-450:
      groundx=0
  # The code till the previous line has to be moved
  screen.blit(images["ground"],[groundx,550])
  bird1.movedown()
  bird1.display()
  pipe1.display()
  pipe1.move()
  # Check if the value of 'state' is "play"
  
      # Move the code to move the ground towards left infinitely
      
      
         
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        # Add the condition to check whether the value of 'state' is "play"
        if event.key==pygame.K_SPACE:
            bird1.moveup()  
  
  
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
