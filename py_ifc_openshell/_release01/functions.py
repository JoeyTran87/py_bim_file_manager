import ifcopenshell,json

def writeFileFromTxtString(PATH, exDat): #from txt string
	with open(PATH,"w") as f:
		f.write(exDat)	
	return exDat
def writeJsonFile(jsonpath,data):
	with open(jsonpath,'w') as fs:
		json.dump(data,fs)
def extractIFC(ifcelems,ifcdefisa= 'IfcRelDefinesByProperties', defname= 'Default'):
	data = []    
	try:
		for ifce in ifcelems:
			d = {}
			d['GlobalId'] = ifce.GlobalId
			d['Type'] = ifce.get_info().get('type')
			d['Tag'] = ifce.get_info().get('Tag')
			d['Name'] = ifce.get_info().get('Name')
			print (ifce.GlobalId,"{")
			ifcedefs = ifce.IsDefinedBy
			for definition in ifcedefs:
				if definition.is_a() == ifcdefisa and definition.RelatingPropertyDefinition.Name == defname:
					for pr in definition.RelatingPropertyDefinition.HasProperties:
						d[pr.Name] = pr.NominalValue.wrappedValue
						print (pr.Name," : ",pr.NominalValue.wrappedValue)
			data.append(d)
			print ("}")
	except Exception(ex):
		print(ex)
		pass
	return json.dumps(data)
def extractIFC2(jsonPath,ifcelems,ifcdefisa= 'IfcRelDefinesByProperties', defname= 'Default'):
	data = []    
	try:
		for ifce in ifcelems:
			d = {}
			d['GlobalId'] = ifce.GlobalId
			d['Type'] = ifce.get_info().get('type')
			d['Tag'] = ifce.get_info().get('Tag')
			d['Name'] = ifce.get_info().get('Name')
			print (ifce.GlobalId,"{")
			ifcedefs = ifce.IsDefinedBy
			for definition in ifcedefs:
				if definition.is_a() == ifcdefisa and definition.RelatingPropertyDefinition.Name == defname:
					for pr in definition.RelatingPropertyDefinition.HasProperties:
						d[pr.Name] = pr.NominalValue.wrappedValue
						print (pr.Name," : ",pr.NominalValue.wrappedValue)
			data.append(d)
			print ("}")
	except Exception(ex):
		print(ex)
		pass
	writeJsonFile(jsonPath,data)
	return json.dumps(data)

def readIfcElementAssemblies(path):#,ifctype,ifcisa):# 'IfcProduct', = 'IfcElementAssembly'):
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
	print("Count of IfcElementAssembly: ",len(ifcElemAssembly))
	# except Exception(ex):
	# 	print(ex)
	# 	pass
	return ifcElemAssembly