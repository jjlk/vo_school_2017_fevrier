# coding: utf8

# Ouverture du catalogue
import stilts
filename = '../catalogues/gll_psc_v16.fit'
table_3fgl = stilts.tread(filename)

# selectionne les BL Lacs et les FSRQs
table_bll = table_3fgl.cmd_select('equals(CLASS1,"bll") || equals(CLASS1,"BLL")')
table_fsrq = table_3fgl.cmd_select('equals(CLASS1,"fsrq") || equals(CLASS1,"FSRQ")')

# Faire un plot indice spectral Vs energie pivot
stilts.plot2d(in_bll=table_bll, name_bll='BL Lacs',
              # bll
              xdata_bll='Pivot_Energy', ydata_bll='PowerLaw_Index',
              shape_bll='open_circle', colour_bll='blue', size_bll='2',
              # fsrq
              in_fsrq=table_fsrq, name_fsrq='FSRQs',
              xdata_fsrq='Pivot_Energy', ydata_fsrq='PowerLaw_Index',
              shape_fsrq='open_square', colour_fsrq='red', size_fsrq='2',
              xlog='true', legend='true', grid='true')

# Ajouter de paramètres HR23 et HR34 dans les tables (3FGL direct)
# Energy moyenne de la bande en énergie (hypothèse power law)
table_3fgl = table_3fgl.cmd_addcol('MeanEnergy2',
                                 '(1.-PowerLaw_Index)/(2.-PowerLaw_Index)*\
(pow(1000.,2.-PowerLaw_Index)-pow(300.,2.-PowerLaw_Index))/(pow(1000.,1.-\
PowerLaw_Index)-pow(300.,1.-PowerLaw_Index))')
table_3fgl = table_3fgl.cmd_addcol('MeanEnergy3','(1.-PowerLaw_Index)/(2.-PowerLaw_Index)*\
(pow(3000.,2.-PowerLaw_Index)-pow(1000.,2.-PowerLaw_Index))/(pow(3000.,1.-\
PowerLaw_Index)-pow(1000.,1.-PowerLaw_Index))')
table_3fgl = table_3fgl.cmd_addcol('MeanEnergy4','(1.-PowerLaw_Index)/(2.-PowerLaw_Index)*\
(pow(10000.,2.-PowerLaw_Index)-pow(3000.,2.-PowerLaw_Index))/(pow(10000.,1.\
-PowerLaw_Index)-pow(3000.,1.-PowerLaw_Index))')

# Calcul du flux en énergie 
table_3fgl = table_3fgl.cmd_addcol('EnergyFlux2','MeanEnergy2*Flux300_1000*1.60217657*1.e-19*1.e7*1.e6')
table_3fgl = table_3fgl.cmd_addcol('EnergyFlux3','MeanEnergy3*Flux1000_3000*1.60217657*1.e-19*1.e7*1.e6')
table_3fgl = table_3fgl.cmd_addcol('EnergyFlux4','MeanEnergy4*Flux3000_10000*1.60217657*1.e-19*1.e7*1.e6')

# Calcul des hardness
table_3fgl = table_3fgl.cmd_addcol('HR23','(EnergyFlux3-EnergyFlux2)/(EnergyFlux3+EnergyFlux2)')
table_3fgl = table_3fgl.cmd_addcol('HR34','(EnergyFlux4-EnergyFlux3)/(EnergyFlux4+EnergyFlux3)')

# Nouvelles sélections
table_bll = table_3fgl.cmd_select('equals(CLASS1,"bll") || equals(CLASS1,"BLL")')
table_fsrq = table_3fgl.cmd_select('equals(CLASS1,"fsrq") || equals(CLASS1,"FSRQ")')

# Faire un plot HR23 Vs HR34
stilts.plot2d(in_bll=table_bll, name_bll='BL Lacs',
              xdata_bll='HR23', ydata_bll='HR34',
              shape_bll='open_circle', colour_bll='blue', size_bll='2',
              in_fsrq=table_fsrq, name_fsrq='FSRQs',
              xdata_fsrq='HR23', ydata_fsrq='HR34',
              shape_fsrq='open_square', colour_fsrq='red', size_fsrq='2',
              legend='true', grid='true')


# Partie 2 : Différence de redshift entre les BL Lacs et les FSRQs

# Concatenate table :
table_blazar = stilts.tcat(in_=[table_bll, table_fsrq])

# Obtenir le catalogue 3LAC, haute latitude, (Vizier, Topcat TAP, ou autres)
# J/ApJ/810/14/highlat
filename = '../catalogues/3LAC.fits'
table_3lac = stilts.tread(filename)

# Cross match avec le 3LAC (haute latitude (|b|>10 degree))
# avec le nom des sources (ici besoin de modifier le nom dans la table 3LAC)
table_3lac = table_3lac.cmd_addcol('Source_Name','"3FGL " + _3FGL')
#table_3lac = table_3lac.write('bob.fits')

table_blazar_3lac_highlat = stilts.tmatch2(in1=table_blazar,
                                           in2=table_3lac,
                                           values1='Source_Name',
                                           values2='Source_Name',
                                           matcher='exact',
                                           #param=1,
                                           join='1and2')

# select again bll and fsrq:
table_3lac_bll = table_blazar_3lac_highlat.cmd_select('equals(CLASS1,"bll") || equals(CLASS1,"BLL")')
table_3lac_fsrq = table_blazar_3lac_highlat.cmd_select('equals(CLASS1,"fsrq") || equals(CLASS1,"FSRQ")')

# kill sources with no redshift
table_3lac_bll = table_3lac_bll.cmd_select('!NULL_z')
table_3lac_fsrq = table_3lac_fsrq.cmd_select('!NULL_z')

# plot redshift distribution 
# marche pas mal fait
# stilts.plot2plane(in_fsrq=table_3lac_fsrq, layer_fsrq='histogram',
#                   x_fsrq='z', color_fsrq='red',
#                   in_bll=table_3lac_bll, layer_bll='histogram',
#                   x_bll='z', color_bll='blue',
#                   legend='true', grid='true', seq=['_fsrq','_bll'])
# deprecated mais fonctionnel
stilts.plothist(in_bll=table_3lac_bll,
                xdata_bll='z', barstyle_bll='tops', name_bll='BL Lacs',
                in_fsrq=table_3lac_fsrq, name_fsrq='FSRQs',
                xdata_fsrq='z', barstyle_fsrq='tops',
                legend='true', grid='true')



# Bonus
# Exemple de plot en 2D
stilts.plot2d(in_3fgl=table_3fgl, xdata_3fgl='GLON', ydata_3fgl='GLAT',
              xerror_3fgl='Conf_95_SemiMinor',
              yerror_3fgl='Conf_95_SemiMajor',
              colour_3fgl='black', size_3fgl=1, shape_3fgl='filled_circle',
              in_bll=table_3lac_bll, xdata_bll='GLON', ydata_bll='GLAT',
              colour_bll='blue', size_bll=1, shape_bll='filled_circle',
              in_fsrq=table_3lac_fsrq, xdata_fsrq='GLON', ydata_fsrq='GLAT',
              colour_fsrq='red', size_fsrq=1, shape_fsrq='filled_circle',
              xlabel="l (Deg)",
              ylabel="b (Deg)",
              name_3fgl='3FGL', name_bll='BL Lacs', name_fsrq='FSRQs', legend='true')
