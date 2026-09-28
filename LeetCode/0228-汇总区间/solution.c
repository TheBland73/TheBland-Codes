/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//关于sprintf 和 malloc

char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    char** res = malloc(sizeof(char*) * numsSize);
    *returnSize = 0;
    if (numsSize == 0) return res;

    int i = 0;
    while (i < numsSize){
        int j = i;
        while (j + 1 < numsSize && nums[j + 1] == nums[j] + 1) j++;

        res[*returnSize] = malloc(32);
        if (i == j)
            sprintf(res[*returnSize],"%d",nums[i]);
        else
            sprintf(res[*returnSize],"%d->%d",nums[i],nums[j]);
        (*returnSize++);

        i = j + 1;
    }
    return res;
}
