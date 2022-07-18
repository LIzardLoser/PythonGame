import time

from ursina import *

option = int(input('Choose A Level: '))



lvlonewin = Entity(model='quad', scale=(.3, .3), color=color.orange, collider='box', position=(-3, 2.75))


def windowYes():
    wn = window

    wn.title = 'gam'
    wn.borderless = False
    wn.fps_counter.enabled = False
    wn.color = color.black
    # wn.fullscreen = True


app = Ursina()


def levels(lvl):
    match lvl:
        case 1:
            e1 = Entity(model='quad', scale=(5, .5), position=(-1, 1), collider='box')
            e2 = Entity(model='quad', scale=(7, .5), position=(0, -1), collider='box')
            e3 = Entity(model='quad', scale=(.5, 5), position=(3.5, 1.25), collider='box')
            e4 = Entity(model='quad', scale=(.5, 2), position=(-3.25, 0), collider='box')
            e5 = Entity(model='quad', scale=(.5, 1.5), position=(1.25, 1.5), collider='box')
            e6 = Entity(model='quad', scale=(5, .5), position=(-1.5, 2), collider='box')
            e7 = Entity(model='quad', scale=(7.5, .5), position=(-.25, 3.5), collider='box')
            e8 = Entity(model='quad', scale=(.5, 2), position=(-3.75, 2.75), collider='box')
        case 2:
            e1 = Entity(model='quad', scale=(.5, 1), position=(1, 1), collider='box')


class Player(Entity):
    def __init__(self):
        super().__init__(
            model='quad',
            scale=(.5, .5),
            color=color.gold,
            collisions=True,
            collider='box'
        )

    def update(self):
        uprc = boxcast(origin=self.world_position, distance=.25, direction=self.up, ignore=(self,), thickness=(1, 3))
        leftrc = boxcast(origin=self.world_position, distance=.25, direction=self.left, ignore=(self,),
                         thickness=(1, 3))
        downrc = boxcast(origin=self.world_position, distance=.25, direction=self.down, ignore=(self,),
                         thickness=(1, 3))
        rightrc = boxcast(origin=self.world_position, distance=.25, direction=self.right, ignore=(self,),
                          thickness=(1, 3))

        if held_keys['w'] and not uprc.hit:
            self.y += 1.5 * time.dt
            camera.y += 1.5 * time.dt
        if held_keys['a'] and not leftrc.hit:
            self.x -= 1.5 * time.dt
            camera.x -= 1.5 * time.dt
        if held_keys['s'] and not downrc.hit:
            self.y -= 1.5 * time.dt
            camera.y -= 1.5 * time.dt
        if held_keys['d'] and not rightrc.hit:
            self.x += 1.5 * time.dt
            camera.x += 1.5 * time.dt

        if self.intersects(lvlonewin):
            Text(text="YOU WIN")


levels(option)

cube = Player()

windowYes()

app.run()
