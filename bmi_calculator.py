from bmi import Bmi

bmi = Bmi()

print(bmi)

print(bmi._kgs)
print(bmi._cms)
bmi.print_bmi_imperial()
bmi.print_bmi_metric()
bmi.metric_bmi()
bmi.imperial_bmi()

bmi.set_metric_inputs(57,164)
bmi.metric_bmi()

print(f"Kgs:{bmi.get_kgs()} Cms:{bmi.get_cms()}")