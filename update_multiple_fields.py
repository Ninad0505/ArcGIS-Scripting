import arcpy

points = r'C:\Academics\Python\ArcGIS_Scripting\Data\ne_10m_populated_places.shp'

field_lists = arcpy.ListFields(points)
list_fields = []

for x in field_lists:
    if x.type == 'String':
        list_fields.append(x.name)

for field in list_fields:
    with arcpy.da.UpdateCursor(points, [field]) as city_cursor :
        for x in city_cursor:
            if x[0] == ' ':
                x[0] = 'we_just_got_updated'
                city_cursor.updateRow(x)

