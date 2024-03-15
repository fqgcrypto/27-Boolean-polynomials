from itertools import product

import time

def evaluate_polynomial_1(x7, x62, x26, x63, x0, x27, x6, x28, x53, x56):
    # polynomial1 {x6 + x7 ∗ x26 + x7 + x26 ∗ x62 + x26 + x28 + x62 + x63 + x0 + x6 + x27 + x28 + x56 + 1 + 1} ∗ (x0 + x6 + x28 ∗ x53 + x28 + 1)
    return (x6^(x7 and x26)^x7^(x26 and x62)^x26^x28^x62^x63^x0^x6^x27^x28^x56) and (x0^x6^(x28 and x53)^x28^1)

def evaluate_polynomial_2(x8, x63, x27, x0, x1, x6, x10, x28,x62,x19,x54):
    # polynomial2 {x0 + x7 + x8∗x27 + x8 + x10 + x27∗x63 + x27 + x63 + 1 + x1 + x6 + x7 + x28 + x62+1+1} ∗ (x1 + x10 + x19 ∗ x54 + x19)
    return (((x8 ^ x63) and (x27 ^ 1))^ x0 ^x1 ^x6 ^x10 ^x27^x28^x62^1) and (x1^x10^(x19 and x54)^x19)

def evaluate_polynomial_3(x7, x63, x0, x28, x53, x1, x34, x62,x9,x8,x44,x55):
    # polynomial3 {x0 ∗ x28 + x0 ∗ x53 + x1 ∗ x34 + x1 ∗ x62 + x1 + x8 + x9 ∗x28
    # + x9 ∗ x53 + x28 ∗ x53 + x34 ∗ x62 + x34 + x62 + x7 + x8 + x63 + 1} ∗ {x8∗x55 + x44 + x53 + 1}
    return ((x0 and x28)^(x0 and x53)^(x1 and x34)^(x1 and x62)^x1^x8^(x9 and x28)^(x9 and x53)^(x28 and x53)^(x34 and x62)^x34^x62^x7^x8^x63^1) and ((x8 and x55)^x44^x53^1)

def evaluate_polynomial_4(x7,x35,x9,x18,x36,x37,x62,x8):
    # polynomial4 {x7∗x35 + x7 + x8 + x35 + x37+x9 + x36 + x37+x18 + x37 + 1+1}∗(x9+x37∗x62)
    return ((x7 and x35)^x7^x8^x35^x37^x9^x36^x37^x18^x37) and (x9^(x37 and x62))

def evaluate_polynomial_5(x6,x9,x36,x8,x17,x7,x10,x19,x37,x63,x28):
    # polynomial5 {x6∗x9 + x6 + x8∗x36 + x17∗x36 + x19 + x36 +1+x7 + x10 + x37 + 1+x6+1}∗(x6 + x10 + x19 + x28∗x63 + x28)
    return ((x6 and x9)^x6^(x36 and (x8^x17^1))^x19^x7^x10^x37^x6^1) and (x6^x10^x19^(x28 and x63)^x28)

def evaluate_polynomial_6(x10,x7,x9,x18,x37,x62,x8,x0,x17,x53):
    # polynomial6 (x10∗(x7+1) + (x9+x18)∗(x37+x62) + x37∗(x62+1) + x62 +x8 }∗(x0∗x17 + x53 + x62)
    return ((x10 and (x7^1)) ^ ((x9^x18) and (x37^x62)) ^ (x37 and (x62+1)) ^ x62 ^ x8) and ((x0 and x17) ^ x53 ^ x62)

def evaluate_polynomial_7(x8,x44,x53,x10,x63,x18,x19,x17,x28,x55,x9,x34,x56,x1,x54):
    # polynomial7 (x8∗x44 + x8∗x53 + x10∗x63 + x10 + x18 + x19∗x63 + x19 + x28 + x44 + x53 + x55 + 1+x9 + x17 + x18 + x34 + x56+1+1}∗(x1 + x18 + x54 + x63)
    return ((x8 and x44)^(x8 and x53)^(x10 and x63)^x10^x18^(x19 and x63)^x19^x28^x44^x53^x55^1^x9^x17^x18^x34^x56) and (x1^x18^x54^x63)

def evaluate_polynomial_8(x0,x9,x34,x45,x18,x19,x55,x10,x35,x56,x44,x54):
    # polynomial8 (x0 + x9∗x34 + x9∗x45 + x9∗x54 + x9 + x19 + x34∗x45 + x34∗x54 + x34 + x45 + x54 + x56 + 1+x10 + x18 + x19 + x35+0+1}∗(x0 + x19∗x44 + x44 + x55)
    return (x0^(x9 and x34)^(x9 and x45)^(x9 and x54)^x9^x19^(x34 and x45)^(x34 and x54)^x34^x45^x54^x56^x10^x18^x19^x35) and (x0^(x19 and x44)^x44^x55)

def evaluate_polynomial_9(x17,x18,x25,x46,x45,x7,x36,x56,x44):
    # polynomial9 (x17 + x25∗x44 + x25 + x44 + x46 + 1+x18 + x45 + x46 + 1+x18 + x56 + 1+1}∗(x7∗x36 + x18 + x36∗x46 + x36 + 1)
    return (x17^(x25 and x44)^x25^x44^x46^1^x18^x45^x46^1^x18^x56) and ((x7 and x36)^x18^(x36 and x46)^x36^1)

def evaluate_polynomial_10(x17,x18,x25,x46,x45,x6,x26,x28,x19,x8,x37):
    # polynomial10 (x6∗x17 + x6∗x26 + x6∗x45 + x6 + x17∗x45 + x17 + x18 + x25 + x26∗x45 + x26 + x28 + x45+x19 + x25 + x46 +1+1+1}∗(x6 + x8∗x37 + x19 + x25 + x37 + 1)
    return ((x6 and x17)^(x6 and x26)^(x6 and x45)^x6^(x17 and x45)^x17^x18^x25^(x26 and x45)^x26^x28^x45^x19^x25^x46^1) and (x6^(x8 and x37)^x19^x25^x37^1)

def evaluate_polynomial_11(x17,x18,x25,x46,x7,x27,x26,x36,x19,x0,x9,x62):
    # polynomial11 (x7∗x18 + x7∗x27 + x7∗x46 + x7 + x18∗x46 + x18 + x19 + x26 + x27∗x46 + x27 + x36 + x46 + 1+x0 + x17 + x25 + x26}∗(x7 + x9 + x62 + 1)
    return ((x7 and x18)^(x7 and x27)^(x7 and x46)^x7^(x18 and x46)^x18^x19^x26^(x27 and x46)^x27^x36^x46^1^x0^x17^x25^x26) and (x7^x9^x62^1)

def evaluate_polynomial_12(x17,x6,x8,x28,x53,x27,x37,x10,x19,x0,x63,x62):
    # polynomial12 (x0 + x6∗x8 + x8∗x19 + x8∗x28 + x17∗x53 + x17∗x62 + x17 + x19 + x27 + x28 + x37 + x53 + x62 + 1 + x27 + x28 + x37 + 1 +1}∗(x8 + x10∗x27 + x63)
    return (x0^(x6 and x8)^(x8 and x19)^(x8 and x28)^(x17 and x53)^(x17 and x62)^x17^x19^x27^x28^x37^x53^x62^1^x27^x28^x37) and (x8^(x10 and x27)^x63)

def evaluate_polynomial_13(x17,x26,x54,x34,x35,x27,x37,x25,x28,x55,x56):
    # polynomial13 (x26∗x54 + x26 + x27 + x34 + x35∗x54 + x35 + x37 + x54 + x56 + 1+x25 + x28 + x34 + x55 + x56+x37+1}∗(x17∗x56 + x28 + x34 + x56 + 1)
    return ((x26 and x54)^x26^x27^x34^(x35 and x54)^x35^x37^x54^x56^1^x25^x28^x34^x55^x56^x37^1) and ((x17 and x56)^x28^x34^x56^1)

def evaluate_polynomial_14(x36,x26,x6,x34,x35,x27,x7,x25,x28,x55,x56,x18):
    # polynomial14 (x25∗x28 + x27∗x55 + x28 + x35 + x36∗x55+x26 + x34 + x35 + x56+x6 +1}∗(x7 + x18 + x35 + 1)
    return ((x25 and x28)^(x27 and x55)^x28^x35^(x36 and x55)^x26^x34^x35^x56^x6^1) and (x7^x18^x35^1)

def evaluate_polynomial_15(x36,x26,x17,x37,x35,x27,x7,x62,x28,x10,x56,x8,x19):
    # polynomial15 (x7∗x26 + x7 + x17∗x28 + x17∗x37 + x17∗x56 + x17 + x26∗x62 + x26 + x28∗x56 + x36 + x37∗x56 + x56 + x62 + 1+x10 + x27 + x35 + x36 + 1+1+1}
    # ∗(x8 + x17 + x19∗x36 + x19 + 1)
    return ((x7 and x26)^x7^(x17 and x28)^(x17 and x37)^(x17 and x56)^x17^(x26 and x62)^x26^(x28 and x56)^x36^(x37 and x56)^x56^x62^x10^x27^x35^x36) and (x8^x17^(x19 and x36)^x19^1)

def evaluate_polynomial_16(x36,x26,x1,x37,x35,x63,x44,x0,x34,x55):
    # polynomial16 (x1 + x35∗x63 + x35 + x36 + x44∗x63 + x44 + x63+x0 + x1 + x34 + x37 + 1+x37+1}∗(x1∗x55 + x26∗x55 + x37 + x55 + 1)
    return (x1^(x35 and x63)^x35^x36^(x44 and x63)^x44^x63^x0^x1^x34^x37^1^x37^1) and ((x1 and x55)^(x26 and x55)^x37^x55^1)

def evaluate_polynomial_17(x36,x25,x1,x37,x35,x45,x44,x0,x34,x6,x27,x56):
    # polynomial17 (x0∗x25 + x0∗x36 + x0∗x45 + x25∗x36 + x25∗x45 + x34∗x37 + x37 + x44+x1 + x35 + x44 + 1+ x6+1}∗(x25 + x27∗x56 + x44 + x56 + 1)
    return ((x0 and x25)^(x0 and x36)^(x0 and x45)^(x25 and x36)^(x25 and x45)^(x34 and x37)^x37^x44^x1^x35^x44^x6) and (x25^(x27 and x56)^x44^x56^1)

def evaluate_polynomial_18(x36,x26,x1,x37,x35,x45,x44,x46,x7,x6,x55,x28,x17):
    # polynomial18 (x1∗x26 + x1∗x37 + x1∗x46 + x7∗x35 + x7 + x26∗x37 + x26∗x46 + x35 + x37 + x46 + x55 + 1+x36 + x44 + x45+x45 + 1+1 }∗(x6∗x28 + x6 + x17 + x26 + x28∗x45 + 1)
    return ((x1 and x26)^(x1 and x37)^(x1 and x46)^(x7 and x35)^x7^(x26 and x37)^(x26 and x46)^x35^x37^x46^x55^1^x36^x44^x45^x45) and ((x6 and x28)^x6^x17^x26^(x28 and x45)^1)

def evaluate_polynomial_19(x36,x8,x19,x37,x27,x45,x56,x46,x7,x62,x18,x17):
    # polynomial19 (x8∗x36 + x17∗x36 + x19 + x27 + x36 + x56+x37 + x45 + x46 + x62+x46+1}∗(x7∗x36 + x7 + x18 + x27 + x36∗x46 + x36)
    return ((x8 and x36)^(x17 and x36)^x19^x27^x36^x56^x37^x45^x46^x62^x46^1) and ((x7 and x36)^x7^x18^x27^(x36 and x46)^x36)

def evaluate_polynomial_20(x44,x8,x53,x10,x55,x9,x0,x46,x35):
    # polynomial20 (x8∗x44 + x8∗x53 + x10 + x44 + x53 + x55 + 1+x9 + x10 + x46+1+1}∗(x0∗x10 + x0∗x35 + x10∗x35 + x35 + x46)
    return ((x8 and x44)^(x8 and x53)^x10^x44^x53^x55^1^x9^x10^x46) and ((x0 and x10)^(x0 and x35)^(x10 and x35)^x35^x46)

def evaluate_polynomial_21(x44,x34,x53,x10,x45,x9,x54,x56,x25,x36):
    # polynomial21 (x9∗x34 + x9∗x45 + x9∗x54 + x9 + x34∗x45 + x34∗x54 + x34 + x45 + x53 + x54 + x56+x10 + x44 + x53+1+1}∗(x25 + x34 + x36∗x53 + x36∗x56 + x36 + x56)
    return ((x9 and x34)^(x9 and x45)^(x9 and x54)^x9^(x34 and x45)^(x34 and x54)^x34^x45^x53^x54^x56^x10^x44^x53) and (x25^x34^(x36 and x53)^(x36 and x56)^x36^x56)

def evaluate_polynomial_22(x44,x0,x53,x10,x45,x35,x54,x46,x25,x55,x6,x28,x26,x37):
    # polynomial22 {x0 + x10∗x35 + x10∗x46 + x10∗x55 + x25∗x44 + x25 + x35∗x46 + x35∗x55 + x44 + x54 + 1+x6 + x28 + x45 + x53 + x54+0+1 }∗(x26 + x35 + x37∗x54 + x37)
    return (x0^(x10 and x35)^(x10 and x46)^(x10 and x55)^(x25 and x44)^x25^(x35 and x46)^(x35 and x55)^x44^x54^x6^x28^x45^x53^x54) and (x26^x35^(x37 and x54)^x37)

def evaluate_polynomial_23(x17,x36,x56,x7,x45,x27,x54,x46,x55,x6,x28,x26):
    # polynomial23 {x6∗x17 + x6∗x26 + x6∗x45 + x6 + x17∗x45 + x17 + x26∗x45 + x26 + x28 + x36∗x56 + x45 + x55+x7 + x36 + x46 + x54 + x55 + 1+1+1}∗(x6 + x27 + x36 + x55)
    return ((x6 and x17)^(x6 and x26)^(x6 and x45)^x6^(x17 and x45)^x17^(x26 and x45)^x26^x28^(x36 and x56)^x45^x55^x7^x36^x46^x54^x55^1) and (x6^x27^x36^x55)

def evaluate_polynomial_24(x17,x0,x53,x62,x19,x18,x54,x44,x55):
    # polynomial24 {x0 + x17∗x53 + x17∗x62 + x17 + x19 + x53 + x54 + x62 + 1+x18 + x19 + x55 + 1+1+1}∗(x19∗x44 + x19 + x55 + 1)
    return (x0^(x17 and x53)^(x17 and x62)^x17^x19^x53^x54^x62^x18^x19^x55) and ((x19 and x44)^x19^x55^1)

def evaluate_polynomial_25(x63,x56,x53,x62,x19,x18,x54,x10,x55,x45,x34):
    # polynomial25 (x18∗x54 + x18∗x63 + x18 + x54 + x55 + x62 + x63+x19 + x53 + x56 + x62 + 1+1+1}∗(x10∗x45 + x10 + x34 + x56 + x62 + 1)
    return ((x18 and x54)^(x18 and x63)^x18^x54^x55^x62^x63^x19^x53^x56^x62^1) and ((x10 and x45)^x10^x34^x56^x62^1)

def evaluate_polynomial_26(x63,x56,x53,x62,x19,x0,x54,x44,x55,x25,x34,x36,x37,x35,x46):
    # polynomial26 {x0∗x19 + x0∗x44 + x19∗x44 + x19∗x55 + x19 + x25∗x53 + x25∗x56 + x34∗x53 + x34∗x56 + x36 + x44∗x55 + x44 + x53∗x56 + x53 +
    # x63 + 1+x37 + x54 + x62 + x63+1+1}∗(x35 + x44 + x46 + x63)
    return ((x0 and x19)^(x0 and x44)^(x19 and x44)^(x19 and x55)^x19^(x25 and x53)^(x25 and x56)^(x34 and x53)^(x34 and x56)^x36^(x44 and x55)^x44^(x53 and x56)
            ^x53^x63^1^x37^x54^x62^x63) and (x35^x44^x46^x63)

def evaluate_polynomial_27(x63,x56,x1,x45,x10,x0,x54,x26,x55,x25,x36,x37,x35):
    # polynomial27 {x0 + x1∗x45 + x1 + x10 + x26∗x54 + x26 + x35∗x54 + x35 + x37 + x45∗x56 + x45 + x54 + x56 + 1+x0 + x55 + x63 + 1+x45+1}
    # ∗(x0∗x25 + x0 + x25 + x36 + x45 + 1)
    return (x0^(x1 and x45)^x1^x10^(x26 and x54)^x26^(x35 and x54)^x35^x37^(x45 and x56)^x45^x54^x56^1^x0^x55^x63^x45) and ((x0 and x25)^x0^x25^x36^x45^1)

def count_zero_cases():
    variables = [0, 1]  # 二进制变量可能的值
    count = 0
    # 遍历所有可能的组合,每个变量取值都是0/1
    for x7, x62, x26, x63, x0, x27, x6, x28, x53,x8,x1,x10,x19,x54,x34,x9,x44,x55,x35,x18,x36,x37,x17,x56,x45,x25,x46 in product(variables, repeat=27):
        result_1 = evaluate_polynomial_1(x7, x62, x26, x63, x0, x27, x6, x28, x53, x56)
        result_2 = evaluate_polynomial_2(x8, x63, x27, x0, x1, x6, x10, x28,x62,x19,x54)
        result_3 = evaluate_polynomial_3(x7, x63, x0, x28, x53, x1, x34, x62, x9, x8, x44, x55)
        result_4 = evaluate_polynomial_4(x7,x35,x9,x18,x36,x37,x62,x8)
        result_5 = evaluate_polynomial_5(x6,x9,x36,x8,x17,x7,x10,x19,x37,x63,x28)
        result_6 = evaluate_polynomial_6(x10, x7, x9, x18, x37, x62, x8, x0, x17, x53)
        result_7 = evaluate_polynomial_7(x8,x44,x53,x10,x63,x18,x19,x17,x28,x55,x9,x34,x56,x1,x54)
        result_8 = evaluate_polynomial_8(x0,x9,x34,x45,x18,x19,x55,x10,x35,x56,x44,x54)
        result_9 = evaluate_polynomial_9(x17,x18,x25,x46,x45,x7,x36,x56,x44)
        result_10 = evaluate_polynomial_10(x17,x18,x25,x46,x45,x6,x26,x28,x19,x8,x37)
        result_11 = evaluate_polynomial_11(x17,x18,x25,x46,x7,x27,x26,x36,x19,x0,x9,x62)
        result_12 = evaluate_polynomial_12(x17,x6,x8,x28,x53,x27,x37,x10,x19,x0,x63,x62)
        result_13 = evaluate_polynomial_13(x17,x26,x54,x34,x35,x27,x37,x25,x28,x55,x56)
        result_14 = evaluate_polynomial_14(x36,x26,x6,x34,x35,x27,x7,x25,x28,x55,x56,x18)
        result_15 = evaluate_polynomial_15(x36,x26,x17,x37,x35,x27,x7,x62,x28,x10,x56,x8,x19)
        result_16 = evaluate_polynomial_16(x36,x26,x1,x37,x35,x63,x44,x0,x34,x55)
        result_17 = evaluate_polynomial_17(x36,x25,x1,x37,x35,x45,x44,x0,x34,x6,x27,x56)
        result_18 = evaluate_polynomial_18(x36,x26,x1,x37,x35,x45,x44,x46,x7,x6,x55,x28,x17)
        result_19 = evaluate_polynomial_19(x36,x8,x19,x37,x27,x45,x56,x46,x7,x62,x18,x17)
        result_20 = evaluate_polynomial_20(x44,x8,x53,x10,x55,x9,x0,x46,x35)
        result_21 = evaluate_polynomial_21(x44,x34,x53,x10,x45,x9,x54,x56,x25,x36)
        result_22 = evaluate_polynomial_22(x44,x0,x53,x10,x45,x35,x54,x46,x25,x55,x6,x28,x26,x37)
        result_23 = evaluate_polynomial_23(x17,x36,x56,x7,x45,x27,x54,x46,x55,x6,x28,x26)
        result_24 = evaluate_polynomial_24(x17,x0,x53,x62,x19,x18,x54,x44,x55)
        result_25 = evaluate_polynomial_25(x63,x56,x53,x62,x19,x18,x54,x10,x55,x45,x34)
        result_26 = evaluate_polynomial_26(x63,x56,x53,x62,x19,x0,x54,x44,x55,x25,x34,x36,x37,x35,x46)
        result_27 = evaluate_polynomial_27(x63,x56,x1,x45,x10,x0,x54,x26,x55,x25,x36,x37,x35)

        if result_1 == 0 and result_2 == 0 and result_3 == 0 and result_4 == 0 and result_5 == 0 and result_6 == 0\
            and result_7 == 0 and result_8 == 0 and result_9 == 0 and result_10 == 0 and result_11 == 0 and result_12 == 0\
            and result_13 == 0 and result_14 == 0 and result_15 == 0 and result_16 == 0 and result_17 == 0 and result_18 == 0\
            and result_19 == 0 and result_20 == 0 and result_21 == 0 and result_22 == 0 and result_23 == 0 and result_24 == 0\
            and result_25 == 0 and result_26 == 0 and result_27 == 0:
            count += 1
    return count


start_time = time.time()

total_zero_cases = count_zero_cases()
print("The total number of cases where multiple Boolean polynomials are equal to 0 at the same time:", total_zero_cases)
print("The probability that multiple Boolean polynomials are equal to 0 at the same time:", total_zero_cases/(2**27))

# 27个布尔函数同时等于0的概率为0.00038189440965652466,约等于2^(-11.355)<(0.75)^27=2^(-11.205)
# 0.75的27次方等于0.00042330569...

end_time = time.time()
execution_time = end_time - start_time
print(f"The code running time is: {execution_time} Second")
