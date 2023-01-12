import pandas as pd
fi_vcf = open("test.vcf")
content = []
while True:
    line = fi_vcf.readline()
    if not line:
        break
    if line.startswith("##"):
        continue
    elif line.startswith("#"):
        header = line
    else:
        content.append(line.rstrip().split())
df = pd.DataFrame(content, columns=header.strip().split("\t"))
