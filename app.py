from flask import Flask, render_template, request, redirect, url_for
import pywhatkit
import pyautogui
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    if request.method == 'POST':
        phone_number = request.form['phone']
        
        # Ensure the phone number starts with '+'
        if not phone_number.startswith('+'):
            phone_number = '+91' + phone_number  # Default to +91 (India)

        message = request.form['message']
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])

        try:
            # Send the WhatsApp message using pywhatkit
            pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

            # Wait a few seconds to ensure the message is written in the textbox
            time.sleep(15)  # Adjust this time if needed
            
            # Simulate pressing the "Enter" key to send the message
            pyautogui.press("enter")
        except Exception as e:
            print(f"Error: {e}")
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)