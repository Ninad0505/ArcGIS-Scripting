import arcpy

arcpy.env.workspace = 'C:\Academics\CEE_Internship\Shape_File\Segregation'

datasets = arcpy.ListFeatureClasses()
print datasets

for shp in datasets :
    points = r'C:\Academics\CEE_Internship\Shape_File\Segregation\{}'.format(shp)

    with arcpy.da.SearchCursor(points, ['FID', 'Total_prop']) as points_cursor :
        Total_HH = 0
        Total_count = 0
        for x in points_cursor :
            Total_HH += x[1]
            Total_count += 1

        print shp, Total_count, Total_HH

