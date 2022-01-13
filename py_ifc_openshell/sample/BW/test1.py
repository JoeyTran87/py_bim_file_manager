"""
https://view.ifcopenshell.org/v/CJqGJhVVVEpqFRZnNGrcvVTGQMwFrFxs
"""

import ifcopenshell
import os


def writeTxtFromTxtString(PATH, exDat): #from txt string
	with open(PATH,"w") as f:
		f.write(exDat)	
	return exDat


path = "R:\\BimESC\\00-BIM STANDARD\\PYTHON\\ifcopenshell\\NHA XUONG 27_2021.03.03 (1).ifc" #"C:\\Users\\USER\\Documents\\GitHub\\cofico\\BIM_master\\Python\\ifcopenshell\\ifcopenshell\\NHA XUONG 27_2021.03.03 (1).ifc"#input("Enter IFC File Path:")#

ifc_file = ifcopenshell.open(path)
products = ifc_file.by_type('IfcProduct')
# print(dir(ifc_file))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add', 'by_guid', 'by_id', 'by_type', 'create_entity', 'from_string', 'get_inverse', 'remove', 'traverse', 'wrapped_data']
"""
CTO = ifc_file.by_type("IfcCartesianTransformationOperator")

pds = ifc_file.by_type("IfcProductDefinitionShape")

res = []
ssss = ""

resCTO = []
allRes = []
allResStr = ""
for product in products:
    # allRes.append(product)
    # allResStr += product.GlobalId + "\t" + product.Name + "\n"
    if product.is_a() == "IfcElementAssembly" and "CO".lower() in product.Tag.lower() : # IfcColumn = 2373 IfcElementAssembly = 11932 IfcGirt = 0 COlumn chinh = 137
        res.append(product)
        ssss += product.GlobalId + "\t" + product.Name + "\t" + product.Tag+ "\n"

# print("IfcProductRepresentation = ",len(pds))
# print(pds[100].get_info())
"""
IfcProductRepresentation =  48834
{'id': 4322, 'type': 'IfcProductRepresentation =  48834
{'id': 4322, 'type': 'IfcProductDefinitionShape', 'Name': None, 'Description': None, 'Representations': (#4321=IfcShapeRepresentation(#12,'Body','Brep',(#4235)),)}', 'Name': None, 'Description': None, 'Representations': (#4321=IfcShapeRepresentation(#12,'Body','Brep',(#4235)),)}
"""
# print("Count Product Column CO=",len(res))
# print("Count All Product=",len(allRes))
# print("Count IfcCartesianTransformationOperator=",len(CTO))
"""
Count Product Column CO= 137
Count All Product= 60769
Count IfcCartesianTransformationOperator= 242
dir(CTO[0])
['Axis1', 'Axis2', 'Axis3', 'LayerAssignments', 'LocalOrigin', 'Scale', 'StyledByItem', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value']
CTO[0]Axist1 = None
CTO[0]Axist2 = None
CTO[0]Axist3 = None
CTO[0]LocalOrigin = #6=IfcCartesianPoint((0.,0.,0.))
CTO[0]get_info = {'id': 151, 'type': 'IfcCartesianTransformationOperator3D', 'Axis1': None, 'Axis2': None, 'LocalOrigin': #6=IfcCartesianPoint((0.,0.,0.)), 'Scale': None, 'Axis3': None}
"""
# print("CTO[0]Axist1 =",CTO[0].Axis1)
# print("CTO[0]Axist2 =",CTO[0].Axis2)
# print("CTO[0]Axist3 =",CTO[0].Axis3)
# print("CTO[0]LocalOrigin =",CTO[0].LocalOrigin)
# print("CTO[0]get_info =",CTO[0].get_info())
col = res[100]
# print(col.get_info())
"""{'id': 31390, 'type': 'IfcElementAssembly', 'GlobalId': '1W1JDn001Bvp4sCJ0vDJOo', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1614765940), 'Name': 'Steel Assembly', 'Description': None, 'ObjectType': None, 'ObjectPlacement': #31389=IfcLocalPlacement(#30,#10), 'Representation': None, 'Tag': 'CO54(?)', 'AssemblyPlace': 'NOTDEFINED', 'PredefinedType': 'RIGID_FRAME'}"""

# pathWrite = "C:\\Users\\USER\\Documents\\GitHub\\cofico\\BIM_master\\Python\\ifcopenshell\\ifcopenshell\\test.txt"#input("Enter Exported TXT File Path:")#"R:\\BimESC\\00-BIM STANDARD\\PYTHON\\ifcopenshell\\test.txt"
# fn = writeTxtFromTxtString(pathWrite,allResStr)
res2 = []
res3 = []
res4 = []
# for co in products:
#     if co.is_a() == "IfcColumn": 
#         res2.append(co)
# for rh in products:
#     if rh.is_a() == "LcIfcRepresentationHolder":
#         res3.append(rh)
# for go in products:
#     if go.is_a() == "Geometry": # IfcColumn = 2373 IfcElementAssembly = 11932 IfcGirt = 0 COlumn chinh = 137
#         res4.append(go)
# print(res)
# print(res2)
# print(res3)
# print(res4)

# print("GET INFO PlacementRelTo = ",col.ObjectPlacement.PlacementRelTo.PlacementRelTo.PlacementRelTo.get_info())#.ObjectPlacement)#ObjectPlacement.RelativePlacement.Location)

"""
GET INFO PlacementRelTo =  #30=IfcLocalPlacement(#28,#10)
{'id': 30, 'type': 'IfcLocalPlacement', 'PlacementRelTo': #28=IfcLocalPlacement(#25,#10), 'RelativePlacement': #10=IfcAxis2Placement3D(#6,#9,#7)}
{'id': 28, 'type': 'IfcLocalPlacement', 'PlacementRelTo': #25=IfcLocalPlacement($,#10), 'RelativePlacement': #10=IfcAxis2Placement3D(#6,#9,#7)}
{'id': 25, 'type': 'IfcLocalPlacement', 'PlacementRelTo': None, 'RelativePlacement': #10=IfcAxis2Placement3D(#6,#9,#7)}
"""


loca = []
for co in res:
    try:
        lo = co.ObjectPlacement.RelativePlacement.Location
        loca.append(lo)
    except:
        pass
# print(loca)
proSet1 = ifc_file.by_id(31394)
# print(proSet1.get_info())
"""{'id': 31394, 'type': 'IfcPropertySet', 'GlobalId': '20sjsT3xv2zPWOORKaAUxY', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1614765940), 'Name': 'Default', 'Description': None, 'HasProperties': (#6301=IfcPropertySingleValue('ASSEMBLY_POSITION_CODE',$,IfcLabel('20-21/H'),$), #3155=IfcPropertySingleValue('ELEVATION',$,IfcLabel(' +10.499'),$), #31391=IfcPropertySingleValue('WEIGHT',$,IfcMassMeasure(409.61637),$), #37=IfcPropertySingleValue('MATERIAL TYPE',$,IfcLabel('STEEL'),$), #3157=IfcPropertySingleValue('LENGTH',$,IfcLengthMeasure(10349.14384),$), #31392=IfcPropertySingleValue('GUID',$,IfcLabel('ID60053371-0000-4BE7-3136-313039353632'),$), #1328=IfcPropertySingleValue('ASSEMBLY_BOTTOM_LEVEL',$,IfcLabel(' +0.150'),$), #1329=IfcPropertySingleValue('MEMBER TYPE',$,IfcLabel('COLUMN'),$), #31393=IfcPropertySingleValue('MEMBER NO',$,IfcLabel('CO54(?)'),$), #4870=IfcPropertySingleValue('AREA',$,IfcAreaMeasure(19.1),$))} """
proSet1Set = ifc_file.by_id(6301)
print(proSet1Set.get_info())
"""{'id': 6301, 'type': 'IfcPropertySingleValue', 'Name': 'ASSEMBLY_POSITION_CODE', 'Description': None, 'NominalValue': IfcLabel('20-21/H'), 'Unit': None}"""
print(proSet1Set.NominalValue)

proSet2 = ifc_file.by_id( 31397)
# print(proSet2.get_info())
"""{'id': 31397, 'type': 'IfcPropertySet', 'GlobalId': '3uepJPkkD5$QAl8SQF__uh', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1614765940), 'Name': 'Tekla Assembly', 'Description': 'Assembly Properties', 'HasProperties': (#45=IfcPropertySingleValue('Control number',$,$,$), #46=IfcPropertySingleValue('Cast unit rebar weight',$,$,$), #31395=IfcPropertySingleValue('Assembly/Cast unit weight',$,IfcMassMeasure(409.6),$), #1334=IfcPropertySingleValue('Assembly/Cast unit bottom elevation',$,IfcLabel(' +0.150'),$), #3163=IfcPropertySingleValue('Assembly/Cast unit top elevation',$,IfcLabel(' +10.499'),$), #6306=IfcPropertySingleValue('Assembly/Cast unit position code',$,IfcLabel('20-21/H'),$), #31396=IfcPropertySingleValue('Assembly/Cast unit Mark',$,IfcLabel('CO54(?)'),$))}"""
proSet3 = ifc_file.by_id( 31399)
# print(proSet3.get_info())
"""{'id': 31399, 'type': 'IfcElementQuantity', 'GlobalId': '0FFvb15Jj0kxJ5xp$5pfMx', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1614765940), 'Name': 'BaseQuantities', 'Description': None, 'MethodOfMeasurement': None, 'Quantities': (#31398=IfcQuantityLength('Width',$,$,200.475394882989),)}"""
ifcA2Pl = ifc_file.by_id(10) #IfcAxis2Placement3D
# print(dir(ifcA2Pl))
# print(ifcA2Pl.get_info())
"""
['Axis', 'LayerAssignments', 'Location', 'RefDirection', 'StyledByItem', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute_name', 'attribute_type', 'get_info', 'get_info_2', 'id', 'is_a', 'unwrap_value', 'walk', 'wrap_value']
{'id': 10, 'type': 'IfcAxis2Placement3D', 'Location': #6=IfcCartesianPoint((0.,0.,0.)), 'Axis': #9=IfcDirection((0.,0.,1.)), 'RefDirection': #7=IfcDirection((1.,0.,0.))}
"""
ifcShapeRepre = ifc_file.by_id(4321) #IfcShapeRepresentation
# print(ifcShapeRepre.get_info())
"""{'id': 4321, 'type': 'IfcShapeRepresentation', 'ContextOfItems': #12=IfcGeometricRepresentationSubContext('Body','Model',*,*,*,*,#11,$,.MODEL_VIEW.,$), 'RepresentationIdentifier': 'Body', 'RepresentationType': 'Brep', 'Items': (#4235=IfcFacetedBrep(#4234),)}"""
ifcGeoRepre = ifc_file.by_id(12) ##12=IfcGeometricRepresentationSubContext
# print(ifcGeoRepre.get_info())
"""{'id': 12, 'type': 'IfcGeometricRepresentationSubContext', 'ContextIdentifier': 'Body', 'ContextType': 'Model', 'CoordinateSpaceDimension': None, 'Precision': None, 'WorldCoordinateSystem': 
None, 'TrueNorth': None, 'ParentContext': #11=IfcGeometricRepresentationContext($,'Model',3,1.E-005,#10,$), 'TargetScale': None, 'TargetView': 'MODEL_VIEW', 'UserDefinedTargetView': None}"""
ifcFBrep = ifc_file.by_id(4235)#IfcFacetedBrep
# print(ifcFBrep.get_info())
"""{'id': 4235, 'type': 'IfcFacetedBrep', 'Outer': #4234=IfcClosedShell((#4214,#4219,#4224,#4227,#4230,#4233))}"""
# print(col.ObjectPlacement.ReferencedByPlacements)
# print(dir(col.ObjectPlacement))#AssemblyPlace)
# print(dir(col))
# property_set=[]
# for definition in col.IsDefinedBy:
#     # To support IFC2X3, we need to filter our results.
#     if definition.is_a('IfcRelDefinesByProperties'):
#         # print(dir(definition))
#         property_set = definition.RelatingPropertyDefinition
#         # print(dir(property_set))
#         print(property_set.Name) # Might return Pset_WallCommon
#         print(property_set.PropertyDefinitionOf)
#         for defi in property_set.PropertyDefinitionOf:
#             if defi.is_a('IfcRelDefinesByProperties'):
#                 proSet = defi.RelatingPropertyDefinition
#                 print(proSet.Name)

# try:
#     for property in property_set.HasProperties:
#         if property.is_a('IfcPropertySingleValue'):
#             print(property.Name)
#             print(property.NominalValue.wrappedValue)
# except:
#     pass

#print(dir(res[0]))

# if col.ObjectPlacement.PlacementRelTo:
#     # Inherit the coordinates of its parents
#     pass
# local_coordinates = col.ObjectPlacement.RelativePlacement.Location[0]
# print(local_coordinates)

# geo = col.Position
# print(geo)

# print(col.get_info())
"""
{'id': 31390, 'type': 'IfcElementAssembly', 'GlobalId': '1W1JDn001Bvp4sCJ0vDJOo', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1614765940), 'Name': 'Steel Assembly', 'Description': None, 'ObjectType': None, 'ObjectPlacement': #31389=IfcLocalPlacement(#30,#10), 'Representation': None, 'Tag': 'CO54(?)', 'AssemblyPlace': 'NOTDEFINED', 'PredefinedType': 'RIGID_FRAME'}
"""
# def getAllgeometry(elem):
#     res = []
#     # for el in elem:
#     #     res.append(el)

#     res = elem.ReferenceTo
#     return res

# print(getAllgeometry(col))
