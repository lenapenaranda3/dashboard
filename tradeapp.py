import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# CSS styling for custom layout and element design
st.markdown("""
<style>
[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

[data-testid="stVerticalBlock"] {
    padding-left: 0rem;
    padding-right: 0rem;
}

[data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}

[data-testid="stMetricDeltaIcon-Up"] {
    position: relative;
    left: 38%;
    transform: translateX(-50%);
}

[data-testid="stMetricDeltaIcon-Down"] {
    position: relative;
    left: 38%;
    transform: translateX(-50%);
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
trade_df['Deficit'] = trade_df['Exports'] - trade_df['Imports']

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
        name='Trade Deficit (Exports - Imports)',
        line=dict(color='yellow', width=2, dash='dash')
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



