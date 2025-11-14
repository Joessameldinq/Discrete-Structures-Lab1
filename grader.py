import subprocess, sys, glob, os

def find_student_file():
    files = glob.glob("lab1_24010854.py")
    if not files:
        print("ERROR: lab1_(STUDENTID).py not found.")
        return None
    return files[0]

if __name__ == "__main__":
    sf = find_student_file()
    if not sf:
        sys.exit(2)
    print("Found student file:", sf)
    ret = subprocess.call([sys.executable, "-m", "pytest", "-q", "tests"])
    sys.exit(ret)
