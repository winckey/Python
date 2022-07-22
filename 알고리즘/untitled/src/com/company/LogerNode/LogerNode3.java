package com.company.LogerNode;


import java.util.*;

public class LogerNode3 {

    public static void main(String[] args) {

          Solution solution = new Solution();
        System.out.println(solution.solution(6, new int[][]{{2, 3}}));
        System.out.println(solution.solution(2, new int[][]{{2, 1}}));
        System.out.println(solution.solution(4, new int[][]{{1, 2}, {2, 3}, {3, 4}, {4, 1}}));

    }


    static class Solution {
        public int solution(int n, int[][] edge) {
            int[] dist = new int[n+1];
            boolean[][] map = new boolean[n+1][n+1];
            for(int i =0; i<edge.length; i++){
                map[edge[i][1]][edge[i][0]] = map[edge[i][0]][edge[i][1]]= true;
            }

            Queue<Integer> que = new LinkedList<Integer>();
            que.add(1);

            while(!que.isEmpty()){
                int temp = que.poll();
                for(int i = 2; i<n+1; i++){
                    if(map[temp][i]&&dist[i]==0){
                        que.add(i);
                        dist[i] = dist[temp]+1;
                    }
                }
            }

            Arrays.sort(dist);
            int i = dist.length-1;
            for(; i>0; --i){
                if(dist[i]!=dist[i-1]){
                    break;
                }
            }

            return dist.length-i;
        }
    }
}
