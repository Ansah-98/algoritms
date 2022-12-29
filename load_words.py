
def load(file):
    try :
        with open(file) as f :
            w = f.readlines()
        return w
    except IOError as e:
        print(f"error opening program ,terminating program because of {e}")
        