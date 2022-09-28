"""
Making simple nested dicts with defaultdict
"""

In [3]: from collections import defaultdict

In [4]: def turtles():
   ...:     return defaultdict(turtles)
   ...:

In [5]: data = turtles()

In [6]: data["hello"] = "hey!"

In [7]: data["foo"]["bar"]["baz"] = "hmmmmmm"

In [8]: print(json.dumps(data, indent=2))
{
  "hello": "hey!",
  "foo": {
    "bar": {
      "baz": "hmmmmmm"
    }
  }
}
