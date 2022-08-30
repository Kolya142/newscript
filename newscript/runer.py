from . import v
cons = {}
def run(sp):
    try:
        if sp[0] == "//":
            return
        elif sp[0] == "set":
            if sp[2] == "input":
                sp[2] = input(sp[3])
            cons[sp[1]] = sp[2]
        elif sp[0] == "show":
            if sp[1] in cons:
                print(cons[sp[1]])
            else:
                print(sp[1])
        elif sp[0] == "if":
            if sp[2] == "==":
                if sp[1] in cons:
                    sp[1] = cons[sp[1]]
                if sp[3] in cons:
                    sp[3] = cons[sp[3]]
                if sp[1] == sp[3]:
                    run(sp[4:])
            elif sp[2] == "!=":
                if sp[1] in cons:
                    sp[1] = cons[sp[1]]
                if sp[3] in cons:
                    sp[3] = cons[sp[3]]
                if sp[1] != sp[3]:
                    run(sp[4:])
            else:
                raise v.newscript_error(f'{sp} is not True',"run_machine")
        elif sp[0] == "run":
            import os
            os.system(sp[1])
        elif sp[0] == "load":
            import os
            os.system("load " + sp[1])
        elif sp[0] in cons:
            if sp[1] == "+=":
                cons[sp[0]] = str(int(cons[sp[2]]) + int(cons[sp[0]]))
            elif sp[1] == "-=":
                cons[sp[0]] = str(int(cons[sp[2]]) - int(cons[sp[0]]))
            elif sp[1] == "*=":
                cons[sp[0]] = str(int(cons[sp[2]]) * int(cons[sp[0]]))
            elif sp[1] == "/=":
                cons[sp[0]] = str(int(cons[sp[2]]) / int(cons[sp[0]]))
            else:
                raise v.newscript_error(f'{sp} is not True',"run_machine")
        else:
            raise v.newscript_error(f'{sp} is not True', "run_machine")
    except Exception as e:
        raise v.newscript_error(e, type(e))