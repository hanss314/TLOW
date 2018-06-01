public static String s1r0(String text,String key){
    char[] output=new char[text.length()];
    for(int c=0;c<text.length();c++){
        int toAdd=key.toUpperCase().charAt(c%4)-'A';
	if(Character.isUpperCase(text.charAt(c)))output[c]=(char)(((text.charAt(c)-'A')+toAdd)%26+'A');
	else if(Character.isLowerCase(text.charAt(c)))output[c]=(char)(((text.charAt(c)-'a')+toAdd)%26+'a');
	else output[c]=text.charAt(c);
    }
    return new String(output);
}