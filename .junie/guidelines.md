# KnowelyPython Project Guidelines

This document provides guidelines and information for developers working on the KnowelyPython project.

## Project Overview

KnowelyPython is a collection of Python examples and tutorials covering various concepts including:
- Object-oriented programming (classes, inheritance, encapsulation, abstraction)
- Data structures (lists, dictionaries, sets)
- String manipulation
- Design patterns (Singleton)
- Python-specific features (mutable vs immutable types, comprehensions)

## Build/Configuration Instructions

This project is a collection of standalone Python examples and doesn't require a specific build process. However, here are some configuration notes:

### Environment Setup

1. Python 3.8+ is recommended for all examples
2. No external dependencies are required for most examples
3. To set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix/MacOS
   source venv/bin/activate
   ```

## Testing Information

### Running Tests

Tests are written using the standard `unittest` framework. To run tests:

1. For a specific test file:
   ```bash
   python test_filename.py
   ```

2. To run all tests in the project (if you have multiple test files):
   ```bash
   python -m unittest discover
   ```

### Writing New Tests

1. Create a new file with the naming convention `test_*.py`
2. Import the `unittest` module and the classes/functions you want to test
3. Create a test class that inherits from `unittest.TestCase`
4. Write test methods that start with `test_`
5. Use assertion methods like `assertEqual`, `assertTrue`, etc.

### Example Test

Here's a simple example of a test for the abstract classes:

```python
import unittest
from classes.abstract import Triangle

class TestTriangle(unittest.TestCase):
    def test_triangle_creation(self):
        triangle = Triangle()
        self.assertEqual(triangle.shape_name, "triangle")
        
    def test_draw_method(self):
        triangle = Triangle()
        # In a real test, you might want to capture stdout
        # and verify the output
        triangle.draw()  # Should not raise exceptions

if __name__ == "__main__":
    unittest.main()
```

## Code Style and Development Guidelines

1. **Code Organization**:
   - Examples are organized by concept (classes, strings, etc.)
   - Each concept may have multiple files demonstrating different aspects

2. **Naming Conventions**:
   - Files are named descriptively (e.g., `abstract.py` for abstract classes)
   - Classes use PascalCase (e.g., `Triangle`, `Person`)
   - Functions and variables use snake_case (e.g., `do_work`, `shape_name`)

3. **Type Hints**:
   - Many examples use type hints for better code clarity
   - Follow this practice when adding new code

4. **Documentation**:
   - Markdown files provide detailed explanations of concepts
   - Code examples should be well-commented
   - When adding new examples, consider creating a corresponding markdown file

5. **Running Examples**:
   - Most examples can be run directly: `python path/to/example.py`
   - Some files are meant to be imported rather than run directly

## Debugging Tips

1. Many examples include print statements that demonstrate the output
2. For classes with inheritance, pay attention to method overriding and super() calls
3. When working with abstract classes, remember that abstract methods must be implemented in subclasses