import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Title and Description
st.title("U.S. Trade Data Dashboard")
st.subheader("Overview of Exports and Imports Over Time with Hot Colorscale")

# Load the data (use relative paths or adapt for deployment environment)
exports_df = pd.read_csv('exports_grouped.csv')
imports_df = pd.read_csv('imports_grouped.csv')

# Group by year and sum values to get total exports and imports for each year
exports_per_year = exports_df.groupby('year')['value'].sum().reset_index()
imports_per_year = imports_df.groupby('year')['value'].sum().reset_index()

# Merging the exports and imports data on 'year' for easier plotting
trade_df = exports_per_year.rename(columns={'value': 'Exports'}).merge(
    imports_per_year.rename(columns={'value': 'Imports'}),
    on='year'
)

# Plotting with Plotly and applying a warm color theme
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

# Update layout for title and labels
fig.update_layout(
    title='U.S. Exports and Imports Over the Years',
    xaxis_title='Year',
    yaxis_title='Trade Value',
    template='plotly_dark'
)

# Display the line chart in Streamlit
st.plotly_chart(fig)
