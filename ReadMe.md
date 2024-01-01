## Python Environment

Build python environment with commond:

`conda create --prefix="your env directory with name" -f ……\……\SurrogateEnvironment.yaml`

## STL to obj

Get **surface mesh**\(not volume mesh\) from Ansys workbench in form of STL. \(Referring to this website [ANSYS Workbench export deformed goemetry](https://zhuanlan.zhihu.com/p/385490698#:~:text=%E5%9C%A8%E5%B7%A6%E4%BE%A7%E6%A8%A1%E5%9E%8B%E6%A0%91%E3%80%90Solution%E3%80%91%E4%B8%8B%E9%9D%A2%E6%89%BE%E5%88%B0%E3%80%90Total%20Deformation%E3%80%91%EF%BC%8C%E5%8F%B3%E9%94%AE%E9%80%89%E6%8B%A9%E3%80%90Export...%E3%80%91%3E%E3%80%90STL%20File%E3%80%91%EF%BC%8C%E5%B0%86%E5%8F%98%E5%BD%A2%E5%90%8E%E7%9A%84%E5%87%A0%E4%BD%95%E5%AF%BC%E5%87%BA%E4%B8%BA%20STL%20%E6%96%87%E4%BB%B6%E3%80%82,%E7%94%A8%20SpaceClaim%20%E6%89%93%E5%BC%80%E5%88%9A%E6%89%8D%E4%BF%9D%E5%AD%98%E7%9A%84%20STL%20%E6%96%87%E4%BB%B6%EF%BC%8C%E5%8F%AF%E4%BB%A5%E7%9C%8B%E5%88%B0%E5%8F%98%E5%BD%A2%E5%90%8E%E7%9A%84%E5%87%A0%E4%BD%95%EF%BC%8C%E4%B8%8D%E8%BF%87%E6%98%AF%E7%89%87%E4%BD%93%E3%80%82%20%E5%B0%86%E7%89%87%E4%BD%93%E8%BD%AC%E5%8C%96%E4%B8%BA%E5%AE%9E%E4%BD%93%EF%BC%8C%E5%B9%B6%E8%BF%9B%E4%B8%80%E6%AD%A5%E4%BF%AE%E8%A1%A5%E5%AE%8C%E5%96%84%EF%BC%8C%E5%BE%97%E5%88%B0%E6%9C%80%E7%BB%88%E7%9A%84%E5%8F%98%E5%BD%A2%E5%90%8E%E5%87%A0%E4%BD%95%E4%BD%93%E3%80%82)\)

Use bin_to_ascii_stl_converter.py to convert a binary stl file into an ASCII stl file.  
Then use stl_to_obj.py to convert stl file into obj file.  

## ANSYS Result Reader

Find the simulation result file in ……\\*projectName*\_files\dp0\SYS-1\MECH, it's always named as file.rst.  
Use CDBtoOBJ.py to extract structural result and physical informations. \(Referring to this website [Read ANSYS result file through python](https://reader.docs.pyansys.com/version/stable/api/archive.html)\)
The Structural information is stored in file.cdb. Add a (APDL)command to generate the cdb file (referring to this website [ANSYS Mechanical pre/after operation](https://zhuanlan.zhihu.com/p/428214118)) 
```
/prep7
cdwrite,all
fini
/SOLU
ALLSEL
```
Use RSTtoOBJ.py in an environment with ANSYS21R1 or higher installed. 
Through DPF-post module, load simulation of rst file. (referring to this website [pymapdl](https://github.com/ansys/pymapdl/tree/6b3d6b1c27e295a709b8b0de41df1a9dccdfedff)) 
