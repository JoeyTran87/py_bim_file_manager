import pandas as pd
import numpy as np
import os, sys, json


bim_projects_data = [
            {   "ProjectNumber": "CHG", #key
                "ProjectName": "Cộng Hòa Garden II",
                "ProjectAddress": "",
                "ProjectClient": "Cong Hoa Garden Investor",
                "ProjectType": "Mixed Use Highrise",
                "ProjectScale": "",
                "ProjectDuration": ""
            },
            {   "ProjectNumber": "MARS", #key
                "ProjectName": "Marubeni Solute",
                "ProjectAddress": "",
                "ProjectClient": "Marubeni",
                "ProjectType": "Factory",
                "ProjectScale": "",
                "ProjectDuration": ""
            }
        ]

# print(bim_projects_data)

project_data_template = {   "ProjectNumber": "",
                "ProjectName": "",
                "ProjectAddress": "",
                "ProjectClient": "",
                "ProjectType": "",
                "ProjectScale": "",
                "ProjectDuration": ""
            }