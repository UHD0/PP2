import pygame as pg

pg.init()
screen = pg.display.set_mode((1010,810))

done = False
color = (255, 0, 0)

x = 505
y = 405

step = 20

while not done:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        done = True
                if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                                done = True
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and x > 25:
                x -= step
        if keys[pg.K_RIGHT] and x < 975:
                x += step
        if keys[pg.K_UP] and y > 25:
                y -= step
        if keys[pg.K_DOWN] and y < 775:
                y += step

        screen.fill((255,255,255))

        pg.draw.circle(screen, color, (x,y), 25)


        pg.display.flip()