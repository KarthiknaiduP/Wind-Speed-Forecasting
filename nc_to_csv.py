import xarray as xr
import pandas as pd

# Open your NetCDF file
ds = xr.open_dataset('2016_THUWAL_data.nc')

# Convert to pandas DataFrame
df = ds.to_dataframe().reset_index()

# Optional: If lon/lat are always the same, drop duplicates
df = df.drop_duplicates(subset=['time'])

# Split datetime if needed
df['date'] = df['time'].dt.date
df['hour'] = df['time'].dt.hour

# Reorder columns as you like
cols = ['date', 'hour', 'lon', 'lat'] + [v for v in ds.data_vars]
df = df[cols]

# Save to CSV
df.to_csv('2016_THUWAL_data_wide.csv', index=False)

