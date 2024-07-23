/**
 * @file test.c
 * @author Jim Tsao 
 * @brief This is the test file
 * @version 0.1
 * @date 2024-07-07
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#include <stdio.h>

/**
 * @brief This function returns the absolute value of the integer argument.
 * 
 * @param[in] a Input integer
 * @return The absolute value of
 */
int abs(int a) {
    if(a < 0)
    {
        a = -a;
    }

  return a;
}