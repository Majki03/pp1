employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
             "JACKSON Peter","JOHNSON Rick",
             "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e:e[0]=="J", employees))

print('\n'.join(f"{emp}" for emp in emp_J))