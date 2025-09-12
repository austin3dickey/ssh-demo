# Data from https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
# hosted by Ursa Labs (see https://ursalabs.org/arrow-r-nightly/articles/dataset.html)

import ibis
from ibis import _
from plotnine import ggplot, aes, geom_bar, scale_x_continuous, ggtitle

# Set up any backend
con = ibis.duckdb.connect()

# Load an ibis table (this doesn't actually read the data yet)
t = con.read_parquet(
    "s3://ursa-labs-taxi-data/**",
    table_name="nyctaxi",
    union_by_name=True,
)

t
len(t.columns)  # 22 columns

# Way too big for laptops if represented in pandas! (Do you have 400 GB of RAM?)
t.count().execute()  # 1_547_741_381 rows

# Find the mean tip percentage by number of passengers, among trips costing more than $100.
analysis = (
    t.filter(
        [
            _.pickup_at < "2009-02-01",
            _.total_amount > 100,
            _.passenger_count > 0,
        ]
    )
    .select(_.tip_amount, _.total_amount, _.passenger_count)
    .mutate(tip_pct=100 * _.tip_amount / _.total_amount)
    .group_by(_.passenger_count)
    .agg(mean_tip_pct=_.tip_pct.mean(), n=_.count())
    .mutate(log_count=_.n.log())
)

# Plot it.
(
    ggplot(data=analysis, mapping=aes(x="passenger_count", y="mean_tip_pct", fill="log_count"))
    + geom_bar(stat="identity")
    + scale_x_continuous(breaks=range(15))
    + ggtitle("Tip % by passenger count (for expensive trips)")
)
