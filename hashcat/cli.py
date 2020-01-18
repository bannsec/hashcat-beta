
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

def cap2hccapx():
    try:
        # Output file
        sys.argv[2] = os.path.abspath(sys.argv[2])
    except:
        pass

    main(program=cap2hccapx_exe_path, cwd=cap2hccapx_dir)

def kwp():
    main(program=kwp_exe_path, cwd=kwp_dir)

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

cap2hccapx_dir = os.path.join(here, "utils", "bin")
cap2hccapx_exe = "cap2hccapx"  + ext
cap2hccapx_exe_path = os.path.join(cap2hccapx_dir, cap2hccapx_exe)

kwp_dir = os.path.join(here, "kwp")
kwp_exe = "kwp"
if platform.uname().system == "Windows":
    kwp_exe += platform.architecture()[0][:-3] + ".exe"
kwp_exe_path = os.path.join(kwp_dir, kwp_exe)

if __name__ == "__main__":
    main()
