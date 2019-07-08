import arcpy

points = r'C:\Academics\CEE_Internship\Maharashtra_ULB\Shapefile\ULBs.shp'

with arcpy.da.UpdateCursor(points, ['Radius']) as ulb_cursor :
    for x in ulb_cursor:
        if x[0] == 0:
            x[0] = 5.0
            ulb_cursor.updateRow(x)


