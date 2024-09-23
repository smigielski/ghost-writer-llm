import logging
import unittest
import sys
sys.path.insert(0, './src')

from markdown_processor import MarkdownProcessor
from ollama_engine import OllamaEngine


class TestOllamaEngine(unittest.TestCase):
    """Verify that ollama engine is working"""

    def setUp(self) -> None:
        logger = logging.getLogger()
        logger.level = logging.DEBUG

    def test_llama_model_is_present(self):
        """Verify that model is set correctly."""
        text = """<!-- #model llama3.1:latest -->
        """
        engine = OllamaEngine()
        processor = MarkdownProcessor(engine)
        patch = processor.process(text)
        self.assertEqual(patch, "")

    def test_simple_chat(self):
        """Verify that model is set correctly."""
        text = """
        <!-- #seed 123 -->
        <!-- #model llama3.1:latest -->
        <!-- #system give one sentence only -->
        <!-- #chat test -->
        """
        engine = OllamaEngine()
        processor = MarkdownProcessor(engine)
        patch = processor.process(text)
        result="""@@ -5,0 +6,2 @@
+Your test is complete.
+<!-- /chat 011d41e2 -->
"""
        self.assertEqual(patch, result)


    def test_chat_is_ignored_when_hash_matches(self):
        """Verify that messege is ignored when hash matches."""
        text = """
        <!-- #seed 123 -->
        <!-- #model llama3.1:latest -->
        <!-- #system give one sentence only -->
        <!-- #chat test -->
        This string is not changed
        <!-- /chat 011d41e2 -->
        """
        engine = OllamaEngine()
        processor = MarkdownProcessor(engine)
        patch = processor.process(text)

        print(patch)
        self.assertEqual(patch,"")

   