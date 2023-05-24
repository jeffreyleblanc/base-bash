#! /usr/bin/env python3

# SPDX-FileCopyRightText: Copyright (c) 2023-present Jeffrey LeBlanc
# SPDX-License-Indentifier: MIT

from pathlib import Path
import shutil
import subprocess
import shlex
from dataclasses import dataclass, field
import argparse

#-- Utilties -----------------------------------------------#

class Printer:
    def p(self, text=''):   print(text)
    def bold(self, text):   print(f"\x1b[1m{text}\x1b[0m")
    def red(self, text):    print(f"\x1b[31m{text}\x1b[0m")
    def yellow(self, text): print(f"\x1b[93m{text}\x1b[0m")
    def blue(self, text):   print(f"\x1b[38;5;27m{text}\x1b[0m")
    def cyan(self, text):   print(f"\x1b[36m{text}\x1b[0m")
    def green(self, text):  print(f"\x1b[92m{text}\x1b[0m")
    def gray(self, text):   print(f"\x1b[38;5;239m{text}\x1b[0m")
    def redbold(self, text):  print(f"\x1b[31;1m{text}\x1b[0m")

def proc(cmd, cwd=None):
    if isinstance(cmd,str):
        cmd = shlex.split(cmd)
    r = subprocess.run(cmd,capture_output=True,cwd=cwd)
    return (
        r.returncode,
        r.stdout.decode('utf-8'),
        r.stderr.decode('utf-8')
    )

def md5sum(file_path):
    c,o,e = proc(f"md5sum {file_path}")
    return o.split(' ')[0]

def same_content(path1, path2, use="diff"):
    if "diff" == use:
        c,o,e = proc(f"diff {path1} {path2}")
        if c == 0:
            return (True,None)
        else:
            return (False,o)
    else:
        raise Exception("Not implemented")

#-- Main -------------------------------------------------#

@dataclass
class FileDiff:
    mirror_path: Path
    real_path: Path
    rel_path: Path
    same: bool = False
    diff: str = ""

@dataclass
class FileReport:
    diffs:   list[FileDiff] = field(default_factory=list)
    missing: list[Path] = field(default_factory=list)
    same:    list[Path] = field(default_factory=list)

    @property
    def has_missing(self): return len(self.missing)>0

    @property
    def has_diffs(self): return len(self.diffs)>0


def make_report():
    # Get our main paths
    HERE = Path(__file__).parent
    HOME = Path.home()
    MIRROR = HERE/"dot-files"
    assert MIRROR.is_dir()

    # Walk the MIRROR and compare to the real
    R = FileReport()
    for mirror_path in MIRROR.glob("**/*"):
        # Get paths
        rel_path = mirror_path.relative_to(MIRROR)
        real_path = HOME/rel_path
        # We will want to check for any symlinks

        if mirror_path.is_dir():
            # we want to make sure exists
            pass
        if mirror_path.is_file():
            if not real_path.exists():
                R.missing.append(real_path)
            else:
                if not real_path.is_file():
                    raise Exception(f"{real_path} is not a file")

                same,_diff = same_content(mirror_path,real_path)
                if not same:
                    R.diffs.append(FileDiff(
                        rel_path = rel_path,
                        mirror_path = mirror_path,
                        real_path = real_path,
                        diff = _diff
                    ))
    return R

def print_report(R):
    P = Printer()

    if not R.has_missing:
        P.green("No missing files")
    else:
        P.red("Missing:")
        for m in R.missing:
            P.p(m)

    if not R.has_diffs:
        P.green("\nNo differences")
    else:
        P.red("\nDifferences:")
        for d in R.diffs:
            P.p(d.rel_path)
            P.gray(d.diff)

def update_mirror(R):
    P = Printer()
    P.blue("Pulling differences to mirror:")
    for d in R.diffs:
        P.p(d.rel_path)
        shutil.copy2(d.real_path,d.mirror_path)


def main():
    VERSION = "0.1"
    parser = argparse.ArgumentParser()
    parser.add_argument("action",choices=("version","calc-diffs","update-mirror"))
    args = parser.parse_args()

    match args.action:
        case "version":
            print(VERSION)
        case "calc-diffs":
            R = make_report()
            print_report(R)
        case "update-mirror":
            R = make_report()
            update_mirror(R)

if __name__ == "__main__":
     main()

