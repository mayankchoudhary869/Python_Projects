import datetime
import time
from playsound import playsound  # Install with: pip install playsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up! It's time!")
            playsound("alarm.mp3")  # Make sure you have a valid 'alarm.mp3' file in the same directory
            break
        time.sleep(1)

def main():
    print("=== Simple Alarm Clock ===")
    alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")

    try:
        # Validate format
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please enter in HH:MM:SS format.")

if __name__ == "__main__":
    main()
