import arcpy

gdb_path = r"{}".format(input("Type your address: "))
arcpy.env.workspace =gdb_path

featureList=arcpy.ListFeatureClasses()
points=[]
lines=[]
polygons=[]

for item in featureList:
    Des=arcpy.Describe(item)
    if Des.shapetype =="Point":
        points.append(item)
    elif Des.shapetype =="Polyline":
        lines.append(item)
    elif Des.shapetype =="Polygon":
        polygons.append(item)    
print("""in this GDB, there are:
{0} Point layers: {1}
{2} Line layers: {3} 
{4} Polygon layers: {5}""".format(len(points)," ; ".join(points)
,len(lines)," ; ".join(lines),len(polygons)," ; ".join(polygons)))