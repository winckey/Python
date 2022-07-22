package com.company.프로그래머스_순위;


import java.util.LinkedList;
import java.util.Queue;

public class Ranking {

    public static void main(String[] args) {

        Solution solution = new Solution();
        System.out.println(solution.solution("hit" , "cog"	, new String[]{"hot", "dot", "dog", "lot", "log", "cog"}));

    }

    static class Solution {
        int[] len;
        int[] visit;
        int[][] map;
        int targetNum=-1;
        int answer = 0;
        public int solution(String begin, String target, String[] words) {
            map = new int[words.length][words.length];
            visit = new int[words.length];

            int count =0;
            for (int i = 0; i < words.length; i++) {
                for (int j = 0; j < words.length; j++) {
                    if(i != j)
                    {
                        String[] strings1 = words[i].split("");
                        String[] strings2 = words[j].split("");
                        int lenCount =0;
                        for (int k = 0; k <strings1.length; k++) {

                            if(strings1[k].equals(strings2[k]))
                                count++;
                        }
                        if(count >= strings1.length-1)
                        {
                            map[i][j] = 1;
                            map[j][i] = 1;
                        }
                        count=0;
                    }
                }
            }

            for (int i = 0; i < words.length; i++) {
                if(words[i].equals(target))
                {
                    targetNum = i;
                }
            }
            if(targetNum == -1)
                return 0;

            for (int i = 0; i < words.length; i++) {
                String[] strings1 = words[i].split("");
                String[] strings2 = begin.split("");
                int lenCount =0;
                for (int k = 0; k <strings1.length; k++) {

                    if(strings1[k].equals(strings2[k]))
                        count++;
                }
                if(count >= strings1.length-1)
                {
                    answer = minDisd(i);
                }
                count=0;
            }

            return answer;
        }

        public int minDisd(int start ){

            Queue<Integer> queue = new LinkedList<>();

            queue.add(start);
            visit[start] = 1;
            while(!queue.isEmpty()){
                int temp = queue.poll();
                for (int i = 0; i < map.length; i++) {
                    if(map[temp][i] != 0 && visit[i] == 0)
                    {
                        visit[i] = visit[temp]+1;
                        queue.add(i);
                    }
                }
            }
            return visit[targetNum];
        }
    }
}
