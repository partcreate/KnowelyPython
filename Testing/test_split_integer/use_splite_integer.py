from split_integer import split_integer

result = {
    "sum_of_parts": {},
    "divisible_by_parts": {},
    "one_part": {},
    "sorted_if_not_equal_parts": {},
    "add_zero_parts": {},
}

with (open("sum_of_parts.txt", "w") as sum_of_parts,
      open("divisible_by_parts.txt", "w") as divisible_by_parts,
      open("one_part.txt", "w") as one_part,
      open("sorted_if_not_equal_parts.txt", "w") as sorted_if_not_equal_parts,
      open("add_zero_parts.txt", "w") as add_zero_parts):

    for i in range(100):
        for j in range(99):

            calc = split_integer(i, j)

            if j < i:

                if j == 1:
                    result["one_part"][i, j] = calc
                    one_part.write(f"({i} {j}): {calc}\n")

                if len(set(calc)) == 1:
                    result["divisible_by_parts"][i, j] = calc
                    divisible_by_parts.write(f"({i} {j}): {calc}\n")
                else:
                    result["sorted_if_not_equal_parts"][i, j] = calc
                    sorted_if_not_equal_parts.write(f"({i} {j}): {calc}\n")

                sum_oif_calc = sum(calc)

                if sum_oif_calc == i:
                    result["sum_of_parts"][i, j] = sum(calc)
                    sum_of_parts.write(f"({i} {j}): {sum(calc)}\n")
            else:

                if  0 in calc:
                    result["add_zero_parts"][i, j] = calc
                    add_zero_parts.write(f"({i} {j}): {calc}\n")




print(result)
