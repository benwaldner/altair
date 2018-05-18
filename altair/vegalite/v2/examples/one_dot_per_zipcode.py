"""
One Dot Per Zipcode
-----------------------
This example shows a geographical plot with one dot per zipcode.
"""
# category: maps
import altair as alt
from altair.expr import datum, substring


zipcodes = alt.datasets.zipcodes.url

alt.Chart(zipcodes).mark_circle(size=3).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color='digit:N'
).project(
    type='albersUsa'
).properties(
    width=650,
    height=400
).transform_calculate(
    "digit", substring(datum.zip_code, 0, 1)
)
