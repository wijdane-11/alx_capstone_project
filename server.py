from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json

    # Server-side validation
    if not data.get('name') or not data.get('email') or not data.get('message'):
        return jsonify({"error": "Please fill in all fields."}), 400
    if not "@" in data.get('email'):
        return jsonify({"error": "Invalid email address."}), 400

    # Send email notification
    try:
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        sender_email = 'your_email@example.com'
        receiver_email = 'your_email@example.com'
        password = 'your_email_password'
        
        message = f"Subject: New Contact Form Submission\n\nName: {data['name']}\nEmail: {data['email']}\nMessage: {data['message']}"
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

        return jsonify({"message": "Message sent successfully."}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send message: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
