# 🏛️ BLACK MARBLE Tax Strategy & Deductions System

## What We've Built

I've created a comprehensive tax strategy and deductions tracking system for your BLACK MARBLE Advisory Group project. This system helps you and your clients maximize tax savings through strategic deduction tracking and year-end planning.

## 🚀 Quick Start

### Option 1: PowerShell Launcher (Recommended for Windows)
```powershell
.\launch_tax_dashboard.ps1
```

### Option 2: Direct Streamlit Launch
```bash
streamlit run scripts/tax_strategy_dashboard.py
```

### Option 3: Python Launcher
```bash
python scripts/launch_tax_dashboard.py
```

## 📊 Dashboard Features

### 1. Overview Tab
- **Real-time KPIs**: Total deductions YTD, estimated tax savings, average monthly deductions
- **Category Breakdown**: Visual charts showing deductions by category
- **Monthly Trends**: Line chart tracking deduction patterns over time
- **Deduction Limits Status**: Progress bars showing how close you are to annual limits

### 2. Add Expense Tab
- **Easy Entry Form**: Date, category, amount, and description fields
- **Smart Categories**: Pre-loaded with IRS-compliant deduction categories
- **Automatic Calculations**: Built-in rules for business meals (50%), mileage rates, etc.
- **Category Guidance**: Helpful descriptions and limit information for each category

### 3. Transaction Log
- **Filterable Table**: Search by category, date range, or amount
- **Export Ready**: Easy to export for tax preparation
- **Detailed View**: Shows original amount, deductible amount, and tax savings

### 4. Analytics Tab
- **Quarterly Breakdown**: Performance by quarter
- **Top Expenses**: Biggest deduction opportunities
- **Efficiency Analysis**: Average deductions by category
- **Annual Projections**: Forecasted year-end totals

### 5. Tax Strategies Tab
- **Year-end Planning**: Specific recommendations for Q4 tax moves
- **Advanced Strategies**: Business structure, retirement, equipment depreciation tips
- **Documentation Best Practices**: IRS compliance guidelines
- **Benchmarking**: Track your deduction efficiency

## 💰 Supported Deductions (2024 Tax Year)

### Business Expenses
- Office supplies and equipment
- Professional development (up to $5,250)
- Business meals (50% deductible)
- Travel expenses
- Home office (simplified method: $5/sq ft, max $1,500)
- Professional fees
- Marketing & advertising
- Insurance premiums
- Software & technology
- Communications

### Vehicle Expenses
- Standard mileage: $0.67/mile (2024 rate)
- Actual expenses (business percentage)

### Retirement Contributions
- SEP-IRA: Up to $69,000
- Solo 401(k): Up to $69,000
- Traditional IRA: $7,000 ($8,000 if 50+)

### Health & Benefits
- Self-employed health insurance
- HSA contributions: $4,300 individual, $8,550 family
- Dependent care: Up to $5,000

## 🎯 Key Benefits

1. **Maximize Tax Savings**: Identify every possible deduction opportunity
2. **IRS Compliance**: Built-in rules ensure proper deduction calculations
3. **Year-end Planning**: Strategic recommendations for Q4 tax moves
4. **Professional Grade**: Suitable for advisory firm client presentations
5. **Data Export**: Easy integration with tax preparation software

## 📁 File Structure

```
BlackMarble/
├── scripts/
│   ├── tax_strategy_dashboard.py      # Main dashboard application
│   ├── launch_tax_dashboard.py        # Python launcher script
│   └── black_marble_dashboard.py      # Your existing financial dashboard
├── docs/
│   ├── tax_strategy_guide.md          # Comprehensive user guide
│   └── README.md                      # Quick start documentation
├── launch_tax_dashboard.ps1           # PowerShell launcher (Windows)
├── requirements.txt.txt               # Updated dependencies
└── tax_transactions.json              # Auto-created data file
```

## 🔧 Technical Details

- **Framework**: Streamlit for web interface
- **Data Storage**: JSON file for simplicity (easily upgradeable to database)
- **Charts**: Built-in Streamlit charts with pandas integration
- **Tax Rules**: 2024 IRS guidelines and limits built-in
- **Responsive**: Works on desktop and mobile devices

## 💡 Next Steps

1. **Launch the Dashboard**: Use one of the quick start options above
2. **Explore Sample Data**: Pre-loaded transactions show system capabilities
3. **Add Real Expenses**: Start tracking your actual business expenses
4. **Review Strategies**: Check the Tax Strategies tab for year-end planning
5. **Customize**: Modify categories or limits as needed for specific clients

## 🏆 Professional Use

This system is designed for:
- **Advisory Firms**: Client presentations and planning sessions
- **Solo Practitioners**: Personal tax optimization
- **Small Businesses**: Year-round expense tracking
- **Consultants**: Demonstrate tax planning expertise

## 📞 Support

The dashboard includes:
- Built-in help text for each deduction category
- IRS compliance notes and warnings
- Professional disclaimers
- Export capabilities for tax professionals

---

**Ready to maximize your tax savings?** Launch the dashboard and start tracking your deductions today!

*Disclaimer: This tool is for informational purposes only. Always consult with a qualified tax professional for specific guidance.*