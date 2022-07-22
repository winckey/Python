package com.company.LogerNode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class LogerNode2 {

    public static void main(String[] args) {

          Solution solution = new Solution();
        System.out.println(solution.solution(6, new int[][]{{2, 3}}));
        System.out.println(solution.solution(2, new int[][]{{2, 1}}));
        System.out.println(solution.solution(4, new int[][]{{1, 2}, {2, 3}, {3, 4}, {4, 1}}));

    }

    static class Solution {
        public int solution(int n, int[][] vertex) {
            ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
            for (int i = 0; i <= n; i++) {
                graph.add(new ArrayList<>());
            }

            for (int i = 0; i < vertex.length; i++) {
                graph.get(vertex[i][0]).add(vertex[i][1]);
                graph.get(vertex[i][1]).add(vertex[i][0]);

            }

            int[] res = bfs(1, n, graph);;
            Arrays.sort(res);

            // count 중 가장 큰 값이 몇개인지를 반환
            return res[n] == 0 ? n - 1: (int) Arrays.stream(res).filter(i -> i == res[n]).count();

        }

        // BFS 수행
        private int[] bfs(int start, int nodeCount, ArrayList<ArrayList<Integer>> graph) {
            boolean[] visited = new boolean[nodeCount + 1];
            int[] count = new int[nodeCount + 1];
            Queue<Integer> q = new LinkedList<>();
            q.offer(start);
            visited[start] = true;

            while (!q.isEmpty()) {
                int cur = q.poll();

                for (int next : graph.get(cur)) {
                    if (!visited[next]) {
                        q.offer(next);
                        visited[next] = true;
                        count[next] = count[cur] + 1;
                    }
                }
            }
            return count;
        }
    }
}
