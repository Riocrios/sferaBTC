# Bitcoin Address Generator and Visualization

This script generates Bitcoin addresses, visualizes them in a 3D scatter plot, and allows users to interactively view details of specific addresses by hovering over points in the plot.

## Features
- **Bitcoin Address Generation**:
  - Creates `num_points` Bitcoin addresses using elliptic curve cryptography (ECDSA).
  - Outputs the private key, Bitcoin address, and SHA-256 hash of the private key.
- **3D Visualization**:
  - Distributes points in 3D space using the golden angle algorithm for uniform placement on a sphere.
  - Interactive visualization using `matplotlib`.
- **Interactive Address Display**:
  - Hover over points to view the corresponding private key, address, and hash.

## Dependencies
The script requires the following Python libraries:
- `os`
- `ecdsa`
- `hashlib`
- `base58`
- `numpy`
- `matplotlib`

To install the dependencies, run:

pip install ecdsa base58 numpy matplotlib
Usage
python script.py
Replace script.py with the name of the Python file.
Adjust Number of Points:

Change the num_points variable to increase or decrease the number of addresses generated.
Interactivity:

Hover over points in the plot to view address details in the terminal.

Notes
The private keys and addresses are randomly generated and should not be used for real transactions.
Increase num_points cautiously; generating too many addresses may slow down the script.
Ensure matplotlib and your Python environment support 3D plotting.


❤️ Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to enhance this project.  
BTC - 1M8xKWXJdNUqv2Yn4jsJsJPrZZVRfRqyUr
ETH-  0x22aD64862711D256E6BCD1E0b33c967553919015
SOL-  BV2kxP5ADuHbFwz9D8K6o1sYGHgHYSp4Uy1NnTtT8jqy
Doge- DTDZnK5b4WdnubyQ4M8UkmUFXCnJohjKhw