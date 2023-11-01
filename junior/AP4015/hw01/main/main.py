from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file -------
with open("./linu850f.data", "rb") as f:
    data = np.fromfile(f, dtype=np.float32)

# To check the content of linus850f.data
# for index, value in enumerate(data):
#     print(index, value)

# Handle the data -------
# for the y-axis
original = data[1:366]
mean_value = data[368:733]
annual_cycle = data[735:1100]
semi_annual_cycle = data[1102:1467]
day_122_cycle = data[1469:1834]
seasonal_cycle = data[1836:2201]
annual_semi_annual_day122_seasonal_cycle = data[2203:2568]
day_6_to_12_cycle = data[2570:2935]
annual_semi_annual_cycle = data[4772:5137]
annual_semi_annual_day_122_cycle = data[5139:5504]
annual_semi_annual_day122_seasonal_day_6_to_12_cycle = data[5506:5871]

annual_cycle += mean_value
semi_annual_cycle += mean_value
day_122_cycle += mean_value
seasonal_cycle += mean_value
annual_semi_annual_day122_seasonal_cycle += mean_value
day_6_to_12_cycle += mean_value
annual_semi_annual_cycle += mean_value
annual_semi_annual_day_122_cycle += mean_value
annual_semi_annual_day122_seasonal_day_6_to_12_cycle += mean_value

filter_out_annual_cycle = data[2937:3302]
filter_out_annual_semi_annual_cycle = data[3304:3669]
filter_out_annual_semi_annual_day_122_cycle = data[3671:4036]
filter_out_annual_semi_annual_day122_seasonal_cycle = data[4038:4403]
filter_out_annual_semi_annual_day122_seasonal_day_6_to_12_cycle = data[4405:4770]

x_tick = [i for i in range(0, 360, 50)]

# for the x-axis
time = np.linspace(1, 365, 365)

# Plot the data -------
# Page 1
fig1 = plt.figure(figsize=(8.27, 11.69), dpi=600)

axs1 = fig1.add_subplot(4, 2, 1)
axs1.plot(time, original,)
axs1.plot(time, mean_value,)
axs1.set_xlim([1, 365])
axs1.set_ylim([-15, 30])
axs1.text(0, 31, 'U(60E, 15N)')
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
plt.legend(['original', 'mean'])
axs1.grid(linestyle="--")
axs1.title.set_text("                               original          109601003")

axs2 = fig1.add_subplot(4, 2, 2)
axs2.plot(time, mean_value)
axs2.plot(time, annual_cycle, linestyle="--")
axs2.plot(time, semi_annual_cycle, linestyle="-.")
axs2.plot(time, day_122_cycle, linestyle=":")
axs2.plot(time, seasonal_cycle, linestyle=(0, (5, 5)))
axs2.set_xlim([1, 365])
axs2.set_ylim([-15, 30])
axs2.text(0, 31, 'U(60E, 15N)')
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
plt.legend(['mean', 'annual', 'semi', '122', 'seasonal'])
axs2.grid(linestyle="--")
axs2.title.set_text("                          compose 1  Hugo ChunHo Lin")

axs3 = fig1.add_subplot(4, 2, 3)
axs3.plot(time, original, )
axs3.plot(time, annual_cycle,)
axs3.set_xlim([1, 365])
axs3.set_ylim([-15, 30])
axs3.text(0, 31, 'U(60E, 15N)')
plt.legend(['original', 'annual'])
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs3.grid(linestyle="--")
axs3.title.set_text("annual cycle")

axs4 = fig1.add_subplot(4, 2, 4)
axs4.plot(time, filter_out_annual_cycle, )
axs4.plot(time, semi_annual_cycle,)
axs4.set_xlim([1, 365])
axs4.set_ylim([-15, 30])
axs4.text(0, 31, 'U(60E, 15N)')
plt.legend(['filter annual', 'semi annual'])
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs4.grid(linestyle="--")
axs4.title.set_text("semi-annual cycle")

axs5 = fig1.add_subplot(4, 2, 5)
axs5.plot(time, filter_out_annual_semi_annual_cycle, )
axs5.plot(time, day_122_cycle,)
axs5.set_xlim([1, 365])
axs5.set_ylim([-15, 30])
axs5.text(0, 31, 'U(60E, 15N)')
plt.legend(['filter_annual_semi', '122'])
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s", fontsize=14)
axs5.grid(linestyle="--")
axs5.title.set_text("day 122 cycle")

axs6 = fig1.add_subplot(4, 2, 6)
axs6.plot(time, filter_out_annual_semi_annual_cycle, )
axs6.plot(time, day_122_cycle,)
axs6.set_xlim([1, 365])
axs6.set_ylim([-15, 30])
axs6.text(0, 31, 'U(60E, 15N)')
plt.legend(['filter_annual_semi', '122'])
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s", fontsize=14)
axs6.grid(linestyle="--")
axs6.title.set_text("day 122 cycle")

axs7 = fig1.add_subplot(4, 2, 7)
axs7.plot(time, original, )
axs7.plot(time, annual_semi_annual_day122_seasonal_cycle,)
axs7.set_xlim([1, 365])
axs7.set_ylim([-15, 30])
axs7.text(0, 31, 'U(60E, 15N)')
plt.legend(['original', '122'])
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs7.grid(linestyle="--")
axs7.title.set_text("annual + semi + day122\n + seasonal cycle")

axs8 = fig1.add_subplot(4, 2, 8)
axs8.plot(time, filter_out_annual_semi_annual_day122_seasonal_cycle, )
axs8.plot(time, day_6_to_12_cycle,)
axs8.set_xlim([1, 365])
axs8.set_ylim([-15, 30])
axs8.text(0, 31, 'U(60E, 15N)')
plt.legend(['filter_annual_semi', '6 to 122'])
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs8.grid(linestyle="--")
axs8.title.set_text("day 6~12 cycle")

fig1.tight_layout()

# Page 2
fig2 = plt.figure(figsize=(8.27, 11.69), dpi=600)

axs1 = fig2.add_subplot(4, 2, 1)
axs1.plot(time, original, )
axs1.plot(time, mean_value,)
axs1.set_xlim([1, 365])
axs1.set_ylim([-15, 30])
axs1.text(0, 31, 'U(60E, 15N)')
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
plt.legend(['original', 'mean'])
axs1.grid(linestyle="--")
axs1.title.set_text("original")

axs2 = fig2.add_subplot(4, 2, 2)
axs2.plot(time, mean_value)
axs2.plot(time, annual_cycle, linestyle="--")
axs2.plot(time, semi_annual_cycle, linestyle="-.")
axs2.plot(time, day_122_cycle, linestyle=":")
axs2.plot(time, seasonal_cycle, linestyle=(0, (5, 5)))
axs2.set_xlim([1, 365])
axs2.set_ylim([-15, 30])
axs2.text(0, 31, 'U(60E, 15N)')
plt.legend(['mean', 'annual', 'semi', '122', 'seasonal'])
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs2.grid(linestyle="--")
axs2.title.set_text("compose 1")

axs3 = fig2.add_subplot(4, 2, 3)
axs3.plot(time, annual_semi_annual_cycle)
axs3.plot(time, annual_semi_annual_day_122_cycle, linestyle="--")
axs3.plot(time, annual_semi_annual_day122_seasonal_cycle, linestyle="-.")
axs3.set_xlim([1, 365])
axs3.set_ylim([-15, 30])
axs3.text(0, 31, 'U(60E, 15N)')
plt.legend(['semi annual', 'semi annual 122', 'semi annual 122 seasonal'])
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs3.grid(linestyle="--")
axs3.title.set_text("compose 2")

axs4 = fig2.add_subplot(4, 2, 4)
axs4.plot(time, original, )
axs4.plot(time, annual_semi_annual_day122_seasonal_cycle,)
axs4.set_xlim([1, 365])
axs4.set_ylim([-15, 30])
axs4.text(0, 31, 'U(60E, 15N)')
plt.legend(['original', 'semi annual 122 seasonal'])
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs4.grid(linestyle="--")
axs4.title.set_text("annual + semi + day122\n + seasonal cycle")

axs5 = fig2.add_subplot(4, 2, 5)
axs5.plot(time, annual_semi_annual_day122_seasonal_cycle)
axs5.plot(time, day_6_to_12_cycle, linestyle="--")
axs5.set_xlim([1, 365])
axs5.set_ylim([-15, 30])
axs5.text(0, 31, 'U(60E, 15N)')
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
plt.legend(['semi annual 122 seasonal', '6 to 122'])
axs5.grid(linestyle="--")
axs5.title.set_text("compose 3")

axs6 = fig2.add_subplot(4, 2, 6)
axs6.plot(time, original, )
axs6.plot(time, annual_semi_annual_day122_seasonal_day_6_to_12_cycle,)
axs6.set_xlim([1, 365])
axs6.set_ylim([-15, 30])
axs6.text(0, 31, 'U(60E, 15N)')
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.legend(['original', 'semi annual 122 seasonal'])
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs6.grid(linestyle="--")
axs6.title.set_text("annual + semi + day122 + seasonal\n+ day 6~12 cycle")

axs7 = fig2.add_subplot(4, 2, 7)
axs7.plot(time, original, marker="o",
          markerfacecolor="white", markeredgecolor="black", markersize=3)
axs7.plot(time, annual_semi_annual_cycle,)
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
plt.legend(['original', 'semi annual'])
axs7.grid(linestyle="--")
axs7.title.set_text("850 hPa U-Wind")

axs8 = fig2.add_subplot(4, 2, 8)
axs8.plot(time, original, marker="o",
          markerfacecolor="white", markeredgecolor="black", markersize=3)
axs8.plot(time, annual_semi_annual_day122_seasonal_day_6_to_12_cycle,)
plt.xticks(ticks=range(1, 361, 50),
        #   color='#f00',
          fontsize=14,
)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
plt.legend(['original', 'semi annual 122 seasonal'])
axs8.grid(linestyle="--")
axs8.title.set_text("850 hPa U-Wind")

fig2.tight_layout()

# create a PDF file and add each figure as a separate page
with PdfPages('[AP3031]_hw01_109601003_林群賀.pdf') as pdf:
    pdf.savefig(fig1)
    pdf.savefig(fig2)