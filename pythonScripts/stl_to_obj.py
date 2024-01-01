import meshio
import os
import argparse

def read_mesh(mesh_path):
    mesh = meshio.read(mesh_path, file_format='stl')
    return mesh

def main(mesh_path, output_path):
    filename = os.path.basename(mesh_path)
    print(filename)
    MeshSTL = read_mesh(mesh_path)
    MeshSTL.write(output_path)

if __name__ == '__main__':
    program_args = argparse.ArgumentParser(description='Bin to ASCII STL Converter')
    program_args.add_argument('-i', '--inputfile' , required=True,  help="Input file path")
    program_args.add_argument('-o', '--outputfile', required=False, help="Output file path")
    args = program_args.parse_args()

    if args.inputfile:
        infilename = args.inputfile
        
    if args.outputfile:
        outfilename = args.outputfile
    else:
        outfilename = os.path.join(os.path.dirname(infilename), f"ASCII-{os.path.basename(infilename)}")
    
    os.makedirs(os.path.dirname(outfilename), exist_ok=True)
    main(infilename, outfilename)
