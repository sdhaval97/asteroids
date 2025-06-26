import pygame

class ScoreBoard:
    def __init__(self, font_size=36):
        self.score = 0
        self.font = pygame.font.SysFont(None, font_size)
    
    def increment(self):
        self.score += 1
    
    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))