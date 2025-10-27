# Geospatial Wheels Index

This is a `pip`-compatible package index for releases in cgohlke's [geospatial-wheels](https://github.com/cgohlke/geospatial-wheels),
which provides precompiled binary wheels for common geospatial Python libraries on Windows.

Simply use `pip install` with the `--index` flag, for example to install `GDAL`:

```shell
pip install --index https://tinyurl.com/gswhl gdal
```

Python 3.10 through 3.14 is supported on `win_arm64`, `win_amd64`, and `win32` architectures. 
The full list of available packages is: 

- basemap
- cartopy
- cftime
- fiona
- gdal
- h5py
- netcdf4
- pygeos
- pyogrio
- pyproj
- rasterio
- rtree
- shapely

### Notes

- The shortened URL https://tinyurl.com/gswhl resolves to the GitHub Pages site hosted by this repository: https://corbel-spatial.github.io/geospatial-wheels-index/

- This index does not contain any actual wheel files; all links point to the GitHub-hosted assets in [releases](https://github.com/cgohlke/geospatial-wheels/releases)
maintained in the `geospatial-wheels` repository.

- Like the `geospatial-wheels` source, this index is provided "as is" and without warranty of any kind. 

- All aspects of this index are open source and hosted in this repository.
Thus it is fully auditable and you are welcome to fork it to create your own version.
Questions and suggestions are welcome in the [Issues](https://github.com/corbel-spatial/geospatial-wheels-index/issues) section.
