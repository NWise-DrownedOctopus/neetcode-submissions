class Solution {
    public int maxProfit(int[] prices) {
        int[] profits = new int[prices.length];

        // Ok so we need to find the best time to buy and sell. In other words max(prices[sell] - prices[buy])
        // We can find the minimum, but that won't necissarially give us the highest delta between buy and sell
        // How could we find the delta. We could maybe do something with two points. Look at a value and then find the best delta in the rest of the
        // array and stash that delta in an array. We could then just grab the max from that array and return it as our profit.
        int firstIndex = 0;
        int secondIndex = 1;
        int max = 0;
        // ok so we start with the first index, we check ever other index for a profit, if that is better than the current entry, we update the value
        // We keep doing this until we get to the end
        while (firstIndex <= prices.length - 2) {
            while(secondIndex <= prices.length - 1) {
                int profit = prices[secondIndex] - prices[firstIndex];
                if (profit > profits[firstIndex]) {
                    profits[firstIndex] = profit;
                    if (profit > max) {
                        max = profit;
                    }
                    
                }                
                secondIndex += 1;
            }

            firstIndex += 1;
            secondIndex = firstIndex + 1;            
        }

        return max;
    }
}
