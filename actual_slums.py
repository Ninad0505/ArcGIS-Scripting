import arcpy

outpath = r'C:\Academics\CEE_Internship\Shape_File'

points = r'C:\Academics\CEE_Internship\Shape_File\slums.shp'

arcpy.MakeFeatureLayer_management(points, 'points_layer', """ "R_Total" > 50 """)

arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'actual_slums')