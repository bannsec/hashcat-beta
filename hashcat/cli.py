
import os
import platform
import subprocess
import sys

def main(program=None, cwd=None):

    if program is None: program = hashcat_exe_path
    if cwd is None: cwd = hashcat_dir

    args = sys.argv[1:] if len(sys.argv) > 1 else []

    # Because hashcat devs can't figure out how to handle paths...
    # https://github.com/hashcat/hashcat/issues/2288
    for i, arg in enumerate(args):
        # Implicitly determine if this is a path and if so, make it absolute
        if os.path.exists(arg):
            args[i] = os.path.abspath(arg)
    
    # Light passthrough
    subprocess.run([program] + args, cwd=cwd)

def pp():
    main(program=pp_exe_path, cwd=pp_dir)

#bits = platform.architecture()[0][:-3]
bits = "" # Only 64-bit in beta releases apparently
ext = ".exe" if platform.uname().system == "Windows" else ".bin"

here = os.path.dirname(os.path.realpath(__file__))

hashcat_dir = os.path.join(here, "hashcat")
hashcat_exe = "hashcat"  + bits + ext
hashcat_exe_path = os.path.join(hashcat_dir, hashcat_exe)

pp_dir = os.path.join(here, "pp")
pp_exe = "pp64"  + ext
pp_exe_path = os.path.join(pp_dir, pp_exe)

if __name__ == "__main__":
    main()
