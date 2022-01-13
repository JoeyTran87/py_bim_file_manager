import ifcopenshell, json
import functions

path = "R:\\BimESC\\00-BIM STANDARD\\PYTHON\\ifcopenshell\\21.006_Z01_P001_09_.ifc"
ifc_file = ifcopenshell.open(path)
products = ifc_file.by_type('IfcProduct')

# print(dir(ifc_file))
"""['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add', 'by_guid', 'by_id', 'by_type', 'create_entity', 'from_string', 'get_inverse', 'remove', 'traverse', 'wrapped_data']"""

# print(dir(products[0]))
"""['CompositionType', 'ContainsElements', 'Decomposes', 'Description', 'GlobalId', 'HasAssignments', 'HasAssociations', 'IsDecomposedBy', 'IsDefinedBy', 'LandTitleNumber', 'LongName', 'Name', 'ObjectPlacement', 'ObjectType', 'OwnerHistory', 'RefElevation', 'RefLatitude', 'RefLongitude', 'ReferencedBy', 'ReferencesElements', 'Representation', 'ServicedBySystems', 'SiteAddress', '__class__', '__delattr__', 
'__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value']"""
#print(products[0].get_info())
"""{'id': 27, 'type': 'IfcSite', 'GlobalId': '1D_Ja3osn9cfVa$kSqEZba', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1616503644), 'Name': 'Undefined', 'Description': None, 'ObjectType': None, 
'ObjectPlacement': #26=IfcLocalPlacement($,#10), 'Representation': None, 'LongName': None, 'CompositionType': 'ELEMENT', 'RefLatitude': None, 'RefLongitude': None, 'RefElevation': 0.0, 'LandTitleNumber': None, 'SiteAddress': None}"""

ifcElemAssembly = []
for product in products:
    try:
        if product.is_a() == "IfcElementAssembly":
            ifcElemAssembly.append(product)
    except:
        pass
print("Count of IfcElementAssembly: ",len(ifcElemAssembly)) #9989
print(ifcElemAssembly[2:5])
#print(ifcElemAssembly[0].get_info())
"""{'id': 34, 'type': 'IfcElementAssembly', 'GlobalId': '1pIRrB3v93aR6Gydg1HXnq', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1616503644), 'Name': 'Steel Assembly', 'Description': None, 'ObjectType': None, 'ObjectPlacement': #33=IfcLocalPlacement(#31,#10), 'Representation': None, 'Tag': '01031904', 'AssemblyPlace': 'NOTDEFINED', 'PredefinedType': 'RIGID_FRAME'}"""
# print(dir(ifcElemAssembly[0]))
"""['AssemblyPlace', 'ConnectedFrom', 'ConnectedTo', 'ContainedInStructure', 'Decomposes', 'Description', 'FillsVoids', 'GlobalId', 'HasAssignments', 'HasAssociations', 'HasCoverings', 'HasOpenings', 'HasPorts', 'HasProjections', 'HasStructuralMember', 'IsConnectionRealization', 'IsDecomposedBy', 'IsDefinedBy', 'Name', 'ObjectPlacement', 'ObjectType', 'OwnerHistory', 'PredefinedType', 'ProvidesBoundaries', 'ReferencedBy', 'ReferencedInStructures', 'Representation', 'Tag', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value']"""
print(dir(ifcElemAssembly[0].get_info()))
# print(ifcElemAssembly[0].IsDefinedBy)
"""(#660413=IfcRelDefinesByProperties('2yUUodWb97ygOsJcjgmD4q',#5,$,$,(#34),#45), #660414=IfcRelDefinesByProperties('1WS24hKW96OgNLXEI7H$GW',#5,$,$,(#34),#53), #660415=IfcRelDefinesByProperties('11nQswDOb099tnHgTVLhOD',#5,$,$,(#34),#55))"""

for definition in ifcElemAssembly[0].IsDefinedBy:
    if definition.is_a() == 'IfcRelDefinesByProperties':
        # print (definition)
        """#660413=IfcRelDefinesByProperties('2yUUodWb97ygOsJcjgmD4q',#5,$,$,(#34),#45)
        #660414=IfcRelDefinesByProperties('1WS24hKW96OgNLXEI7H$GW',#5,$,$,(#34),#53)
        #660415=IfcRelDefinesByProperties('11nQswDOb099tnHgTVLhOD',#5,$,$,(#34),#55)"""
        # print (definition.get_info())
        """{'id': 660413, 'type': 'IfcRelDefinesByProperties', 'GlobalId': '2yUUodWb97ygOsJcjgmD4q', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1616503644), 'Name': None, 'Description': None, 'RelatedObjects': (#34=IfcElementAssembly('1pIRrB3v93aR6Gydg1HXnq',#5,'Steel Assembly',$,$,#33,$,'01031904',.NOTDEFINED.,.RIGID_FRAME.),), 'RelatingPropertyDefinition': #45=IfcPropertySet('0juQaczUT00AUohd65MM2E',#5,'Default',$,(#35,#36,#37,#38,#39,#40,#41,#42,#43,#44))}"""
        # print (dir(definition))
        """['Description', 'GlobalId', 'Name', 'OwnerHistory', 'RelatedObjects', 'RelatingPropertyDefinition', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value']"""
        # print (definition.RelatingPropertyDefinition)
        """#45=IfcPropertySet('0juQaczUT00AUohd65MM2E',#5,'Default',$,(#35,#36,#37,#38,#39,#40,#41,#42,#43,#44))
        #53=IfcPropertySet('1FceZr3bf43f4MuV9Ob8dE',#5,'Tekla Assembly','Assembly Properties',(#46,#47,#48,#49,#50,#51,#52))
        #55=IfcElementQuantity('0F6RxOR6zD1fwTQ$WbQNwB',#5,'BaseQuantities',$,$,(#54)"""
        # print (definition.RelatingPropertyDefinition.get_info())
        """{'id': 45, 'type': 'IfcPropertySet', 'GlobalId': '0juQaczUT00AUohd65MM2E', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1616503644), 'Name': 'Default', 'Description': None, 'HasProperties': (#35=IfcPropertySingleValue('MATERIAL_TYPE',$,IfcLabel('STEEL'),$), #36=IfcPropertySingleValue('WEIGHT',$,IfcMassMeasure(248.79167),$), #37=IfcPropertySingleValue('LENGTH',$,IfcLengthMeasure(9900.),$), #38=IfcPropertySingleValue('GUID',$,IfcLabel('ID7349BD4B-0F92-4391-B190-F27A81461C74'),$), #39=IfcPropertySingleValue('ASSEMBLY_TOP_LEVEL',$,IfcLabel(' +9.900'),$), #40=IfcPropertySingleValue('ASSEMBLY_POSITION_CODE',$,IfcLabel('X1/Y4-Y5/+0.00-+10.000'),$), #41=IfcPropertySingleValue('ASSEMBLY_POS',$,IfcLabel('01031904'),$), #42=IfcPropertySingleValue('ASSEMBLY_NAME',$,IfcLabel('RHS300x150x3'),$), #43=IfcPropertySingleValue('ASSEMBLY_BOTTOM_LEVEL',$,IfcLabel(' +0.000'),$), #44=IfcPropertySingleValue('AREA',$,IfcAreaMeasure(18.94938),$))}"""
        # print (dir(definition.RelatingPropertyDefinition))
        """['DefinesType', 'Description', 'GlobalId', 'HasAssociations', 'HasProperties', 'Name', 'OwnerHistory', 'PropertyDefinitionOf', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value']"""
        # print (definition.RelatingPropertyDefinition)
        if definition.RelatingPropertyDefinition.Name == "Default":
            # print(definition.RelatingPropertyDefinition.PropertyDefinitionOf)#(#660413=IfcRelDefinesByProperties('2yUUodWb97ygOsJcjgmD4q',#5,$,$,(#34),#45),)
            # print(dir(definition.RelatingPropertyDefinition.PropertyDefinitionOf))#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
            # print (definition.RelatingPropertyDefinition.HasProperties)#(#35=IfcPropertySingleValue('MATERIAL_TYPE',$,IfcLabel('STEEL'),$), #36=IfcPropertySingleValue('WEIGHT',$,IfcMassMeasure(248.79167),$), #37=IfcPropertySingleValue('LENGTH',$,IfcLengthMeasure(9900.),$), #38=IfcPropertySingleValue('GUID',$,IfcLabel('ID7349BD4B-0F92-4391-B190-F27A81461C74'),$), #39=IfcPropertySingleValue('ASSEMBLY_TOP_LEVEL',$,IfcLabel(' +9.900'),$), #40=IfcPropertySingleValue('ASSEMBLY_POSITION_CODE',$,IfcLabel('X1/Y4-Y5/+0.00-+10.000'),$), #41=IfcPropertySingleValue('ASSEMBLY_POS',$,IfcLabel('01031904'),$), #42=IfcPropertySingleValue('ASSEMBLY_NAME',$,IfcLabel('RHS300x150x3'),$), #43=IfcPropertySingleValue('ASSEMBLY_BOTTOM_LEVEL',$,IfcLabel(' +0.000'),$), #44=IfcPropertySingleValue('AREA',$,IfcAreaMeasure(18.94938),$))
            # for pr in definition.RelatingPropertyDefinition.HasProperties:
                # print(dir(pr))#['Description', 'Name', 'NominalValue', 'PartOfComplex', 'PropertyDependsOn', 'PropertyForDependance', 'Unit', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value']
                # print(dir(pr.NominalValue))
                """['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']
                ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']
                ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']
                ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']
                ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']
                ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']
                ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']
                ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']
                ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']
                ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value', 'wrappedValue']"""
                # print(pr.Name," : ",pr.NominalValue.wrappedValue)

# elemByGuid = ifc_file.by_guid('0G70A15V15qB6T_H0Ue')
# print(elemByGuid)

def extractIFC(ifcelems):
    data = []
    for ifce in ifcelems:
        d = {}
        d['GlobalId'] = ifce.GlobalId
        print (ifce.GlobalId,"{")
        ifcedefs = ifce.IsDefinedBy
        for definition in ifcedefs:
            if definition.is_a() == 'IfcRelDefinesByProperties'and definition.RelatingPropertyDefinition.Name == "Default":
                for pr in definition.RelatingPropertyDefinition.HasProperties:
                    d[pr.Name] = pr.NominalValue.wrappedValue
                    print (pr.Name," : ",pr.NominalValue.wrappedValue)
        data.append(d)
        print ("}")
    return data

# data = extractIFC(ifcElemAssembly[2:5])
# for dic in data:
#     # print ("Guid: ",dic)
#     for di in dic:
#         print (di," : ",dic.get(di))

# print(json.dumps(data))