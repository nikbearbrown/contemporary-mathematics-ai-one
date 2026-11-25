# Check the average and the downside

An outdoor activity could raise more for the community event than an indoor activity. It could also leave the event short of what it owes. Imagine the group has two offers. Neither the attendance predictions nor the costs are observations about a real event.

| Choice | State | Assumed probability | Event receipts | Event costs in that state |
| --- | --- | ---: | ---: | ---: |
| Outdoor | Dry | 3/4 | $360 | $240 |
| Outdoor | Wet | 1/4 | $70 | $240 |
| Indoor | Either | 1 | $200 | $175 |

**First attempt.** Compute the outdoor result in each state, and then its weighted average. Compare with the indoor result. Would you change your choice if the event could cover at most $100 of loss? Write down your rule before you look at the result.

## An average is not a possible receipt

Take costs out before averaging. Dry outdoors yields $120. Wet outdoors yields a $170 loss. The weighted average, called the **expected value**, is (3/4 × $120) + (1/4 × −$170) = $47.50. Indoors yields $25 in either state by assumption. The probabilities sum to one, and both dollar inputs describe net results for the same event.

No row pays $47.50. The average lets you compare a model of the alternatives, not treat the result as spendable cash. In this model the outdoor plan loses $170 with probability 1/4. The indoor plan satisfies a $100 loss limit in both modeled states; the outdoor plan fails it. If the loss limit is a hard constraint, filter out the outdoor choice before ranking by expected value. A policy based on expected value alone ranks the choices the other way.

You can also ask which assumption moves the ranking. Let p be the probability of dry weather. The outdoor expectation is 120p − 170(1 − p), or 290p − 170 dollars. It equals the indoor result when p = 195/290 = 39/58, about 67.2%. Above that probability outdoor has the higher expected value; below it indoor does. Even a dry-weather estimate above that boundary does not remove the modeled wet-weather loss. Changing the probability and changing the consequences are two different interventions.

## Do not promote a count into a forecast

Suppose six of eight past events with recorded conditions were dry. The observed fraction is 6/8, or 3/4. It says what happened in those eight records. Treating it as the chance that your event is dry assumes those dates and venue conditions tell you something about this event. A different month, missing reports from cancellations, or overlapping events in one weather spell could weaken that inference. If only the eight-event count is known, use 3/4 as a scenario assumption and check a plausible alternative such as 1/2. At 1/2, the outdoor expected value is −$25, not $47.50.

## Write the base next to the percentage

Suppose next season's shelter estimate starts at $240. Compare two invented budgeting rules over two increases.

| Rule | Now | After one increase | After two increases |
| --- | ---: | ---: | ---: |
| Add $24 each time | $240.00 | $264.00 | $288.00 |
| Add 10% of the current estimate each time | $240.00 | $264.00 | $290.40 |

The first changes the amount by the same number of dollars. The second changes it by the same fraction of its current level: multiply by 1.10 at each step. In the second period 10% of $264 is $26.40, not $24. Neither rule says what a vendor will actually charge. For a decision about a quote, use the time period and price terms the quote actually specifies.

A fictional assistant writes, “Ten percent twice is twenty percent, so both rules end at $288.” Draw two arrows for the compounded path and write the amount beneath each. The first increase is 10% of $240; the second is 10% of $264. Over the two steps, $290.40 is 21% above $240. Addition works for the fixed-dollar plan, not for percentages taken from different bases.

## Transfer

1. **Change a probability.** Keep the cash amounts fixed but assume a dry probability of 2/3. Compute both expected values. Which offers more under this criterion, and which passes the $100 loss limit?
2. **Change the consequence.** A sponsor offers to cover $80 of the outdoor loss in wet weather only. With the original probabilities, compute the new loss and expected value. State a nonmathematical condition you would check before treating the support as real.
3. **Change the planning horizon.** Extend both shelter estimates to a third increase. Put the cost, its difference from $240, and the percentage above $240 in separate columns.

For the event poster, report the expected value and the downside separately. Show one boundary or changed assumption, and tell the committee which would make you reconsider.
