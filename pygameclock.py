import pygame
import time
import math

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))

black = (0, 0, 0)
pink = (240, 150, 255)
cyan = (155, 255, 255)

clockpace = pygame.time.Clock()

def clocktime():
    seconds = time.localtime().tm_sec
    minutes = time.localtime().tm_min
    hours = time.localtime().tm_hour

    if hours < 10 and minutes < 10 and seconds < 10:
        return pygame.display.set_caption(f"0{hours}:0{minutes}:0{seconds}")
    elif hours < 10 and minutes < 10 and 10 <= seconds < 60:
        return pygame.display.set_caption(f"0{hours}:0{minutes}:{seconds}")
    elif hours < 10 and minutes < 60 and seconds < 10:
        return pygame.display.set_caption(f"0{hours}:{minutes}:0{seconds}")
    elif hours < 10 and 10 <= minutes < 60 and 10 <= seconds < 60:
        return pygame.display.set_caption(f"0{hours}:{minutes}:{seconds}")
    elif 10 <= hours < 24 and minutes < 10 and seconds < 10:
        return pygame.display.set_caption(f"{hours}:0{minutes}:0{seconds}")
    elif 10 <= hours < 24 and minutes < 10 and 10 <= seconds < 60: 
        return pygame.display.set_caption(f"{hours}:0{minutes}:{seconds}")
    elif 10 <= hours < 24 and 10 <= minutes < 60 and seconds < 10:
        return pygame.display.set_caption(f"{hours}:{minutes}:0{seconds}")
    else:
        return pygame.display.set_caption(f"{hours}:{minutes}:{seconds}")

def clock():
    add_to_seconds = round(6.0, 2)
    add_to_minutes = round(0.1, 2)
    add_to_hours = round(0.016666667, 10)

    start_angle = round(90, 2)

    seconds = time.localtime().tm_sec
    minutes = time.localtime().tm_min
    hours = time.localtime().tm_hour

    seconds_angle = (round(seconds, 2) * add_to_seconds) - start_angle
    minutes_angle = (round(minutes, 2) * add_to_seconds) - start_angle + (round(seconds) * add_to_minutes)
    hours_angle = (round(hours, 2) * round(30, 2)) - start_angle + (round(minutes) * round(0.3, 2) * add_to_hours)

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                exit()

        clocktime()

        screen.fill(black)

        # the outer edge of the clock
        pygame.draw.circle(screen, pink, (width/2, height/2), width/3, 5)

        # the inside point of the clock
        pygame.draw.circle(screen, pink, (width/2, height/2), 10)

        # second hand x and y
        second_x = 320+math.cos(math.radians(seconds_angle))*200
        second_y = 240+math.sin(math.radians(seconds_angle))*200

        # minute hand x and y
        minute_x = 320+math.cos(math.radians(minutes_angle))*190
        minute_y = 240+math.sin(math.radians(minutes_angle))*190

        # hour hand x and y
        hour_x = 320+math.cos(math.radians(hours_angle))*150
        hour_y = 240+math.sin(math.radians(hours_angle))*150

        # second hand
        pygame.draw.line(screen, cyan, (width/2, height/2),(second_x, second_y), 2)

        # minute hand
        pygame.draw.line(screen, cyan, (width/2, height/2),(minute_x, minute_y), 3)

        # hour hand
        pygame.draw.line(screen, cyan, (width/2, height/2),(hour_x, hour_y), 4)

        # adding to seconds
        seconds_angle += add_to_seconds
        if seconds_angle > (360 - start_angle - add_to_seconds):
            seconds_angle = -start_angle

        # adding to minutes
        minutes_angle += add_to_minutes
        if minutes_angle > (360 - start_angle - add_to_minutes):
            minutes_angle = -start_angle

        # adding to hours
        hours_angle += add_to_hours
        if hours_angle > (2*360 - start_angle - (2*add_to_hours)):
            hours_angle = -start_angle

        pygame.display.flip()
        clockpace.tick(1)

if __name__ == '__main__':
    clock()
