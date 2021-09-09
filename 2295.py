table_value = list(map (float, input (). split ()))
alcool_rend = table_value[2] / table_value[0]
gas_rend = table_value[3] / table_value[1]
if alcool_rend > gas_rend:
    print('A')
else:
    print('G')