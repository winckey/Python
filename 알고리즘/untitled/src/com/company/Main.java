package com.company;

import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void main(String[] args) {
        int [][] test = 	{{1, 0, 1, 1, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 1}, {1, 1, 1, 0, 1}, {0, 0, 0, 0, 1}};
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

        public static int solution(int[][] maps) {
            int answer = 0;
            int[][] visit = new int[maps.length][maps[0].length];
            int[] dx = {0,0,1,-1};
            int[] dy = {1,-1,0,0};

            Queue<Pair> q = new LinkedList<Pair>();
            q.add(new Pair(0,0 ));
            visit[0][0] = 1;

            while(!q.isEmpty()){
                Pair p = q.poll();

                for(int i=0;i<4;i++){
                    int nx = p.x+dx[i];
                    int ny = p.y+dy[i];
                    //경계값
                    if(nx < 0 || nx > maps.length-1 || ny < 0 || ny > maps[0].length-1)
                        continue;
                    else {
                        // 갈수있는 지역이면서 가지않은곳
                        if(maps[nx][ny]==1 && visit[nx][ny]==0){

                            q.add(new Pair(nx,ny));

                            visit[nx][ny]=visit[p.x][p.y]+1;
                        }
                    }
                }
            }
            System.out.println(visit[maps.length-1][maps[0].length-1]);
            for (int i = 0; i < maps.length ; i++) {
                for (int j = 0; j < maps[0] .length; j++) {
                    System.out.print(visit[i][j]+" ");
                }
                System.out.println();
            }
            System.out.println(visit[maps.length-1][maps[0].length-1]);
            return visit[maps.length-1][maps[0].length-1]>0?visit[maps.length-1][maps[0].length-1]:-1;
        }
    }
}
