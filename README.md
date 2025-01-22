# Basic System Report Script

This repository contains a simple Python script that generates a basic system performance report in PDF format. The script collects information about memory, disk usage, connected users, and generates pie charts to visualize the data.

I am not an expert in Python scripting, but I understand the basics of running scripts, working with libraries, and modifying code. This project is an example of how I can adapt and implement small Python utilities for practical tasks.


## Features

- **Generates a PDF report** with:
  - Memory usage (Used and Free).
  - Disk usage (Used and Free).
  - Number of connected users.
- **Includes pie charts** for memory and disk usage.
- Simple and easy to modify for anyone with basic Python knowledge.

## Example Output

After running the script, you will get a PDF file similar to this:

- **Memory Usage** and **Disk Usage** pie charts.
- Basic system information (report time, number of users).

## Prerequisites

You need the following Python libraries installed:
- `psutil`: For retrieving system information.
- `matplotlib`: For creating pie charts.
- `fpdf`: For generating the PDF.

To install them, run:
```bash
pip install psutil matplotlib fpdf
