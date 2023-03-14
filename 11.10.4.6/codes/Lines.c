#include <stdio.h>
#include <stdlib.h>

void line_intersect(int* n1, int* A1, int* n2, int* A2, double* P) {
  double det = (double)n1[0] * n2[1] - (double)n1[1] * n2[0];
  double x = ((double)A2[1] - (double)A1[1]) * n1[0] - ((double)A2[0] - (double)A1[0]) * n1[1];
  double y = ((double)A2[0] - (double)A1[0]) * n2[1] - ((double)A2[1] - (double)A1[1]) * n2[0];
  P[0] = x / det;
  P[1] = y / det;
}

void matmul(double (*mat1)[2], int* vec, double* result) {
  for(int i=0; i<2; i++) {
    result[i] = 0.0;
    for(int j=0; j<2; j++) {
      result[i] += mat1[i][j] * (double)vec[j];
    }
  }
}

int main() {
  int n1[2] = {1, -7};
  int n2[2] = {3, 1};
  int A1[2] = {-5, 0};
  int A2[2] = {0, 0};
  double P[2];
  double Q[2];
  int m[2] = {0, 1};
  double z[2][2] = {{0, 1}, {-1, 0}};
  double m1[2];
  double m2[2];
  
  line_intersect(n1, A1, n2, A2, P);
  Q[0] = P[0];
  Q[1] = P[1];
  matmul(z, n1, m1);
  matmul(z, n2, m2);
  
  printf("m1 = [%lf, %lf]\n", m1[0], m1[1]);
  printf("m2 = [%lf, %lf]\n", m2[0], m2[1]);
  
  return 0;
}
