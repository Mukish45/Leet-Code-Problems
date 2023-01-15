/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize){
    int *ret=(int*)malloc(numsSize*sizeof(int));
    *returnSize=numsSize;
    ret[0]=1;
    for(int i=1;i<numsSize;i++){
        ret[i]=nums[i-1]*ret[i-1];
    }
    int temp=1;
    for(int i=numsSize-1;i>=0;i--){
        ret[i]*=temp;
        temp*=nums[i];
    }
    return ret;
}