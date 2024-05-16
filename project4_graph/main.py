import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df = pd.DataFrame({"a": ["c"], "b": [2]})
df.plot(x="a", y="b", kind="bar", ax=ax)
display(fig, target="graph")