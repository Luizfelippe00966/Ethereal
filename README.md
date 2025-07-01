# Ethereal

**Auto Connect and Faucet Ethereal**

---

## About The Project

Ethereal is a Python automation tool designed to automatically connect to the Ethereal platform and claim tokens from its faucet. This project simplifies the process of interacting with the Ethereal testnet by automating wallet connection and faucet claiming steps.

---

## Features

- Automatically opens the Ethereal platform
- Connects wallet (manual approval required for wallet extensions)
- Claims faucet tokens automatically
- Supports Ethereum test networks
- Headless browser support for automation environments

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pyppeteer library for browser automation
- A compatible Ethereum wallet browser extension (e.g., MetaMask) installed and configured

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/Luizfelippe00966/Ethereal.git
   cd Ethereal
   ```

2. Install dependencies:

   ```
   pip install pyppeteer
   ```

---

## Usage

Run the main automation script:

```
python autoconnect_faucet.py
```

The script will launch a Chromium browser, navigate to the Ethereal platform, and attempt to connect your wallet and claim faucet tokens.

> **Note:** Wallet connection and transaction approvals require manual confirmation in your wallet extension popup.

---

## Customization

- Update CSS selectors in the script to match any changes in the Ethereal UI.
- Adjust wait times depending on network speed and transaction confirmation times.
- Modify the script to support additional wallet types or networks as needed.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, enhancements, or new features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

