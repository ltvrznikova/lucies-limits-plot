#plot limits from experiments in 2018
import numpy as np
from pylab import *
from scipy import interpolate

matplotlib.rcParams.update({'font.size': 14})
fig, ax = subplots(1,1, figsize = (9,7))

#plot excluded region
m_excl, xs_excl = np.loadtxt('./limits/maximum_limits.txt', unpack = True)
fill_between(m_excl, xs_excl, 1e-28, color = '#aaffc3', zorder = 0, alpha = 0.5, lw = 0)

#plot pMSSM predictions
m_pMSSM, xs_pMSSM = np.loadtxt('./limits/contours-pMSSM11-1s.dat', unpack = True)
fill(m_pMSSM, xs_pMSSM, facecolor = '0.2', zorder = 0, alpha = 0.5, lw=0, label = 'pMSSM')
m_pMSSM_2s, xs_pMSSM_2s = np.loadtxt('./limits/contours-pMSSM11-2s.dat', unpack = True)
fill(m_pMSSM_2s, xs_pMSSM_2s, facecolor = '#424242', zorder = 1, alpha = 0.5, lw=0)

#plot neutrino floor
m_neutrinoLZ, xs_neutrinoLZ = np.loadtxt('./limits/SI_NeutrinoFloor_Ruppin_LZ_Fig3_1000ty.txt', unpack = True)
fill_between(m_neutrinoLZ, xs_neutrinoLZ, label = 'Neutrino floor', color = '#ffe119', zorder = 2, alpha = 0.5, lw=0)

#plot DAMA claims
mDL, xsDL = np.loadtxt('./limits/DAMA_detection.txt', unpack = True)
xsDL = xsDL*1e-36
blob2_start = np.where(mDL<10)[0][0]
fill(mDL[:blob2_start], xsDL[:blob2_start], color = '#ffd8b1', alpha = 0.5, label = 'DAMA')
fill(mDL[blob2_start:], xsDL[blob2_start:], color = '#ffd8b1', alpha = 0.5)

#plot limits from PICO C3F8
mPI, xsPI = np.loadtxt('./limits/PICO_CF3I_2015.txt', unpack = True)
plot(mPI, xsPI, label='PICO CF$_3$I 2015', zorder = 3, c = '#911eb4')

#plot limits from PICO C3F8
mP, xsP = np.loadtxt('./limits/PICO_C3F8_2017.txt', unpack = True)
plot(mP, xsP, label='PICO C$_3$F$_8$ 2017', zorder = 3, c = '#e6beff')

#plot limits from CDEX 10
mCDEX, xsCDEX = np.loadtxt('./limits/CDEX10_2018.txt', unpack = True)
plot(mCDEX, xsCDEX, label='CDEX-10 2018', zorder = 3, c = '#800000')

#plot limits from CDMSlite
mCD, xsCD = np.loadtxt('./limits/CDMSLite_2016.txt', unpack = True)
plot(mCD, xsCD, label='CDMSlite 2016', zorder = 3, c = '#e6194b')

#plot limits from CRESST II
mC, xsC = np.loadtxt('./limits/CRESSTII_2015.txt', unpack = True)
xsC = xsC*1e-36
plot(mC, xsC, label='CRESST-II 2015', zorder = 3, c='#42d4f4')

#plot limits from CRESST III
mC3, xsC3 = np.loadtxt('./limits/CRESSTIII_2017.txt', unpack = True)
xsC3 = xsC3*1e-36
plot(mC3, xsC3, label='CRESST-III 2017', zorder = 3, c = '#4363d8')

#plot limits from v-cleus
mv, xsv = np.loadtxt('./limits/nucleus_2017.txt', unpack = True)
mv = mv*1e-6
plot(mv, xsv, label='CRESST-surface 2017', zorder = 3, c = '#000075')

#plot limits from DarkSide50 - binomial 2018
mD, xsD = np.loadtxt('./limits/DarkSide50_binomial_2018.txt', unpack = True)
plot(mD, xsD, label='DarkSide-50 2018', zorder = 3, c = '#f032e6')

#plot limits from NEWS-G
mC, xsC = np.loadtxt('./limits/NEWS_G_2018.txt', unpack = True)
xsC = xsC*1e-36
plot(mC, xsC, label='NEWS-G 2018', zorder = 3, c = '#469990')

#plot limits from XMASS
mXM, xsXM = np.loadtxt('./limits/XMASS_2018.txt', unpack = True)
plot(mXM, xsXM, label='XMASS 2018', c = '#fabebe', zorder = 0)

#plot limits from PandaX
mXT, xsXT = np.loadtxt('./limits/PandaX_2017.txt', unpack = True)
plot(mXT, xsXT, label='PandaX-II 2017', zorder = 3, c = '#f58231')

#plot limits from XENON1T
mXT, xsXT = np.loadtxt('./limits/XENON1T_2018.txt', unpack = True)
plot(mXT, xsXT, label='XENON1T 2018', zorder = 3, c = '#3cb44b')

#plot limits from LUX complete exposure
mL, xsL = np.loadtxt('./limits/LUX_completeExposure_2016.txt', unpack = True)
xsL = xsL*1e-45
plot(mL, xsL, label='LUX', zorder = 3, c = '#000000')

#plot computed and expected upper limits from LUX
mass, xs_computed, xs_expected_median, xs_expected_m1sigma, xs_expected_p1sigma, xs_expected_m2sigma, xs_expected_p2sigma = np.loadtxt('./limits/LUX_Migdal_HeavyScalarMediator_noNuis_2018.txt', unpack = True)
xs_computed = xs_computed*1.e-45
plot(mass, xs_computed, c = '#000000', zorder = 3)

#plot LZ projection
mLZ, xsLZ = np.loadtxt('./limits/LZ_projection_2018.txt', unpack = True)
xsLZ = xsLZ*1e-36
plot(mLZ, xsLZ, '--', label='LZ', zorder = 3, c = '#000000')

#plot SuperCDMS projection
mSS, xSS = np.loadtxt('./limits/SuperCDMS_SNOLAB_projection_2017.txt', unpack = True)
plot(mSS, xSS, '--', label='SuperCDMS', zorder = 3, c = '#e6194b')

#plot XENONnT projections
mXT, xsXT = np.loadtxt('./limits/XENONnT_projection_2016.txt', unpack = True)
plot(mXT, xsXT, '--', label='XENON1T 2018', zorder = 3, c = '#3cb44b')


#make it pretty
xscale('log')
yscale('log')
xlim(3.00678e-1,1e3)
ylim(1e-50,1e-30)
xlabel('WIMP mass [GeV/c$^{2}$]')
ylabel('WIMP-nucleon cross section [cm$^{2}$]')
show()
ax.xaxis.set_tick_params(top = 'on', which='minor')
ax.yaxis.set_tick_params(top = 'on', which='major')


#save plot without legend
gcf().savefig('limits_plot_all_noLegend.pdf', bbox_inches = 'tight')

#save plot with legend
legend(fontsize = 10, loc='center left', bbox_to_anchor=(1, 0.5))
gcf().savefig('limits_plot_all.pdf', bbox_inches = 'tight')

