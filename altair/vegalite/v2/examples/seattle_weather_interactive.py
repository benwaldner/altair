"""
Seattle Weather Interactive
===========================
This chart provides an interactive exploration of Seattle weather over the
course of the year. It includes a one-axis brush selection to easily
see the distribution of weather types in a particular date range.
"""
# category: interactive charts
import altair as alt


scale = alt.Scale(domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
                  range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd'])
color = alt.Color('weather:N', scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_multi(encodings=['color'])

# Top panel is scatter plot of temperature vs time
points = alt.Chart().mark_point().encode(
    alt.X('date:T', timeUnit='monthdate', axis=alt.Axis(title='Date')),
    alt.Y('temp_max:Q',
        axis=alt.Axis(title='Maximum Daily Temperature (C)'),
        scale=alt.Scale(domain=[-5, 40])
    ),
    color=alt.condition(brush, color, alt.value('lightgray')),
    size=alt.Size('precipitation:Q', scale=alt.Scale(range=[5, 200]))
).properties(
    width=600,
    height=300
).add_selection(
    brush
).transform_filter(
    click
)

# Bottom panel is a bar chart of weather type
bars = alt.Chart().mark_bar().encode(
    x='count()',
    y='weather:N',
    color=alt.condition(click, color, alt.value('lightgray')),
).transform_filter(
    brush
).properties(
    width=600,
).add_selection(
    click
)

alt.vconcat(points, bars,
    data=alt.datasets.seattle_weather.url,
    title="Seattle Weather: 2012-2015"
)
