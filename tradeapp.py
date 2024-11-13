import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Title and Description
st.title("U.S. Trade Data Dashboard")
st.subheader("Overview of Exports and Imports Over Time with Hot Colorscale")

# Sample Data - Replace with your actual dataset or load it from a CSV file
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],  # Replace with actual years
    'Exports': [1500, 1600, 1550, 1650, 1700],  # Replace with actual export values
    'Imports': [1800, 1750, 1700, 1850, 1900]  # Replace with actual import values
}
df = pd.DataFrame(data)

# Plotting with Plotly and applying "Hot" colorscale
fig = go.Figure()

# Add trace for Exports
fig.add_trace(
    go.Scatter(
        x=df['Year'],
        y=df['Exports'],
        mode='lines+markers',
        name='Exports',
        line=dict(color='hot', width=2)
    )
)

# Add trace for Imports
fig.add_trace(
    go.Scatter(
        x=df['Year'],
        y=df['Imports'],
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
