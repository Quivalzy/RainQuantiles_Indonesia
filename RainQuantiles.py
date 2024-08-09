import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy as crt

# Akses data tableA1 dan menampilkan 5 entri pertama
meteoData = pd.read_csv('tableA1.txt', delimiter='\t', header=None, names=['date', 'pr1', 'tx1', 'tn1', 'pr2', 'tx2', 'tn2'])
meteoData.head()
dataSmry = meteoData.describe()
dataMean = meteoData.mean()
dataMedian = meteoData.median()
dataStd = meteoData.std()
dataVar = meteoData.var()
dataQuan1 = meteoData.quantile(0.25)
dataQuan3 = meteoData.quantile(0.75)
dataInterQRange = dataQuan3 - dataQuan1
dataSkewn = meteoData.skew()
dataKurt = meteoData.kurt()
dataMinV = meteoData.min()
dataMaxV = meteoData.max()
dataTriMean = (dataQuan1 + 2*dataMedian + dataQuan3)/4

#Data Spasio-Temporal
precipData = xr.open_dataarray('MSWEP_MON_INA_197902-202011.nc')
prClimVar = precipData.groupby('time.season').var()
prClimMin = precipData.groupby('time.season').min()
prClimMax = precipData.groupby('time.season').max()
prClimQ1 = precipData.groupby('time.season').quantile(0.25)
prClimQ3 = precipData.groupby('time.season').quantile(0.75) 

# Plot Variansi Curah Hujan
season = ['MAM', 'JJA', 'SON', 'DJF']
for item in season:
    prj = crt.crs.PlateCarree()
    fgr = plt.figure(figsize=(16,8))
    axs = plt.axes(projection = prj)
    prClimVar.sel(season = item).plot(ax = axs, transform = prj, cmap = 'jet') # ubah variabel dengan yang diinginkan
    axs.set_title(f'Variansi Curah Hujan di Indonesia pada Musim {item}' , fontsize = 20, fontweight = 'bold')
    axs.coastlines()
    axs.gridlines(draw_labels = True)
    plt.savefig(f'var_{item}.png')
    plt.clf()

    prj = crt.crs.PlateCarree()
    fgr = plt.figure(figsize=(16,8))
    axs = plt.axes(projection = prj)
    prClimMin.sel(season = item).plot(ax = axs, transform = prj, cmap = 'jet') # ubah variabel dengan yang diinginkan
    axs.set_title(f'Curah Hujan Minimum di Indonesia pada Musim {item}' , fontsize = 20, fontweight = 'bold')
    axs.coastlines()
    axs.gridlines(draw_labels = True)
    plt.savefig(f'min_{item}.png')
    plt.clf()

    prj = crt.crs.PlateCarree()
    fgr = plt.figure(figsize=(16,8))
    axs = plt.axes(projection = prj)
    prClimMax.sel(season = item).plot(ax = axs, transform = prj, cmap = 'jet') # ubah variabel dengan yang diinginkan
    axs.set_title(f'Curah Hujan Maksimum di Indonesia pada Musim {item}' , fontsize = 20, fontweight = 'bold')
    axs.coastlines()
    axs.gridlines(draw_labels = True)
    plt.savefig(f'max_{item}.png')
    plt.clf()

    prj = crt.crs.PlateCarree()
    fgr = plt.figure(figsize=(16,8))
    axs = plt.axes(projection = prj)
    prClimQ1.sel(season = item).plot(ax = axs, transform = prj, cmap = 'jet') # ubah variabel dengan yang diinginkan
    axs.set_title(f'Kuartil 1 Curah Hujan di Indonesia pada Musim {item}' , fontsize = 20, fontweight = 'bold')
    axs.coastlines()
    axs.gridlines(draw_labels = True)
    plt.savefig(f'q1_{item}.png')
    plt.clf()

    prj = crt.crs.PlateCarree()
    fgr = plt.figure(figsize=(16,8))
    axs = plt.axes(projection = prj)
    prClimQ3.sel(season = item).plot(ax = axs, transform = prj, cmap = 'jet') # ubah variabel dengan yang diinginkan
    axs.set_title(f'Kuartil 3 Curah Hujan di Indonesia pada Musim {item}' , fontsize = 20, fontweight = 'bold')
    axs.coastlines()
    axs.gridlines(draw_labels = True)
    plt.savefig(f'q3_{item}.png')
    plt.clf()