import sys, zipfile, os, os.path

def unzip_file_into_dir(file, dir):
    if os.path.exists(dir) == False:
        os.mkdir(dir, 0777)
    zfobj = zipfile.ZipFile(file)
    for name in zfobj.namelist():
        if name.endswith('/'):
            try:
                os.mkdir(os.path.join(dir, name))
            except :
                name=None
        else:
            outfile = open(os.path.join(dir, name), 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
    os.remove(file.path)
