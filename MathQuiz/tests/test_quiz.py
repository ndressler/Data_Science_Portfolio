import unittest
from unittest.mock import patch
from scripts.quiz import Quiz, Math

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.quiz = Quiz()

    def test_calculate_percentage(self):
        result = self.quiz.calculate_percentage(5, 10)
        self.assertEqual(result, 50.0)

class TestMath(unittest.TestCase):
    def setUp(self):
        self.math = Math()

    @patch('random.randint')
    @patch('random.choice')
    def test_generate_question(self, mock_choice, mock_randint):
        mock_randint.return_value = 1
        mock_choice.return_value = '+'
        question, answer = self.math.generate_question()
        self.assertEqual(question, "1 + 1 + 1")
        self.assertEqual(answer, 3.0)

if __name__ == '__main__':
    unittest.main()
