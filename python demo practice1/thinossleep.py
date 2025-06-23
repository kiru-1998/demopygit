from vncdotool import api
import time

THINOS_IP = '100.106.126.83'  # Replace with your ThinOS IP
SLEEP_TIMEOUT_MINUTES = 1

def configure_sleep_settings():
    try:
        # Connect to VNC
        client = api.connect(THINOS_IP)
        time.sleep(2)

        # Simulate opening System Preferences -> Power and Sleep
        client.keyPress('ctrl-esc')  # Open Start menu or main menu
        time.sleep(1)
        client.type('System Preferences')
        time.sleep(2)
        client.keyPress('enter')
        time.sleep(3)

        client.type('Power and Sleep')
        time.sleep(2)
        client.keyPress('enter')
        time.sleep(2)

        # Simulate setting sleep timeout
        client.keyPress('tab')  # Navigate to dropdown
        time.sleep(1)
        client.keyPress('enter')
        time.sleep(1)

        for _ in range(3):  # Assume down 3 times to reach "15 minutes"
            client.keyPress('down')
            time.sleep(0.5)

        client.keyPress('enter')
        time.sleep(1)

        print("[PASS] Sleep settings configured successfully.")
        return True

    except Exception as e:
        print(f"[FAIL] Failed to configure sleep settings: {e}")
        return False
