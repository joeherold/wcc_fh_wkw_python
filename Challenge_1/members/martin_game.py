# Erstellung eines Spiels mit pygame
# pygame ist eine Library, welche die einfache Erstellung von Spielen ermöglicht. 
# Nachfolgend wird die Erstellung eines einfachen Spiels mit Pygame dargestellt. 
# Was bringt diese Kenntnis für FH Schüler? Während langweiligen wirtschaftsfächern kann sich die Zeit vertrieben werden. 

# Um pygame auszuführen muss dies in der Shell / Terminal installiert werden. Dazu ist der folgende Befehle notwendig: 
# pip install pygame

# Mit dem nachfolgendem Befehl kann die Installation in der Shell / Terminal getestet werden. Erschein ein Mini-Game hat es funktioniert. 
# python3 -m pygame.examples.aliens

import pygame # Import der Library
import random # Ermöglicht die Generierung von Zufallswerten

# Damit wird die Steuerung für das Spiel importiert
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Festlegung des Bildschirms für das Spiel. Das Fenster wird vom Betriebssystem geöffnet. 
fensterBreite = 800
fensterHöhe = 600

heldFarbe = (50, 50, 50)

# Definition des Spielers: 
class Held(pygame.sprite.Sprite):
    def __init__(self):
        super(Held, self).__init__()
        self.surf = pygame.Surface((80, 40))
        self.surf.fill(heldFarbe)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):     # Festlegung der Bewegung des Spielers
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -6)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 6)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-6, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(6, 0)
    
        if self.rect.left < 0:          # Behalten des Spielers am Bildschirm
            self.rect.left = 0
        if self.rect.right > fensterBreite:
            self.rect.right = fensterBreite
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= fensterHöhe:
            self.rect.bottom = fensterHöhe

# Erstellen von Feinden am Spielfeld
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((40, 20))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(fensterBreite + 20, fensterBreite + 100),
                random.randint(0, fensterHöhe),
            )
        )
        self.speed = random.randint(2, 10)
# Angaben zur Bewegung der Hindernisse    
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


pygame.init() # Initialisierung von pygame, damit dies auch verwendet werden kann. Der Vorteil ist, dass pygame auf Windows, Linux und Mac genutzt werden kann. 


screen = pygame.display.set_mode((fensterBreite, fensterHöhe)) # Erstellt das Fenster für das Spiel. Die Einstellungen werden on oben übernommen. 

# Hinzufügen von Feinden, alle 250 Millisekunden, 4/Sekunde. Dies gilt für das Gesamt Spiel
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250) 


held = Held() # Erstellen des Spielers


feinde = pygame.sprite.Group() # Fesstellen von Kollisionen
all_sprites = pygame.sprite.Group() # Erstellen einer Gruppe von allen Elementen zum Rendern
all_sprites.add(held)

clock = pygame.time.Clock() # Erstellen einer Uhr für die Spielgeschwindigkeit

# Die Ausführung des Spiels festlegen, bis diese beendet wird durch schließen des Fensters. 
running = True 

while running:
    for event in pygame.event.get(): # Erfasst eingaben im Spiel durch den User. 
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: # Das Spiel wird durch die Taste Escape beendet. FUNKTIONIERT NOCH NICHT
                running = False
        elif event.type == QUIT: # Das Spiel wird durch schließen des Fensters beendet
            running = False
        elif event.type == ADDENEMY: # Hinzufügen von Feinden im Spiel und Zuweisung zu allen Elementen
            new_enemy = Enemy()
            feinde.add(new_enemy)
            all_sprites.add(new_enemy)
    
    pressed_keys = pygame.key.get_pressed() # Erfassen der Usereingaben

    held.update(pressed_keys) # Ermöglicht die Steuerung des Spielerelements

    feinde.update() # die Feinde werden aktualisiert

    screen.fill((255, 204, 153)) # die Hintergrundfarbe
    #pygame.display.flip()

    # Anzeigen aller Spielelemente
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    if pygame.sprite.spritecollideany(held, feinde):# Prüfen ob der Spieler mit den Feinden kollidiert
        held.kill()
        running = False
        
    pygame.display.flip() # Aktualisiert den Bildschirm

    clock.tick(100) # Frames per second
