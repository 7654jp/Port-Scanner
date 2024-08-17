# Port Scanner

   A simple port scanner written in Python.

   ## Description

   This script scans a range of ports on a target IP address or hostname and identifies which ports are open.

   ## Features

   - Scans a range of ports.

   - Multithreaded for faster scanning.

   - Provides output for both open and closed ports.

   ## Requirements

   - Python 3.x

   - Libraries: `socket`, `threading`, `datetime`, `argparse`

   ## Installation

   1. Clone the repository:

   git clone https://github.com/MadlyAbi/Port-Scanner.git

   2. Navigate to the project directory:

   cd Port-Scanner
   
   ## Usage

   Run the script with the target IP/hostname and port range:

   python port_scanner.py example.com 1 1024

   For verbose output (showing closed ports as well):

   python port_scanner.py example.com 1 1024 --verbose

   ## Example

   python port_scanner.py 191.162.1.1 1 1024

   ## Contributing

   Contributions are welcome! Please fork the repository and submit a pull request.

   ## License

   This project is licensed under the MIT License. See the `LICENSE` file for details.

   ## Author

   - MadlyAbi([Abinesh](https://github.com/Madlyabi))

   ## Acknowledgments
   - Inspired by the need for a simple port scanner
