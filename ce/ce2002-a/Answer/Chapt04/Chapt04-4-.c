Call : a = ReadPoly();

PolyPointer ReadPoly()
{ /*read the polynomial into a chain */
  PolyPointer front, rear, temp;
  float coefficient;
  int exponent;
  front = rear = NULL;
  printf("Enter an exponent Less than 0 to quit: \n");
  printf("Coefficient, Exponent: ");
  scanf("%f,%d", &coefficient, &exponent);
  while (exponent >= 0)
  {
    temp = (PolyPointer)malloc(sizeof(struct PolyNode));
    temp->coef = coefficient;
    temp->expon = exponent;
    temp->link = NULL;
    if (!front)
      front = temp;
    else
      rear->link = temp;
    rear = temp;
    printf("Coefficient, Exponent: ");
    scanf("%f,%d", &coefficient, &exponent);
  }
  return front;
}

Call : result = evalPoly(x0, a);

float evalPoly(float x0, PolyPointer ptr)
{ /*evaluate the polynomial at point x */
  PolyPointer temp;
  float result = 0;
  for (temp = ptr; temp; temp = temp->link)
    result = result + temp->coef * pow(x0, temp->expon);
  return result;
}

Call : a = ReadPoly();

PolyPointer ReadPoly()
{ /*read in the polynomial */
  PolyPointer node, c;
  float coefficient;
  int exponent;

  node = GetNode();
  node->coef = -1.0;
  node->expon = -1;
  node->link = node;
  printf("Enter an exponent < 0 to quit: ");
  printf("\nCoefficient, Exponent: ");
  scanf("%f,%d", &coefficient, &exponent);
  while (exponent >= 0)
  {
    c = GetNode();
    c->coef = coefficient;
    c->expon = exponent;
    c->link = node->link;
    node->link = c;
    printf("Coefficient, Exponent: ");
    scanf("%f,%d", &coefficient, &exponent);
  }
  return node;
}

Call : printf("\nAt %f the polynomial is: %5.2f\n", x0, evalPoly(x0, a));

float evalPoly(float x0, PolyPointer ptr)
{ /*evaluate the polynomial */
  PolyPointer c;
  float result = 0;
  for (c = ptr->link; c != ptr; c = c->link)
  {
    result = result + c->coef * pow(x0, c->expon);
    printf("%f, %d\n", c->coef, c->expon);
  }
  return result;
}