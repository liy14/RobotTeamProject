import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3
import time


class MyDelegate(object):
    def __init__(self):
        self.running = True

    def go_forward_left(self, speed):
        left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        assert left_motor.connected
        left_motor.run_forever(speed_sp=speed)

    def go_forward_right(self, speed):
        right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert right_motor.connected
        right_motor.run_forever(speed_sp=speed)

    def loop_forever(self):
        while self.running:
            time.sleep(0.1)

    def shutdown(self):
        self.running = False


def main():
    ev3.Sound.speak("Let's go").wait()
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    # mqtt_client.connect_to_pc("35.194.247.175")  # Off campus IP address of a GCP broker
    robot.loop_forever()

main()


