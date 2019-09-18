#define min(a,b) (a>b)?b:a

// Dynamic priogramming solution.
int mincostTickets(int* days, int daysSize, int* costs, int costsSize){
  int calSize = 366;
  int calendar[calSize]; // Will be set to 1 on days we need to travel.
  int durations[costsSize]; // Will store the dorations of each day
  int minCost[calSize]; // Will store the lowest possible cost on day i.
  // Initialize calendar.
  for (int i = 0; i < calSize; i++)
    calendar[i] = 0;
  for (int i = 0; i < daysSize; i++)
    calendar[*(days + i)] = 1;
  // initialize durations/
  durations[0] = 1;
  durations[1] = 7;
  durations[2] = 30;
  // Compute min cost from day 1 to 365.
  minCost[0] = 0;
  for (int i = 1; i < calSize; i++)
    if (calendar[i]) { // If we need to travel on this specific day.
      // Check the lowest cost of the 3 options if we would've bought a ticket x days ago.
      minCost[i] = minCost[i-durations[0]]+costs[0]; 
      for (int j = 1; j < costsSize; j++)
          minCost[i] = min(
                        costs[j]+minCost[(i < durations[j])?0:i - durations[j]],
                        minCost[i]
                      );
    } else
      minCost[i] = minCost[i-1];
  return minCost[365];
}
