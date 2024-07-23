/**
 * @file mathlib.c
 * @brief This file contains mathematical utility functions.
 *
 * @author Jim Tsao
 * @date 2024-07-07
 */

#include <stdio.h>

/**
 * @brief This function returns the larger of two integer arguments.
 *
 * @param[in] a The first integer.
 * @param[in] b The second integer.
 * @return The larger value of a and b.
 */
int max (int a, int b) 
{
  return (a > b) ? a : b;
}

/**
 * @brief This function returns the smaller of two integer arguments.
 *
 * @param[in] a The first integer.
 * @param[in] b The second integer.
 * @return The smaller value of a and b.
 */
int min (int a, int b) 
{
  return (a < b) ? a : b;
}
