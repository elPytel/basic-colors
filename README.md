# Basic colors

## Installation
You can install the module using pip:
```bash
pip install basic-colors
```

## Usage
Module `basic_colors` provides you with a set of variables that you can use to color your text in terminal.

### Colored text
```python
from basic_colors import *

print(Blue + "Ahoj" + Reset)
```

### Logging like messages
```python
from basic_colors import print_warning, print_error, verbose_print

print_warning("This is a warning message.")
print_error("This is an error message.")
set_verbose(True)
verbose_print("This is a verbose message.")
```

## Sources:
- [stackoverflow.com](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
