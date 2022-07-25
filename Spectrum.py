import numpy as np
import matplotlib.pyplot as plt


# Original code created by Michael Gallis
# From Java to Python conversion is created by Jones Jernfors with minor changes

# Gallis, Michael. X-Ray Spectrum Model. Computer software. 2014. Java (JRE) 1.6. 1 Apr. 2022
# <https://www.compadre.org/Repository/document/ServeFile.cfm?ID=13241&DocID=3775>.
# https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode

# This script is to calculate the x ray spectrum

def spectrum(Emax, mas, Z1=0, rho1=0, t1=0, Z2=-1, rho2=-1, t2=-1):
    Em0 = 160
    Im0 = 1
    Imax = Emax / Em0 * Im0
    Npoints = 320
    dE = Em0 / Npoints
    E0 = 100
    Z0 = 20
    tau0 = 0.085
    sigma0 = 0.2

    def filt(EE, ZZ, rrho, tt):
        mmu = rrho * (tau0 * (ZZ / Z0) ** 3 * (E0 / EE) ** 3 + sigma0 * (E0 / EE))
        return np.exp(-mmu * tt)

    def raw_spectrum(Etmp, this_Emax):
        Imax = this_Emax / Em0 * Im0
        I58 = 0
        if this_Emax > 70.3:
            I58 = Imax * (this_Emax - 58) / this_Emax * (0.086 * this_Emax - 6.05)
        Ispec_out = Imax * (this_Emax - Etmp) / this_Emax
        dI = 0
        if abs(Etmp - 58 - 0.499999 * dE) <= 0.5 * dE:
            dI = I58
        elif abs(Etmp - 59.5 - 0.499999 * dE) <= 0.5 * dE:
            dI = 1.75 * I58
        elif abs(Etmp - 67 - 0.499999 * dE) <= 0.5 * dE:
            dI = 0.597 * I58
        elif abs(Etmp - 69 - 0.499999 * dE) <= 0.5 * dE:
            dI = 0.157 * I58
        return max(Ispec_out + dI, 0)

    def base_spectrum(EE):
        return raw_spectrum(EE, Emax) * filt(EE, 29, 1, 0.1)

    def filt_spectrum(EE):
        return base_spectrum(EE) * filt(EE, Z1, rho1, t1)

    def filt_spectrum2(EE):
        return base_spectrum(EE) * filt(EE, Z1, rho1, t1) * filt(EE, Z2, rho2, t2)

    Etmp = 0
    if Emax > 70.3:
        I58 = Imax * (Emax - 58) / Emax * (0.086 * Emax - 6.05)

    baseKvp = []
    baseInt = []
    for i in range(1, Npoints + 1, 1):
        Etmp = i * dE
        baseKvp.append(Etmp)
        baseInt.append(base_spectrum(Etmp)*mas)

    Etmp = 0
    filtKvp = []
    filtInt = []
    for i in range(1, Npoints + 1, 1):
        Etmp = i * dE
        filtKvp.append(Etmp)
        filtInt.append(filt_spectrum(Etmp)*mas)

    Etmp = 0
    filtKvp2 = []
    filtInt2 = []
    for i in range(1,Npoints + 1, 1):
        Etmp = i * dE
        filtKvp2.append(Etmp)
        filtInt2.append(filt_spectrum2(Etmp)*mas)

    if Z1 and rho1 and t1 > 0 and Z2 and rho2 and t2 < 0:
        based = sum(np.multiply(baseKvp, baseInt))
        filted = sum(np.multiply(filtKvp, filtInt))
    elif Z1 and rho1 and t1 and Z2 and rho2 and t2 > 0:
        based = sum(np.multiply(baseKvp, baseInt))
        filted = sum(np.multiply(filtKvp2, filtInt2))
    else:
        based = 1
        filted = 1

    dose_coefficient = filted / based
    plt.clf()
    plt.plot(baseKvp, baseInt, 'b', label="Unfiltered")
    if Z1 and rho1 and t1 > 0 and Z2 and rho2 and t2 < 0:
        plt.plot(filtKvp, filtInt, 'r', label="Filtered")
    elif Z1 and rho1 and t1 and Z2 and rho2 and t2 > 0:
        plt.plot(filtKvp2,filtInt2, "r", label="Filtered")

    plt.xlabel("kVp")
    plt.ylabel("Relative intensity")
    plt.title("x ray spectrum")
    plt.legend(loc="upper right")
    plt.savefig("Images/fig.png")

    if Z1 and rho1 and t1 > 0 and Z2 and rho2 and t2 < 0:
        return filtKvp, filtInt, dose_coefficient
    elif Z1 and rho1 and t1 and Z2 and rho2 and t2 > 0:
        return filtKvp2, filtInt2, dose_coefficient
    return baseKvp, baseInt, dose_coefficient
