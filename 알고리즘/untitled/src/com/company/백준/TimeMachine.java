package com.company.백준;

import com.company.프로그래머스_순위.Ranking;

import java.io.*;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;

public class TimeMachine {

    static int N, M;

    static int[][] dist; // 자료형을 int로 할 경우 오버플로우 발생함.
    static final int INF = 987654321;
    private static int[][] map;

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); // 도시의 개수
        M = Integer.parseInt(st.nextToken()); // 버스 노선의 개수
        map  = new int[N+1][N+1];
        dist = new int[N+1][N+1];
        Arrays.fill(map , 9999);
        Arrays.fill(dist , 9999);
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()); // 도시의 개수
            int y = Integer.parseInt(st.nextToken()); // 버스 노선의 개수
            int time = Integer.parseInt(st.nextToken()); // 버스 노선의 개수
            map[x][y] = time;
        }




        System.out.println(N);

        

    }

    public static void solve(int num, int[][] adj, int src, int dst) {
        int[] dists = new int[num];
        Arrays.fill(dists, INF);
        dists[src] = 0;

        for(int v=0; v < num; ++v) {
            for(int w=0; w < num; ++w) {
                if(adj[v][w] != INF)
                    dists[w] = Math.min(dists[w], dists[v] + adj[v][w]);
            }
        }

        for(int i=0; i< num; ++i)
            System.out.println(dists[i]);
    }
}