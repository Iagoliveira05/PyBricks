from pybricks.tools import hub_menu

hub_selected = hub_menu("1", "2", "3")

if (hub_selected == "1"):
    import main_1  # Missão 1
elif (hub_selected == "2"):
    import main_2  # Missão 2
elif (hub_selected == "3"):
    import main_3  # Missão 3