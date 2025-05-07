# 🚀 IPO Search Bot

A Python-based tool that leverages Google's Gemini AI to fetch real-time information about upcoming and live Initial Public Offerings (IPOs) in the Indian market.

## ✨ Features

- Real-time tracking of live IPOs
- Upcoming IPO information for the next 4 days
- Detailed IPO information including:
  - Company Name
  - IPO Open/Close Dates
  - Price Band
  - Lot Size
  - One Lot Price
  - Grey Market Premium (GMP)
  - Price After Grey Market
  - Issue Size
  - Current Status

## 🛠️ Technical Stack

- Python 3.x
- Google Gemini AI API
- python-dotenv for environment management
- JSON for data structuring

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- Google API key for Gemini AI

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ipos-bot.git
cd ipos-bot
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Google API key:
```bash
GOOGLE_API_KEY=your_api_key_here
```

### Usage

Run the script:
```bash
python ipo_search.py
```

The script will output a JSON containing information about current and upcoming IPOs in the Indian market.

## 📊 Sample Output

```json
{
  "ipos": [
    {
      "company_name": "Example Corp",
      "ipo_open_date": "15 March 2024",
      "ipo_close_date": "18 March 2024",
      "price_band": "₹850-900",
      "lot_size": 16,
      "one_lot_price": "₹13,600",
      "grey_market_premium": "+₹50",
      "price_after_gmp": "₹900",
      "issue_size": "₹1,200 crores",
      "status": "Live"
    }
  ]
}
```

## 🔧 Configuration

The script automatically calculates the date range for IPO search:
- Current date
- Next 4 days

You can modify the date range by adjusting the `timedelta` parameter in the code.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for informational purposes only. The IPO information provided should not be considered as financial advice. Always do your own research before making investment decisions.

## 🔗 Links

- [Google Gemini AI](https://ai.google.dev/)
- [NSE India](https://www.nseindia.com/)
- [SEBI](https://www.sebi.gov.in/)

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.
