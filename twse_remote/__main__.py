import os, sys
def load_pyc_files(filepath):
    path, fname = os.path.split(filepath)
    module, _ = os.path.splitext(fname)
        
    if path not in sys.path:            
        sys.path.insert(0, path)
        
    return __import__(module)

if __name__ == '__main__':
    builder = load_pyc_files(r'twse_remote\builder\build.pyc')
    builder.Main().__start__()