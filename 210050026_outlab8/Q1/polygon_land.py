def minCost(values):
    r"""
        This function accepts list
        It returns the result as cost.
    """
    if len(values) < 3:         # minCost is 0 if number of values < 3
        return 0
    costs = []               # list to store all Cost
    for i in range(1,len(values)-1):
        min_cost1 = minCost(values[i:len(values)])      
        min_cost2 = minCost(values[:i+1])
        min_cost = values[0]*values[len(values)-1]*values[i]
        costs.append(min_cost1 + min_cost2 + min_cost)
    return min(costs)


if __name__ == "__main__":
    import argparse
    CLI=argparse.ArgumentParser()
    CLI.add_argument("--values",  nargs="*",  type=int, default=[1, 2, 3])
    args = CLI.parse_args()
    print("values: %r" % args.values)
    cost = minCost(args.values)
    print(cost)