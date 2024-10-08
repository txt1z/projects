from win10toast_click import ToastNotifier  # Install with: pip install win10toast_click
import schedule
import time

# Create an instance of ToastNotifier
notifier = ToastNotifier()

def show_notification(message, schedule_next=False):
    # Function to show the notification
    def on_ok():
        print("You clicked OK. Next reminder will follow the original schedule.")

    def on_remind():
        print("You clicked Remind Again. Reminder will pop up in 2 minutes.")
        time.sleep(120)  # 2 minutes delay
        show_notification(message)

    # Show notification with two options
    notifier.show_toast(
        "Medication Reminder",
        message,
        duration=10,
        threaded=True,
        icon_path=None,  # Add an icon path here if needed
        callback_on_click=on_ok
    )
    # Optionally schedule next reminder
    if schedule_next:
        schedule_next_reminder(message)

def schedule_next_reminder(message):
    show_notification(message, schedule_next=False)

# Schedule notifications for eyedrop and pills at specific times
def schedule_reminders():
    schedule.every().day.at("10:00").do(show_notification, "Time to take your eyedrop!")
    schedule.every().day.at("14:00").do(show_notification, "Time to take your pills after lunch!")
    schedule.every().day.at("21:00").do(show_notification, "Time to take your pills after dinner!")

# Main loop to run the scheduled tasks
if __name__ == "__main__":
    schedule_reminders()
    while True:
        schedule.run_pending()
        time.sleep(1)
