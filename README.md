# pluto-jl-jupyter-conversion-cleaner

Thanks to [fonsp](https://github.com/fonsp) for [pluto-jl-jupyter-conversion](https://observablehq.com/@olivier_plas/pluto-jl-jupyter-conversion) 

This repository contains code to clean the Jupyter notebooks converted from Pluto.jl using: 
[pluto-jl-jupyter-conversion](https://observablehq.com/@olivier_plas/pluto-jl-jupyter-conversion) 

The original conversion from pluto to jupyter makes even the the markdown cells as code cells. This utility can be used to clean them.

## Steps

1. Use [pluto-jl-jupyter-conversion](https://observablehq.com/@olivier_plas/pluto-jl-jupyter-conversion) to convert the Pluto.jl notebook to a Ipython notebook.
2. After that:
```
git clone https://github.com/Abhiswain97/pluto-jl-jupyter-conversion-cleaner.git
cd pluto-jl-jupyter-conversion-cleaner
python convert.py --fname <your converted .ipynb file>
```
> Note: The converted file is saved as file-name-converted.ipynb

## Examples

Checkout [examples](https://github.com/Abhiswain97/pluto-jl-jupyter-conversion-cleaner/tree/main/examples) for the demo.
