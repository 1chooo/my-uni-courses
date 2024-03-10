import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file -------
with open("linu850f.data", "rb") as f:
    data = np.fromfile(f, dtype=np.float32)

# for ii in range(len(data)):
#     print(ii, data[ii])
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

annualCycle += meanValue
semiAnnualCycle += meanValue
day122Cycle += meanValue
seasonalCycle += meanValue
annual_semiAnnual_day122_seasonalCycle += meanValue
day6To12Cycle += meanValue

filterOutAnnualCycle = data[2937:3302]
filterOutAnnual_semiAnnualCycle = data[3304:3669]
filterOutAnnual_semiAnnual_day122Cycle = data[3671:4036]
filterOutAnnual_semiAnnual_day122_seasonalCycle = data[4038:4403]
filterOutAnnual_semiAnnual_day122_seasonal_day6To12Cycle = data[4405:4770]

# for the x-axis
time = np.linspace(1, 365, 365)

# Plot the data -------
fig = plt.figure(figsize=(8.27, 11.69), dpi=600)

axs = plt.subplot(4, 2, 1)
axs.plot(time, original)
axs.plot(time, meanValue)
axs.set_xlim([1, 365])
axs.set_ylim([-15, 30])
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs.grid(linestyle="--")
axs.title.set_text("                               original          109601003")

axs = plt.subplot(4, 2, 2)
axs.plot(time, original,)
axs.plot(time, annualCycle,)
axs.set_xlim([1, 365])
axs.set_ylim([-15, 30])
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs.grid(linestyle="--")
axs.title.set_text("Hugo ChunHo Lin    annual cycle                        ")

axs = plt.subplot(4, 2, 3)
axs.plot(time, filterOutAnnualCycle,)
axs.plot(time, semiAnnualCycle,)
axs.set_xlim([1, 365])
axs.set_ylim([-15, 30])
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs.grid(linestyle="--")
axs.title.set_text("semi-annual cycle")

axs = plt.subplot(4, 2, 4)
axs.plot(time, filterOutAnnual_semiAnnualCycle,)
axs.plot(time, day122Cycle,)
axs.set_xlim([1, 365])
axs.set_ylim([-15, 30])
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs.grid(linestyle="--")
axs.title.set_text("day 122 cycle")

axs = plt.subplot(4, 2, 5)
axs.plot(time, filterOutAnnual_semiAnnual_day122Cycle,)
axs.plot(time, seasonalCycle,)
axs.set_xlim([1, 365])
axs.set_ylim([-15, 30])
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs.grid(linestyle="--")
axs.title.set_text("seasonal cycle")

axs = plt.subplot(4, 2, 6)
axs.plot(time, original,)
axs.plot(time, annual_semiAnnual_day122_seasonalCycle,)
axs.set_xlim([1, 365])
axs.set_ylim([-15, 30])
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs.grid(linestyle="--")
axs.title.set_text("annual+semi+day122+seasonal cycle")

axs = plt.subplot(4, 2, 7)
axs.plot(time, filterOutAnnual_semiAnnual_day122_seasonalCycle,)
axs.plot(time, day6To12Cycle,)
axs.set_xlim([1, 365])
axs.set_ylim([-15, 30])
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs.grid(linestyle="--")
axs.title.set_text("day 6~12 cycle")

axs = plt.subplot(4, 2, 8)
axs.plot(time, meanValue)
axs.plot(time, annualCycle, linestyle="--")
axs.plot(time, semiAnnualCycle, linestyle="-.")
axs.plot(time, day122Cycle, linestyle=":")
axs.set_xlim([1, 365])
axs.set_ylim([-15, 30])
plt.xlabel("Days", fontsize=14)
plt.ylabel("Wind speed(m/s)", fontsize=14)
axs.grid(linestyle="--")
axs.title.set_text("compose")

fig.tight_layout()
plt.savefig("test.pdf")
plt.show()