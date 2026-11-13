import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def out_dir():
    for var in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR", "MAKEFUN_OUT"):
        v = os.environ.get(var)
        if v:
            return v
    for cand in ("/output", os.path.join(os.getcwd(), "output"),
                 os.path.dirname(os.path.abspath(__file__))):
        try:
            os.makedirs(cand, exist_ok=True)
            probe = os.path.join(cand, ".probe")
            with open(probe, "w"):
                pass
            os.remove(probe)
            return cand
        except OSError:
            continue
    raise RuntimeError("no writable output directory")


dst = os.path.join(out_dir(), "entry.png")
shutil.copyfile(SRC, dst)
print("wrote", dst, os.path.getsize(dst), "bytes")
