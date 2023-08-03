import pygame
pygame.init()

GAME_WINDOW = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Test Option Selection")

_clock = pygame.time.Clock()
_fps = 60

_white = (255, 255, 255)
_black = (0, 0, 0)
_selector = (112, 142, 190)

def gameloop():
    _end_loop = False
    _font = pygame.font.SysFont(None, 30)
    
    _options_dict = {1 : pygame.Rect((GAME_WINDOW.get_width() / 2) - 100, 200, 200, 30), 
                     2 : pygame.Rect((GAME_WINDOW.get_width() / 2) - 100, 230, 200, 30)}
    i = 1
    
    while not _end_loop:
        
        GAME_WINDOW.fill(_white)
        
        pygame.draw.rect(GAME_WINDOW, _selector, _options_dict[i])
        
        _opt_1 = _font.render("SINGLE PLAYER", 1, _black)
        GAME_WINDOW.blit(_opt_1, [(_options_dict[1].centerx - _opt_1.get_width() / 2), _options_dict[1].centery - _opt_1.get_height() / 2])
        
        _opt_2 = _font.render("TWO PLAYERS", 1, _black)
        GAME_WINDOW.blit(_opt_2, [(_options_dict[2].centerx - _opt_2.get_width() / 2), _options_dict[2].centery - _opt_2.get_height() / 2])
        
        pygame.display.update()
        _clock.tick(_fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _end_loop = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if i > 1:
                        i -= 1
                        
                if event.key == pygame.K_DOWN:
                    if i == 1:
                        i += 1
                                        
    pygame.quit()
    return

gameloop()