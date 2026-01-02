#!/usr/bin/env python3
import sys
input = sys.stdin.buffer.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    

    
def main():
    T = int(input())  # set to int(input()) if multiple test cases
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()


import heapq
import sys

def can_kill_all(monsters, K):
    """
    monsters: list of tuples (h, p)
    K: initial attack power (int)
    returns: True if Genos can kill all monsters, False otherwise
    """
    if not monsters:
        return True

    # Map power -> min-heap of healths for that power
    power_to_heap = {}
    # Global heap by health to pop dead monsters quickly: (health, power)
    health_heap = []

    # Alive counts per power (for quick removal from power map)
    from collections import Counter
    power_count = Counter()

    for (h, p) in monsters:
        if p not in power_to_heap:
            power_to_heap[p] = []
        heapq.heappush(power_to_heap[p], h)
        heapq.heappush(health_heap, (h, p))
        power_count[p] += 1

    # Use a sorted container of powers to get current min power quickly.
    # Python has no built-in ordered map; we will keep a min-heap of powers and
    # lazily remove powers with zero count when popped.
    powers_min_heap = list(power_to_heap.keys())
    heapq.heapify(powers_min_heap)

    total_alive = len(monsters)
    S = 0          # cumulative damage applied to each monster so far
    Kcur = K       # current attack damage

    # helper to clean top of powers_min_heap until it has a positive count
    def get_current_min_power():
        while powers_min_heap:
            p = powers_min_heap[0]
            if power_count.get(p, 0) <= 0:
                heapq.heappop(powers_min_heap)
                continue
            return p
        return None

    # Remove all monsters whose health <= S (already dead)
    def remove_dead_by_S():
        nonlocal total_alive
        while health_heap and health_heap[0][0] <= S:
            h0, p0 = heapq.heappop(health_heap)
            # it's possible this (h0,p0) has been logically removed earlier,
            # but we guard by checking count in that power's heap top.
            # We also need to pop it from the corresponding power_to_heap.
            if power_count.get(p0, 0) <= 0:
                continue
            # Remove this exact health from power_to_heap[p0] (it must be there)
            # The heap at power_to_heap[p0] may have elements <= S; pop them.
            while power_to_heap[p0] and power_to_heap[p0][0] <= S:
                heapq.heappop(power_to_heap[p0])
                power_count[p0] -= 1
                total_alive -= 1
            if power_count[p0] <= 0:
                # will be lazily removed from powers_min_heap in get_current_min_power
                pass

    # sum of AP for m attacks when decrement per attack is 'p' and starting at Kcur:
    # D(m) = m*Kcur - p * m*(m-1)//2
    def D_of_m(m, Kstart, p):
        return m * Kstart - (p * m * (m - 1)) // 2

    # Binary search minimal m in [1, tmax] such that D(m) >= req
    def min_attacks_to_reach(req, Kstart, p):
        # if req <= 0, zero attacks needed (we handle earlier as removal)
        if req <= 0:
            return 0
        # maximum positive attacks until K would become <= 0 after the last attack:
        # Kstart - (t-1)*p > 0  => t <= floor((Kstart + p - 1)/p)
        if p == 0:
            # if p == 0, K doesn't decrease. Then required m = ceil(req / Kstart) if Kstart>0.
            if Kstart <= 0:
                return None
            return (req + Kstart - 1) // Kstart
        tmax = (Kstart + p - 1) // p
        if tmax <= 0:
            return None
        lo, hi = 1, tmax
        ans = None
        while lo <= hi:
            mid = (lo + hi) // 2
            if D_of_m(mid, Kstart, p) >= req:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    # Main loop
    while total_alive > 0:
        # Clean up monsters already dead due to previous S
        remove_dead_by_S()
        if total_alive == 0:
            return True

        if Kcur <= 0:
            # can't deal positive damage anymore, and monsters remain
            return False

        p = get_current_min_power()
        if p is None:
            # no more powers alive
            return True

        # Ensure the group's heap is clean of dead entries
        group_heap = power_to_heap.get(p, [])
        while group_heap and group_heap[0] <= S:
            heapq.heappop(group_heap)
            power_count[p] -= 1
            total_alive -= 1
        if power_count[p] <= 0:
            # group exhausted, loop to next min power
            continue
        # smallest health among monsters that have the minimal power p
        min_h_in_group = group_heap[0]
        req = min_h_in_group - S
        # find minimal attacks needed to kill at least one in this group
        m = min_attacks_to_reach(req, Kcur, p)
        if m is None:
            # even doing all positive attacks cannot kill this group -> fail
            return False
        # Apply m attacks
        add_damage = D_of_m(m, Kcur, p)
        S += add_damage
        Kcur -= m * p
        # After applying, clean dead monsters (will remove from both heaps)
        remove_dead_by_S()
        # continue loop

    return True

# Example usage / small driver
if __name__ == "__main__":
    it = iter(data)
    n = int(next(it))
    K = int(next(it))
    monsters = []
    for _ in range(n):
        h = int(next(it)); p = int(next(it))
        monsters.append((h, p))
    print("YES" if can_kill_all(monsters, K) else "NO")

