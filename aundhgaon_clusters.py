import arcpy

arcpy.env.workspace = 'C:\Academics\CEE_Internship\Shape_File\Clustering'
arcpy.env.overwriteOutput = True

datasets = arcpy.ListFeatureClasses()
print datasets

outpath = r'C:\Academics\CEE_Internship\Shape_File\Segregation'

for shp in datasets :
    points = r'C:\Academics\CEE_Internship\Shape_File\Clustering\{}'.format(shp)
    boundaries = r'C:\Academics\CEE_Internship\Shape_File\boundaries.shp'

    arcpy.MakeFeatureLayer_management(points, 'points_layer_{}'.format(shp))

    with arcpy.da.SearchCursor(boundaries, [ 'Name' ]) as boundaries_cursor :
        for x in boundaries_cursor:
            print shp, x

            arcpy.MakeFeatureLayer_management(boundaries, 'boundaries_layer_{}'.format(x[0]), """ "Name" = '{}' """.format(x[0]))
            arcpy.SelectLayerByLocation_management('points_layer_{}'.format(shp), 'WITHIN', 'boundaries_layer_{}'.format(x[0]))
            arcpy.FeatureClassToFeatureClass_conversion('points_layer_{}'.format(shp), outpath, '{}_{}'.format(x[0], shp))







