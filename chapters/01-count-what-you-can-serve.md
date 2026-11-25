# Count what you can serve

The event committee wants to hand out 87 meals. A quote promises sealed trays, each with 1.5 liters of soup. Someone replies, “Order 13 trays. That’s 19.5 liters, plenty for 87.” Before you agree, ask what unit the word *plenty* is doing the work of.

**First attempt.** Assume one 240-milliliter portion per person and a 1,000-milliliter reserve that nobody can serve without a release. Trays must be ordered whole. Find the smallest order that supplies the portions and keeps the reserve. Write the equation with its units, then check the next smaller order. Do this before reading past the table.

| Item | Quantity | What it counts |
| --- | ---: | --- |
| Confirmed meal requests | 87 people | One portion for each request |
| Portion size | 240 mL per person | Volume to serve |
| Tray content | 1.5 L per tray | Volume purchased |
| Reserve | 1,000 mL | Volume not planned for serving |

## Put every volume on the same scale

Convert the tray, not the people: one tray contains 1,500 mL. Multiply 87 people by 240 mL/person; the people cancel and the result is 20,880 mL. The reserve is not an extra person. It is a separate 1,000 mL that must still be there after serving. Therefore the purchased volume has to reach at least 21,880 mL.

Fourteen trays offer 21,000 mL; fifteen offer 22,500 mL. That proves fifteen works and fourteen fails. The order is not the nearest integer to a quotient. It is the first integer at or above a threshold. If you simply round what looks close, you can buy less soup than the commitments require. Checking the two neighboring orders also catches a calculator set to the wrong rounding rule.

An estimate makes a good second check. Twenty liters is enough for fewer than 84 portions at 240 mL, even before the reserve. So thirteen trays and 19.5 liters cannot be enough. The rough check does not give the exact order; it does expose the confident wrong answer quickly.

## Left over does not mean available

Fifteen trays leave 1,620 mL after the named 87 meals. Of that, 1,000 mL is reserved and 620 mL is uncommitted. At most two *additional full* portions can be offered with the reserve intact. A third would require 720 mL, 100 mL more than is available. Recomputing only at the end matters: rounding every tray to six portions before combining would suggest 90 total portions, but the problem permits pouring from adjacent trays. If service rules forbid combining remainders, model that restriction and calculate again.

Now inspect a fictional assistant answer: “Raise the portion to 250 mL; you still have the same extra capacity because 250 is only 10 more than 240.” The change is 10 mL **per person**. For 87 portions, that is 870 mL. Fifteen trays after reserve provide 21,500 mL, enough for exactly 86 portions at 250 mL. You would need sixteen trays to honor all 87 requests and protect the reserve. The small difference at the ladle lives inside a multiplication; the whole-tray outcome makes the error visible.

## Transfer

1. Set a 1,200 mL reserve and leave the portion size at 240 mL. Check the smallest feasible order, the maximum new full servings and the exact spare volume.
2. Suppose a vendor advertises “serves six” but only guarantees 1.4 L. Decide whether the label proves six of your 240 mL portions can be served from each tray. State what verified quantity replaces the label in your calculation.
3. Define two groups: confirmed reservations and walk-ins. Design a condition that decides which walk-ins can be served without using the reserve. Explain why two reservations recorded under the same person might invalidate the count. Do not infer anything about a person the ledger does not establish.

Write a brief recommendation that someone could audit: named inputs, common units, a whole-number boundary and a condition that would change the recommendation. You may ask a model to invent an alternative after you commit to your own results; use only this fictional situation and test each claim against the thresholds yourself.
