from distutils.core import setup
import py2exe
from distutils.filelist import findall
import os
import matplotlib
matplotlibdatadir = matplotlib.get_data_path()
matplotlibdata = findall(matplotlibdatadir)
matplotlibdata_files = []
for f in matplotlibdata:
    dirname = os.path.join('matplotlibdata', f[len(matplotlibdatadir)+1:])
    matplotlibdata_files.append((os.path.split(dirname)[0], [f]))


setup(
    console=['main.py'],
    options={
             'py2exe': {
                        'includes': ["sip", "PyQt4.QtGui"],
                        'packages' : ['matplotlib', 'pytz'],
                        'excludes': ['_gtkagg', '_tkagg']
                       }
            },
    data_files=matplotlibdata_files
)