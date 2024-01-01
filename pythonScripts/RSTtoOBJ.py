import vtk
import os
import argparse
# from ansys.mapdl import reader as pymapdl_reader
from ansys.dpf import post

def main(infilename, outfilename, surface_filt):
    filename = os.path.basename(infilename)
    print(filename)
    sim = post.load_solution(filename)
    print(sim)
    writer = vtk.vtkOBJWriter()
    writer.SetFileName(outfilename)
    sim.plot_nodal_solution(0)
    mesh = sim.mesh
    if surface_filt:
        surface_filter = vtk.vtkDataSetSurfaceFilter()
        surface_filter.SetInputData(mesh)
        surface_filter.Update()
        mesh = surface_filter.GetOutput()
        writer.SetInputData(mesh)
    else:
        writer.SetInputData(mesh)
    writer.Write()

if __name__ == '__main__':
    program_args = argparse.ArgumentParser(description='RST to OBJ')
    program_args.add_argument('-i', '--inputfile' , required=True,  help="Input file path")
    program_args.add_argument('-o', '--outputfile', required=False, help="Output file path")
    program_args.add_argument('-s', '--surface_filter', required=False, help="Surface Filter")
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

