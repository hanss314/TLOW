string Vigenere(string text, string key)
{
    string alphabet = "abcdefghijklmnopqrstuvwxyz", result = "";
    for (int i = 0; i < text.Length; i++)
        if (char.IsLetter(text[i]))
            if (char.IsUpper(text[i])) result += char.ToUpper(alphabet[(alphabet.IndexOf(char.ToLower(text[i])) + alphabet.IndexOf(char.ToLower(key[i % key.Length]))) % 26]);
            else result += alphabet[(alphabet.IndexOf(text[i]) + alphabet.IndexOf(char.ToLower(key[i % key.Length]))) % 26];
        else result += text[i];
    return result;
}
