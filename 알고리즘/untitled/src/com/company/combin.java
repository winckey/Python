package com.company;

import java.util.LinkedList;
import java.util.Queue;

public class combin {

    public static void main(String[] args) {
        int [] test = 	{1,2,3,4,5};
        Solution.solution(test);
    }

    protected static class Pair{
        int x;
        int y;
        Pair(int x,int y ){
            this.x=x;
            this.y=y;
        }
    }

    static class Solution {

        static  boolean visited[];


        public static int solution(int[] maps) {

            visited = new boolean[maps.length];

            combine(maps , 0 , 0 , 4);
            return 0;
        }

        public static void combine(int[] maps, int start, int count, int endCount){

            if(count == endCount)
            {
                for (int i = 0; i < visited.length; i++) {
                    if (visited[i])
                    {
                        System.out.print(maps[i] + " "  );
                    }
                }
                System.out.println();
                return;
            }


            for (int i = start; i <  maps.length; i++) {
          
                visited[i] = true;
                combine(maps , i+1 , count+1 , endCount);
                visited[i] = false;
            }
        }
    }
}
