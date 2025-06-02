import random
from collections import deque
import os

class CacheSimulator:
    def __init__(self, cache_size, block_size, associativity, replacement_policy):
        self.cache_size = cache_size
        self.block_size = block_size
        self.associativity = associativity
        self.replacement_policy = replacement_policy

        
        self.num_sets = cache_size // (block_size * associativity)
        self.cache = [deque() for _ in range(self.num_sets)]

        
        self.trace = []
        self.hits = 0
        self.misses = 0
        self.cold_misses = 0
        self.conflict_misses = 0
        self.loaded_blocks = set()
        self.logs = []

    def load_trace(self, logs):
        with open(logs, 'r') as f:
            self.trace = [int(line.strip(), 16) for line in f if line.strip()]

    def get_set_index(self, address):
        return (address // self.block_size) % self.num_sets

    def run(self):
        for i, address in enumerate(self.trace):
            block = address // self.block_size
            set_index = self.get_set_index(address)
            cache_set = self.cache[set_index]

            if block in cache_set:
                self.hits += 1
                self.logs.append(f"[{i}] HIT  - Addr: {hex(address)} | Set: {set_index}")
                if self.replacement_policy == 'LRU':
                    cache_set.remove(block)
                    cache_set.append(block)
            else:
                self.misses += 1
                self.logs.append(f"[{i}] MISS - Addr: {hex(address)} | Set: {set_index}")
                if block not in self.loaded_blocks:
                    self.loaded_blocks.add(block)
                    self.cold_misses += 1
                else:
                    self.conflict_misses += 1
                if len(cache_set) >= self.associativity:
                    if self.replacement_policy == 'FIFO':
                        cache_set.popleft()
                    elif self.replacement_policy == 'Random':
                        cache_set.remove(random.choice(list(cache_set)))
                    elif self.replacement_policy == 'LRU':
                        cache_set.popleft()
                cache_set.append(block)

    def report(self):
        total = self.hits + self.misses
        hit_ratio = self.hits / total if total > 0 else 0
        print(f"Hits: {self.hits}")
        print(f"Misses: {self.misses}")
        print(f"Cold Misses: {self.cold_misses}")
        print(f"Conflict Misses: {self.conflict_misses}")
        print(f"Hit Ratio: {hit_ratio:.2f}")

    def save_logs(self, logs):
        os.makedirs(os.path.dirname(logs), exist_ok=True)
        with open(logs, 'w') as f:
            for line in self.logs:
                f.write(line + '\n')
