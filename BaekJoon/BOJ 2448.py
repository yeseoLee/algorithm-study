# 골드 4 별찍기-11 https://www.acmicpc.net/problem/2448


def solution(x, y, n):
    ## 가장 작은 단위
    if n <= 3:
        star[x][y] = "*"
        star[x + 1][y - 1] = "*"
        star[x + 1][y + 1] = "*"
        star[x + 2][y - 2 : y + 3] = ["*"] * 5
        return

    # 재귀 호출
    n //= 2
    solution(x, y, n)
    solution(x + n, y - n, n)
    solution(x + n, y + n, n)


n = int(input())
# 가로 6 * (2**k), 세로 3 * (2**k)
star = [[" " for _ in range(n * 2)] for _ in range(n)]
solution(0, n - 1, n)
for i in range(n):
    print("".join(star[i]))

"""
24 (3 * 2**k, k=3)
                       *                        
                      * *                       
                     *****                      
                    *     *                     
                   * *   * *                    
                  ***** *****                   
                 *           *                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****             
           *                       *            
          * *                     * *           
         *****                   *****          
        *     *                 *     *         
       * *   * *               * *   * *        
      ***** *****             ***** *****       
     *           *           *           *      
    * *         * *         * *         * *     
   *****       *****       *****       *****    
  *     *     *     *     *     *     *     *   
 * *   * *   * *   * *   * *   * *   * *   * *  
***** ***** ***** ***** ***** ***** ***** ***** 
"""
