🎓 Uni-Cho: Auto Refresh Tool for Azad University Course Registration

A Python GUI application (built with PyQt5) that automatically refreshes the course registration page of Azad University every 10 seconds by simulating F5 and Enter key presses. This tool helps students access the course selection page faster during heavy traffic times.

⚠️ **Note:** The **Scheduled Mode** feature is still under development and may not work as expected.

---

📌 Features

- Opens the Azad University registration login page directly
- Automatically presses `F5` and `Enter` every 10 seconds
- Start and Stop buttons to manually control the refresh process
- Optional **Scheduled Mode** to run automatically between specific hours (⏳ *still incomplete*)
- Simple and user-friendly PyQt5 interface

---

🚀 How to Run

	1. Make sure Python is installed on your system.
	2. Install the required dependencies:
		pip install pyqt5 pyautogui
	3.Run the script:
		python uni_cho.py
Usage Instructions:

Click "Open Link" to open the Azad University login page in your browser.

After logging in:

You can start manual refresh with the "Start" button.

Or enable Scheduled Mode and set the start/end time (still under development).

Once the course selection page is available, click "Stop" to disable automatic actions.

🗂️ File Structure

	uni_cho.py                # Main application script
	README.md                 # Project documentation
⚠️ Important Notes

This tool is designed specifically for use with Azad University's online registration system.

The Scheduled Mode feature is incomplete and might not trigger at the exact time.

Use this script responsibly. Overuse may affect your or others' access to the system.

👤 Author
	[Mahdiyar Tabatabaei](https://github.com/mahdiyar-tabatabaei)
