"""Checks for the G2 2024-25 and A2 2025-26 additions."""
import subprocess, tempfile, os
from check_ch8 import vg
E = [(1,2),(1,3),(3,4),(3,5),(4,5),(5,6),(5,7),(6,9),(7,8),(7,9),(8,9),(9,10),(9,11),(10,11),(2,12),(11,12)]
print('discount', vg(E))
src = r'''
#include <stdio.h>
#include <string.h>
static int capped;
float calculate_discount(float total_amount, int is_member, char coupon_code[]) {
    capped = 0;
    if (total_amount <= 0) return 0;
    float discount = 0;
    if (is_member) discount += total_amount * 0.1;
    if (strcmp(coupon_code, "SAVE20") == 0) discount += total_amount * 0.2;
    else if (strcmp(coupon_code, "SAVE10") == 0) discount += total_amount * 0.1;
    float max_discount = total_amount * 0.3;
    if (discount > max_discount) { discount = max_discount; capped = 1; }
    return total_amount - discount;
}
int main(void) {
    struct { float t; int m; char *c; } tc[] = {{0,0,"NONE"},{100,0,"NONE"},{100,1,"NONE"},{100,1,"SAVE20"},{100,1,"SAVE10"},{200,1,"SAVE20"},{3,1,"SAVE20"}};
    for (int i = 0; i < 7; i++) { float r = calculate_discount(tc[i].t, tc[i].m, tc[i].c); printf("%g %d %s -> %.7g capped=%d\n", tc[i].t, tc[i].m, tc[i].c, r, capped); }
    int n = 0; for (int t = 1; t <= 100000; t++) { calculate_discount(t, 1, "SAVE20"); n += capped; }
    printf("capped for %d of totals 1..100000 (member, SAVE20)\n", n);
    return 0;
}'''
d = tempfile.mkdtemp(); open(os.path.join(d, 'd.c'), 'w').write(src)
subprocess.run(['gcc', '-O0', '-o', os.path.join(d, 'd'), os.path.join(d, 'd.c')], check=True)
print(subprocess.run([os.path.join(d, 'd')], capture_output=True, text=True).stdout)
# exact arithmetic: member + SAVE20 = 0.1t + 0.2t = 0.3t = cap, never greater
from fractions import Fraction as F
print('exact cap reachable:', any(F(1,10)*t + F(2,10)*t > F(3,10)*t for t in range(1, 1000)))
