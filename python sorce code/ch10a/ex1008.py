# program0808.py
try:
    try:
        raise IOError
    except IOError:
        print("inner exception")
        raise  # <same as raise IOError>
except IOError:
    print("outter exception")
