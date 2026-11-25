"""Enumerate all simple paths of the book's small directed example."""
EDGES = [
    ("G", "J", 2, "walk"), ("J", "H", 2, "stairs"), ("J", "E", 1, "walk"),
    ("E", "H", 4, "lift"), ("G", "W", 4, "walk"), ("W", "H", 5, "walk"),
    ("J", "W", 1, "unverified"),
]


def paths(start="G", goal="H", stepfree=False, lift=True, passage=False, wait=0):
    def traverse(vertices, elapsed):
        if vertices[-1] == goal:
            yield elapsed, "".join(vertices)
            return
        for tail, head, time, kind in EDGES:
            if tail != vertices[-1] or head in vertices:
                continue
            if (kind == "stairs" and stepfree or kind == "lift" and not lift
                    or kind == "unverified" and not passage):
                continue
            yield from traverse(vertices + [head], elapsed + time + (wait if kind == "lift" else 0))
    return sorted(traverse([start], 0))


def check():
    assert paths() == [(4, "GJH"), (7, "GJEH"), (9, "GWH")]
    assert paths(stepfree=True) == [(7, "GJEH"), (9, "GWH")]
    assert paths(stepfree=True, lift=False) == [(9, "GWH")]
    assert paths(stepfree=True, lift=False, passage=True) == [(8, "GJWH"), (9, "GWH")]
    assert min(paths(stepfree=True), key=lambda x: len(x[1])) == (9, "GWH")
    assert paths(stepfree=True, wait=1)[0] == (8, "GJEH")
    assert paths(stepfree=True, wait=2) == [(9, "GJEH"), (9, "GWH")]
    assert paths(stepfree=True, wait=3)[0] == (9, "GWH")
    assert paths(start="H", goal="G") == []
    print("9 explicit path checks passed.")


if __name__ == "__main__":
    check()
