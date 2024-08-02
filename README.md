# Password Checker

This is a simple Python script designed to check if a given password has been exposed in known data breaches. The script queries a public API to determine how many times the password has been compromised.

## Features

- **Password Exposure Check**: Determines if the given password has been found in data breaches.
- **Command Line Interface**: Run the script from the command line with the password as an argument.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/emma-stoned/password-checker.git
   cd password-checker
   ```
2. **Install Dependencies**

No external dependencies are required for this script.

## Usage
To use the password checker, run the script with a password argument:

```bash
  python checkmypass.py <password>
  ```
  
**Replace** <password> with the password you want to check.

## Example
``` bash

python checkmypass.py mypassword123
```
## Contributing
Feel free to fork the repository and submit pull requests. Please make sure your code adheres to the project's coding standards.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This tool is provided for educational purposes only. Use responsibly and ensure you follow best practices for password management.
