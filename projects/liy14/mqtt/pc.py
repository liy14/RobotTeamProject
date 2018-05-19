import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=50)
    main_frame.grid()

    name_lable = ttk.Label(main_frame, text='Name')
    name_lable.grid(row=1, column=0)
    name_entry = ttk.Entry(main_frame, width=8)
    name_entry.grid(row=2, column=0)

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=1, column=1)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=2, column=1)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=1, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=2, column=2)

    frequency_lable = ttk.Label(main_frame, text='Frequency')
    frequency_lable.grid(row=1, column=3)
    frequency_entry = ttk.Entry(main_frame, width=8)
    frequency_entry.grid(row=2, column=3)

    add_message_lable = ttk.Label(main_frame, text='Additional Message')
    add_message_lable.grid(row=1, column=4)
    add_message_entry = ttk.Entry(main_frame, width=30)
    add_message_entry.grid(row=2, column=4)

    alarm_button = ttk.Button(main_frame, text="Alarm")
    alarm_button.grid(row=0, column=0)
    alarm_button['command'] = lambda: wake_up(mqtt_client, name_entry, left_speed_entry, right_speed_entry,frequency_entry, add_message_entry)
    root.bind('<Return>', lambda event: wake_up(mqtt_client, name_entry,left_speed_entry, right_speed_entry, frequency_entry, add_message_entry))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=5, column=0)
    stop_button['command'] = lambda: stop(mqtt_client)
    root.bind('<space>', lambda event: stop(mqtt_client))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=5, column=1)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


# ----------------------------------------------------------------------
# Tkinter callbacks
# ----------------------------------------------------------------------
# Done: 4. Implement the functions for the drive button callbacks.
def wake_up(mqtt_client, name_entry, left_speed_entry, right_speed_entry, frequency_entry, add_message_entry):
    print('Wake up!')
    mqtt_client.send_message('wake',[str(name_entry.get()), int(left_speed_entry.get()),int(right_speed_entry.get()), int(frequency_entry.get()), str(add_message_entry.get())])


def stop(mqtt_client):
    print('stop')
    mqtt_client.send_message('stop')


# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
