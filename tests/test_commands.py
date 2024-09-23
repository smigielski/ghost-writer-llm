import unittest
import sys
sys.path.insert(0, './src')
from markdown_processor import MarkdownProcessor
import utils.unifieddiff as udiff
import logging

class MockEngine:
    def __init__(self):
        self.current_model = None
        self.current_system = None
        self.model_stack = []
        self.system_stack = []
        
    def model(self, model):
        self.model_stack.append(self.current_model)
        self.current_model = model
        return ""

    def close_model(self):
        self.current_model=self.model_stack.pop()
        return ""

    def system(self, system):
        self.system_stack.append(self.current_system)
        self.current_system = system
        return ""
    
    def close_system(self):
        self.current_system = self.system_stack.pop()
        return ""

    def chat(self, text):
        return "This is test string.\n"
    
    def close_chat(self):
        return "<!-- ERROR: Closing chat that is not opened properly"


class TestCommands(unittest.TestCase):
    """Test cases for markdown processor"""

    def setUp(self) -> None:
        logger = logging.getLogger()
        logger.level = logging.DEBUG

    def test_model(self):
        """Verify that model is set correctly."""
        text = """<!-- #model llama3.1 -->"""
        engine = MockEngine()
        processor = MarkdownProcessor(engine)
        processor.process(text)
        self.assertEqual(engine.current_model, "llama3.1")

    def test_pop_model(self):
        """Verify that model is popped correctly and comands can be multiline"""
        text = """<!-- #model llama3.1 --><!-- #model llama3.2 -->"""
        engine = MockEngine()
        processor = MarkdownProcessor(engine)
        processor.process(text)
        self.assertEqual(engine.current_model,"llama3.2")
        text = """<!-- 
        /model 
        -->     """
        processor.process(text)
        self.assertEqual(engine.current_model, "llama3.1")
        text = """<!-- /model -->"""
        processor.process(text)
        self.assertEqual(engine.current_model,None)


        
if __name__ == "__main__":
    unittest.main()
