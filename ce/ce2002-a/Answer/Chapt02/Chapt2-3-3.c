double peval(float x, polynomial terms[], int n)
{ /*evaluate the polynomial for x */
  int i;
  float answer = 0;
  for (i = 0; i < n; i++)
    answer = answer + terms[i].coef * pow(x, terms[i].expon);
  return answer;
}