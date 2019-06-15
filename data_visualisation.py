import arcpy

arcpy.env.overwriteOutput = True
outpath = r'C:\Academics\CEE_Internship\Shape_File\Clipped'

points = r'C:\Academics\CEE_Internship\Shape_File\WGS_Data_Pts.shp'
arogya_koyhi = r'C:\Academics\CEE_Internship\Shape_File\arogya kothis_aundh.shp'

arcpy.MakeFeatureLayer_management(points, 'points_layer')

with arcpy.da.SearchCursor(arogya_koyhi, [ 'Kothi' ]) as kothi_cursor:
    for x in kothi_cursor:
        arcpy.MakeFeatureLayer_management(arogya_koyhi, 'kothi_layer', """ "Kothi" = '{}' """.format(x[0]))
        arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'kothi_layer')
        arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, '{}'.format(x[0]))
        print '{}'.format(x[0])


