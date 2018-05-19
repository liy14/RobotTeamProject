import tkinter
from tkinter import ttk
import ev3dev.ev3 as ev3

import mqtt_remote_method_calls as com

def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    color_label = ttk.Label(main_frame, text='Color')
    color_label.grid(row = 5, column=0)
    color_entry = ttk.Entry(main_frame, width=8)
    color_entry.grid(row=6, column=0)

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: stop(mqtt_client)
    root.bind('<space>', lambda event: stop(mqtt_client))

    go_button = ttk.Button(main_frame, text="Go")
    go_button.grid(row=3, column=2)
    go_button['command'] = lambda: go(mqtt_client,color_entry)
    root.bind('<Up>', lambda event: go(mqtt_client, color_entry))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=1)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=3, column=0)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    reset_button = ttk.Button(main_frame, text='Reset')
    reset_button.grid(row=4, column=2)
    reset_button['command'] = lambda : go_down(mqtt_client)





    root.mainloop()


def forward(mqtt_client, left_speed_entry, right_speed_entry):
    print('forward')
    mqtt_client.send_message('forward',[int(left_speed_entry.get()),int(right_speed_entry.get())])

def left(mqtt_client, left_speed_entry, right_speed_entry):
    print('left')
    mqtt_client.send_message('left', [int(left_speed_entry.get()), int(right_speed_entry.get())])

def right(mqtt_client, left_speed_entry, right_speed_entry):
    print('right')
    mqtt_client.send_message('right',[int(left_speed_entry.get()),int(right_speed_entry.get())])

def stop(mqtt_client):
    print('stop')
    mqtt_client.send_message('stop')

def back(mqtt_client, left_speed_entry, right_speed_entry):
    print('back')
    mqtt_client.send_message('back',[int(left_speed_entry.get()),int(right_speed_entry.get())])

def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")

def drive_color(mqtt_client, color_entry):
    print("drive to")
    mqtt_client.send_message("drive_to_color",[int(color_entry.get())])

def go(mqtt_client, color_entry):
    print("Go!")
    print(int(color_entry.get()))
    print(type(int(color_entry.get())))
    mqtt_client.send_message('stop_by', [int(color_entry.get())])



def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()

def go_down(mqtt_client):
    print('go down')
    mqtt_client.send_message('arm_down')







main()