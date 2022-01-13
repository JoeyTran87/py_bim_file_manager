import ifcopenshell
import functions

# # # INPUT
path = input("(1) Đường dẫn file ifc (có đuôi file): ")#R:\BimESC\00-BIM STANDARD\PYTHON\ifcopenshell\21.006_Z01_P001_09_.ifc
jsonpath = input("(2) Đường dẫn file Json để lưu dữ liệu IFC (có đuôi file): ")#R:\BimESC\00-BIM STANDARD\PYTHON\ifcopenshell\21.006_Z01_P001_09_.json

try:
    if __name__ == "__main __":
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
except KeyboardInterrupt:
    quit()


