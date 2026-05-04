import pandas as pd

df = pd.read_excel("test.xlsx", header=None)

replacements = {
    "{{kwan}}": "Yo"
}

"""
def replace_tags(x):
    if isinstance(x, str):
        for tag, value in replacements.items():
            x = x.replace(tag, str(value))
        return x
"""

def replace_tags(x):
    print(x)

df = df.map(replace_tags)
