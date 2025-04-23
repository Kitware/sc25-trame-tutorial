# Running a ParaView visualization

With ParaView things are different as ParaView is __not__ available via `pip install`. Technically it is available via conda and can be used as such, but for this hands-on we will be using ParaView downloaded from [Kitware Website](https://www.paraview.org/download/).

## Steps needed

1. Download ParaView 5.13.3 or newer for your system.
2. Create a new virtual environment compatible with the downloaded ParaView.
3. Install the trame pieces that you need.
4. Run pvpython with the `--venv` argument so the trame import could be resolved.

## Exact command lines and steps

Based on which version of ParaView you've downloaded you will have to create a virtual environment with either __python 3.10 or 3.12__.



::: code-group

```bash [Create venv]
uv venv -p 3.10 .pv-venv
```

```bash [Install dependencies]
# Activate venv 
source .pv-venv/bin/activate

# Install dependencies
uv pip install trame trame-vuetify trame-vtk
```

<<< ../../../code/04-visualization-3d/05-paraview-cone.py [Code]


```python [Run]
# shortcut to pvpython
export PVPYTHON=/Applications/ParaView-5.13.3.app/Contents/bin/pvpython 

# Run from repo
$PVPYTHON --venv .pv-venv ./code/04-visualization-3d/05-paraview-cone.py
```

::: 

## Result


![](/python/04/pv-trame.png)