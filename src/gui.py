class GUI:
    import pygame
    pygame.init()
    display = pygame.display

    def __init__(self, x: "int", y: "int",
                 title: "str" = 'GUI', icon: "str" = None):
        self.screen = self.display.set_mode((x, y))
        self.screen.fill('black')
        self.display.set_caption(title)
        if icon is not None: self.display.set_icon(self.pygame.image.load(icon))
        self.done = False

    def run_loop(self):
        while not self.done:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.done = True
            self.display.flip()
