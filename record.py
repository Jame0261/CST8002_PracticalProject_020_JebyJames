"""
CST8002 Practical Project 1
Author: Jeby James
Professor: Stanley Pieda
Date: 2025-09-21
Description: Record class for dataset entity
"""

class KelpFishRecord:
    def __init__(self, site_identification, year, diver_identification,
                 transect, average_depth_ft, species_code, count, survey_type):
        self.site_identification = site_identification
        self.year = year
        self.diver_identification = diver_identification
        self.transect = transect
        self.average_depth_ft = average_depth_ft
        self.species_code = species_code
        self.count = count
        self.survey_type = survey_type

    def __str__(self):
        return (f"Site: {self.site_identification}, Year: {self.year}, "
                f"Diver: {self.diver_identification}, Transect: {self.transect}, "
                f"Depth(ft): {self.average_depth_ft}, Species: {self.species_code}, "
                f"Count: {self.count}, Survey: {self.survey_type}")
