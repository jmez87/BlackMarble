# BLACK MARBLE Financial Dashboard (Streamlit)

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Financial data
startup_costs = 8400
monthly_burn = 468
break_even_month = 9
current_month = 6
projected_revenue = [0, 200, 450, 720, 1100, 1500, 1950, 2400, 2900, 3500, 4200, 4900]
actual_revenue = [0, 180, 420, 680, 1050, 1380]
expenses = {
    'Office Rent': 150,
    'Software': 89,
    'Marketing': 120,
    'Professional Fees': 75,
    'Insurance': 34
}

# Metrics
current_revenue = actual_revenue[current_month - 1]
projected_current = projected_revenue[current_month - 1]
total_expenses = sum(expenses.values())
cash_flow = current_revenue - total_expenses
months_to_breakeven = max(0, break_even_month - current_month)
revenue_variance = ((current_revenue - projected_current) / projected_current * 100) if projected_current else 0

st.set_page_config(
    page_title="BLACK MARBLE Dashboard", 
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

st.title("📊 BLACK MARBLE Advisory Group Financial Dashboard")
st.markdown("**Real-time financial metrics and performance tracking**")

# KPI Cards
st.subheader("📈 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Current Revenue", 
        f"${current_revenue:,}", 
        f"{revenue_variance:.1f}% vs projected",
        delta_color="normal" if revenue_variance >= 0 else "inverse"
    )

with col2:
    st.metric(
        "Cash Flow", 
        f"${cash_flow:,}",
        delta_color="normal" if cash_flow >= 0 else "inverse"
    )

with col3:
    st.metric(
        "Break-Even", 
        f"{months_to_breakeven} months left",
        delta_color="inverse" if months_to_breakeven > 0 else "normal"
    )

with col4:
    st.metric(
        "Burn Rate", 
        f"${monthly_burn}/mo"
    )

st.markdown("---")

# Revenue Chart
st.subheader("📊 Revenue Trends")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df_revenue = pd.DataFrame({
    "Month": months,
    "Projected": projected_revenue,
    "Actual": actual_revenue + [None]*(12-len(actual_revenue))
})

# Create tabs for different views
tab1, tab2 = st.tabs(["Revenue Chart", "Data Table"])

with tab1:
    st.line_chart(df_revenue.set_index("Month"))
    
    # Add some insights
    if len(actual_revenue) > 1:
        growth_rate = ((actual_revenue[-1] - actual_revenue[-2]) / actual_revenue[-2]) * 100 if actual_revenue[-2] > 0 else 0
        st.info(f"Month-over-month growth: {growth_rate:.1f}%")

with tab2:
    st.dataframe(df_revenue, use_container_width=True)

# Expenses Breakdown
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💰 Expense Breakdown")
    df_expenses = pd.DataFrame(list(expenses.items()), columns=["Category", "Amount"])
    st.bar_chart(df_expenses.set_index("Category"))

with col2:
    st.subheader("📋 Expense Details")
    for category, amount in expenses.items():
        percentage = (amount / total_expenses) * 100
        st.write(f"**{category}**: ${amount} ({percentage:.1f}%)")
    
    st.metric("Total Monthly Expenses", f"${total_expenses}")
    
    # Efficiency metrics
    if current_revenue > 0:
        expense_ratio = (total_expenses / current_revenue) * 100
        st.metric("Expense Ratio", f"{expense_ratio:.1f}%")

# Break-Even Analysis
st.subheader("🎯 Break-Even Analysis")

col1, col2 = st.columns([2, 1])

with col1:
    breakeven_data = pd.DataFrame({
        "Month": months,
        "Projected Revenue": projected_revenue,
        "Monthly Expenses": [total_expenses] * 12,
        "Net Income": [rev - total_expenses for rev in projected_revenue]
    })
    
    # Add break-even line
    st.line_chart(breakeven_data.set_index("Month")[["Projected Revenue", "Monthly Expenses"]])
    
with col2:
    st.write("**Break-Even Metrics**")
    st.metric("Break-Even Month", f"Month {break_even_month}")
    st.metric("Revenue Needed", f"${total_expenses}")
    
    # Show progress to break-even
    if current_month <= break_even_month:
        progress = current_month / break_even_month
        st.progress(progress, text=f"{progress:.1%} to break-even")
    else:
        st.success("✅ Break-even achieved!")

# Detailed table
with st.expander("📊 Detailed Break-Even Analysis"):
    st.dataframe(breakeven_data, use_container_width=True)

st.markdown("---")

# Sidebar with additional metrics and controls
st.sidebar.header("📊 Dashboard Controls")
st.sidebar.metric("Current Month", f"Month {current_month}")
st.sidebar.metric("Startup Costs", f"${startup_costs:,}")

# Add some scenario analysis
st.sidebar.header("🔍 Scenario Analysis")
revenue_multiplier = st.sidebar.slider("Revenue Multiplier", 0.5, 2.0, 1.0, 0.1)
adjusted_revenue = [rev * revenue_multiplier for rev in projected_revenue]
adjusted_breakeven = next((i+1 for i, rev in enumerate(adjusted_revenue) if rev >= total_expenses), 12)

st.sidebar.write(f"**Adjusted Break-Even**: Month {adjusted_breakeven}")
st.sidebar.write(f"**Adjusted Year 1 Revenue**: ${sum(adjusted_revenue):,.0f}")

# Footer with enhanced information
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.caption(f"**Startup Costs**: ${startup_costs:,}")
    st.caption(f"**Monthly Burn**: ${monthly_burn}")

with col2:
    st.caption(f"**Break-Even Month**: {break_even_month}")
    st.caption(f"**Current Month**: {current_month}")

with col3:
    st.caption(f"**Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    st.caption("**© 2024 BLACK MARBLE Advisory Group**")
