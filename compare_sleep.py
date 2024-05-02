from convert_time import convert_time_2


def compare_sleep(rows, i, var):
    for row in rows:
        if row[i] is not None:
            var_compare = convert_time_2(row[i])
            assert var_compare == var, f'{i} Not equal - case 1'
            # print(f"Var_compare {i}: ", var_compare)
        else:
            rows_2 = [tuple('--:--' if item is None else item for item in tuple_) for tuple_ in rows]
            for r in rows_2:
                assert r[i] == var, f'{i} Not equal - case 2'
                # print(f'{i}', r[i])
