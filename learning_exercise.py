def sales_pmf(appt1, appt2, deluxe_sale, std_cost, deluxe_cost):
  '''INPUT:
    appt1: probability of making a sale at appointment one
    appt2: probability of making a sale at appointment two
    deluxe_sale: given a sale, probability of selling a deluxe model
    std_cost: cost of a standard model
    deluxe_cost: cost of a deluxe model

    OUTPUT:
    sales_pmf: dictionary showing probabilities of all possible sales totals
    '''

    import itertools as it
    # All possible probabilities of a sale for each customer
    probs = list(it.product([1 - appt1, appt1 * (1 - deluxe_sale), appt1 * deluxe_sale],
                            [1 - appt2, appt2 * (1 - deluxe_sale), appt2 * deluxe_sale]))
    # All possible sale amounts for each customer
    sales = list(it.product([0, std_cost, delux_cost], [0, std_cost, delux_cost]))
    prob_sales = {p[0] + p[1]: p[0]*s[0] + p[1]*s[1] for p in probs for s in sales}
    total_prob = sum(prob_sales.keys())
    # Normalize the probabilities so it totals is 1.0

    norm_prob_sales = {round( p / total_prob, 4): found(s,2) for p,s in prob_sales.items()}
    return norm_prob_sales
