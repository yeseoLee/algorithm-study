import java.util.Arrays;

class Solution {
    int answer = 0;
    int[] primeArray;
    int[] nums;
    public int solution(int[] nums) {  
        this.nums = nums;
        primeArray = getprimeArray(3000);
        pickThreeNum(0,0,0);
        return answer;
    }

    void pickThreeNum(int idx, int cnt, int sum){
        if (cnt == 3){
            if(primeArray[sum] == 1){
                this.answer += 1;
            }
            return;
        }
        if (idx < nums.length){        
            pickThreeNum(idx+1, cnt+1, sum+nums[idx]);
            pickThreeNum(idx+1, cnt, sum);
        }
    }

    int[] getprimeArray(int size){
        int[] primeArray = new int[size+1];
        if (size <= 1) {
            return primeArray;
        }
        Arrays.fill(primeArray,1);

        primeArray[0]=0;
        primeArray[1]=0;
        for (int i=2; i<(int) Math.sqrt(size); i++){
            for (int j=2*i; j < size+1; j+=i) {
                primeArray[j]=0;
            }
        }
        return primeArray;
    }
}
