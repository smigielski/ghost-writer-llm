import unittest
import sys
sys.path.insert(0, './src')
from lark import Lark, Token, Tree
import logging

class TestLarkEngine(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff= None
        logger = logging.getLogger()
        logger.level = logging.DEBUG

    def test_model(self):

        with open('./src/command_grammar.lark') as grammar_file:
            parser = Lark(grammar_file.read(), start='start')

        text = """
        <!-- #seed 123 -->
                <!-- #model llama3.1:latest -->
                <!-- #system give one sentence only -->
                <!-- #chat test -->
        <!-- #generated -->
        ---
        Generated by: [ghost-writer-llm](https://github.com/smigielski/ghost-writer-llm)
        <!-- /generated -->
        """
        tree = parser.parse(text)
        logging.info(tree.pretty())

        # Function to recover the original text from the tree
        def recover_text(tree):
            if isinstance(tree, Tree):
                return ''.join(recover_text(child) for child in tree.children)
            elif isinstance(tree, Token):              
                return tree.value  # Leaf node in the tree, just return its value (text content)

        # Recover the original text from the tree
        recovered_text = recover_text(tree)
        logging.info(recovered_text)
        self.assertEqual(recovered_text, text)