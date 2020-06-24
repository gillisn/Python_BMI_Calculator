from bmi_prop import BmiProperty

bmi=BmiProperty()

print(bmi.kgs)
print(bmi.cms)
bmi.print_bmi_imperial()
bmi.print_bmi_metric()
bmi.metric_bmi()
bmi.imperial_bmi()

bmi.metric_bmi()

print(f"Kgs:{bmi.kgs()} Cms:{bmi.cms()}")