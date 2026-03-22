from gencontent import extract_title
import unittest

class TestGencontent(unittest.TestCase):

    def test_extract_title(self):
        md = """
# heading

```
for i in x:
    print(i)
```
"""
        title = extract_title(md)
        self.assertEqual(title, "heading")

    
    def test_extract_title_text_before(self):
        md = """
*This is some text before the heading*

# heading

```
for i in x:
    print(i)
```
"""
        title = extract_title(md)
        self.assertEqual(title, "heading")