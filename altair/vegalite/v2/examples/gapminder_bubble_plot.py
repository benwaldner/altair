"""
Gapminder Bubble Plot
=====================
This example shows how to make a bubble plot showing the correlation between
health and income for 187 countries in the world (modified from an example
in Lisa Charlotte Rost's blog post ('One Chart, Twelve Charting Libraries')[http://lisacharlotterost.github.io/2016/05/17/one-chart-code/)].
"""
# category: scatter plots
import altair as alt


gapminder = alt.datasets.gapminder_health_income.url

alt.Chart(gapminder).mark_circle().encode(
    alt.X('income:Q', scale=alt.Scale(type='log')),
    alt.Y('health:Q', scale=alt.Scale(zero=False)),
    size='population:Q'
)
