package com.company.프로그래머스_네트워크;


import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class NetWork {

    public static void main(String[] args) {

          Solution solution = new Solution();
        System.out.println(solution.solution(3, new int[][]{{1, 1, 0},{1, 1, 0},{0, 0, 1}}));
        System.out.println(solution.solution(3, new int[][]{{1, 1, 0},{1, 1, 1},{0, 1, 1}}));

    }

    static class Solution {
        int [] len;
        int [] visit;
        int[][] map;
        public int solution(int n, int[][] computers) {

            visit = new int[n];


            Queue<Integer> queue = new LinkedList<>();
            int count =0;
            for (int k = 0; k < n; k++) {
                if (visit[k] ==0 ) {
                    queue.add(k);
                    visit[k] = 1;
                    while (!queue.isEmpty()) {
                        int temp = queue.poll();

                        for (int i = 1; i < n; i++) {
                            if (computers[temp][i] != 0 && visit[i] == 0) {
                                visit[i] = 1;
                                queue.add(i);
                            }


                        }
                    }
                    count++;
                }
            }









            return count;
        }
    }
}
