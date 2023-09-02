def buffer_calculator(mg_ppm, ca_ppm, bicarbonate_ppm):
    # molecular weights and compositions
    mg_in_mgso4 = 24.305 / 246.47
    ca_in_cacl2 = 40.08 / 110.98
    bicarbonate_in_nahco3 = 61.01714 / 84.007
    
    # calculations based on desired ppm
    mgso4_weight = mg_ppm / mg_in_mgso4 / 1000  # Epsom salt for Mg
    cacl2_weight = ca_ppm / ca_in_cacl2 / 1000  # Calcium chloride for Ca
    nahco3_weight = bicarbonate_ppm / bicarbonate_in_nahco3 / 1000  # Baking soda for bicarbonate

    # calculate 100x concentrate weights
    mgso4_concentrate = mgso4_weight * 100
    cacl2_concentrate = cacl2_weight * 100
    nahco3_concentrate = nahco3_weight * 100

    return mgso4_weight, cacl2_weight, nahco3_weight, mgso4_concentrate, cacl2_concentrate, nahco3_concentrate

# input desired ppm values
mg_ppm = float(input("Enter desired ppm for Mg: "))
ca_ppm = float(input("Enter desired ppm for Ca: "))
bicarbonate_ppm = float(input("Enter desired ppm for bicarbonate: "))

# calculate and print results
mgso4, cacl2, nahco3, mgso4_conc, cacl2_conc, nahco3_conc = buffer_calculator(mg_ppm, ca_ppm, bicarbonate_ppm)
print(f"\nFor 1 liter of water, add:\n{mgso4:.4f} g of Epsom Salt\n{cacl2:.4f} g of Calcium Chloride\n{nahco3:.4f} g of Baking Soda")
print(f"\nFor a 100x concentrate solution (to be diluted 1:100):\n{mgso4_conc:.4f} g of Epsom Salt\n{cacl2_conc:.4f} g of Calcium Chloride\n{nahco3_conc:.4f} g of Baking Soda")

