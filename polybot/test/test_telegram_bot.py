import unittest
from unittest.mock import patch, Mock, mock_open, MagicMock
from polybot.bot import ImageProcessingBot
import os

img_path = 'polybot/test/beatles.jpeg' if '/polybot/test' not in os.getcwd() else 'beatles.jpeg'

mock_msg = {
    'message_id': 349,
    'from': {
        'id': 5957525411,
        'is_bot': True,
        'first_name': 'MockDevOpsBot',
        'username': 'MockDevOpsBot'
    },
    'chat': {
        'id': 1243002838,
        'first_name': 'John',
        'last_name': 'Doe',
        'type': 'private'
    },
    'date': 1690105468,
    'photo': [
        {
            'file_id': 'AgACAgQAAxkDAAIBXWS89nwr4unzj72WKH0XpwLdcrzqAAIBvzEbx73gUbDHoYwLMSkCAQADAgADcwADLwQ',
            'file_unique_id': 'AQADAb8xG8e94FF4',
            'file_size': 2235,
            'width': 90,
            'height': 90
        },
        {
            'file_id': 'AgACAgQAAxkDAAIBXWS89nwr4unzj72WKH0XpwLdcrzqAAIBvzEbx73gUbDHoYwLMSkCAQADAgADbQADLwQ',
            'file_unique_id': 'AQADAb8xG8e94FFy',
            'file_size': 37720,
            'width': 320,
            'height': 320
        },
        {'file_id': 'AgACAgQAAxkDAAIBXWS89nwr4unzj72WKH0XpwLdcrzqAAIBvzEbx73gUbDHoYwLMSkCAQADAgADeAADLwQ',
         'file_unique_id': 'AQADAb8xG8e94FF9',
         'file_size': 99929,
         'width': 660,
         'height': 660
         }
    ],
    'caption': 'Rotate'
}


class TestBot(unittest.TestCase):

    @patch('telebot.TeleBot')
    def setUp(self, mock_telebot):
        bot = ImageProcessingBot(token='bot_token', bot_app_url='webhook_url')
        bot.telegram_bot_client = mock_telebot.return_value

        mock_file = Mock()
        mock_file.file_path = 'photos/beatles.jpeg'
        bot.telegram_bot_client.get_file.return_value = mock_file

        with open(img_path, 'rb') as f:
            bot.telegram_bot_client.download_file.return_value = f.read()

        self.bot = bot

    def test_contour(self):
        @patch('polybot.bot.TeleBot')
        def test_handle_message_no_text_or_caption(self, MockBot):
            mock_msg = {
                'message_id': 350,
                'chat': {'id': 1243002839, 'type': 'private'}
            }

            bot_instance = MockBot.return_value

            try:
                self.bot.handle_message(mock_msg)
            except KeyError as err:
                self.fail(f"Unexpected KeyError: {err}")

            mock_method.assert_called_once()
            self.bot.telegram_bot_client.send_photo.assert_called_once()

    @patch('builtins.open', new_callable=mock_open)
    def handle_message(self, msg):
        """Handle incoming messages."""
        try:
            chat_id = msg['chat']['id']

            # Check if message contains an image
            if 'photo' in msg:
                # Handle image message
                photo = msg['photo'][-1]  # Get the highest resolution photo
                file_id = photo['file_id']
                # Process the image...

            # Check if message contains text
            elif 'text' in msg:
                # Handle text message
                self.send_text(chat_id, f'Your original message: {msg["text"]}')

            else:
                self.send_text(chat_id, 'Please send an image or text message.')

        except Exception as e:
            # Log the error and send error message to user
            print(f"Error handling message: {str(e)}")
            if 'chat' in msg:
                self.send_text(msg['chat']['id'], f'Error processing message: {str(e)}')

