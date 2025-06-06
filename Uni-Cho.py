import sys
from pyautogui import press
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout,
    QPushButton, QTimeEdit, QDesktopWidget
)
from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtGui import QFont
from PyQt5.Qt import QDesktopServices, QUrl


class CustomButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFont(QFont('Arial Rounded MT Bold', 12, QFont.Bold))
        self.setStyleSheet("""
            QPushButton {
                background-color: #404040;
                color: #1c1f23;
                border-radius: 10px;
                padding: 10px;
                margin: 10px;
                border: 2px solid #404040;
            }
            QPushButton:hover {
                color: #4CC9F0;
            }
        """)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.running = False
        self.auto_mode = False
        self.initUI()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.run_operations)

        self.check_timer = QTimer(self)
        self.check_timer.timeout.connect(self.check_time)
        self.check_timer.start(60000)

        self.open_link()

    def initUI(self):
        self.setWindowTitle('Uni-Cho')
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #1c1f23;")

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        layout = QVBoxLayout(self)

        label = QLabel("Press 'Start' to begin, 'Stop' to end.", self)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont('Courier', 10))
        label.setStyleSheet("color: #4CC9F0; margin-bottom: 10px;")
        layout.addWidget(label)

        self.status_label = QLabel("Status: Stopped", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont('Arial Rounded MT Bold', 12))
        self.status_label.setStyleSheet("color: #4CC9F0; margin-bottom: 10px;")
        layout.addWidget(self.status_label)

        time_layout = QHBoxLayout()
        time_layout.addWidget(QLabel("Start Time:", self))
        self.start_time_edit = QTimeEdit(self)
        self.start_time_edit.setDisplayFormat("HH:mm")
        self.start_time_edit.setTime(QTime.currentTime())
        time_layout.addWidget(self.start_time_edit)

        time_layout.addWidget(QLabel("End Time:", self))
        self.end_time_edit = QTimeEdit(self)
        self.end_time_edit.setDisplayFormat("HH:mm")
        self.end_time_edit.setTime(QTime.currentTime().addSecs(3600))
        time_layout.addWidget(self.end_time_edit)

        layout.addLayout(time_layout)

        self.auto_button = CustomButton('Enable Scheduled Mode', self)
        self.auto_button.setCheckable(True)
        self.auto_button.clicked.connect(self.toggle_auto_mode)
        layout.addWidget(self.auto_button)

        button_layout = QHBoxLayout()

        self.start_button = CustomButton('Start', self)
        self.start_button.clicked.connect(self.toggle_operations)
        button_layout.addWidget(self.start_button)

        open_link_button = CustomButton('Open Link', self)
        open_link_button.clicked.connect(self.open_link)
        button_layout.addWidget(open_link_button)

        exit_button = CustomButton('Exit', self)
        exit_button.clicked.connect(self.close)
        button_layout.addWidget(exit_button)

        layout.addLayout(button_layout)

    def toggle_auto_mode(self):
        self.auto_mode = self.auto_button.isChecked()
        if self.auto_mode:
            self.auto_button.setText('Disable Scheduled Mode')
            self.status_label.setText("Status: Scheduled Mode Enabled")
            self.toggle_operations(stop=True)
        else:
            self.auto_button.setText('Enable Scheduled Mode')
            self.status_label.setText("Status: Scheduled Mode Disabled")
            self.toggle_operations(stop=True)

    def toggle_operations(self, stop=False):
        if stop:
            self.running = False
            self.start_button.setText('Start')
            self.status_label.setText("Status: Stopped")
            self.timer.stop()
            return

        self.running = not self.running
        self.start_button.setText('Stop' if self.running else 'Start')
        self.status_label.setText("Status: Running" if self.running else "Status: Stopped")
        if self.running:
            self.timer.start(10000)
        else:
            self.timer.stop()

    def check_time(self):
        if not self.auto_mode:
            return

        now = QTime.currentTime()
        start = self.start_time_edit.time()
        end = self.end_time_edit.time()

        if start <= end:
            in_range = start <= now < end
        else:
            in_range = now >= start or now < end

        if in_range:
            if not self.running:
                self.toggle_operations()
        else:
            if self.running:
                self.toggle_operations()

    def run_operations(self):
        if self.running:
            for key in ('f5', 'enter'):
                press(key)

    def open_link(self):
        url = 'https://stdn.iau.ir/Student/captchaProcess'
        QDesktopServices.openUrl(QUrl(url))
        self.status_label.setText("Status: Link Opened")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
