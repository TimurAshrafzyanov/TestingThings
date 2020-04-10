import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (226, 85, 106)
PURPLE = (74, 66, 135)
ORANGE = (242, 159, 125)

class Button:
    def __init__(self, x, y, surface, image, image1=False):
        self.x = x
        self.y = y
        self.surface = surface
        self.ifimage = True
        self.image = image
        self.image1 = image1
        self.width = image.get_width()
        self.height = image.get_height()
        self.currentim = self.image
    def ispressed(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        if mouse_x > self.x:
            if mouse_x < self.x + self.width:
                if mouse_y > self.y:
                    if mouse_y < self.y + self.height:
                        mouse_click = pygame.mouse.get_pressed()
                        left_click = mouse_click[0]
                        if left_click:
                            if self.image1:
                                self.surface.blit(self.image1, (self.x, self.y))
                                self.currentim = self.image1
                                pygame.display.flip()
                            return True

    def drawbutton(self):
            self.surface.blit(self.currentim, (self.x, self.y))


class Slider:
    def __init__(self, x, y, surface, image, image1, image2, image3):
        self.x = x
        self.y = y
        self.surface = surface
        self.image = image
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pressed = False
        self.position = image
    def ispressed(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        if mouse_x > self.x and self.y < mouse_y < self.y + self.height:
            if mouse_x < self.x + self.width / 3:
                pygame.display.update()
                mouse_click = pygame.mouse.get_pressed()
                left_click = mouse_click[0]
                if left_click:
                    self.surface.blit(self.image1, (self.x, self.y))
                    pygame.display.flip()
                    self.pressed = True
                    self.position = self.image1
                    return 1
                else: return 0
            else:
                if mouse_x < self.x + 2 * (self.width / 3):
                    mouse_click = pygame.mouse.get_pressed()
                    left_click = mouse_click[0]
                    if left_click:
                        self.surface.blit(self.image2, (self.x, self.y))
                        pygame.display.flip()
                        self.pressed = True
                        self.position = self.image2
                        return 2
                    else:
                        return 0
                else:
                    mouse_click = pygame.mouse.get_pressed()
                    left_click = mouse_click[0]
                    if left_click:
                        self.surface.blit(self.image3, (self.x, self.y))
                        pygame.display.flip()
                        self.pressed = True
                        self.position = self.image3
                        return 3
                    else:
                        return 0
        return 0


    def drawbutton(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        if self.x + self.width > mouse_x > self.x  and self.y < mouse_y < self.y + self.height:
            if mouse_x < self.x + self.width/3:
                self.surface.blit(self.image1, (self.x, self.y))
                pygame.display.flip()
            else:
                if mouse_x < self.x + 2* (self.width / 3):
                    self.surface.blit(self.image2, (self.x, self.y))
                    pygame.display.flip()
                else:
                    self.surface.blit(self.image3, (self.x, self.y))
                    pygame.display.flip()
        else:
            self.surface.blit(self.position, (self.x, self.y))
            pygame.display.flip()