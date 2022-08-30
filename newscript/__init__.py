from . import pars, runer
def start():
    while True:
        p = pars.pars(input(">>"))
        if p == ["end"]:
            break
        if not p == []:
            runer.run(p)
    print("Process finished\nvirtual machine disconnect")
def main(file_name):
    with open(file_name) as f:
        while True:
            p = pars.pars(f.readline())
            if p == ["end"]:
                break
            if not p == []:
                runer.run(p)
        print("Process finished\nvirtual machine disconnect")