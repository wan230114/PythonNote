# %%

# pip install bashlex
import bashlex
parts = bashlex.parse('true && cat <(echo $(echo foo))')
for ast in parts:
    print(ast.dump())
