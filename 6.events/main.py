import arcade
import random
from app_objects import Polygon2D

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Matrices de transformacion"


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.objects = []
    
    '''
    x:int,
    y:int,
    button:int,
    modifiers:int
    '''
    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.objects.append(Polygon2D(
                vertices=[
                    (x, y),
                    (100 + x, y),
                    (50 + x, 100 + y)
                ],
                color=get_random_color(),
                rot_speed=random.uniform(-2.5, 2.5)
            ))

    '''
    symbol:int
    modifiers:int
    '''
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            for obj in self.objects:
                obj.scale(1.1, 1.1)
        if symbol == arcade.key.DOWN:
            for obj in self.objects:
                obj.scale(0.9, 0.9)

    def on_update(self, delta_time: float):
        for obj in self.objects:
            obj.rotate(obj.rot_speed * delta_time)
        
    def on_draw(self):
        arcade.start_render()
        for obj in self.objects:
            obj.draw()
    
    
if __name__ == "__main__":
    app = App()
    arcade.run()
