# Count the vote three ways

The room schedule is settled. Now imagine that the event committee has time for one opening activity: A, an art demonstration; B, a repair demonstration; or C, a community-history presentation. The committee got twelve ranked ballots. It can name a winner without collecting another ballot, but it cannot do that without deciding what the word *winner* means.

**First attempt.** Find the option with the most first choices. Then cross out the option with the fewest first choices and recount. Finally, compare each pair, treating the third option as if it were never on the ballot. Record what each count used and what it ignored.

| Number of ballots | First choice | Second choice | Third choice |
| ---: | --- | --- | --- |
| 5 | A | B | C |
| 4 | C | B | A |
| 3 | B | C | A |

## Plurality: count first choices

A has five first choices, C has four, and B has three. **A wins by plurality.** Plurality rewards the largest first-choice count even when it falls short of a strict majority, which means more than half. Five of twelve is less than half. Saying that A led the count is accurate; saying that most voters put A first is not.

This rule uses exactly one entry per ballot. It can be tallied without learning the other preferences. That simplicity also means it leaves the difference between a voter's second and last choices unused.

## Instant runoff: transfer after elimination

For the event's **instant-runoff** rule, count each ballot for its highest-ranked option that is still in the running. Stop when an option has more than half of the continuing ballots. Otherwise eliminate the option with the fewest votes and repeat. The example has no tie; a complete event rule would have to say what to do in a tie and when no ballots remain. Ranked-choice elections can use comparable elimination and transfer mechanics; consult the rules for the specific election rather than assuming they match this classroom rule. The [Maine Secretary of State’s voter materials](https://www.maine.gov/sos/elections-voting/resources-for-ranked-choice-voting) explain the transfer step with sample ballots.

Nobody has a majority in the first round. B has the fewest first choices and is eliminated. Each of its three ballots ranks C next. A keeps five and C rises to seven. The sum stays twelve: the ballots moved, and none was added or counted twice. **C wins the instant runoff, 7–5.**

An option that has few first choices can be eliminated before the count ever asks whether most voters would prefer it to one of the finalists. B is about to show why that matters.

## Head to head: compare each pair

A head-to-head comparison asks only which of two options each ballot ranks higher. For A versus B, the five ballots that start with A prefer A. The four C-first ballots and three B-first ballots all place B above A. Therefore B wins 7–5. For C versus B, the four C-first ballots prefer C; the other eight prefer B. Thus B wins 8–4. For completeness, C beats A 7–5.

| Pair | Voters preferring the first option | Voters preferring the second |
| --- | ---: | ---: |
| B versus A | 7 | 5 |
| B versus C | 8 | 4 |
| C versus A | 7 | 5 |

An option that beats every other option head to head is a **Condorcet winner**. Here that is **B**. It won both comparisons even though it would be eliminated first under the event's instant-runoff rule. A head-to-head majority can cycle: with one ballot each for A > B > C, B > C > A, and C > A > B, A beats B, B beats C, and C beats A, each 2–1. There is no Condorcet winner in that profile. An organizer who asks for one winner still needs to say what happens when no such option exists.

## The right winner with the wrong evidence

Change one of the three B > C > A ballots to a ballot that lists only B. The first round is unchanged. After B leaves, two of its ballots transfer to C. The B-only ballot has no remaining ranked option; under the event's rule it **exhausts**. The final tally is A 5, C 6, exhausted 1. Those numbers reconcile to the twelve originally cast.

A fictional assistant summary says, “C wins with six of twelve ballots, a strict majority.” Preserve the right result and repair its reason. Six of twelve is exactly one half. Six of eleven continuing ballots is greater than one half, so C wins under the stated rule. The receipt needs both denominators, not a rounded percentage that hides the missing ballot.

## Transfer

1. **Trace a new transfer.** Return to complete ballots. Change one B > C > A ballot to B > A > C. Tally both runoff rounds. If the final pair ties, identify the provision needed before the committee can name a winner.
2. **Audit a different committee.** A fictional library has six ballots for R > T > S, five for S > T > R, and four for T > R > S. An assistant claims R wins both instant runoff and head to head because R has the most first choices. Keep any supported part; correct the rest. Show which ballots move and independently count T versus each opponent.
3. **Defend a rule before seeing ballots.** For the event poster, state whether the committee aims to favor first-choice support, use an elimination process, or elect a head-to-head winner when one exists. Specify what happens if there is a tie or the ballots do not rank every option. Name one result that the rule does not guarantee.

Explain your tally aloud without the worked example: identify the counting rule, trace the ballots used, and correct one statement the arithmetic cannot support. If you ask an assistant to critique your work afterward, give it only fictional ballots and check each proposed correction against your own count.
