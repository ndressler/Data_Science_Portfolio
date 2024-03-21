import unittest
from unittest.mock import patch, MagicMock
from main import main

class TestMain(unittest.TestCase):
    @patch('main.Math')
    def test_main(self, MockMath):
        # Arrange
        mock_math = MockMath.return_value
        mock_math.get_user_info.return_value = 'mock_user'
        mock_math.start_quiz.return_value = None

        # Act
        main()

        # Assert
        MockMath.assert_called_once()
        mock_math.get_user_info.assert_called_once()
        mock_math.start_quiz.assert_called_once_with('mock_user')

if __name__ == '__main__':
    unittest.main()
