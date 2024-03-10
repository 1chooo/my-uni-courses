from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file -------
with open("linu850f.data", "rb") as f:
    data = np.fromfile(f, dtype=np.float32)

# for index, value in enumerate(data):
#     print(index, value)

# Handle the data -------
# for the y-axis
original = data[1:366]
meanValue = data[368:733]
annualCycle = data[735:1100]
semiAnnualCycle = data[1102:1467]
day122Cycle = data[1469:1834]
seasonalCycle = data[1836:2201]
annual_semiAnnual_day122_seasonalCycle = data[2203:2568]
day6To12Cycle = data[2570:2935]
annual_semiAnnualCycle = data[4772:5137]
annual_semiAnnual_day122Cycle = data[5139:5504]
annual_semiAnnual_day122_seasonal_day6To12Cycle = data[5506:5871]

annualCycle += meanValue
semiAnnualCycle += meanValue
day122Cycle += meanValue
seasonalCycle += meanValue
annual_semiAnnual_day122_seasonalCycle += meanValue
day6To12Cycle += meanValue
annual_semiAnnualCycle += meanValue
annual_semiAnnual_day122Cycle += meanValue
annual_semiAnnual_day122_seasonal_day6To12Cycle += meanValue

filterOutAnnualCycle = data[2937:3302]
filterOutAnnual_semiAnnualCycle = data[3304:3669]
filterOutAnnual_semiAnnual_day122Cycle = data[3671:4036]
filterOutAnnual_semiAnnual_day122_seasonalCycle = data[4038:4403]
filterOutAnnual_semiAnnual_day122_seasonal_day6To12Cycle = data[4405:4770]

# for the x-axis
time = np.linspace(1, 365, 365)

# Plot the data -------
# Page 1
fig1 = plt.figure(figsize=(8.27, 11.69), dpi=600)

axs1 = fig1.add_subplot(4, 2, 1)
axs1.plot(time, original, color="steelblue")
axs1.plot(time, meanValue, color="tomato")
axs1.set_xlim([1, 365])
axs1.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs1.grid(linestyle="--")
axs1.title.set_text("                               original          109601005")

axs2 = fig1.add_subplot(4, 2, 2)
axs2.plot(time, meanValue)
axs2.plot(time, annualCycle, linestyle="--")
axs2.plot(time, semiAnnualCycle, linestyle="-.")
axs2.plot(time, day122Cycle, linestyle=":")
axs2.plot(time, seasonalCycle, linestyle=(0, (5, 5)))
axs2.set_xlim([1, 365])
axs2.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs2.grid(linestyle="--")
axs2.title.set_text("compose 2")

axs3 = fig1.add_subplot(4, 2, 3)
axs3.plot(time, original, color="mediumseagreen")
axs3.plot(time, annualCycle, color="tomato")
axs3.set_xlim([1, 365])
axs3.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs3.grid(linestyle="--")
axs3.title.set_text("Hsieh Wen-Liang    annual cycle                        ")

axs4 = fig1.add_subplot(4, 2, 4)
axs4.plot(time, filterOutAnnualCycle, color="mediumseagreen")
axs4.plot(time, semiAnnualCycle, color="tomato")
axs4.set_xlim([1, 365])
axs4.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs4.grid(linestyle="--")
axs4.title.set_text("semi-annual cycle")

axs5 = fig1.add_subplot(4, 2, 5)
axs5.plot(time, filterOutAnnual_semiAnnualCycle, color="mediumseagreen")
axs5.plot(time, day122Cycle, color="tomato")
axs5.set_xlim([1, 365])
axs5.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s", fontsize=14)
axs5.grid(linestyle="--")
axs5.title.set_text("day 122 cycle")

axs6 = fig1.add_subplot(4, 2, 6)
axs6.plot(time, filterOutAnnual_semiAnnualCycle, color="mediumseagreen")
axs6.plot(time, day122Cycle, color="tomato")
axs6.set_xlim([1, 365])
axs6.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s", fontsize=14)
axs6.grid(linestyle="--")
axs6.title.set_text("day 122 cycle")

axs7 = fig1.add_subplot(4, 2, 7)
axs7.plot(time, original, color="mediumseagreen")
axs7.plot(time, annual_semiAnnual_day122_seasonalCycle, color="tomato")
axs7.set_xlim([1, 365])
axs7.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs7.grid(linestyle="--")
axs7.title.set_text("annual+semi+day122+seasonal cycle")

axs8 = fig1.add_subplot(4, 2, 8)
axs8.plot(time, filterOutAnnual_semiAnnual_day122_seasonalCycle, color="mediumseagreen")
axs8.plot(time, day6To12Cycle, color="tomato")
axs8.set_xlim([1, 365])
axs8.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs8.grid(linestyle="--")
axs8.title.set_text("day 6~12 cycle")

fig1.tight_layout()

# Page 2
fig2 = plt.figure(figsize=(8.27, 11.69), dpi=600)

axs1 = fig2.add_subplot(4, 2, 1)
axs1.plot(time, original, color="steelblue")
axs1.plot(time, meanValue, color="tomato")
axs1.set_xlim([1, 365])
axs1.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs1.grid(linestyle="--")
axs1.title.set_text("                               original          109601005")

axs2 = fig2.add_subplot(4, 2, 2)
axs2.plot(time, meanValue)
axs2.plot(time, annualCycle, linestyle="--")
axs2.plot(time, semiAnnualCycle, linestyle="-.")
axs2.plot(time, day122Cycle, linestyle=":")
axs2.plot(time, seasonalCycle, linestyle=(0, (5, 5)))
axs2.set_xlim([1, 365])
axs2.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs2.grid(linestyle="--")
axs2.title.set_text("compose 2")

axs3 = fig2.add_subplot(4, 2, 3)
axs3.plot(time, annual_semiAnnualCycle)
axs3.plot(time, annual_semiAnnual_day122Cycle, linestyle="--")
axs3.plot(time, annual_semiAnnual_day122_seasonalCycle, linestyle="-.")
axs3.set_xlim([1, 365])
axs3.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs3.grid(linestyle="--")
axs3.title.set_text("compose 1")

axs4 = fig2.add_subplot(4, 2, 4)
axs4.plot(time, original, color="mediumseagreen")
axs4.plot(time, annual_semiAnnual_day122_seasonalCycle, color="tomato")
axs4.set_xlim([1, 365])
axs4.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs4.grid(linestyle="--")
axs4.title.set_text("annual+semi+day122+seasonal cycle")

axs5 = fig2.add_subplot(4, 2, 5)
axs5.plot(time, annual_semiAnnual_day122_seasonalCycle)
axs5.plot(time, day6To12Cycle, linestyle="--")
axs5.set_xlim([1, 365])
axs5.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs5.grid(linestyle="--")
axs5.title.set_text("compose 3")

axs6 = fig2.add_subplot(4, 2, 6)
axs6.plot(time, original, color="mediumseagreen")
axs6.plot(time, annual_semiAnnual_day122_seasonal_day6To12Cycle, color="tomato")
axs6.set_xlim([1, 365])
axs6.set_ylim([-15, 30])
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs6.grid(linestyle="--")
axs6.title.set_text("annual+semi+day122+seasonal\n+ day 6~12 cycle")

axs7 = fig2.add_subplot(4, 2, 7)
axs7.plot(time, original, color="steelblue", marker="o",
          markerfacecolor="white", markeredgecolor="black", markersize=3)
axs7.plot(time, annual_semiAnnualCycle, color="tomato")
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs7.grid(linestyle="--")
axs7.title.set_text("850 hPa U-Wind")

axs8 = fig2.add_subplot(4, 2, 8)
axs8.plot(time, original, color="steelblue", marker="o",
          markerfacecolor="white", markeredgecolor="black", markersize=3)
axs8.plot(time, annual_semiAnnual_day122_seasonal_day6To12Cycle, color="tomato")
plt.xlabel("Date", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs8.grid(linestyle="--")
axs8.title.set_text("850 hPa U-Wind")

fig2.tight_layout()

# create a PDF file and add each figure as a separate page
with PdfPages('test.pdf') as pdf:
    pdf.savefig(fig1)
    pdf.savefig(fig2)