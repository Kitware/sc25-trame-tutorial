import ptc
from paraview import simple

sphere = simple.Sphere()
rep = simple.Show(sphere)
view = simple.Render()

simple.ColorBy(rep, ("POINTS", "vtkProcessId"))

rep.RescaleTransferFunctionToDataRange(True, False)
rep.SetScalarBarVisibility(view, True)

web_app = ptc.Viewer()
web_app.start()