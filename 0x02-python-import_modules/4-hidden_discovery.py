#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for objName in dir(hidden_4):
        if objName[0] != "_" and objName[1] != "__":
            print(objName)
