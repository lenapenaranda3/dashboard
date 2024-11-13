import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# CSS styling for custom layout and element design
st.markdown("""
<style>
/* Main container styling */
.css-1y0tads {  /* This class targets the main container */
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
    margin-bottom: -7rem !important;
}

/* Metric block styling */
.css-1aumxhk { /* This class targets the st.metric component */
    background-color: #393939 !important;
    text-align: center;
    padding: 15px 0 !important;
}

/* Center metric labels */
.css-1kyxreq { /* This targets the metric labels */
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
}
</style>
""", unsafe_allow_html=True)

# Title and Description
st.title("U.S. Trade Data Dashboard")
st.subheader("Overview of Exports, Imports, and Trade Deficit Over Time")

# Load the data
exports_df = pd.read_csv('exports_grouped.csv')
imports_df = pd.read_csv('imports_grouped.csv')

# Group by year and sum values to get total exports and imports for each year
exports_per_year = exports_df.groupby('year')['value'].sum().reset_index()
imports_per_year = imports_df.groupby('year')['value'].sum().reset_index()

# Merge the exports and imports data on 'year' for easier plotting
trade_df = exports_per_year.rename(columns={'value': 'Exports'}).merge(
    imports_per_year.rename(columns={'value': 'Imports'}),
    on='year'
)

# Calculate the trade deficit as Exports - Imports
trade_df['Deficit'] = trade_df['Imports'] - trade_df['Exports']

# Plotting with Plotly
fig = go.Figure()

# Add trace for Exports
fig.add_trace(
    go.Scatter(
        x=trade_df['year'],
        y=trade_df['Exports'],
        mode='lines+markers',
        name='Exports',
        line=dict(color='red', width=2)
    )
)

# Add trace for Imports
fig.add_trace(
    go.Scatter(
        x=trade_df['year'],
        y=trade_df['Imports'],
        mode='lines+markers',
        name='Imports',
        line=dict(color='orange', width=2)
    )
)

# Add trace for Deficit
fig.add_trace(
    go.Scatter(
        x=trade_df['year'],
        y=trade_df['Deficit'],
        mode='lines+markers',
        name='Trade Deficit (Imports - Exports)',
        line=dict(color='white', width=2, dash='dash')
    )
)

# Update layout for title and labels
fig.update_layout(
    title='U.S. Exports, Imports, and Trade Deficit Over the Years',
    xaxis_title='Year',
    yaxis_title='Trade Value',
    template='plotly_dark'
)

# Display the line chart in Streamlit
st.plotly_chart(fig)
