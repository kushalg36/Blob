import random

class Blob:
    def __init__(self,color,x_bound,y_bound):  
        self.x_bound=x_bound
        self.y_bound=y_bound
        self.x=random.randrange(0,x_bound)
        self.y=random.randrange(0,y_bound)
        self.size=random.randrange(4,8)
        self.color=color

    def move(self):
        self.move_x=random.randrange(-5,5)
        self.move_y=random.randrange(-5,5)
        self.x += self.move_x
        self.y +=self.move_y

        if self.x < 0:
            self.x=0
        elif self.x > self.x_bound:
            self.x=self.x_bound
        
        if self.y < 0:
            self.y=0
        elif self.y > self.y_bound:
            self.y = self.y_bound
