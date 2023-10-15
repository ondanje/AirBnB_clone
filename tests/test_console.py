# from console import HBNBCommand
# import unittest
# import json
# from models.engine.file_storage import FileStorage
# import io
# import sys


# class TestConsole(unittest.TestCase):
#     """Test cases for HBNBCommand class."""

#     def setUp(self):
#         """Set up test environment."""
#         self.console = HBNBCommand()

#     def tearDown(self):
#         """Tear down test environment."""
#         self.console = None

#     def test_quit(self):
#         """Test the quit command."""
#         with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
#             self.assertTrue(self.console.onecmd("quit"))
#             self.assertEqual(mock_stdout.getvalue(), "")

#     def test_help(self):
#         """Test the help command."""
#         with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
#             self.assertTrue(self.console.onecmd("help"))
#             self.assertNotEqual(mock_stdout.getvalue(), "")


#     def test_create(self):
#         """Test the create command."""
#         with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
#             self.assertFalse(self.console.onecmd("create"))
#             output = mock_stdout.getvalue().strip()
#             self.assertTrue(output.startswith("** class name is missing **"))


# if __name__ == "__main__":
#     unittest.main()
