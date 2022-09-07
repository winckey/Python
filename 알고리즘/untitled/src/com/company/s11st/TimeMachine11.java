package com.company.s11st;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class TimeMachine11 {

    static int N, M;



    public static void main(String[] args) throws NumberFormatException, IOException {

            Solution solution = new Solution();
        System.out.println(solution.solution(5 ,8));

    }


    static class Solution {
        public int solution(int N, int K) {

            int temp = K;
            int co = N;
            int count =0;
            while(temp > 0){

                if(co <1){
                    break;
                }

                if(co <= temp){
                    temp = temp - co;
                    count ++;
                }
                co--;

            }

            if(temp > 0){
                return -1;
            }
            return count;
        }
    }


}