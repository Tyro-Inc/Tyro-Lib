import pyglet

class App:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.window = pyglet.window.Window(width=self.width, height=self.height, caption=self.name)
        self.window.background_color = (0, 0, 0, 255)
        self.objects = []
        self.images = []
    
    def run(self):
        pyglet.app.run()
    
    def draw(self):
        @self.window.event
        def on_draw():
            self.window.clear()
            for obj in self.objects:
                obj.draw()
    
    def label(self, text, x, y, color=(255, 255, 255, 255), font_size=12, ):
        label = pyglet.text.Label(text, x=x, y=y, color=color, font_size=font_size)
        self.window.dispatch_event('on_draw')
        self.objects.append(label)
        return label
    
    def square(self, x, y, width, height, color=(255, 255, 255)):
        square = pyglet.shapes.Rectangle(x=x, y=y, width=width, height=height, color=color)
        self.window.dispatch_event('on_draw')
        self.objects.append(square)
        return square
    
    def ellipse(self, x, y, width, height, color=(255, 255, 255)):
        ellipse = pyglet.shapes.Ellipse(x=x, y=y, a=width, b=height, color=color)
        self.window.dispatch_event('on_draw')
        self.objects.append(ellipse)
        return ellipse

