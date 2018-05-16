"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time


class Snatch3r(object):
    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

        assert self.left_motor.connected
        assert self.right_motor.connected

        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        assert self.arm_motor.connected

        self.running = True

        self.color_sensor = ev3.ColorSensor()
        assert self.color_sensor.connected

    def forward_inches(self, inches, speed=100,stop_action='brake'):
        k = 4.5
        degrees_for_motor=k+ inches/speed
        self.left_motor.run_to_rel_pos(speed_sp=speed,postion_sp=degrees_for_motor,stop_action=stop_action)
        self.right_motor.run_to_rel_pos(speed_sp=speed, postion_sp=degrees_for_motor, stop_action=stop_action)
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def forward(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def backward_inches(self, inches, speed=100,stop_action='brake'):
        k = 4.5
        degrees_for_motor = k + inches/speed
        self.left_motor.run_to_rel_pos(speed_sp=speed,postion_sp=-degrees_for_motor,stop_action=stop_action)
        self.right_motor.run_to_rel_pos(speed_sp=speed, postion_sp=-degrees_for_motor, stop_action=stop_action)
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def back(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=-left_speed)
        self.right_motor.run_forever(speed_sp=-right_speed)

    def loop_forever(self):
        while True:
            if self.running is False:
                 time.sleep(0.1)

    def right(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=20)

    def left(self, right_speed, left_speed):
        self.right_motor.run_forever(speed_sp=right_speed)
        self.left_motor.run_forever(speed_sp=20)

    def arm_up(self):
        self.arm_motor.run_forever(speed_sp=400)
        touch_sensor = ev3.TouchSensor
        while True:
            if touch_sensor.is_pressed:
                break

    def arm_down(self):
        self.arm_motor.run_to_abs_pos(speed_sp=-400, position_sp=14.2)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        self.arm_motor.stop()

    def shutdown(self):
        ev3.Sound.speak('Goodbye').wait()
        self.running = False
    
    # TODO: Implement the Snatch3r class as needed when working the sandox exercises
    # (and delete these comments)


