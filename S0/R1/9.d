void main() {
    import std.stdio, std.net.curl, std.file;
    File ram = File("RAM", "w");
    bool enoughRam = false; //Obviously Malcolm doesn't have enough RAM
    while(!enoughRam)
        ram.writeln(get("https://downloadmoreram.com"));
}