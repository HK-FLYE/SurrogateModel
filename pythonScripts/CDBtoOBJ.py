import vtk
import os
import argparse
from ansys.mapdl import reader as pymapdl_reader
import pyvista as pv
import pandas as pd
import math
from ansys.mapdl.core import launch_mapdl
# import pyansys

def replace_file_extension(file_path, new_extension):
    file_name, _ = os.path.splitext(file_path)
    return f"{file_name}.{new_extension}"

def calculateAbsoluteDisplacement(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)

def calculateEquivalentStress(stress_dis:list):
    x, y, z, xy, yz, xz = stress_dis
    stress_eq = math.sqrt(x ** 2 + y ** 2 + z ** 2 - x * y - x * z - y * z + 3 * (xy ** 2 + yz ** 2 + xz ** 2)) 
    return stress_eq

def main(infilename, outfilename, surface_filt):
    RSTextension = "rst"
    filename = os.path.basename(infilename)
    RSTfilename = replace_file_extension(filename, RSTextension)
    print(RSTfilename)
    print(filename)
    archive = pymapdl_reader.Archive(filename)
    result = pymapdl_reader.read_binary(RSTfilename)
    print(result)
    print(len(result.mesh.nnum))
    result.plot_nodal_displacement(99)

    '''
    Store VTK file and use pyvista to read unstructured grid
    '''
    grid = archive.grid
    newExtention = "vtk"
    tmpfilename = replace_file_extension(outfilename, newExtention)
    grid.save(tmpfilename)
    mesh = pv.read(tmpfilename)
    fullMesh_points = mesh.GetPoints()

    '''
    export OBJ file
    '''
    writer = vtk.vtkOBJWriter()
    plotter = pv.Plotter()
    plotter.add_mesh(mesh)
    plotter.export_obj(outfilename)

    '''
     Get OBJ information, PolyData
    '''
    reader = vtk.vtkOBJReader()
    reader.SetFileName(outfilename)
    reader.Update()
    mesh = reader.GetOutput()
    mesh_points = mesh.GetPoints()
    num_points = mesh_points.GetNumberOfPoints()

    '''
    loop for extracting simData of each step
    
    # for i in range(result.n_results):
    #    nnum, nodal_stress = result.nodal_stress(i)
    #    …………
    '''
    data_type = 'NSL'
    nnum, data = result.nodal_displacement(20) # change step number(first argument) and datatype(second argument)
    # node_values = [0] * (len(result.mesh.nnum) + 1)
    # for i in range(len(enode)):
    #     for j in range(len(enode[i])):
    #         if edata[i] is not None:
    #             node_values[enode[i][j]] = edata[i][7 * j + 6]
    #         print(str(enode[i][j]) + ' ' + str(node_values[enode[i][j]]))
    # print(node_values)
    
    file_path = os.path.basename(r".\\" + data_type + ".txt")
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(fullMesh_points)
    locator = vtk.vtkPointLocator()
    locator.SetDataSet(polydata)
    locator.BuildLocator()
    
    with open(file_path, 'w') as file:
        for i in range(num_points):
            point = mesh_points.GetPoint(i)
            closestPointId = locator.FindClosestPoint(point)
            nodal_value = calculateAbsoluteDisplacement(data[closestPointId])

            file.write(str(i + 1) + "\t" + str(nodal_value) + "\n")

    # print(num_points)
    # for i in range(num_points):
    #     print(mesh_points.GetPoint(i))
    
    ### Use VTK surface filter
    # if surface_filt:
    #     surface_filter = vtk.vtkDataSetSurfaceFilter()
    #     surface_filter.SetInputData(mesh)
    #     surface_filter.Update()
    #     mesh = surface_filter.GetOutput()
    #     writer.SetInputData(mesh)
    # else:
    #     writer.SetInputData(mesh)
    # writer.Write()
    
if __name__ == '__main__':
    program_args = argparse.ArgumentParser(description='CDB to OBJ')
    program_args.add_argument('-i', '--inputfile' , required=True,  help="Input file path")
    program_args.add_argument('-o', '--outputfile', required=False, help="Output file path")
    program_args.add_argument('-s', '--surface_filter', action='store_true', default=False, required=False, help="Surface Filter")
    args = program_args.parse_args()

    if args.inputfile:
        infilename = args.inputfile
    if args.outputfile:
        outfilename = args.outputfile
    if args.surface_filter:
        surface_filt = True
    else:
        surface_filt = False

    main(infilename, outfilename, surface_filt)
    print("Done")
    input("Press Enter to continue...")
    exit()