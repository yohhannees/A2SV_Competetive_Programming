class Solution {
    public int minFlipsMonoIncr(String s) {
        int zeroes = 0;
        int ones = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '0') {
                zeroes++;
            }
        }
        int output = zeroes;
        for (char ch : s.toCharArray()) {
            if (ch == '0') {
                zeroes--;
            } else if (ch == '1') {
                ones++;
            }
            output = Math.min(output, zeroes + ones);
        }
        return output;
    }
}