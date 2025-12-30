import subprocess
import sys
import os

DEVKITPRO = r"C:\devkitPro"
LIBGBA = os.path.join(DEVKITPRO, "libgba")

def compile_cpp_to_gba(source_cpp, output_gba):
    elf = "temp.elf"

    compile_cmd = [
        "arm-none-eabi-g++",
        source_cpp,

        "-mthumb",
        "-mthumb-interwork",
        "-mcpu=arm7tdmi",

        f"-I{LIBGBA}\\include",
        f"-L{LIBGBA}\\lib",

        "-specs=gba.specs",
        "-O2",
        "-Wall",

        "-o", elf,
        "-lgba"
    ]

    objcopy_cmd = [
        "arm-none-eabi-objcopy",
        "-O", "binary",
        elf,
        output_gba
    ]

    print("Compiling C++ → ELF...")
    subprocess.check_call(compile_cmd)

    print("Converting ELF → GBA...")
    subprocess.check_call(objcopy_cmd)

    os.remove(elf)
    print("Done! Output:", output_gba)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gbaconvert.py main.cpp game.gba")
        sys.exit(1)

    compile_cpp_to_gba(sys.argv[1], sys.argv[2])
