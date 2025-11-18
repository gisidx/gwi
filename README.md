# Geospatial Wheels Index

This is a `pip`-compatible package index for releases in cgohlke's [geospatial-wheels](https://github.com/cgohlke/geospatial-wheels),
which provides precompiled binary wheels for common geospatial Python libraries on Windows.

Simply use `pip install` with the `--index` flag, for example to install `GDAL`:

```shell
pip install --index https://gisidx.github.io/gwi gdal
```

Python 3.10 through 3.14 is supported on `win_arm64`, `win_amd64`, and `win32` architectures. 
Packages available on this index: 

- basemap
- Cartopy
- cftime
- Fiona
- GDAL
- h5py
- netCDF4
- pygeos
- pyogrio
- pyproj
- rasterio
- Rtree
- shapely

To install all packages, first install dependencies from PyPI:

```shell
pip install affine attrs certifi click click-plugins cligj basemap_data matplotlib numpy pyshp
```

Then install all packages from `cgohlke/geospatial-wheels` via this package index:

```shell
pip install --index https://gisidx.github.io/gwi basemap cartopy cftime fiona gdal h5py netcdf4 pygeos pyogrio pyproj rasterio rtree shapely
```

### Notes

- The index is hosted on this repository's GitHub Pages site: https://corbel-spatial.github.io/geospatial-wheels-index/

- For convenience, a [forked repository](https://github.com/gisidx/gwi) provides this shorter index URL: https://gisidx.github.io/gwi

- The index does not contain any actual wheel files; all links point to the GitHub-hosted assets in [releases](https://github.com/cgohlke/geospatial-wheels/releases)
maintained in the `cgohlke/geospatial-wheels` repository.

- The index automatically syncs with `cgohlke/geospatial-wheels` every Tuesday at 21:00 UTC. Please open an [Issue](https://github.com/corbel-spatial/geospatial-wheels-index/issues) if it's out of date.

- Like the `geospatial-wheels` source, this index is provided "as is" and without warranty of any kind. 

- All aspects of this index are open source and hosted in this repository.
Thus it is fully auditable and you are welcome to fork it to create your own version.
Questions and suggestions are welcome in the [Issues](https://github.com/corbel-spatial/geospatial-wheels-index/issues) section.
