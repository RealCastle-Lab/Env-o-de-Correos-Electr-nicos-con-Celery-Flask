from flask import render_template, request, jsonify
from flask_mail import Message

def init_routes(app, mail, celery):

    @app.route('/send_email', methods=['POST'])
    def send_email():
        email_data = request.get_json()
        send_async_email.delay(email_data['recipient'], email_data['subject'], email_data['message'])
        return jsonify({"message": "Email sending initiated"}), 202

    @celery.task
    def send_async_email(recipient, subject, message):
        msg = Message(subject,
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[recipient])
        msg.body = message
        with app.app_context():
            mail.send(msg)
