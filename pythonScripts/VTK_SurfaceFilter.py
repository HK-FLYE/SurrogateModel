import vtk
import os
import argparse

def main(infilename, outfilename):
    filename = os.path.basename(infilename)
    print(filename)
    reader = vtk.vtkOBJReader()
    reader.SetFileName(infilename)
    reader.Update()
    mesh = reader.GetOutput()
    surface_filter = vtk.vtkDataSetSurfaceFilter()
    surface_filter.SetInputData(mesh)
    surface_filter.Update()
    surface = surface_filter.GetOutput()
    writer = vtk.vtkOBJWriter()
    writer.SetInputData(surface)
    writer.SetFileName(outfilename)
    writer.Write()

if __name__ == '__main__':
    program_args = argparse.ArgumentParser(description='Surface Filter')
    program_args.add_argument('-i', '--inputfile' , required=True,  help="Input file path")
    program_args.add_argument('-o', '--outputfile', required=False, help="Output file path")
    args = program_args.parse_args()

    if args.inputfile:
        infilename = args.inputfile
    if args.outputfile:
        outfilename = args.outputfile
    else:
        outfilename = infilename.replace(".obj", "_surface.obj")

    main(infilename, outfilename)
    print("Done")
    input("Press Enter to continue...")
    exit()