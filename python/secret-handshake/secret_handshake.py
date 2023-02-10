def commands(binary_str):
    cmdlst = ["jump", "close your eyes", "double blink", "wink"]
    outlst = []
    for bin in range(1, 5):
        if int(binary_str[bin]):
            outlst.append(cmdlst[bin-1])
    if binary_str[0] == '0':
        outlst.reverse()
    return outlst
