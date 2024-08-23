
### Actualización de las Pruebas

Para las pruebas unitarias, asegúrate de incluir tests que verifiquen tanto la funcionalidad de envío de correos electrónicos como la interacción con la API REST. Aquí un ejemplo de cómo podrías estructurar una prueba para el envío de correos:

```python
# tests/test_app.py
import unittest
from app import create_app
from flask_mail import Mail

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        """Setup the Flask app for testing."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['MAIL_SUPPRESS_SEND'] = True  # Suprime el envío de correos reales durante las pruebas

    def test_send_email(self):
        """Test sending email through the task."""
        with self.app.app_context():
            mail = Mail(self.app)
            with mail.record_messages() as outbox:
                response = self.client.post('/send_email', json={'recipient': 'test@example.com', 'subject': 'Test', 'message': 'This is a test.'})
                self.assertEqual(response.status_code, 202)
                self.assertEqual(len(outbox), 1)
                self.assertEqual(outbox[0].subject, 'Test')

if __name__ == '__main__':
    unittest.main()
