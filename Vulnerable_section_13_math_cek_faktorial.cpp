 #include <cassert>
 #include <iostream>
 
 /**
  * @param n angka faktorial yang ingin di cek
  * @return jika faktorial maka kembali nilai true
 */
bool adalah_faktorial(uint64_t n) {
     if (n <= 0) {
         return false;
     }
    for (uint32_t i = 1;; i++) {
         if (n % i != 0) {
             break;
         }