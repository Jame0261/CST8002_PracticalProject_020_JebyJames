"""
Defines the KelpFishRecord class (entity/model).
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

    def to_dict(self):
        return {
            'Site identification': self.site_identification,
            'Year': self.year,
            'Diver identification': self.diver_identification,
            'Transect': self.transect,
            'Average depth (ft)': self.average_depth_ft,
            'Species code': self.species_code,
            'Count': self.count,
            'Survey type': self.survey_type
        }

    def __str__(self):
        return f"{self.site_identification}, {self.year}, {self.diver_identification}, {self.transect}, {self.average_depth_ft}, {self.species_code}, {self.count}, {self.survey_type}"
