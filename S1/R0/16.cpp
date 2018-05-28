string viciph(string text, string key) {
    int k = key.length();
    int t = text.length();
    char b[k];
    char a[t];
    strcpy(b, key.c_str());
    strcpy(a, text.c_str());
    for (int i = 0; i < t; i++) a[i]=abs(abs(a[i]-93.5)-16)<13?((a[i]%32+b[i%k]%32-2)%26+(abs(a[i]-77.5)<13?65:97)):a[i];
    return text = a;
}
