#BatchInstall.py
import os
libs = {"numoy","matplotlib","pillow","sklearn","requests","beautifulsoup4","wheel","django"\
        "flask","werobot","sympy","pandas","networkx","pyqt5","pyopengl","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip install " + lib)
        print("success! for install"+lib)
except:
    print("somthing wrong!")
