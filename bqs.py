#!/usr/bin/env python3

import dataclasses
import concurrent.futures
import time

from collections.abc import Sequence

@dataclasses.dataclass
class Item:
    """Single key-value result."""
    key: int
    value: str

def stub_method(keys: list[int]) -> tuple[Item]:
    """Fake RPC for a lookup."""
    time.sleep(1)
    return tuple(Item(key=k, value='V'+str(k)) for k in keys)

def do_all(keys: Sequence[int], chunk: int, concurrency: int) -> dict[int, str]:
    """Processes all of the items."""
    outcome = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        promises = []
        for s in range(0, len(keys), chunk):
            promises.append(pool.submit(stub_method, keys[s:s+chunk]))
        for items in concurrent.futures.as_completed(promises):
            for i in items.result():
                outcome[i.key] = i.value
    return outcome

def main():
    original = list(range(1000))
    chunk = 7
    concurrency = 16
    print(do_all(original, chunk, concurrency))
    
if __name__ == "__main__":
    main()
