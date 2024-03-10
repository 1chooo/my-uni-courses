# %%
import requests
import xarray as xr
import matplotlib.pyplot as plt

# %% [markdown]
# ### 1. Please demonstrate that you are able to use above code to produce profiles of temperature and salinity, respectively, with respect to pressure on your laptop computer;

# %%
# Specify the URL of the ARGO data file
# url = 'http://www.argodatamgt.org/Accessing-Data/Search-for-Data/Simple-Search?region=ETP&start_date=2020-11-01&end_date=2020-11-30&format=netCDF&qc_level=1'
# url='http://www.example.com/argo_data.nc'
url='https://data.nodc.noaa.gov/argo/gadr/data/aoml/5906017/nodc_5906017_prof.nc'

# Download the data using the requests library
response = requests.get(url)

# Open the data using xarray
ds = xr.open_dataset(response.content)
# Extract the temperature, salinity, and pressure data
temp = ds['temp']
salinity = ds['psal']
pressure = ds['pres']

fig, (ax1,ax2) = plt.subplots(1,2, sharey=True, figsize=(10,6))


# Create a plot of temperature and salinity vs. pressure
ax1.plot(temp, pressure, label='Temperature')
ax2.plot(salinity, pressure, label='Salinity')
#plt.plot(salinity, pressure, label='Salinity')

ax1.set_xlabel('Temperature (°C)')
ax2.set_xlabel('Salinity (PSU)')
ax1.set_ylabel('Pressure (dbar)')
plt.title('ARGO Data')

ax1.invert_yaxis()

#plt.legend()
#plt.show()

#plt.plot(salinity, pressure, label='Salinity')
#plt.xlabel('Salinity (PSU)')
#plt.ylabel('Pressure (dbar)')
plt.title('ARGO Data')
# plt.legend()
plt.savefig("./109601003.jpg")
plt.show()

# %%
print(ds)

# %%



