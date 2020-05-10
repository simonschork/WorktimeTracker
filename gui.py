import tracker
import datetime
from tkinter import Tk, Button, Label


# Initialize global variables
safe_starttime = tracker.current()
safe_pausetime = tracker.current()
safe_workduration = tracker.current()
safe_pauseduration = tracker.current()


# Start button function
def start():
    # Set variable to time when button pressed for calculating duration
    global safe_starttime
    safe_starttime = tracker.current()
    # Set empty label value to starttime
    worktime_start_value.config(text=tracker.formatTime(safe_starttime))


def pause():
    # Set variable to time when button pressed for calculating duration
    global safe_pausetime
    safe_pausetime = tracker.current()
    # Set empty label value to pausetime
    pause_start_value.config(text=tracker.formatTime(safe_pausetime))


def resume():
    # Get global variable for calculation
    global safe_pausetime
    # Set variable to time when button pressed for calculating duration
    safe_resumetime = tracker.current()
    # Calculating time delta
    safe_pauseduration = safe_resumetime - safe_pausetime
    # Set empty label value to resumetime
    pause_stop_value.config(text=tracker.formatTime(safe_resumetime))
    # Set empty label value to pauseduration
    pause_duration_value.config(
        text=tracker.strfdelta(safe_pauseduration, "%H:%M:%S"))


def stop():
    # Get global variable for calculation
    global safe_starttime
    # Set variable to time when button pressed for calculating duration
    safe_stoptime = tracker.current()
    # Calculating time delta
    safe_workduration = safe_stoptime - safe_starttime
    # Set empty label value to stoptime
    worktime_stop_value.config(text=tracker.formatTime(safe_stoptime))
    # Set empty label value to workduration
    worktime_duration_value.config(
        text=tracker.strfdelta(safe_workduration, "%H:%M:%S")
    )


if __name__ == "__main__":
    # Create window
    app = Tk()

    # Format window
    app.title("Track your worktime")

    # Start button
    start_button = Button(app, text="Start", command=start, height=2, width=10)
    start_button.grid(row=0, column=0)

    # Pause button
    pause_button = Button(app, text="Pause", command=pause, height=2, width=10)
    pause_button.grid(row=0, column=1)

    # Resume button
    resume_button = Button(
        app, text="Resume", command=resume, height=2, width=10)
    resume_button.grid(row=0, column=2)

    # Stop button
    stop_button = Button(app, text="Stop", command=stop, height=2, width=10)
    stop_button.grid(row=0, column=3)

    # Row labels
    worktime_label = Label(app, text="Worktime:")
    worktime_label.grid(row=2, column=0)
    pause_label = Label(app, text="Pause:")
    pause_label.grid(row=3, column=0)

    # Start column
    start_label = Label(app, text="Start")
    start_label.grid(row=1, column=1)
    worktime_start_value = Label(app, text="")
    worktime_start_value.grid(row=2, column=1)
    pause_start_value = Label(app, text="")
    pause_start_value.grid(row=3, column=1)

    # Stop column
    stop_label = Label(app, text="Stop")
    stop_label.grid(row=1, column=2)
    worktime_stop_value = Label(app, text="")
    worktime_stop_value.grid(row=2, column=2)
    pause_stop_value = Label(app, text="")
    pause_stop_value.grid(row=3, column=2)

    # Duration column
    duration_label = Label(app, text="Duration")
    duration_label.grid(row=1, column=3)
    worktime_duration_value = Label(app, text="")
    worktime_duration_value.grid(row=2, column=3)
    pause_duration_value = Label(app, text="")
    pause_duration_value.grid(row=3, column=3)

    # Start app
    app.mainloop()
