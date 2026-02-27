import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.express as px
from detector import analyze_vulnerability

# 1. Page Configuration (Wide layout & initially collapsed)
st.set_page_config(
    page_title="Sentinel-Duty AI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. Professional CSS "Kill-Switch" (Hides the sidebar button completely)
st.markdown("""
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. UI Header
st.title("🛡️ Sentinel-Duty AI")
st.markdown("### UK Consumer Duty: Vulnerability Detection & Outcome Monitoring")

# 4. Data Logic
spiral, shock = analyze_vulnerability()
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, 'data', 'sentinel.db')

conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM transactions", conn)
conn.close()

# 5. Top Row Metrics
m1, m2, m3 = st.columns(3)
m1.metric("Total Transactions", len(df))
m2.metric("⚠️ Vulnerable Flags", len(set(spiral + shock)), delta="Needs Review", delta_color="inverse")
m3.metric("System Health", "Active (FCA 2026)")

# 6. Main Dashboard Layout
st.divider()
c1, c2 = st.columns([2, 1])

with c1:
    st.write("#### 📊 Spending Trends")
    fig = px.bar(
        df.groupby('category')['amount'].sum().reset_index(), 
        x='category', 
        y='amount', 
        color='category', 
        template="plotly_dark"
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.write("#### 🎯 High-Risk Targets")
    risk_df = pd.DataFrame({
        "User ID": list(set(spiral + shock)),
        "Status": ["Vulnerable"] * len(set(spiral + shock))
    })
    st.dataframe(risk_df, use_container_width=True, hide_index=True)

# 7. Raw Audit Trail
st.write("### 📜 Real-time Transaction Audit Trail")
st.dataframe(df.sort_values('timestamp', ascending=False), use_container_width=True)

# 8. Regulatory Footer (The Expert Polish)
st.divider()
with st.expander("ℹ️ About Sentinel-Duty & UK Compliance"):
    st.write("""
    This system is designed to meet the **FCA Consumer Duty** requirements (2026 Standards). 
    It specifically monitors for:
    * **Financial Resilience:** Identifying customers with high-frequency gambling spend or sudden debt increases.
    * **Life Events:** Flagging patterns that suggest a customer may be in financial distress.
    * **Data Privacy:** Built using local-first SQLite to ensure strict GDPR compliance.
    """)