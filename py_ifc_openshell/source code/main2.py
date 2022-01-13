import ifcopenshell
import functions

# # # INPUT
# path = input("(1) Đường dẫn file ifc (có đuôi file): ")#R:\BimESC\00-BIM STANDARD\PYTHON\ifcopenshell\21.006_Z01_P001_09_.ifc
# jsonpath = input("(2) Đường dẫn file Json để lưu dữ liệu IFC (có đuôi file): ")#R:\BimESC\00-BIM STANDARD\PYTHON\ifcopenshell\21.006_Z01_P001_09_.json

try:
    path = r"F:\_NGHIEN CUU\_Github\py_bim_file_manager\py_ifc_openshell\sample\ACR\production.ifc"
    if __name__ == "__main __":
        ifcElemAssembly = []
        ifc_file = ifcopenshell.open(path)
        products = ifc_file.by_type('IfcProduct')
        try:
            for product in products:
                if product.is_a() == 'IfcElementAssembly':            
                    ifcElemAssembly.append(product)
        except:
            pass
except KeyboardInterrupt:
    quit()


