# BLACK MARBLE Tax Strategy & Deductions Dashboard

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date
import json
import os

# Tax deduction categories and their IRS limits/rules (2024 tax year)
TAX_DEDUCTIONS = {
    "Business Expenses": {
        "Office Supplies": {"limit": None, "description": "Pens, paper, computers, software"},
        "Professional Development": {"limit": 5250, "description": "Training, conferences, certifications"},
        "Business Meals": {"limit": None, "rate": 0.50, "description": "50% deductible for business meals"},
        "Travel Expenses": {"limit": None, "description": "Airfare, hotels, car rentals for business"},
        "Home Office": {"limit": 1500, "description": "Simplified method: $5/sq ft up to 300 sq ft"},
        "Professional Fees": {"limit": None, "description": "Legal, accounting, consulting fees"},
        "Marketing & Advertising": {"limit": None, "description": "Website, ads, promotional materials"},
        "Insurance": {"limit": None, "description": "Professional liability, business insurance"},
        "Software & Technology": {"limit": None, "description": "Business software subscriptions, hardware"},
        "Communications": {"limit": None, "description": "Business phone, internet, mobile plans"}
    },
    "Vehicle Expenses": {
        "Mileage": {"rate": 0.67, "description": "Standard mileage rate per mile (2024)"},
        "Actual Expenses": {"limit": None, "description": "Gas, maintenance, insurance (business %)"}
    },
    "Retirement Contributions": {
        "SEP-IRA": {"limit": 69000, "description": "Up to 25% of compensation or $69k"},
        "Solo 401(k)": {"limit": 69000, "description": "Employee + employer contributions"},
        "Traditional IRA": {"limit": 7000, "description": "$7k limit, $8k if 50+"}
    },
    "Health & Benefits": {
        "Health Insurance": {"limit": None, "description": "Self-employed health insurance premium"},
        "HSA Contributions": {"limit": 4300, "description": "$4,300 individual, $8,550 family"},
        "Dependent Care": {"limit": 5000, "description": "Dependent care FSA"}
    }
}

# Sample transactions for demonstration
SAMPLE_TRANSACTIONS = [
    {"date": "2024-01-15", "category": "Office Supplies", "description": "Laptop for business", "amount": 1200.00},
    {"date": "2024-01-20", "category": "Professional Development", "description": "Industry conference", "amount": 850.00},
    {"date": "2024-02-05", "category": "Business Meals", "description": "Client lunch", "amount": 75.00},
    {"date": "2024-02-10", "category": "Travel Expenses", "description": "Flight to client meeting", "amount": 450.00},
    {"date": "2024-03-01", "category": "Home Office", "description": "Home office setup", "amount": 300.00},
    {"date": "2024-03-15", "category": "Professional Fees", "description": "Accounting services", "amount": 500.00},
    {"date": "2024-04-01", "category": "Marketing & Advertising", "description": "Website development", "amount": 2000.00},
    {"date": "2024-04-15", "category": "Software & Technology", "description": "Business software license", "amount": 120.00},
    {"date": "2024-05-01", "category": "Insurance", "description": "Professional liability insurance", "amount": 400.00},
    {"date": "2024-05-15", "category": "Mileage", "description": "Client visits - 150 miles", "amount": 100.50}
]

def load_transactions():
    """Load transactions from file or return sample data"""
    try:
        with open('tax_transactions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return SAMPLE_TRANSACTIONS

def save_transactions(transactions):
    """Save transactions to file"""
    with open('tax_transactions.json', 'w') as f:
        json.dump(transactions, f)

def calculate_deduction_amount(category, amount, description=""):
    """Calculate the actual deductible amount based on IRS rules"""
    if category == "Business Meals":
        return amount * 0.50  # 50% deductible
    elif category == "Mileage":
        # Extract miles from description if possible
        try:
            miles = float(description.split()[0]) if "miles" in description.lower() else 0
            return miles * 0.67  # 2024 standard mileage rate
        except:
            return amount
    elif category == "Home Office":
        # Simplified method calculation
        return min(amount, 1500)
    else:
        return amount

def get_tax_savings_estimate(deduction_amount, tax_bracket=0.22):
    """Estimate tax savings based on marginal tax bracket"""
    return deduction_amount * tax_bracket

st.set_page_config(page_title="Tax Strategy Dashboard", layout="wide", page_icon="📊")

# Header
st.title("🏛️ BLACK MARBLE Tax Strategy & Deductions Dashboard")
st.markdown("**Maximize your tax savings with strategic deduction tracking and planning**")

# Sidebar for configuration
st.sidebar.header("Tax Settings")
tax_bracket = st.sidebar.selectbox(
    "Marginal Tax Bracket",
    [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
    index=2,
    format_func=lambda x: f"{x:.0%}"
)

tax_year = st.sidebar.selectbox("Tax Year", [2024, 2023], index=0)

# Load transactions
transactions = load_transactions()
df = pd.DataFrame(transactions)
df['date'] = pd.to_datetime(df['date'])
df['deductible_amount'] = df.apply(lambda row: calculate_deduction_amount(row['category'], row['amount'], row['description']), axis=1)
df['tax_savings'] = df['deductible_amount'] * tax_bracket

# Main metrics
col1, col2, col3, col4 = st.columns(4)

total_deductions = df['deductible_amount'].sum()
total_tax_savings = df['tax_savings'].sum()
avg_monthly_deductions = df.groupby(df['date'].dt.to_period('M'))['deductible_amount'].sum().mean()
total_transactions = len(df)

col1.metric("Total Deductions YTD", f"${total_deductions:,.2f}")
col2.metric("Estimated Tax Savings", f"${total_tax_savings:,.2f}")
col3.metric("Avg Monthly Deductions", f"${avg_monthly_deductions:,.2f}")
col4.metric("Tracked Transactions", f"{total_transactions}")

st.markdown("---")

# Tabs for different views
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "➕ Add Expense", "📋 Transaction Log", "📈 Analytics", "💡 Tax Strategies"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Deductions by Category")
        category_totals = df.groupby('category')['deductible_amount'].sum().sort_values(ascending=False)
        st.bar_chart(category_totals)
        
        st.subheader("Top Deduction Categories")
        for category, amount in category_totals.head(5).items():
            savings = amount * tax_bracket
            st.write(f"**{category}**: ${amount:,.2f} (saves ${savings:,.2f})")
    
    with col2:
        st.subheader("Monthly Deduction Trends")
        monthly_deductions = df.groupby(df['date'].dt.to_period('M'))['deductible_amount'].sum()
        monthly_df = pd.DataFrame({
            'Month': monthly_deductions.index.astype(str),
            'Deductions': monthly_deductions.values
        })
        st.line_chart(monthly_df.set_index('Month'))
        
        st.subheader("Deduction Limits Status")
        for main_category, subcategories in TAX_DEDUCTIONS.items():
            st.write(f"**{main_category}**")
            for subcat, rules in subcategories.items():
                current_amount = df[df['category'] == subcat]['deductible_amount'].sum()
                if rules.get('limit'):
                    percentage = (current_amount / rules['limit']) * 100
                    st.progress(min(percentage / 100, 1.0), text=f"{subcat}: ${current_amount:,.0f} / ${rules['limit']:,.0f}")
                else:
                    st.write(f"• {subcat}: ${current_amount:,.2f} (no limit)")

with tab2:
    st.subheader("Add New Tax-Deductible Expense")
    
    col1, col2 = st.columns(2)
    
    with col1:
        expense_date = st.date_input("Date", value=date.today())
        
        # Flatten categories for selection
        all_categories = []
        for main_cat, subcats in TAX_DEDUCTIONS.items():
            all_categories.extend(list(subcats.keys()))
        
        category = st.selectbox("Category", sorted(all_categories))
        amount = st.number_input("Amount ($)", min_value=0.01, value=1.00, step=0.01)
    
    with col2:
        description = st.text_area("Description", placeholder="Enter details about this expense...")
        
        # Show category info
        for main_cat, subcats in TAX_DEDUCTIONS.items():
            if category in subcats:
                st.info(f"**{category}**: {subcats[category]['description']}")
                if subcats[category].get('limit'):
                    st.warning(f"Annual limit: ${subcats[category]['limit']:,}")
                if subcats[category].get('rate'):
                    st.info(f"Deduction rate: {subcats[category]['rate']:.0%}")
                break
    
    if st.button("Add Expense", type="primary"):
        new_transaction = {
            "date": expense_date.strftime("%Y-%m-%d"),
            "category": category,
            "description": description,
            "amount": amount
        }
        transactions.append(new_transaction)
        save_transactions(transactions)
        st.success("Expense added successfully!")
        st.rerun()

with tab3:
    st.subheader("Transaction Log")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_category = st.multiselect("Filter by Category", df['category'].unique())
    with col2:
        date_range = st.date_input("Date Range", value=[df['date'].min().date(), df['date'].max().date()], key="date_range")
    with col3:
        min_amount = st.number_input("Minimum Amount", value=0.0)
    
    # Apply filters
    filtered_df = df.copy()
    if filter_category:
        filtered_df = filtered_df[filtered_df['category'].isin(filter_category)]
    if len(date_range) == 2:
        filtered_df = filtered_df[
            (filtered_df['date'].dt.date >= date_range[0]) & 
            (filtered_df['date'].dt.date <= date_range[1])
        ]
    filtered_df = filtered_df[filtered_df['amount'] >= min_amount]
    
    # Display table
    display_df = filtered_df[['date', 'category', 'description', 'amount', 'deductible_amount', 'tax_savings']].copy()
    display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
    display_df['amount'] = display_df['amount'].apply(lambda x: f"${x:,.2f}")
    display_df['deductible_amount'] = display_df['deductible_amount'].apply(lambda x: f"${x:,.2f}")
    display_df['tax_savings'] = display_df['tax_savings'].apply(lambda x: f"${x:,.2f}")
    
    st.dataframe(display_df, use_container_width=True)

with tab4:
    st.subheader("Tax Analytics & Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Quarterly Breakdown**")
        df['quarter'] = df['date'].dt.quarter
        quarterly_summary = df.groupby('quarter').agg({
            'deductible_amount': 'sum',
            'tax_savings': 'sum'
        }).round(2)
        st.dataframe(quarterly_summary)
        
        st.write("**Top 10 Individual Expenses**")
        top_expenses = df.nlargest(10, 'deductible_amount')[['description', 'category', 'deductible_amount', 'tax_savings']]
        st.dataframe(top_expenses)
    
    with col2:
        st.write("**Deduction Efficiency Analysis**")
        efficiency = df.groupby('category').agg({
            'deductible_amount': ['sum', 'count', 'mean']
        }).round(2)
        efficiency.columns = ['Total', 'Count', 'Average']
        st.dataframe(efficiency)
        
        st.write("**Projected Annual Totals**")
        current_month = datetime.now().month
        if current_month > 0:
            annual_projection = (total_deductions / current_month) * 12
            annual_savings_projection = annual_projection * tax_bracket
            st.metric("Projected Annual Deductions", f"${annual_projection:,.2f}")
            st.metric("Projected Annual Tax Savings", f"${annual_savings_projection:,.2f}")

with tab5:
    st.subheader("💡 Tax Strategy Recommendations")
    
    st.write("### Year-End Tax Planning Strategies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**🎯 Immediate Opportunities**")
        
        # Check for underutilized deductions
        current_home_office = df[df['category'] == 'Home Office']['deductible_amount'].sum()
        if current_home_office < 1500:
            remaining_home_office = 1500 - current_home_office
            st.write(f"• **Home Office**: You can deduct ${remaining_home_office:,.2f} more (saves ${remaining_home_office * tax_bracket:,.2f})")
        
        current_retirement = df[df['category'].str.contains('IRA|401')]['deductible_amount'].sum()
        retirement_limit = 69000  # SEP-IRA limit
        if current_retirement < retirement_limit:
            remaining_retirement = retirement_limit - current_retirement
            st.write(f"• **Retirement Contrib**: Up to ${remaining_retirement:,.2f} more possible")
        
        st.write("• **Equipment Purchases**: Consider buying needed equipment before year-end")
        st.write("• **Professional Development**: Conferences, training, certifications")
        st.write("• **Business Meals**: Track all business-related meals (50% deductible)")
        
        st.write("**📋 Documentation Tips**")
        st.write("• Keep detailed receipts and descriptions")
        st.write("• Use mileage log for business travel")
        st.write("• Separate business and personal expenses")
        st.write("• Consider dedicated business credit card")
    
    with col2:
        st.write("**💼 Advanced Strategies**")
        st.write("• **Business Structure**: Consider LLC or S-Corp election")
        st.write("• **Retirement Plans**: Maximize SEP-IRA or Solo 401(k)")
        st.write("• **Equipment Depreciation**: Section 179 deduction up to $1.16M")
        st.write("• **Health Savings**: HSA contributions if self-employed")
        
        st.write("**📊 Benchmarking**")
        avg_deduction_rate = total_deductions / max(df['amount'].sum(), 1) * 100
        st.metric("Your Deduction Rate", f"{avg_deduction_rate:.1f}%")
        
        if avg_deduction_rate < 80:
            st.warning("⚠️ Consider reviewing expenses for additional deductions")
        else:
            st.success("✅ Good deduction tracking!")
        
        st.write("**🎯 Goals for Next Quarter**")
        st.write("• Increase tracking of small expenses")
        st.write("• Document home office usage")
        st.write("• Plan equipment purchases strategically")
        st.write("• Review quarterly estimated taxes")

# Footer
st.markdown("---")
st.markdown("*This dashboard is for informational purposes only. Consult with a tax professional for specific advice.*")
st.markdown("**BLACK MARBLE Advisory Group** - Tax Strategy & Financial Planning")