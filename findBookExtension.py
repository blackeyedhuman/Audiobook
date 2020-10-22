#find pdfs
def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))
