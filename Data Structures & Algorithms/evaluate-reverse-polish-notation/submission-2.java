class Solution {
    public int evalRPN(String[] tokens) {
        int final_value = Integer.parseInt(tokens[0]);

        ArrayList<Integer> stack = new ArrayList<>();

        for(int i = 0; i < tokens.length; i++) {
            try {
                stack.add(Integer.parseInt(tokens[i]));
            } catch (NumberFormatException e) {
                int second_term = stack.remove(stack.size() - 1);
                int first_term = stack.remove(stack.size() - 1);

                if (tokens[i].equals("+")) {
                    final_value = first_term + second_term;
                } else if (tokens[i].equals("-")) {
                    final_value = first_term - second_term;
                } else if (tokens[i].equals("*")) {
                    final_value = first_term * second_term;
                } else if (tokens[i].equals("/")) {
                    final_value = first_term / second_term;
                }

                // System.out.println(first_term + " " + tokens[i] + " " + second_term + " = " + final_value);
                stack.add(final_value);
            }
        }

        return final_value;
        
    }
}
