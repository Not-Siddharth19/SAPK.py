import os
import time

# Set the APK file path
apk_file_path = 'C:\\Users\\notsi\PycharmProjects\SAPK.py\SAPK PY'

# Function to check if the Android device is connected
def is_device_connected():
    return os.system('adb devices') == 0

# Function to install the APK
def install_apk():
    os.system(f'adb install -r "{apk_file_path}"')

# Main function
def main():
    while True:
        if is_device_connected():
            print("Device connected. Installing APK...")
            install_apk()
            print("APK installed successfully!")
            break
        else:
            print("Waiting for device to connect...")
            time.sleep(2)

if __name__ == '__main__':
    main()