/**
 * 2798. Number of Employees Who Met the Target
 * https://leetcode.com/problems/number-of-employees-who-met-the-target/
 * Difficulty: Easy  Topic: Array
 *
 * Return the count of employees whose hours >= target.
 */
int numberOfEmployeesWhoMetTarget(int *hours, int hoursSize, int target) {
    int res = 0;
    for (int i = 0; i < hoursSize; i++)
        if (hours[i] >= target) res++;
    return res;
}
