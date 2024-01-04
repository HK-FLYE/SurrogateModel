### Test nodal series functions 

import vtk
import os
import argparse
from ansys.mapdl import reader as pymapdl_reader

def main (infilename):
    filename = os.path.basename(infilename)
    result = pymapdl_reader.read_binary(filename)
    print(result.available_results)
    node_number = result.mesh.nnum
    nnum, nodal_stress = result.nodal_stress(0)
    print(nnum)
    print(nodal_stress)
    # print(edata)
    # print(enode)

if __name__=="__main__":
    program_args = argparse.ArgumentParser(description='Fit Node Value')
    program_args.add_argument('-i', '--inputfile', required=True, help='Input file')


    args = program_args.parse_args()

    if args.inputfile:
        infilename = args.inputfile

    main(infilename)
    print("Done")
    input("Press Enter to continue...")
    exit()

