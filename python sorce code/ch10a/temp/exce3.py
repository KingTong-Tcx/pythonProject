def problem():
    raise NameError

def method1():
    try:
        print("a")
        problem()
    except NameError:
        print("b")
    except Exception:
        print("c")
    finally:
        print("d")
    print("e")
    
method1()

        
