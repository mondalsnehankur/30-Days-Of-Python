# ============================================================
# DAY 9: CONDITIONALS — THEORY EXAMPLES
# ============================================================

# 1. IF CONDITION
if condition:
    statement


# 2. IF ELSE
if condition:
    statement_if_true
else:
    statement_if_false


# 3. IF ELIF ELSE
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3


# 4. SHORT-HAND IF ELSE
statement_if_true if condition else statement_if_false


# 5. NESTED CONDITIONS
if condition1:
    if condition2:
        statement


# 6. AND OPERATOR
if condition1 and condition2:
    statement


# 7. OR OPERATOR
if condition1 or condition2:
    statement


# 8. MEMBERSHIP WITH CONDITIONALS
if item in collection:
    statement


# 9. COMBINING CONDITIONS
if age >= 18 and country == "India":
    print("Eligible")


# 10. BASIC BOOLEAN CONDITIONS
is_student = True

if is_student:
    print("The person is a student.")
