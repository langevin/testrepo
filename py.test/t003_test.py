import subprocess

def test_three():
    print('this is a test')
    val = subprocess.call(['gfortran', '--version'])
    raise Exception('Trying fortran compiler')
    return
    