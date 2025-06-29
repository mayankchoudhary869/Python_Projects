import time
import datetime
import platform

try:
    from plyer import notification  # Optional popup (install with pip)
    HAS_NOTIFICATION = True
except ImportError:
    HAS_NOTIFICATION = False

def reminder(reminder_time, message):
    print(f"⏰ Reminder set for {reminder_time} — Message: '{message}'")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == reminder_time:
            print(f"\n🔔 Reminder: {message}")
            if HAS_NOTIFICATION:
                notification.notify(
                    title="🔔 Reminder",
                    message=message,
                    timeout=10
                )
            break
        time.sleep(30)  # Check every 30 seconds

def main():
    print("=== Simple Reminder App ===")
    reminder_time = input("Enter reminder time (HH:MM, 24-hour): ")
    message = input("Enter your reminder message: ")

    try:
        datetime.datetime.strptime(reminder_time, "%H:%M")
        reminder(reminder_time, message)
    except ValueError:
        print("❌ Invalid time format. Please use HH:MM (24-hour).")

if __name__ == "__main__":
    main()
