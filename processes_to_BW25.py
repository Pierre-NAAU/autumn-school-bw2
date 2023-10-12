#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 21:23:28 2023

@author: andreavargasf
"""



import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import BW25 packages. You'll notice the packages are imported individually, unlike a one-and-done import with BW2.
import bw2data as bd
import bw2io as bi
import bw2calc as bc
import bw2analyzer as bwa

name = "asphalt"
bd.projects.set_current(name)
bd.projects
bi.bw2setup()
bd.databases
#bd.Database("ecoinvent-391-cutoff").delete()
#del bd.databases['ecoinvent-391-cutoff']

ei_path = "//Users/andreavargasf/Documents/ecoinvent/ecoinvent 3.9.1_cutoff_ecoSpold02/datasets"

# You will also need to give your database a name. This name will appear when you call bd.databases.
# Here, I am using EI v3.9.1 cutoff.
ei_name = "ecoinvent-391-cutoff"



# When we execute this cell, we will check if it's already been imported, and if not (else) we import it.

if ei_name in bd.databases:
    print("Database has already been imported.")
else:
# Go ahead and import:
    ei_importer = bi.SingleOutputEcospold2Importer(ei_path, ei_name)
    # Apply stragegies 
    ei_importer.apply_strategies()
    # We can get some statistics
    ei_importer.statistics()
    # Now we will write the database into our project. 
    ei_importer.write_database()

# You will also need to give your database a name. This name will appear when you call bd.databases.
# Here, I am using EI v3.9.1 cutoff.
ei_name = "ecoinvent-391-cutoff"

bd.databases
eidb = bd.Database(ei_name)
print("The imported ecoinvent database is of type {} and has a length of {}.".format(type(eidb), len(eidb)))
eidb.graph_technosphere()


# Include the path to the foreground database
fg_db = "/Users/andreavargasf/Library/CloudStorage/OneDrive-UniversityofTwente/My Drive/Autumn School/Beavers/Asphalt/Foreground.xlsx"

# Import your LCI
lci = bi.ExcelImporter(fg_db)

# Need to match FG_DB to itself
lci.match_database(fields=["name", "unit", "location"])

# Need to match FG_DB to the biosphere
lci.match_database(ei_name, fields=["name", "reference product", "location", "unit"])
lci.match_database("biosphere3", fields=["name", "categories"])

bi.create_core_migrations()

# Once your package is imported we need to apply strategies
lci.apply_strategies()

# We need to match databases - name and categories but ATTENTION! the categories in
# the excel file is "None" so we willlci.write_excel() also need to match against unit.

lci.statistics()

lci.write_excel()
lci.write_database()

bd.databases



















