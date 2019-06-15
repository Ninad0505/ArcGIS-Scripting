import arcpy

arcpy.env.workspace = 'C:\Academics\CEE_Internship\Shape_File\Clipped'

datasets = arcpy.ListFeatureClasses()
print datasets

for shp in datasets :
    points = r'C:\Academics\CEE_Internship\Shape_File\Clipped\{}'.format(shp)
    with arcpy.da.SearchCursor(points, ['R_Total', 'residentia', 'commercial','R_and_C','pmc_govt','R_slum','open_plot']) as kothi_cursor:
        List = []
        Total_HH = 0
        Residential = 0
        Commercial = 0
        Mix = 0
        Open_Plot = 0
        Slum = 0

        for x in kothi_cursor:
            Total_HH += x[0]
            if x[1] == 1:
                Residential += x[0]
            elif x[2] == 1:
                Commercial += x[0]
            elif x[3] == 1:
                Mix += x[0]
            elif x[6] == 1:
                Open_Plot += x[0]
            elif x[5] == 1:
                Slum += x[0]

    print "In {} Total HH = {}, Residential HH = {}, Commercial HH = {}, Mix HH = {}, Open Plots = {}, Slum HH = {}".format(shp, Total_HH, Residential, Commercial, Mix, Open_Plot, Slum)










