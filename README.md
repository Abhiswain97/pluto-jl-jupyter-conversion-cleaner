# pluto-jl-jupyter-conversion-cleaner

<p align="center">
  <img src="plutojl_fastpages.jpg" height="" width="400">
</p>

_I also have written blogs to accompany this:_

- **medium version: [Pluto.jl + fastpages](https://abhi08as-as.medium.com/pluto-jl-fastpages-9d698c013b3a)**
- **my blog: [Pluto.jl + fastpages](https://abhishekswain.me/blog%20post/fastai/fastpages/2021/03/14/pluto-to-Jupyter-cleaned.html)**

Thanks to [fonsp](https://github.com/fonsp) for [pluto-jl-jupyter-conversion](https://observablehq.com/@olivier_plas/pluto-jl-jupyter-conversion)

This repository contains code to clean the Jupyter notebooks converted from Pluto.jl using:
[pluto-jl-jupyter-conversion](https://observablehq.com/@olivier_plas/pluto-jl-jupyter-conversion)

The original conversion from pluto to jupyter makes even the the markdown cells as code cells. This utility can be used to clean them.

## Steps

1. Use [pluto-jl-jupyter-conversion](https://observablehq.com/@olivier_plas/pluto-jl-jupyter-conversion) to convert the Pluto.jl notebook to a Ipython notebook.

2. Clone repo:
   ```
   git clone https://github.com/Abhiswain97/pluto-jl-jupyter-conversion-cleaner.git
   ```
3. Install all the requirements:

   For windows: `run.bat` <br>
   For Linux: `sh run.sh`
   
4. Use it:
    
   ```
   cd pluto-jl-jupyter-conversion-cleaner
   python run cleaner.py --path <your .ipynb file path>
   ```

## Help:

    python cleaner.py --help

> Note: The converted file is saved as file-name-cleaned.ipynb

## Examples

Checkout [examples](https://github.com/Abhiswain97/pluto-jl-jupyter-conversion-cleaner/tree/main/examples) for the demo. <br>
The converted and cleaned file in the example is also made into a blog post using fastpages, check it out [Logistic regression with a neural network mindset](https://abhishekswain.me/machine%20learning/maths/2020/07/28/Logistic_regression-Copy1.html)
