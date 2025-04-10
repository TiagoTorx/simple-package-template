# string-tools-practice

**string-tools-practice** is a simple Python package for string manipulation and analysis.

## Features

- **Manipulate strings**  
  - Capitalize words  
  - Remove whitespace

- **Analyze strings**  
  - Count the number of vowels  
  - Identify if a string is a palindrome  

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install:

```bash
pip install string-tools-practice
```

## Usage

```python
from string_tools import formatting, analysis

text = "Level"

print(formatting.capitalize_words(text))  # Example: "Level"
print(analysis.is_palindrome(text))       # Example: True

```

## Requirements
Python >= 3.8

## Author
TiagoTorx

## License
[MIT](https://choosealicense.com/licenses/mit/)