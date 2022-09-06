package com.company.프로그래머스_네트워크;


public class NetWork {

    private static int moneyR;
    long[][] stocksR;


    public static void main(String[] args) {


    }

    class Solution {
        public long solution(int money, long[][] stocks) {
            moneyR = money;
            stocksR = stocks;
            long answer = 0;
            return answer;
        }
    }
    static void combination(int[] arr, boolean[] visited, int start, int n , int sum) {
        if (moneyR <= sum) {
            print(arr, visited, n);
            return;
        }

        for (int i = start; i < n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, n - 1);
            visited[i] = false;
        }
    }
    static void print(int[] arr, boolean[] visited, int n) {
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }
}
