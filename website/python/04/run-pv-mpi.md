# Running a ParaView MPI visualization

When using the downloaded version of ParaView, you will need to use the __mpiexec__ from the ParaView bundle.


::: code-group


```bash [Install extra dependencies]
# Activate venv 
source .pv-venv/bin/activate

# Install dependencies
uv pip install paraview-trame-components
```


<<< ../../../code/04-visualization-3d/06-paraview-mpi.py [Code]

```python [Run]
# shortcut to pvbatch and mpiexec
export MPI=/Applications/ParaView-5.13.3.app/Contents/bin/mpiexec
export PVBATCH=/Applications/ParaView-5.13.3.app/Contents/bin/pvbatch

# Run from repo
$MPI -n 4 $PVBATCH --venv .pv-venv ./code/04-visualization-3d/06-paraview-mpi.py
```

::: 

## Result

![](/python/04/pv-trame-mpi.png)