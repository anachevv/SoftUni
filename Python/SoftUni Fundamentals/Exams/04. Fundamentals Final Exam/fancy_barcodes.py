import re

n_times = int(input())
regex = r"((@#+)([A-Z][A-Z0-9a-z]{4,}[A-Z])(@#+))"
barcodes_and_groups = {}

for _ in range(n_times):
    barcode = input()
    search_pattern = re.findall(regex, barcode)
    group = 'Invalid barcode'
    if barcode not in barcodes_and_groups:
        for match in search_pattern:
            if barcode in match:
                if not [x for x in barcode if x.isdigit()]:
                    group = '00'
                else:
                    group = ''.join(x for x in barcode if x.isdigit())
        barcodes_and_groups[barcode] = group
for group in barcodes_and_groups.values():
    if group != 'Invalid barcode':
        print(f'Product group: {group}')
    else:
        print('Invalid barcode')

