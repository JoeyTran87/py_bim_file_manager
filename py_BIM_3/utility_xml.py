import pandas as pd
import numpy as np

def main():
    """"""
    path_xml = r'C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_bim_3\configure_folder.xml'#input('Path: ')
    df_xml = pd.read_xml(path_xml)
    print(df_xml)

if __name__ == '__main__':
    """"""
    main()