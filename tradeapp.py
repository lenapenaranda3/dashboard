
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Title and Description
st.title("U.S. Trade Data Dashboard")
st.subheader("Overview of Exports and Imports Over Time")

# Load the data
exports_df = pd.read_csv('exports_grouped.csv')
imports_df = pd.read_csv('imports_grouped.csv')

# Assuming both files have a 'Year' and 'Trade Value' or similar column names; adjust if needed
# Merging data on the 'Year' column to create a combined DataFrame
trade_df = exports_df[['Year', 'Trade Value']].rename(columns={'Trade Value': 'Exports'}).merge(
    imports_df[['Year', 'Trade Value']].rename(columns={'Trade Value': 'Imports'}),
    on='Year'
)

# Plotting with Plotly and applying "Hot" colorscale
fig = go.Figure()

# Add trace for Exports
fig.add_trace(
    go.Scatter(
        x=trade_df['Year'],
        y=trade_df['Exports'],
        mode='lines+markers',
        name='Exports',
        line=dict(color='red', width=2)
    )
)

# Add trace for Imports
fig.add_trace(
    go.Scatter(
        x=trade_df['Year'],
        y=trade_df['Imports'],
        mode='lines+markers',
        name='Imports',
        line=dict(color='orange', width=2)
    )
)

# Update layout for title and labels
fig.update_layout(
    title='U.S. Exports and Imports Over the Years',
    xaxis_title='Year',
    yaxis_title='Trade Value',
    template='plotly_dark'
)

# Display the line chart in Streamlit
st.plotly_chart(fig)

