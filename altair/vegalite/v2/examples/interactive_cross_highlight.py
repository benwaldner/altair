"""
Interactive Chart with Cross-Highlight
======================================
This example shows an interactive chart where selections in one portion of
the chart affect what is shown in other panels. Click on the bar chart to
see a detail of the distribution in the upper panel.
"""
# category: interactive charts
import altair as alt


pts = alt.selection(type="single", encodings=['x'])

rect = alt.Chart(alt.datasets.movies.url).mark_rect().encode(
    alt.X('IMDB_Rating:Q', bin=True),
    alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
    alt.Color('count()',
        scale=alt.Scale(scheme='greenblue'),
        legend=alt.Legend(title='Total Records')
    )
)

circ = rect.mark_point().encode(
    alt.ColorValue('grey'),
    alt.Size('count()',
        legend=alt.Legend(title='Records in Selection')
    )
).transform_filter(
    pts
)

bar = alt.Chart(alt.datasets.movies.url).mark_bar().encode(
    x='Major_Genre:N',
    y='count()',
    color=alt.condition(pts, alt.ColorValue("steelblue"), alt.ColorValue("grey"))
).properties(
    selection=pts,
    width=550,
    height=200
)

alt.vconcat(
    rect + circ,
    bar
).resolve_legend(
    color="independent",
    size="independent"
)
