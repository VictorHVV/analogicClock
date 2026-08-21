import pygame
from math import pi, sin, cos
import datetime

width, height = 600, 600
center = (width // 2, height // 2)
clock_radius = 300


pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()
FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)

def numbers (number, size, position):
    font = pygame.font.SysFont("Arial", size, True, False)
    text = font.render(number, True, white)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect) 
    
def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta/180) 
    y = r * cos(pi * theta/180) 
    return x + width // 2, height // 2 - y

def main():
    run = True
    while run:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        seconds = current_time.second
        minutes = current_time.minute
        hours = current_time.hour
        
        day = current_time.day
        month = current_time.month
        year = current_time.year
        weekday = current_time.today().isoweekday()
        calendar = current_time.isocalendar()
        
        weekdays_abbr = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}
        weekday_abbr = weekdays_abbr.get(weekday)
        
        months_abbr = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
        month_abbr = months_abbr.get(month)
        
        screen.fill(black)
        pygame.draw.circle(screen, white, center, clock_radius -5, 5)
        pygame.draw.circle(screen, white, center, 10)
        pygame.draw.rect(screen, grey, (width / 2 - 136, height / 2 - 22, 70, 45), 1)
        pygame.draw.rect(screen, red, (width / 2 - 205, height / 2 - 22, 70, 45), 1)
        pygame.draw.rect(screen, green, (width / 2 + 65, height / 2 - 22, 70, 45), 1)
        pygame.draw.rect(screen, blue, (width / 2 + 135, height / 2 - 22, 70, 45), 1)
        pygame.draw.rect(screen, white, (width / 2 - 50, height / 2 + 110, 100, 45), 1)
        
        numbers(str(weekday_abbr), 30, (width / 2 - 170, height / 2))
        numbers(str(calendar[1]), 30, (width / 2 - 100, height / 2))
        numbers(str(day), 30, (width / 2 + 100, height / 2))
        numbers(str(month_abbr), 30, (width / 2 + 170, height / 2))
        numbers(str(year), 30, (width / 2, height / 2 + 130))
        
        for number in range(1, 13):
            numbers(str(number), 60, polar_to_cartesian(clock_radius - 60, number * 30))
            
        
        for number in range(0, 360, 6):
            if number % 5:
                pygame.draw.line(screen, white, polar_to_cartesian(clock_radius - 10, number), polar_to_cartesian(clock_radius - 20, number), 2)
            else:
                pygame.draw.line(screen, white, polar_to_cartesian(clock_radius - 10, number), polar_to_cartesian(clock_radius - 25, number), 6)
        
        #hours hand
        r = 150
        theta = (hours % 12 + minutes / 60) * (360 / 12)
        pygame.draw.line(screen, white, center, polar_to_cartesian(r, theta), 8)
        
        #minutes hand
        r = 200
        theta = (minutes % 60 + seconds / 60) * (360 / 60)
        pygame.draw.line(screen, white, center, polar_to_cartesian(r, theta), 6)

        #Seconds hand
        r = 250
        theta = seconds * (360 / 60)
        pygame.draw.line(screen, red, center, polar_to_cartesian(r, theta), 4)
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    
main()