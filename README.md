Here is a `README.md` you can use for your GitHub repository:

---

# 🛡️ ByDeF - Undetectable PE Generator (Defender / AV Bypass)

> **Author:** [@40sp3l](https://github.com/40sp3l)
> **Purpose:** Quickly generate a Python payload, obfuscate it, and compile it to a fully undetectable Windows PE (.exe) file, even with **Windows Defender enabled**.

---

## 📦 Features

* Simple and elegant GUI using PyQt5
* Replace `LHOST` and `LPORT` dynamically in your payload
* Automatically open a browser to obfuscate your payload
* Copy obfuscated code back and compile it to an executable
* Built-in Netcat listener setup
* Works with **Windows Defender ON**

---

## ⚙️ Requirements

Make sure the following are installed on your system:

* Python 3.x
* `pyinstaller`
  Install it via pip:

  ```bash
  pip install pyinstaller
  ```
* `PyQt5`
  Install it via pip:

  ```bash
  pip install pyqt5
  ```
* `nc.exe` (Netcat for Windows) – Place it in the same folder as this tool.
* A file named `payload.txt` should be in the same directory, containing the original payload with the following placeholders:

  ```
  LHOST=127.0.0.1
  LPORT=4444
  ```

---

## 🚀 How to Use

### 1. Launch the Tool

```bash
python bydef_gui.py
```

### 2. Set LHOST and LPORT

* Enter your **IP address** and **Port** in the corresponding fields.
* Click the `⚙️ Replace Values` button to update the values inside `payload.txt`.

### 3. Obfuscate the Payload

* Click `🕶️ Obfuscate Code`. This does:

  * Copies the payload content to clipboard
  * Opens [https://freecodingtools.org/tools/obfuscator/python](https://freecodingtools.org/tools/obfuscator/python)

> **Instructions for obfuscation:**

* Delete the default content:

  ```python
  # Online Python Compiler
  print("Hello, World!")
  ```
* Press `CTRL+V` to paste your payload.
* Click the **Play Triangle** button to obfuscate.
* Click on **Copy Output** on the right side.

### 4. Save the Obfuscated Payload

* Return to **ByDeF GUI**.
* Click `💾 Write to File` to save the clipboard content to a file called `comp.py`.

### 5. Compile the Payload

* Enter a name for your payload in the **Payload Name** field (e.g., `payload_stealth`)
* Click `🧪 Compile`. It will:

  * Use `pyinstaller` to generate a `.exe` file
  * Move the `.exe` to your current directory
  * Clean up all build folders

### 6. Start Netcat Listener

* Click `🔊 Start NC Listener`
* A terminal will open with Netcat listening on your defined port

### 7. Execute the Payload

* Run the compiled `.exe` file on the victim machine.
* A reverse shell will open in your terminal.

> ✅ Ensure **Windows Defender** is ON to test the undetectable behavior.

---

## 🧠 Notes

* You **must** replace `LHOST` and `LPORT` **before** obfuscating.
* Do **not** edit the `payload.txt` file manually; use the GUI instead.
* The generated executable will appear as `{payload_name}.exe` in the main folder.

---

## ❗ Disclaimer

> This tool is intended **for educational and ethical testing purposes only**.
> The author is **not responsible** for any misuse or illegal activities performed with this tool.

---

