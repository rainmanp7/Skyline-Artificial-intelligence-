### 9. **Parallel Processing Unit Test**

```python
from concurrent.futures import ThreadPoolExecutor
import unittest

class TestParallelProcessing(unittest.TestCase):
    def test_parallel_execution(self):
        def dummy_task(x):
            return x * 2
        
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(dummy_task, [1, 2, 3, 4]))
        
        self.assertEqual(results, [2, 4, 6, 8])
```