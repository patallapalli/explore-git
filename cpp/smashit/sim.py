import pygame, pygame.gfxdraw, time

import things

SHOW_TIME = False

class PygView(object):
  
    def __init__(self, layout, config):
        """Initialize pygame, window, background, font,...
           default arguments 
        """
        self.radius = config['radius']
        self.aspect = config['aspect']
        self.w = config['width']
        self.h = int(self.w / self.aspect)
        self.fps = float(config['fps'])
        self.RESTITUTION = float(config['restitution'])

        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.screen = pygame.display.set_mode((self.w, self.h), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.background.fill((255, 255, 255)) # fill background white
        
        self.clock = pygame.time.Clock()
        self.playtime = 0
        self.time_font = pygame.font.SysFont('monospace', 17)
        self.layout = layout

        self.make_objects()

    def make_objects(self):
        self.paddle = None
        self.balls = [things.Ball( (200, 150), (-2.1, 1.74), self.radius, self)]
        self.brickMap = None

    def fix_bg(self, contour = None, maxcost = None):
        """painting on the surface"""
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))   

    def stash_balls(self):
        for ball in self.balls:
            ball.update()
            pygame.gfxdraw.filled_circle(self.background, int(ball.pos[0]), int(ball.pos[1]), ball.radius, (145, 120, 170))

    def run(self):
        """The mainloop
        """
        running = True
        while running:
            # handle any events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            # Clean the background
            self.background.fill((255, 255, 255)) # fill background white
            if SHOW_TIME:
                self.playtime += self.clock.tick(self.fps) / 1000.0
                self.draw_text(self.time_font, "FPS: {:6.3} {:6.3} sec.".format(self.clock.get_fps(), self.playtime), (15, self.h - 15))
            # get all game-state from cpp-engine
            
            # update all objects' position, color, etc.
            self.stash_balls()

            # finally, update screen
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))          
        pygame.quit()

    def draw_text(self, font, txt, pos, color=(0,0,0)):
        t = font.render(txt, True, (0, 0, 0))
        self.screen.blit(t, pos)

    def transform(self, coords):
        # coords must lie in [0.0, 1.0] ~ x, y
        return (int(coords[0] * self.w), int(coords[1] * self.h))

# call with width of window and fps
config = {'width'       : 400,
          'height'      : 400 * 9 / 16,
          'friction'    : 0,
          'restitution' : 1,
          'radius'      : 8,
          'aspect'      : 16.0/9,
          'fps'         : 30}
layout = ""
myWin = PygView(layout, config)
myWin.fix_bg()
#time.sleep(2)

myWin.run()
#myWin.run()