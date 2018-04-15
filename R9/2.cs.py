#if false 
""" 
#endif
static string quine(string input){
    string data = "#if false \"\"\"#endifstatic string quine(string input){{    string data = \"{0}\";    return input == \"\" ? string.Format(data, data) : input;    }}/*\"\"\"def quine(x):  data = \"{0}\"  return x if x is not '' else data.replace(\"{{{{\", \"{{\", 4).replace(\"}}}}\",\"}}\", 4).replace(\"{0}\", data, 2)";
    return input == "" ? string.Format(data, data) : input;
    }/*"""
def quine(x):
  data = "#if false \"\"\"#endifstatic string quine(string input){{    string data = \"{0}\";    return input == \"\" ? string.Format(data, data) : input;    }}/*\"\"\"def quine(x):  data = \"{0}\"  return x if x is not '' else data.replace(\"{{{{\", \"{{\", 4).replace(\"}}}}\",\"}}\", 4).replace(\"{0}\", data, 2)"
  return x if x is not '' else data.replace("{{", "{", 4).replace("}}","}", 4).replace("{0}", data, 1)
