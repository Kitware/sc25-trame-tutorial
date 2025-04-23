# From remote rendering to local?

In this hands on session, we will expand the previous solution and run it using different modality. 
- remote rendering (what we've done)
- local rendering using vtk.js
- local rendering using VTK.wasm

> [!WARNING]
> For WASM, you will need to install __trame-vtklocal__
> ```bash
> uv pip install trame-vtklocal
> ```


## Option 1 (repo)

```bash
python ./code/04-visualization-3d/04-vtk-trame-remote.py
python ./code/04-visualization-3d/04-vtk-trame-local-js.py
python ./code/04-visualization-3d/04-vtk-trame-local-wasm.py
```

## Option 2 (copy/paste)

### Create file with content

Create the files and paste their content below into it.

::: code-group

<<<< ../../../../../code/04-visualization-3d/04-vtk-trame-local-js.diff
<<<< ../../../../../code/04-visualization-3d/04-vtk-trame-local-wasm.diff
<<<< ../../../../../code/04-visualization-3d/04-vtk-trame-remote.py
<<<< ../../../../../code/04-visualization-3d/04-vtk-trame-local-js.py
<<<< ../../../../../code/04-visualization-3d/04-vtk-trame-local-wasm.py

:::

### Run example

```bash
python 04-vtk-trame-remote.py
python 04-vtk-trame-local-js.py
python 04-vtk-trame-local-wasm.py
```
