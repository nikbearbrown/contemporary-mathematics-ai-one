# Check the route before you time it

Suppose the community event promises that a guest can get from the gate to the hall in eight minutes by a step-free route. The floor map shows a lift, a ramp and something that looks like a shortcut. Counting the arrows will not settle the question. Neither will adding the minutes on an arrow the organizer has not checked.

**First attempt.** Find the quickest verified trip for a guest who can use stairs. Next, find the quickest verified step-free trip when the lift works, then when it closes. Keep these three answers separate. For this fictional venue only, use the estimated times below and take verified status as current at the start of the journey.

| From → to | Time (minutes) | What is known |
| --- | ---: | --- |
| Gate (G) → Junction (J) | 2 | Open walk, step-free |
| Junction (J) → Hall (H) | 2 | Open stairs |
| Junction (J) → Lift landing (E) | 1 | Open walk, step-free |
| Lift landing (E) → Hall (H) | 4 | Step-free only while the lift is operating; estimate includes ordinary waiting |
| Gate (G) → West entrance (W) | 4 | Open ramp, step-free |
| West entrance (W) → Hall (H) | 5 | Open entrance, step-free |
| Junction (J) → West entrance (W) | 1 | Possible passage; open and step-free status both unverified |

## Write down the places, arrows and weights

The places are the **vertices** of a graph. An **edge** joins two places in the direction shown by its arrow. The edge's **weight** is the estimated time. A **path** is an unbroken chain of arrows in the correct direction. Cost means elapsed minutes here, so add the weights along the path. The table does not establish travel in the reverse direction or along an unlisted connection.

The checked routes through the graph are easy to exhaust. From the gate, go via the junction or the west entrance. Through the junction, the stairs make G → J → H cost 2 + 2 = 4. Through the junction and lift landing, G → J → E → H costs 2 + 1 + 4 = 7 while the lift operates. Through the west entrance, G → W → H costs 4 + 5 = 9. If the one-minute passage were confirmed, G → J → W → H would cost 2 + 1 + 5 = 8. It stays outside the set of verified routes for now.

The seven-minute lift route has three arrows; the nine-minute ramp route has only two. Counting edges answers the question “How many separate segments do I travel?” It does not answer “How many minutes do I need?” unless each segment costs the same. On this map it gives the wrong choice even after the stairs are removed.

## Decide what's usable, then compare minutes

For a verified step-free route, every edge has to meet three tests: it connects in the right direction, it is step-free, and it is available. A single failing or unverified edge keeps the whole path out of the verified set. When the lift works, the fastest verified step-free route takes seven minutes. When the lift is closed, the only verified step-free path takes nine. A real-world analogue is the [MBTA station pathways specification](https://github.com/mbta/gtfs-documentation/blob/master/reference/gtfs.md#pathwaystxt), which distinguishes pathway types and can associate a pathway with a separate facility status. A path on a map and evidence about its current availability answer different questions.

A fictional assistant writes, “Once the lift closes, go G → J → W → H. That is eight minutes, so we can promise an on-time step-free route.” Keep the sum. Reject the promise. The passage has not been checked, which does not prove it is closed; it means the eight-minute route is conditional. The evidence still supports the nine-minute estimate for the ramp. And a seven- or eight-minute modeled time is not a guarantee about every guest's travel time. A commitment would need an agreed allowance for actual variation, especially if the rule says people must arrive before an activity starts.

The lift has a two-minute advantage over the ramp when it operates. With two extra minutes of waiting, its route costs nine and ties the ramp, if the other segment estimates stay fixed. With more than two extra minutes, the ramp is faster among the verified step-free options. Calling the lift “fastest” without naming its waiting-time assumption blurs an estimate into a property of the building.

## Transfer

1. **Check a link.** A steward confirms that J → W is open and step-free while the lift is closed. Find the quickest verified step-free route and its time. Is it strictly under eight minutes?
2. **Change the objective.** While the lift works, someone prefers fewer separate segments over a shorter travel estimate. For the verified step-free routes, say which one this guest might choose and why.
3. **Check a boundary.** Suppose the ramp route remains at nine minutes. Compute the lift route with one, two and three extra minutes of waiting. For each case give the faster route or report the tie.
4. **Draw only what you know.** Can you promise the return from H to G on this table? Name the data you would need. Explain why a route labeled step-free does not by itself resolve constraints on doorway width, slope, or other needs.

On the event decision poster, present the selected path, its estimated time, one availability assumption, and the fallback if that assumption fails. If you want to see how software handles larger fixed graphs with nonnegative costs, continue with [Represent reachability and cost](https://github.com/nikbearbrown/algorithms-ai-one/blob/main/chapters/02-reachability.md).
