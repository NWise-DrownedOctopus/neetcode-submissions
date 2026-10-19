class Solution {
    public int maxArea(int[] heights) {
        // I think we can solve this with two pinter
        // One at the start of the array, and one at the end

        // I would assume the further apart the bars the better ( if all are equal )
        // So let's start by checking the ends storage capacity. We could then test if moving
        // in would make the stroage capacity better, if not we check the other end.

        // We could maybe stash the value moving in and pick which is better. We only need to update
        // the max if we find a better than the first initial storage capacity.
        // Let's start there, and see how things look

        int leftIdx = 0;
        int rightIdx = heights.length - 1;

        System.out.println("Heights: ");
        for (int num: heights) {
            System.out.print(num + " ");
        }
        System.out.println();

        int startingWidth = rightIdx - leftIdx;
        System.out.println("Starting width: " + startingWidth);

        int startingHeight = Math.min(heights[leftIdx], heights[rightIdx]);
        System.out.println("Starting height: " + startingHeight);

        int maxStorage = (startingWidth) * (startingHeight);
        System.out.println("Starting Capacity: " + maxStorage);

        if (heights.length == 2) {
            return maxStorage;
        }
        // Now let's start checking values till we have the index meet one another
        while(true) {
            // Find which next height is smaller, and move that bar
            if(heights[leftIdx] >= heights[rightIdx]) {
                rightIdx -= 1;
            }
            else {
                leftIdx += 1;
            }

            if (leftIdx < 0 || rightIdx > heights.length - 1) {
                return maxStorage;
            }

            // Calculate our updated values with the nex index in place
            int updatedWidth = rightIdx - leftIdx;            
            int updatedStorage = (updatedWidth) * (Math.min(heights[leftIdx], heights[rightIdx]));
            maxStorage = Math.max(updatedStorage, maxStorage);

            if (updatedWidth < 1) {
                return maxStorage;
            }

        }
    }
}
