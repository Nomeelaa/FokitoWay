"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class WalkState for player.
"""
from gale.input_handler import InputData

import settings
#from src.states.player_states.BaseEntityState import BaseEntityState
from src.states.entities.player_states.BaseEntityState import BaseEntityState


class WalkState(BaseEntityState):
    def enter(self, direction: str) -> None:
        self.entity.init_direction = direction
        
        print("direction: ", self.entity.actual_direction)

        if direction in("left", "right"):
            self.entity.vx = settings.PLAYER_SPEED
            self.entity.change_animation("walk_horizontal")
        if direction == "up":
            self.entity.vy = -settings.PLAYER_SPEED
            self.entity.change_animation("walk_up")
        if direction == "down":
            self.entity.vy = settings.PLAYER_SPEED
            self.entity.change_animation("walk_down")

    def update(self, dt: float) -> None:

        if self.entity.vx != 0:
            self.entity.x += self.entity.vx * dt
        if self.entity.vy != 0:
            self.entity.y += self.entity.vy * dt

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.
        if self.entity.actual_direction in ("left", "right"):
            if (self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()):
                self.entity.vx = 0

        if self.entity.actual_direction in ("up", "down"):
            if (self.entity.handle_tilemap_collision_on_top() or self.entity.handle_tilemap_collision_on_bottom()):
                self.entity.vy = 0


    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.entity.vx = -settings.PLAYER_SPEED
                self.entity.flipped = True
                self.entity.direction = "left"
            elif input_data.released and self.entity.vx <= 0:
                self.entity.change_state("idle")
        elif input_id == "move_right":
            if input_data.pressed:
                self.entity.vx = settings.PLAYER_SPEED
                self.entity.flipped = False
                self.entity.direction = "right"
            elif input_data.released and self.entity.vx >= 0:
                self.entity.change_state("idle")
        
        if input_id == "move_up":
            if input_data.pressed:
                self.entity.vy = -settings.PLAYER_SPEED
                self.entity.flipped = True
                self.entity.direction = "up"
            elif input_data.released and self.entity.vy <= 0:
                self.entity.change_state("idle")
        elif input_id == "move_down":
            if input_data.pressed:
                self.entity.vy = settings.PLAYER_SPEED
                self.entity.flipped = False
                self.entity.direction = "down"
            elif input_data.released and self.entity.vy >= 0:
                self.entity.change_state("idle")

        #if input_id == "jump" and input_data.pressed:
        #    self.entity.change_state("jump")
        
