# test_server.py

import unittest
import asyncio

# Assuming your server code is saved in a file named 'mcp_server.py'
# We import the specific tool function we want to test.
from app.mcp_server import test_hello

class TestMCPServerTools(unittest.TestCase):
    """
    Test suite for the tools defined in the MCP server.
    """

    def test_tool_test_hello_with_string(self):
        """
        Tests the test_hello tool with a simple string input.
        """
        # Since test_hello is an async function, we use asyncio.run()
        # to execute it and get the result.
        name_input = "world"
        expected_output = "hello world"
        
        actual_output = asyncio.run(test_hello(name_input))
        
        self.assertEqual(actual_output, expected_output)

    def test_tool_test_hello_with_empty_string(self):
        """
        Tests the test_hello tool with an empty string to check edge cases.
        """
        name_input = ""
        expected_output = "hello "
        
        actual_output = asyncio.run(test_hello(name_input))
        
        self.assertEqual(actual_output, expected_output)

    def test_tool_test_hello_with_number_string(self):
        """
        Tests the test_hello tool with a string containing numbers.
        """
        name_input = "MCP-9000"
        expected_output = "hello MCP-9000"

        actual_output = asyncio.run(test_hello(name_input))

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    # This allows you to run the tests directly from the command line
    unittest.main()
