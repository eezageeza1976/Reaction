#Game to test your reactions
import pygame as pg
import pygame.freetype
import time
from rectangle import Rectangle
from rectangle import Timer

WIN_WIDTH = 1200
WIN_HEIGHT = 980
BLACK = (0, 0, 0)
START_SCREEN_TEXT_POS = (250, WIN_HEIGHT/2)

def windowSetup():
    window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    window.fill(BLACK)
    return window

screen = windowSetup()


def main():
    running = True
    timer_stop = False
    game_start = False
    game_ended = False
    rect_list = []
    timer_list = []
    next_rect = 0
    next_timer = 0
    timer_posY = 100
    game_start_time = 0
    total_squares = 10
    font = pg.freetype.SysFont(None, 50)
    font.origin = True
    split_text_posX = 250
    split_text_posY = 100
        
    for i in range(total_squares):
        rect_list.append(Rectangle())

    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return pg.K_ESCAPE
            elif event.type == pg.MOUSEBUTTONDOWN:
                if game_start:
                    if rect_list[next_rect].collision(pg.mouse.get_pos()):
                        timer_stop = True
                        timer_list[next_timer].setEndTime()
                        timer_list[next_timer].CalcSplit()
                        timer_list[next_timer].draw(screen)
                elif not game_start:
                    game_start = True
                    game_start_time = time.time()
                    timer_list.append(Timer())
        
        screen.fill(BLACK)        
        
        if len(timer_list) <= total_squares:
            if game_start:
                if not timer_stop:
                    rect_list[next_rect].draw(screen)
                    
                    for t in timer_list:
                        t.draw(screen)
                    
                if timer_stop:
                    timer_posY += 30
                    timer_list.append(Timer(timer_posY))
                    next_rect += 1
                    next_timer += 1
                    timer_stop = False
                    
                timer_list[next_timer].CalcTime(game_start_time)
                
            elif not game_start and not game_ended:
                start_screen = (f"Press Mouse Button To Start")
                font.render_to(screen, START_SCREEN_TEXT_POS, start_screen, pg.Color('dodgerblue'))
        
        elif len(timer_list) > total_squares:
            game_ended = True
        
        if game_ended:
            for t in timer_list:
                text = '{minutes:02d}:{seconds:02d}:{millis:02d}'.format(minutes=int(t.split_minutes),
                                                                         millis=int(t.split_millis),
                                                                         seconds=int(t.split_seconds))
                font.render_to(screen, (split_text_posX, split_text_posY), text, pg.Color('dodgerblue'))
                split_text_posY += 40
                
            split_text_posY = 100   
                
        pg.display.flip()
        
        
        
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()