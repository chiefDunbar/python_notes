import pygame
import random

class LoveAndMonsters:

    def __init__(self, resolution=(640, 480)):
        self.resolution = resolution
        pygame.init()
        self.load_images()
        self.initialize_attributes()
        self.initialize_game()

    def initialize_attributes(self):
        self.background_color = (255, 255, 255)
        self.banner_color = (204, 229, 225)
        self.banner_height = int(self.resolution[1] * 0.15)
        self.score = 0
        self.robot_position = [self.resolution[0] / 2 - self.robot.get_width() / 2, self.resolution[1] - self.robot.get_height()]
        self.robot_speed = 2
        self.robot_move_left = False
        self.robot_move_right = False
        self.coins = []
        self.coin_speed = 3
        self.monsters = []
        self.monster_speed = 4

    def initialize_game(self):
        self.create_screen()
        self.run_game()

    def load_images(self):
        self.robot = pygame.image.load("robot.png")
        self.coin = pygame.image.load("coin.png")
        self.monster = pygame.image.load("monster.png")

    def create_screen(self):
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Love and Monsters")
        self.clock = pygame.time.Clock()

    

    def print_screen(self):

        def print_background():
            self.screen.fill(self.background_color)

        def print_banner():               
            pygame.draw.rect(self.screen, self.banner_color, (0, 0, self.resolution[0], self.banner_height))
            instructions_text = pygame.font.SysFont("Arial", 24).render(f"Exit: esc     Reset: F2", True, (0, 0, 0))
            self.screen.blit(instructions_text, ((self.resolution[0] * 0.05) // 1, (self.resolution[1] * 0.05) // 1))

        def print_score():
            score_text = pygame.font.SysFont("Arial", 24).render(f"Score: {self.score}", True, (0, 0, 0))
            self.screen.blit(score_text, (self.resolution[0] - score_text.get_width() - 20, 20))

        def print_characters():
            self.screen.blit(self.robot, self.robot_position)
            for coin_position in self.coins:
                self.screen.blit(self.coin, coin_position)
            for monster_position in self.monsters:
                self.screen.blit(self.monster, monster_position)
                
        print_background()
        print_banner()
        print_score()
        print_characters()
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.robot_move_left = True
                if event.key == pygame.K_RIGHT:
                    self.robot_move_right = True
                if event.key == pygame.K_F2:
                    self.initialize_attributes()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.robot_move_left = False
                if event.key == pygame.K_RIGHT:
                    self.robot_move_right = False

    def update_robot_position(self):
        if self.robot_move_left and self.robot_position[0] > 0:
            self.robot_position[0] -= self.robot_speed
        if self.robot_move_right and self.robot_position[0] < self.resolution[0] - self.robot.get_width():
            self.robot_position[0] += self.robot_speed

    def drop_stuff(self):
        def new_stuff():
            if random.random() > 0.95:
                self.coins.append([random.randint(0, self.resolution[0] - self.coin.get_width()), self.banner_height])
            if random.random() > 0.98:
                self.monsters.append([random.randint(0, self.resolution[0] - self.monster.get_width()), self.banner_height]) 

        def out_of_bounds(height: int):
            return height >= self.resolution[1] - 20
        
        def robot_touched(object_position: tuple, object_type: str):
            object_dimension = (self.coin.get_width(), self.coin.get_height()) if object_type == "coin" else (self.monster.get_width(), self.monster.get_height())
            return (self.robot_position[0] <= object_position[0] <= self.robot_position[0] + self.robot.get_width() and
                    self.robot_position[1] <= object_position[1] <= self.robot_position[1] + self.robot.get_height())

        new_stuff()

        # iterating in reverse order to delete out of bounds stuff
        for c in range(len(self.coins) - 1, -1, -1):
            self.coins[c][1] += self.coin_speed
            if out_of_bounds(self.coins[c][1]):
                del self.coins[c]
            elif robot_touched(self.coins[c], "coin"):
                self.score += 1
                del self.coins[c]

        for m in range(len(self.monsters) - 1, -1, -1):
            self.monsters[m][1] += self.monster_speed
            if out_of_bounds(self.monsters[m][1]):
                del self.monsters[m]
            elif robot_touched(self.monsters[m], "monster"):
                self.score -= 2
                del self.monsters[m]

    def run_game(self):
        while True:
            self.handle_events()
            self.update_robot_position()
            self.drop_stuff()
            self.print_screen()
            self.clock.tick(60)

if __name__ == "__main__":
    game = LoveAndMonsters()
