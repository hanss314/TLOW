using namespace std;
char ReturnAtbashChar(char charVariable) {
	if (charVariable >= 65 && charVariable <= 90) {       /* If charVariable is an uppercase letter... */
		charVariable = 155 - charVariable;                 /* I found that a quick solution is to subtract charVariable from the sum of the values of A and Z; nifty! */
	}
	if (charVariable >= 97 && charVariable <= 122) {      /* If charVariable is a lowercase letter... (if charVariable isn't a letter, neither of these if statements occur) */
		charVariable = 219 - charVariable;
	}
	return charVariable;
}