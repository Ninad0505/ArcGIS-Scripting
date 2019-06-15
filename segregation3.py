import arcpy

outpath = r'C:\Academics\CEE_Internship\Shape_File\Clustering'

points = r'C:\Academics\CEE_Internship\Shape_File\Clipped\Aundh Gaon.shp'

arcpy.MakeFeatureLayer_management(points, 'points_layer', """ "Total_prop" < 25  """)

arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'segregation00')