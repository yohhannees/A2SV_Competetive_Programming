
class RestoreIPAddresses {
    public List<String> restoreIpAddresses(String s) {
        if (s.length() < 4 || s.length() > 12) {
            return new ArrayList<>();
        }

        List<String> result = new ArrayList<>();
        LinkedList<String> temp = new LinkedList<>();

        backtrack(result, temp, s);
        return result;
    }

    public void backtrack(List<String> result, LinkedList<String> temp, String s) {
        if (s.length() == 0 && temp.size() == 4) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < temp.size(); i++) {
                sb.append(temp.get(i));
                if (i != temp.size() - 1) {
                    sb.append(".");
                }
            }
            result.add(sb.toString());
        }

        for (int i = 1; i < 4; i++) {
            if (s.length() < i) {
                continue;
            }

            String sliced = s.substring(0, i);
            if ((sliced.length() > 1 && sliced.charAt(0) == '0') || (Integer.parseInt(sliced) > 255)) {
                continue;
            }

            temp.add(sliced);
            String backtrackString = s.substring(i);
            backtrack(result, temp, backtrackString);
            temp.removeLast();
        }
    }
}