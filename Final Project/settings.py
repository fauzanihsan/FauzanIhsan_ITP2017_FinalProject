class Settings():
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 600

        #level settings
        self.level = 1

        #player settings
        self.player_speed_factor = 7
        self.ship_limit = 0

        #enemy settings
        self.enemy_speed_factor = 7

        #bullet settings
        self.bullet_width = 16
        self.bullet_height = 3
        self.bullet_color = 255,0,0
        self.bullets_allowed = 20
        self.bullet_speed_factor = 3

        #scoring
        self.enemy_points = 50

    #function to level up each time player gain +500 score
    def levelup(self, score):
        if score > 500:
            self.level = 2
        if score > 1000:
            self.level = 3
        if score > 1500:
            self.level = 4
        if score >2000:
            self.level = 5

