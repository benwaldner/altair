"""
Trellis Area Chart
------------------
This example shows small multiples of an area chart.
"""
# category: area charts
import altair as alt


iowa = alt.datasets.iowa_electricity()

alt.Chart(iowa).mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N",
    row="source:N"
)
