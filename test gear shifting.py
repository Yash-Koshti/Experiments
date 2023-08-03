import pygame
pygame.init()

GAME_WINDOW = pygame.display.set_mode([1300, 300])
pygame.display.set_caption("")

class Car:
    def __init__(self) -> None:
        self.gear = 0
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.motion = 0.03
        
        #This is formatted string which will only store float values with only 2 decimal values
        self.velocity = '0.0'
    
    def draw_car(self):
        self.frame = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(GAME_WINDOW, _black, self.frame)
        
        if self.gear == 1:
            self.top_speed = 10
        elif self.gear == 2:
            self.top_speed = 20
        elif self.gear == 3:
            self.top_speed = 30
        elif self.gear == -1:
            self.top_speed = -10
        else:
            self.top_speed = 0
        
    def accelerate(self, _key_pressed):
        if _key_pressed[pygame.K_UP]:
            if self.gear != 0:
                self.motion = 0.03
            else:
                self.motion = 0.01
            
            if float(self.velocity) < self.top_speed:
                #Here the calculation will be splitted into .2f format from whatever the float value is generated.
                #   eg: 3.332244 --> 3.33
                #       For actual demo you have screenshot.
                self.velocity = "{:.2f}".format(float(self.velocity) + self.motion)
            elif float(self.velocity) > self.top_speed:
                self.velocity = "{:.2f}".format(float(self.velocity) - self.motion)
            
            self.x += float(self.velocity)
        else:
            self.motion = 0.01
            
            if float(self.velocity) < 0:
                self.velocity = "{:.2f}".format(float(self.velocity) + self.motion)
            elif float(self.velocity) > 0:
                self.velocity = "{:.2f}".format(float(self.velocity) - self.motion)
            
            self.x += float(self.velocity)

_clock = pygame.time.Clock()
_fps = 60

_white = (255, 255, 255)
_black = (0, 0, 0)

_font = pygame.font.SysFont(None, 30)

car = Car()

def gameloop():
    _end_loop = False
    
    #car.x = (GAME_WINDOW.get_width() / 2) - (car.width / 2)
    car.y = GAME_WINDOW.get_height() - car.height
    
    while not _end_loop:
        
        GAME_WINDOW.fill(_white)
        
        car.draw_car()
        
        _vel_font = _font.render("Gear: " + str(car.gear) + ", Velocity: " + car.velocity + ", Position-x: " + "{:.2f}".format(car.x), 1, _black)
        GAME_WINDOW.blit(_vel_font, [GAME_WINDOW.get_width() - _vel_font.get_width(), 0])
        
        pygame.display.update()
        _clock.tick(_fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _end_loop = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                        
                if event.key == pygame.K_DOWN:
                    pass
                
                if event.key == pygame.K_LSHIFT:
                    if car.gear < 3:
                        car.gear += 1
                    
                if event.key == pygame.K_LCTRL:
                    if car.gear > -1:
                        car.gear -= 1
        #End of for loop of events
                    
        _key_pressed = pygame.key.get_pressed()
        
        car.accelerate(_key_pressed)
        # print(car.x) #This will print current position of the car.
    #End of while
                    
    pygame.quit()
    return
#End of gameloop

gameloop()