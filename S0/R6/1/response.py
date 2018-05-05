def tlowscript(program):
    lines, varis, line = "".join([i for i in program if i.isalnum() or i in " \n"]).split("\n"), {}, 1
    if lines[0] != "This is TLOWScript": print("NotTLOWException"); return None
    while line < len(lines): 
        lsplit = lines[line].split(" ")
        if lsplit[0] == "var": varis[lsplit[1]] = 0
        elif lsplit[0] in ("inc", "dec"): varis[lsplit[1]] += 1 if lsplit[0] == "inc" else -1
        elif lsplit[0] in ("prn", "prc"): print((str if lsplit[0] == "prn" else chr)(varis[lsplit[1]]))
        elif lsplit[0] == "jgt" and varis[lsplit[1]] > varis[lsplit[2]]: line = lines.index("lab " + lsplit[3])
        line += 1
