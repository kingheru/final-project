import pygame
pygame.init()

Screen_X = 800
Screen_Y = 511
#storing custom made main menu screen
bg = pygame.image.load("background.png")
screen = pygame.display.set_mode((Screen_X,Screen_Y))
pygame.display.set_caption("Risk x Reward")
#loading the font and text questions
base_font = pygame.font.Font(None,32)
user_text = ""
desc = "Event/Party Profit Simulator (integers only)"
helper = "Click Start To Add/Skip"
question0 = "Whats The Max Capacity of your Venue?"
question1 = "How Much Should General Entry Cost?"
question2 = "What is The Average Cost for a Cold Beverage?"
question3 = "How Much does the Venue Cost / Daily Rent?"
question4 = "YOUR TOTAL PROFITS ARE..."
data1 = 0
data2 = 0
data3 = 0
data4 = 0
text = False
ques_count = 0
#loading start button image
start_png = pygame.image.load("start_button.png").convert_alpha()
#creating rectangle for input box
input_rect = pygame.Rect(200,200,340,32)
input_color = pygame.Color("skyblue")
#Creating a class for buttons
class Button():
    def __init__(self, x, y, image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width *scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self):
        action = False
        #find mouse position
        pos = pygame.mouse.get_pos()
        
        #test if mouse is hovering over

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print("True")
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
    
start_button = Button(300,300,start_png,0.7)

screen.blit(bg, (0,0))

#the game loop

engine = True
while engine:
    
    
    if start_button.draw():
        screen.fill(("black"))
        text = True
        pygame.draw.rect(screen,input_color,input_rect,2)
        ques_surface = base_font.render(eval("question" + str(ques_count)),True,(255,255,255))
        screen.blit(ques_surface,(200,150))
        ques_count += 1
        help_surface = base_font.render(helper,True,(255,255,255))
        screen.blit(help_surface, (40,350))
        if ques_count == 2 and user_text != "":
            data1 =  int(user_text)
        if ques_count == 3:
            data2 = int(user_text)
        if ques_count == 4:
            data3 = int(user_text)
        if ques_count == 5:
            data4 = int(user_text)    
        if ques_count == 5:
            result = ((data1 * data2) + (data3*data1*0.5) - data4)
            user_text = str(result)
            text_surface = base_font.render(user_text,True,(255,255,255))
            screen.blit(text_surface, (input_rect.x + 5,input_rect.y + 5))
            
        if ques_count != 6:
            user_text = "" 
    if text == False:
        desc_surface = base_font.render(desc,True,(255,255,255))
        screen.blit(desc_surface, (200,200))

    text_surface = base_font.render(user_text,True,(255,255,255))
    screen.blit(text_surface, (input_rect.x + 5,input_rect.y + 5))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and text == True:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[0:-1]
            else:
                user_text += event.unicode
            
        if event.type == pygame.QUIT:
            engine = False
    pygame.display.update()
pygame.quit()

