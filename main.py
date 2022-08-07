# First part
# from SLAMTEST import env, sensors
# import pygame
# import math
#
# environment = env.buildEnvironment((600, 1200))
# running = True  # for closing the setup
#
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     pygame.display.update()


#second Part
from SLAMTEST import env, sensors
import pygame
environment = env.buildEnvironment((600, 1200))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(200, environment.originalMap, uncertanity=(0.5, 0.01))
environment.map.fill((0, 0, 0))
environment.infomap = environment.map.copy()

running = True

while running:
    sensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorON=True
        elif not pygame.mouse.get_focused():
            sendorON=False
    if sendorON:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sense_obstacles()
        environment.dataStorge(sensor_data)
        environment.show_sensorData()
    environment.map.blit(environment.infomap, (0,0))
    pygame.display.update()
