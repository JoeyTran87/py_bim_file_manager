import ifcopenshell
import functions

# # # INPUT
path = input("(1) Path of IFC file inclue file name with extension: ")#R:\BimESC\00-BIM STANDARD\PYTHON\ifcopenshell\21.006_Z01_P001_09_.ifc
jsonpath = input("(2) Json File Path inclue file name with extension: ")#R:\BimESC\00-BIM STANDARD\PYTHON\ifcopenshell\21.006_Z01_P001_09_.json


# # # EXECUTE
ifcElemAssembly = []
# try:
ifc_file = ifcopenshell.open(path)
products = ifc_file.by_type('IfcProduct')
try:
    for product in products:
        if product.is_a() == 'IfcElementAssembly':            
            ifcElemAssembly.append(product)
except:
    pass
# print("Count of IfcElementAssembly: ",len(ifcElemAssembly))

# print(functions.extractIFC(ifcElemAssembly[2:5]))

j = functions.extractIFC2(jsonpath,ifcElemAssembly)

print("OK DONE")


