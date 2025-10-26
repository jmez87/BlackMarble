# BLACK MARBLE Advisory Group - Documentation

## 🚀 **QUICK ACCESS LINKS**

### 📊 **Financial Dashboard**
**Local URL**: [http://localhost:8502](http://localhost:8502)
- Real-time financial metrics & performance tracking
- Revenue trends and break-even analysis
- Interactive scenario planning

### 💰 **Tax Strategy Dashboard**  
**Local URL**: [http://localhost:8501](http://localhost:8501)
- Tax deduction tracking & optimization
- IRS-compliant calculations
- Year-end planning strategies

---

## Launch Options

### Option 1: **One-Click Launchers** (Recommended)
```powershell
# Financial Dashboard
.\launch_financial_dashboard.ps1

# Tax Strategy Dashboard  
.\launch_tax_dashboard.ps1
```

### Option 2: **Direct Commands**
```bash
# Financial Dashboard
streamlit run scripts/black_marble_dashboard.py --server.port 8502

# Tax Strategy Dashboard
streamlit run scripts/tax_strategy_dashboard.py --server.port 8501
```

### Option 3: **Manual Start**
```bash
# Start both dashboards in separate windows
Start-Process PowerShell -ArgumentList "-Command", "streamlit run scripts/black_marble_dashboard.py --server.port 8502"
Start-Process PowerShell -ArgumentList "-Command", "streamlit run scripts/tax_strategy_dashboard.py --server.port 8501"
```

### Key Features
- **📊 Real-time Expense Tracking**: Monitor deductible expenses throughout the year
- **💰 Tax Savings Calculator**: Estimate savings based on your tax bracket
- **📈 Visual Analytics**: Charts showing spending patterns and opportunities
- **🎯 Strategic Recommendations**: Year-end planning suggestions
- **📱 Mobile Friendly**: Responsive design for expense entry on-the-go

### Documentation Files
- `tax_strategy_guide.md` - Comprehensive user guide and tax strategies
- `README.md` - This file with quick start instructions

### Support
For questions or support, contact BLACK MARBLE Advisory Group.