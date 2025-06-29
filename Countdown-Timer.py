import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Time left: {timer_display}", end="")
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Time's up!")

def main():
    print("=== Countdown Timer ===")
    try:
        total_seconds = int(input("Enter time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()