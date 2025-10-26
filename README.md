# 🏛️ BLACK MARBLE Advisory Group Dashboard System

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A comprehensive financial and tax strategy dashboard system designed for advisory firms and financial professionals.

## 🚀 Quick Start

### 📊 Access Dashboards
- **Financial Dashboard**: [http://localhost:8502](http://localhost:8502)
- **Tax Strategy Dashboard**: [http://localhost:8501](http://localhost:8501)

### 🎯 One-Click Launch (Windows)
```powershell
# Financial Dashboard
.\launch_financial_dashboard.ps1

# Tax Strategy Dashboard
.\launch_tax_dashboard.ps1
```

## ✨ Features

### 📊 Financial Dashboard
- **Real-time KPIs**: Revenue, cash flow, burn rate, break-even analysis
- **Visual Analytics**: Interactive charts and trend analysis
- **Scenario Planning**: Revenue projection tools
- **Performance Tracking**: Month-over-month growth metrics

### 💰 Tax Strategy Dashboard
- **Deduction Tracking**: Comprehensive expense categorization
- **IRS Compliance**: Built-in 2024 tax rules and limits
- **Tax Savings Calculator**: Real-time savings estimates
- **Year-end Planning**: Strategic recommendations
- **Mobile-Friendly**: Easy expense entry on-the-go

## 📋 Supported Tax Deductions

- **Business Expenses**: Office supplies, software, marketing, professional fees
- **Travel & Meals**: Business travel, client meals (50% deductible)
- **Home Office**: Simplified method ($5/sq ft, max $1,500)
- **Vehicle Expenses**: Standard mileage ($0.67/mile) or actual expenses
- **Retirement**: SEP-IRA, Solo 401(k), Traditional IRA contributions
- **Health & Benefits**: HSA, health insurance, dependent care

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/BlackMarble.git
   cd BlackMarble
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt.txt
   ```

3. **Launch dashboards**
   ```bash
   # Option 1: Use PowerShell launchers (Windows)
   .\launch_financial_dashboard.ps1
   .\launch_tax_dashboard.ps1
   
   # Option 2: Direct commands
   streamlit run scripts/black_marble_dashboard.py --server.port 8502
   streamlit run scripts/tax_strategy_dashboard.py --server.port 8501
   ```

## 📁 Project Structure

```
BlackMarble/
├── 📊 scripts/
│   ├── black_marble_dashboard.py      # Financial dashboard
│   ├── tax_strategy_dashboard.py      # Tax strategy dashboard
│   └── launch_tax_dashboard.py        # Python launcher
├── 📚 docs/
│   ├── tax_strategy_guide.md          # Comprehensive tax guide
│   └── README.md                      # Documentation hub
├── 🔧 config/
│   └── README.md                      # Configuration guides
├── 🧪 tests/
│   └── README.md                      # Test documentation
├── 🚀 Launchers
│   ├── launch_financial_dashboard.ps1 # Windows financial launcher
│   ├── launch_tax_dashboard.ps1       # Windows tax launcher
│   └── dashboard_hub.html             # Visual dashboard hub
├── 📋 Documentation
│   ├── README_TAX_SYSTEM.md           # Tax system overview
│   ├── FIXES_AND_IMPROVEMENTS.md      # Technical improvements
│   ├── LOCAL_LINKS.md                 # Quick access links
│   └── requirements.txt.txt           # Python dependencies
```

## 💡 Key Benefits

### For Advisory Firms
- **Client Presentations**: Professional dashboards for meetings
- **Tax Planning**: Year-end strategy sessions
- **Performance Monitoring**: Real-time business metrics
- **Compliance**: IRS-compliant deduction tracking

### For Business Owners
- **Tax Optimization**: Maximize deductions and savings
- **Financial Planning**: Break-even and cash flow analysis
- **Record Keeping**: Automated expense categorization
- **Strategic Insights**: Data-driven business decisions

## 🔧 Technical Details

- **Framework**: Streamlit for web interface
- **Backend**: Python with pandas for data processing
- **Storage**: JSON files (easily upgradeable to databases)
- **Charts**: Native Streamlit charts with interactive features
- **Compatibility**: Windows, macOS, Linux

## 📈 Advanced Features

### Financial Dashboard
- Monthly trend analysis
- Break-even progress tracking
- Expense ratio calculations
- Revenue variance reporting
- Interactive scenario modeling

### Tax Strategy Dashboard
- Automatic deduction calculations
- IRS limit tracking with progress bars
- Quarterly tax summaries
- Annual projection tools
- Professional tax strategies

## 🛡️ Compliance & Security

- **IRS Guidelines**: Built-in 2024 tax rules and limits
- **Data Privacy**: Local storage, no cloud dependencies
- **Record Keeping**: 7-year retention compliance
- **Audit Support**: Detailed transaction logs

## 🎯 Use Cases

- **Tax Preparation**: End-of-year planning and optimization
- **Client Consulting**: Advisory firm presentations
- **Business Planning**: Financial forecasting and analysis
- **Expense Management**: Real-time deduction tracking
- **Performance Monitoring**: KPI dashboards for leadership

## 🔄 Updates & Maintenance

- **Annual Tax Updates**: New IRS limits and rules
- **Feature Enhancements**: Regular improvements
- **Bug Fixes**: Continuous maintenance
- **Documentation**: Updated guides and tutorials

## 📞 Support

For questions, issues, or feature requests:
- **Documentation**: Check the `/docs` folder
- **Issues**: Create GitHub issues for bugs
- **Discussions**: Use GitHub Discussions for questions

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io) for the web interface
- Tax rules and limits based on [IRS Publication 535](https://www.irs.gov/publications/p535)
- Professional financial dashboard design principles

---

**BLACK MARBLE Advisory Group**  
*Professional Financial & Tax Strategy Solutions*

[![Deploy](https://img.shields.io/badge/Deploy-Streamlit%20Cloud-FF4B4B?style=for-the-badge)](https://streamlit.io/cloud)
[![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)](https://python.org)