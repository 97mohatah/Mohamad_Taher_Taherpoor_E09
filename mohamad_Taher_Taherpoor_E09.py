import arcpy

gdb_path = r"{}".format(input("Type your address: "))
arcpy.env.workspace =gdb_path

featureList=arcpy.ListFeatureClasses()
count_Point=0
count_Line=0
count_Polygon=0

for item in featureList:
    Des=arcpy.Describe(item)
    if Des.shapetype =="Point":
        count_Point +=1
    elif Des.shapetype =="Polyline":
        count_Line +=1
    elif Des.shapetype =="Polygon":
        count_Polygon +=1    
    print("Layer name is : ",Des.name," ;","Layer type is : ",Des.shapetype)
print("""in this GDB, there are:\n{0} Point layers. \n{1} Line layers. 
{2} Polygon layers.""".format(count_Point,count_Line,count_Polygon))