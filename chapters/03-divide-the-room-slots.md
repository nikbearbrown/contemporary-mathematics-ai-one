# Divide the room slots

Imagine the same community event has three programs that can use its meeting room. The art group requests five one-hour bookings, the repair group requests three, and the history group requests one. There are four interchangeable hours to give out. No group gets more hours than it asked for, and for now no group is promised a minimum.

**First attempt.** Divide the four hours in proportion to the requests, but give each group a whole number of hours. Write down how you decide what to do with the fractions. Now suppose the custodian opens a fifth hour. Can the group that asked for one hour lose the slot it had? Make a prediction before calculating.

## From fractions to a schedule

Nine requests compete for four slots. Each request carries a share of four ninths of a slot. Multiply that share by a group's requests to get its **quota**, the number of hours it would receive if hours could be divided exactly. Art's quota is 20/9, or 2 + 2/9. Repair gets a quota of 12/9, or 1 + 3/9. History gets 4/9.

The **largest-remainder rule** takes the whole parts first: two, one, zero. Those claims use three slots. The one remaining slot goes to the group whose fraction is largest. Four ninths beats three ninths and two ninths, so history gets the slot. The rule uses all the capacity, and each result is either the whole part of that group's quota or the next integer up, if its quota was fractional. The fraction is a claim to compare, not an extra bookable hour.

| Group | Requests | Four-slot quota | Four-slot allocation | Five-slot quota | Five-slot allocation |
| --- | ---: | ---: | ---: | ---: | ---: |
| Art | 5 | 2 + 2/9 | 2 | 2 + 7/9 | 3 |
| Repair | 3 | 1 + 3/9 | 1 | 1 + 6/9 | 2 |
| History | 1 | 0 + 4/9 | 1 | 0 + 5/9 | 0 |
| Total | 9 | 4 | 4 | 5 | 5 |

The fifth hour increases all three quotas, but that does not protect every allocation. At five slots the whole parts still use only three hours. Two hours remain. Art's 7/9 and repair's 6/9 now outrank history's 5/9, so history drops from one hour to zero. History did not submit a weaker request. The other fractions grew faster. All the totals balance, and every share is still within its quota bounds.

The desired guarantee that no group loses when the total increases, with demands unchanged, is called **house monotonicity**. The failure of this guarantee under largest remainder is commonly called the **Alabama paradox**, from the history of U.S. congressional apportionment. The [U.S. Census Bureau describes Hamilton/Vinton](https://www.census.gov/about/history/historical-censuses-and-surveys/census-programs-surveys/decennial-census/methods.html), a historical application of the same rounding idea. These room bookings are invented, and the event's access rules are not legislative rules.

## Specify the promise before you pick the rule

An organizer might say, “Anyone with an eligible program should get at least one slot.” That is an added constraint, not a correction to the arithmetic. Here is one way to fulfill it in this example. Reserve one slot per group first. The remaining unmet requests are now four for art, two for repair, and zero for history. Apply largest remainder only to those six unmet requests. At four slots there is one left after the reservations, and it goes to art. At five slots there are two left: the whole parts give art one, and repair's remainder 4/6 beats art's 2/6 for the other. The new allocations are (2, 1, 1) and (2, 2, 1). History keeps its hour, and art gets two hours rather than the three it got under the original rule at capacity five. The allocations at five slots are still within the original bounds in this example: art can receive two or three slots, repair can receive one or two, and history can receive zero or one. That need not be true for every set of inputs.

Promising one slot each cannot work if there are more eligible groups than available slots. In that case the organizer needs a different rule or more usable capacity. Also check whether the slots are truly interchangeable. A group can hold an allocation on paper and still have no usable booking if the available hours conflict with its schedule. Separate the number of hours to award from the problem of scheduling actual hours.

For ties, publish the rule before the requests arrive. A fixed order is easy to check, but repeated ties can favor the same program. A documented rotation or draw trades predictability for different treatment over time. The table above needs no tie rule because neither cutoff is tied. Do not explain an untied loss as a tie-break.

## Transfer

1. **Compute.** Requests are now four, three, and two, and six hours are available. Compute the whole parts and compare the remainders using ninths. Check that the allocation uses six slots and respects the quota bounds.
2. **Expose a policy choice.** Two eligible groups with identical requests compete for one slot. Show why proportional arithmetic cannot decide their tie. Propose a procedure the organizer could explain to both groups, and state what would change if the arrangement repeated each month.
3. **Test a claim.** A fictional assistant says, “When everyone’s quota increases, nobody’s final allocation can go down.” Find the smallest piece of the four-to-five-slot calculation that disproves it. Identify one thing the example does *not* prove about all allocation rules.
4. **Defend a rule.** Write a two-sentence policy for the event: first name the access promise, then say how extra hours and ties are handled. Explain what would make that policy infeasible.

For the decision poster, report the weights, the available hours, the exact rule, and one check against a proposed change. If you use an assistant after doing the calculations, ask it to change one assumption and check the resulting table by hand.
