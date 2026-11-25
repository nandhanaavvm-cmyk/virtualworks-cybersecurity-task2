# Port Status Checker

A lightweight Python command-line utility that checks whether a specific TCP port on a target host or IP address is open or closed.

## Features
- **Custom Host & Port Input:** Supports scanning both local (`127.0.0.1`) and remote hosts across valid TCP ports (`1–65535`).
- **Input Validation:** Verifies numeric port ranges and handles DNS resolution or connection errors gracefully.
- **Fast Timeout Handling:** Uses non-blocking socket timeouts so closed or filtered ports report quickly.

## How to Run
1. Ensure Python 3 is installed on your system.
2. Run the script in your terminal:
   ```bash
   python port_checker.py
