import math
import random
import pygame


class Background:
   

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wall_top = 46        # épaisseur du mur du haut
        self.wall_side = 14       # épaisseur des murs gauche / droite / bas
        self.rng = random.Random(7)        # même décor à chaque lancement
        self.lights = []                   # positions des lumières d'urgence
        self.glow = self.make_glow(38, (255, 40, 40))
        self.surface = pygame.Surface((width, height))
        self.build()

    # ---------- outils ----------
    def make_glow(self, radius, color):
        """Halo lumineux : cercles de plus en plus transparents vers l'extérieur."""
        glow = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        for r in range(radius, 0, -1):
            alpha = int(110 * (1 - r / radius) ** 2)
            pygame.draw.circle(glow, (color[0], color[1], color[2], alpha),
                               (radius, radius), r)
        return glow

    def neon_line(self, start, end, color):
        """Ligne néon : 3 traits superposés (large et pâle -> fin et vif)."""
        layer = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for thickness, alpha in ((11, 35), (6, 80), (2, 255)):
            pygame.draw.line(layer, (color[0], color[1], color[2], alpha),
                             start, end, thickness)
        self.surface.blit(layer, (0, 0))

    # ---------- construction du décor ----------
    def build(self):
        self.draw_floor()
        self.draw_walls()
        self.draw_doors()
        self.draw_screens()
        self.draw_warning_signs()
        self.draw_broken_equipment()
        self.draw_neon()
        self.draw_emergency_lights()

    def draw_floor(self):
        s = self.surface
        tile = 50
        for row in range(self.height // tile + 1):
            for col in range(self.width // tile + 1):
                shade = (26, 31, 44) if (row + col) % 2 == 0 else (22, 26, 37)
                pygame.draw.rect(s, shade, (col * tile, row * tile, tile, tile))
                pygame.draw.rect(s, (34, 40, 56), (col * tile, row * tile, tile, tile), 1)
        # rayures et taches discrètes sur le sol
        for _ in range(25):
            x = self.rng.randint(30, self.width - 30)
            y = self.rng.randint(60, self.height - 30)
            dx = self.rng.randint(-25, 25)
            dy = self.rng.randint(-10, 10)
            pygame.draw.line(s, (31, 37, 52), (x, y), (x + dx, y + dy), 1)

    def draw_walls(self):
        s = self.surface
        w, h = self.width, self.height
        t, e = self.wall_top, self.wall_side
        metal = (38, 44, 60)
        edge = (72, 84, 110)
        pygame.draw.rect(s, metal, (0, 0, w, t))                 # haut
        pygame.draw.rect(s, metal, (0, 0, e, h))                 # gauche
        pygame.draw.rect(s, metal, (w - e, 0, e, h))             # droite
        pygame.draw.rect(s, metal, (0, h - e, w, e))             # bas
        pygame.draw.line(s, edge, (0, t), (w, t), 3)
        pygame.draw.line(s, edge, (e, t), (e, h - e), 2)
        pygame.draw.line(s, edge, (w - e, t), (w - e, h - e), 2)
        pygame.draw.line(s, edge, (e, h - e), (w - e, h - e), 2)
        # panneaux du mur du haut (joints verticaux + boulons)
        for x in range(100, w, 100):
            pygame.draw.line(s, (28, 33, 46), (x, 0), (x, t - 3), 2)
            pygame.draw.circle(s, (70, 80, 100), (x - 6, 8), 2)
            pygame.draw.circle(s, (70, 80, 100), (x + 6, 8), 2)

    def draw_doors(self):
        s = self.surface
        frame = (95, 108, 135)
        # deux portes dans le mur du haut
        for x in (120, 560):
            pygame.draw.rect(s, (16, 20, 30), (x, 6, 70, 40))
            pygame.draw.rect(s, frame, (x, 6, 70, 40), 3)
            pygame.draw.line(s, frame, (x + 35, 6), (x + 35, 46), 2)
            pygame.draw.rect(s, (0, 190, 255), (x + 8, 10, 54, 3))   # bandeau lumineux
        # porte sur le mur de droite
        pygame.draw.rect(s, (16, 20, 30), (self.width - 14, 230, 14, 80))
        pygame.draw.rect(s, frame, (self.width - 14, 230, 14, 80), 2)

    def draw_screens(self):
        s = self.surface
        for x, color in ((270, (0, 220, 255)), (400, (60, 255, 140))):
            pygame.draw.rect(s, (10, 16, 24), (x, 8, 56, 32))
            pygame.draw.rect(s, (85, 96, 120), (x, 8, 56, 32), 3)
            for i in range(4):                    # lignes de texte / données
                length = 14 + (i * 11 + x) % 28
                pygame.draw.line(s, color, (x + 6, 15 + i * 6), (x + 6 + length, 15 + i * 6), 2)

    def draw_warning_signs(self):
        s = self.surface
        # triangle d'avertissement dans le mur du haut
        cx, cy = 490, 26
        pygame.draw.polygon(s, (205, 170, 30), [(cx, cy - 16), (cx - 17, cy + 12), (cx + 17, cy + 12)])
        pygame.draw.polygon(s, (30, 26, 10), [(cx, cy - 16), (cx - 17, cy + 12), (cx + 17, cy + 12)], 2)
        pygame.draw.line(s, (30, 26, 10), (cx, cy - 6), (cx, cy + 3), 3)
        pygame.draw.circle(s, (30, 26, 10), (cx, cy + 8), 2)
        # bandes jaune / noir dans le coin bas-droit (zone dangereuse)
        x0, y0, w, h = self.width - 120, self.height - 14, 100, 14
        s.set_clip(pygame.Rect(x0, y0, w, h))
        pygame.draw.rect(s, (25, 22, 10), (x0, y0, w, h))
        for i in range(-h, w, 18):
            pygame.draw.polygon(s, (170, 140, 25),
                                [(x0 + i, y0 + h), (x0 + i + 9, y0 + h),
                                 (x0 + i + 9 + h, y0), (x0 + i + h, y0)])
        s.set_clip(None)

    def draw_broken_equipment(self):
        s = self.surface
        # machine cassée en bas à gauche
        pygame.draw.rect(s, (44, 50, 68), (30, self.height - 78, 64, 50))
        pygame.draw.rect(s, (90, 100, 125), (30, self.height - 78, 64, 50), 2)
        pygame.draw.polygon(s, (52, 58, 78), [(30, self.height - 78), (94, self.height - 78),
                                              (80, self.height - 92), (20, self.height - 86)])
        pygame.draw.lines(s, (14, 16, 24), False,
                          [(50, self.height - 78), (58, self.height - 64),
                           (52, self.height - 52), (64, self.height - 38)], 2)   # fissure
        pygame.draw.line(s, (255, 220, 60), (88, self.height - 58), (98, self.height - 66), 2)   # étincelles
        pygame.draw.line(s, (0, 220, 255), (88, self.height - 58), (100, self.height - 54), 2)
        # tube de laboratoire brisé en bas à droite
        pygame.draw.rect(s, (36, 48, 66), (self.width - 80, self.height - 62, 18, 34))
        pygame.draw.rect(s, (80, 110, 140), (self.width - 80, self.height - 62, 18, 34), 2)
        pygame.draw.polygon(s, (60, 255, 140), [(self.width - 78, self.height - 36), (self.width - 60, self.height - 36),
                                                (self.width - 52, self.height - 28), (self.width - 90, self.height - 28)])  # liquide renversé

    def draw_neon(self):
        w, h = self.width, self.height
        t, e = self.wall_top, self.wall_side
        blue = (0, 150, 255)
        self.neon_line((e + 4, h - e - 4), (w - e - 4, h - e - 4), blue)     # bas
        self.neon_line((e + 4, t + 4), (e + 4, h - e - 4), blue)             # gauche

    def draw_emergency_lights(self):
        s = self.surface
        for x in (40, 330, 745):
            y = 23
            pygame.draw.circle(s, (50, 14, 14), (x, y), 9)
            pygame.draw.circle(s, (210, 35, 35), (x, y), 6)
            pygame.draw.circle(s, (95, 105, 130), (x, y), 9, 2)
            self.lights.append((x, y))

    # ---------- affichage ----------
    def draw(self, screen):
        screen.blit(self.surface, (0, 0))
        # les lumières rouges clignotent doucement
        pulse = (math.sin(pygame.time.get_ticks() / 350) + 1) / 2
        self.glow.set_alpha(int(70 + 150 * pulse))
        r = self.glow.get_width() // 2
        for x, y in self.lights:
            screen.blit(self.glow, (x - r, y - r))
