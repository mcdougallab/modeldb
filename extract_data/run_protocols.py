"""
TODO: 151817... so many options, not sure how to run
TODO: redo 3507... there are actually 3 figures there... well, maybe, the models are the same

TODO: 146376: need to load morphometric file... not sure what it wants... need to manually curate
TODO: 139656 -- large network
TODO: 97917_*
TODO: 93326 -- maybe this should be more than 1... depending on VClamp/IClamp?
TODO: 147366 -- this is a lytton model... nonstandard setup
TODO: 140881 -- another lytton model... no fadvances, json_generator fails
TODO: 12631 -- another lytton model... no fadvances, json_generator fails
TODO: 19366_1 -- doesn't actually run... need to click the "Plot" buttons, but not clear where they come from
TODO: 22203 -- runs everything in a different process!
TODO: 124513 -- large model, complains about not running an fadvance, but seems like it must
TODO: 95960 -- can switch between many cells and many figures...
TODO: 51781 -- large network
TODO: 84612 -- push buttons... many many push buttons
TODO: 147460 -- buried code, no mosinit... shouldn't be that hard, looks like only two cases
TODO: 53437 -- possibly no sections?
TODO: 140038 -- push buttons, needs a manual setup
TODO: 144511 -- python... no mosinit.hoc (shouldn't be hard, but needs a manual setup)
TODO: 138379 -- no sections (lytton model)
TODO: 117207_* -- button pressing troubles (e.g. 'hoc.HocObject' object has no attribute 'RunBestFit')
TODO: 76879_* -- no sections (ermentrout)
TODO: 151404 -- runs with a script instead of mosinit... need to figure out what to do herer
TODO: 84589 -- no mosinit.hoc, but seems like it should have one (emailed Tom)
TODO: confirm 52034 sets up a structure (it says it doesn't run... figure out why not)
TODO: 21984 -- no sections
TODO: 140299_* -- should also have mixed diameter buttons but the files were missing when the run protocols were generated
TODO: 98017 -- useless mosinit, readme... no way of knowing how to run, lots of hoc files
TODO: 97985 -- shell scripts
TODO: 113435 -- modelview available, but only for 113435 which is an alternate of the xpp model 97747... database issues
TODO: 3658: lots of options, needs manual setup
TODO: 135902 -- can't figure out how to run
TODO: 114355 -- needs manual setup; many cell choices (see runme: main file is main.hoc)
TODO: 144549 -- no sections
TODO: 151282 -- extra_scatter_gather not allowed with multiple threads
TODO: 114359 -- methods paper. not sure what's going on here
TODO: 33728 -- pure artificial cells?
TODO: 139421 -- extra_scatter_gather not allowed with multiple threads
TODO: 144007 -- generates a large number of HOC files dynamically to run sweeps
TODO: 51196 -- two options selectable by a radio button somewhere, but too tired to find
TODO: 144570 -- mitral cell model from Shepherd lab... not sure how to create... modelview showed no sections
TODO: 144450 -- needs manual setup, not sure how to run
TODO: 33975 -- all but the outer two simulations crash
TODO: 151817 -- supports batch simulation, not quite sure what's going on, also radiobuttons
TODO: 144589 -- crashes NEURON's modelview
TODO: 150284 -- runs with scripts
TODO: 3808 -- MyFirstNEURON -- complicated NEURON demo, nearly infinite number of options
TODO: 97868 -- Sam model, weird errors from NQS
TODO: 136309 -- many cells to choose from, no GUI
TOFINISH: 83319_3 and 83319_4 -- no sections
TODO: 97874 -- NQS no demo
TODO: 3793 -- complicated model with many layers that needs to be done manually
TODO: 114665 -- not sure how to explain
TODO: 64229 -- multiple mosinits... it looks like the real one is in the root folder, but confused
TODO: 144579 -- looks like needs a PBS installation, runs with a script
TODO: 9888 -- choose parameters from two panels, needs manual setup
TODO: 141505 -- runs with scripts
TODO: 3817 -- no sections?
TODO: 83440 -- multiple versions
TODO: 149000 -- Loading morphology confusion
TODO: 105507 -- Lytton model
TODO: 116838 -- Lytton model
TODO: 144538 -- Sam, George, Cliff, Bill... seems to be missing files
TODO: 141063 -- multiple button sets to choose HCN type and graph
TODO: 18501 -- many many cells, and two figures for each
TODO: 3264_4,5 -- no sections (the other cases work)... protocol instructions commented out
TODO: 19746 -- broke h.allsec somehow. protocol instructions left in but commented out
TODO: 141272 -- couldn't find accept button somehow (also: uses xradiobuttons, but straightforwardish)
TODO: 152197 -- multiple threads breaks extra_scatter_gather
TODO: 143671 -- there is a button for pick a cell, but not visible... not sure how to run exactly
TODO: 137845 -- no sections? or are they all on different processors?
TODO: 125385 -- syntax errors with both branches
TODO: 5426 -- buttons, loading of idraw?
TODO: 144526 -- crashes NEURON's modelview
TODO: 149174 -- requires editing runall.py, also a script
TODO: 138273 -- MATLAB must be run before NEURON
TODO: 147461 -- extra_scatter_gather does not work with multiple threads
TODO: 150621 -- there are messages about changing parameters before running; should we add this?
TODO: 83523 -- no simulation; just mod files
TODO: 147141 -- runs via script
TODO: 144054 -- mitral cell model. requires selecting a cell
TODO: 53893 -- no sections?
TODO: 116838 -- repeated prompts
TODO: 53965 -- 3 choices of models, buttons for each

Some models need manual intervention:
53869 -- press enter after the h.restart
143114_* -- press enter after h.load_file

136715 -- contains additional instructions in the readme about changing parameters, which these instructions do not do

Skipped 39948 -- lots of buttons, not immediately clear how to use

Skipped for now: Traub et al 2005
123897_2 crashes with "NEURON: procedure too big", also have to rename lib/U_Dvdt.hoc to fix case sensitive filename issue
93321_* causes classic modelview to core dump
143635 -- Amanda Casale's model only presents one parameter set when run with mosinit.hoc, but two others are available; should these be viewable in modelview?
28316_1 -- classic modelview crashes due to point processes not being inserted in a section... still need to put in the rest of 28316_*, but seems no point for now
141273 -- no mosinit.hoc; not clear what's going on

127388 -- interesting model. no fadvance

144586 -- no sections. no modelview yet

71312 -- skipped for now, not sure if 1 modelview or 16

20212 -- to run, need to have . on path



Weird quirks:
19920 says it didn't fadvance, but it seems to
116862 says it didn't fadvance, but it seems to
"""

"""
added today:
(ran at work)
126640, 116491, 7988_*, 114394, 105385_*, 3660, 82849, 10360, 83319_*, 148644, 145672_*, 112359_*, 146565, 18742_*, 102288, 2730_*, 149415, 2487_*, 3342, 3648, 3665, 127995, 50210_*, 97263, 146030, 43039_*, 87454, 143100, 149100, 2488_*, 3677_*, 144482

3673, 135898, 150245_*, 140471, 128446, 3264_*, 29942, 64228_*, 150556, 9852_*, 87585, 120692_*, 62673, 110560_*, 53451_*, 62284, 8210_*, 143442, 3805_*, 3810, 3493, 18502_*, 116769, 39949, 50391, 144523, 108459_*, 64259, 64195_*, 150621_*, 121253_*, 150446_*, 139657_*, 136095, 19591_*, 124043, 3815_*, 19747, 129067_*, 19920, 9849, 116862, 9889, 3684, 3533, 3670_*, 17663_*, 3343_*, 37819, 122442_*

(ran at home)
74298, 64216, 139883_*, 84655, 151443, 3511, 127507_*, 83547, 97860, 147539_*, 118631, 3488, 3457, 3491, 3483, 3802, 144533_*, 50997_*, 95870

added from bottom up:
144566 3812 3682 93325 96444_* 20014_* 53569 62285 122442

***
NEXT TIME
***

From top down: 
From bottom up: Tight junction model of CNS myelinated axons (Devaux and Gow 2008)




deal with 20212 (Poirazi?) -- only have one so far
remove 20212_2 since missing a variable definition? or make work?

    '20212_2':
        {
            'variant': 'Disperse Equal Sized',
            'compile': ['cd CA1_multi/experiment/cluster-dispersion', 'nrnivmodl ../../mechanism', 'chmod +x newshiftsyn', 'export PATH=.:$PATH'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Disperse_equal_sized.hoc")'],
            'cleanup': ['cd ../../..', 'rm -fr CA1_multi']
        },        

"""
automatically_curated_protocols = {
    '170030_1':
        {
            'variant':'Kv7.2+Kv7.3',
            'compile': ['cd Kv72_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Kv72_ModelDB']
        },
    '170030_2':
        {
            'variant':'Kv7.2+Kv7.2R201C+Kv7.3',
            'compile': ['cd Kv72_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("setKvR201C()")'],
            'cleanup': ['cd ../', 'rm -fr Kv72_ModelDB']
        },
    '83344_1':
        {
            'variant': 'a. Backpropagating AP',
            'compile': ['cd BACFiring', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.figBAP()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr BACFiring']
        },
    '83344_2':
        {
            'variant': 'b. EPSP',
            'compile': ['cd BACFiring', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.figEPSP()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr BACFiring']
        },
    '83344_3':
        {
            'variant': 'c. Ca spike',
            'compile': ['cd BACFiring', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.figCa()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr BACFiring']
        },
    '83344_4':
        {
            'variant': 'd. BAC firing',
            'compile': ['cd BACFiring', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.figBAC()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr BACFiring']
        },
    '180373':
        {
            'compile': ['cd ShaiEtAl2015', 'nrnivmodl simulationcode'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ShaiEtAl2015']
        },
    '122442_1':
        {
            'variant': 'Double Cable Model (DCM)',
            'compile': ['cd Gow_Devaux_2009'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("DCM_0.6um_axon.ses")'],
            'cleanup': ['cd ../', 'rm -fr Gow_Devaux_2009']
        },
    '122442_2':
        {
            'variant': 'Tight Junction Model (TJM)',
            'compile': ['cd Gow_Devaux_2009'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("TJM_0.6um_axon.ses")'],
            'cleanup': ['cd ../', 'rm -fr Gow_Devaux_2009']
        },
    '37819':
        {
            'compile': ['cd thal_aug_resp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr thal_aug_resp']
        },
    '3343_1':
        {
            'variant': 'Spindle oscillations - short run',
            'compile': ['cd DLGN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fspin")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr DLGN_NEW']
        },
    '3343_2':
        {
            'variant': 'Spindle oscillations - long run',
            'compile': ['cd DLGN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("FspinL")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr DLGN_NEW']
        },
    '3343_3':
        {
            'variant': 'Bicuculline-induced oscillations - short run',
            'compile': ['cd DLGN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fbic")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr DLGN_NEW']
        },
    '3343_4':
        {
            'variant': 'Bicuculline-induced oscillations - long run',
            'compile': ['cd DLGN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("FbicL")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr DLGN_NEW']
        },
    '3343_5':
        {
            'variant': 'Delta oscillations - short run',
            'compile': ['cd DLGN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fdelta")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr DLGN_NEW']
        },
    '3343_6':
        {
            'variant': 'Delta oscillations - long run',
            'compile': ['cd DLGN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("FdeltaL")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr DLGN_NEW']
        },
   '17663_1':
        {
            'variant': 'Burst behavior in single-compartment model',
            'compile': ['cd dendre', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("re1_cc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendre']
        },
    '17663_2':
        {
            'variant': 'Burst behavior in 3-compartment model',
            'compile': ['cd dendre', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("re3_cc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendre']
        },
    '17663_3':
        {
            'variant': 'Voltage-clamp in 3-compartment cell model',
            'compile': ['cd dendre', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("re3_vc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendre']
        },
    '17663_4':
        {
            'variant': 'Burst behavior in detailed cell model',
            'compile': ['cd dendre', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("re80_cc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendre']
        },
    '17663_5':
        {
            'variant': 'Voltage-clamp in detailed cell model',
            'compile': ['cd dendre', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("re80_vc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendre']
        },
    '17663_6':
        {
            'variant': 'Burst behavior in dissociated cell model',
            'compile': ['cd dendre', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("reD_cc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendre']
        },
    '17663_7':
        {
            'variant': 'Voltage-clamp in dissociated cell model',
            'compile': ['cd dendre', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("reD_vc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendre']
        },
    '3670_1':
        {
            'variant': 'Fig. 5a',
            'compile': ['cd NTW_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig5A")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NTW_NEW']
        },
    '3670_2':
        {
            'variant': 'Fig. 5b',
            'compile': ['cd NTW_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig5B")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NTW_NEW']
        },
    '3670_3':
        {
            'variant': 'Fig. 6a',
            'compile': ['cd NTW_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig6A")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NTW_NEW']
        },
    '3670_4':
        {
            'variant': 'Fig. 6b',
            'compile': ['cd NTW_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig6B")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NTW_NEW']
        },
    '3670_5':
        {
            'variant': 'Fig. 6c',
            'compile': ['cd NTW_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig6C")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NTW_NEW']
        },
    '3670_6':
        {
            'variant': 'Fig. 6d',
            'compile': ['cd NTW_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig6D")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NTW_NEW']
        },
    '3670_7':
        {
            'variant': 'Fig. 13a',
            'compile': ['cd NTW_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig13A")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NTW_NEW']
        },
    '3670_8':
        {
            'variant': 'Fig. 13b',
            'compile': ['cd NTW_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig13B")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NTW_NEW']
        },
    '3533':
        {
            'compile': ['cd IcaT', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr IcaT']
        },
    '3684':
        {
            'compile': ['cd h_tc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr h_tc']
        },
    '9889':
        {
            'compile': ['cd lytton97', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr lytton97']
        },
    '116862':
        {
            'compile': ['cd b09jan13', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr b09jan13']
        },
    '9849':
        {
            'compile': ['cd westerfield78'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr westerfield78']
        },
    '19920':
        {
            'compile': ['cd CaT', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CaT']
        },
    '19747':
        {
            'compile': ['cd CoHCNS2000', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CoHCNS2000']
        },
    '3815_1':
        {
            'variant': 'Fig. 1A pyramid-->pyramid (depression)',
            'compile': ['cd tsodyks', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig1a()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr tsodyks']
        },
    '3815_2':
        {
            'variant': 'Fig. 1B pyramid-->interneuron at 20 Hz (facilitation)',
            'compile': ['cd tsodyks', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig1b()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr tsodyks']
        },
    '3815_3':
        {
            'variant': 'Fig. 1C pyramid-->interneuron at 70 Hz (facilitation-depression)',
            'compile': ['cd tsodyks', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig1c()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr tsodyks']
        },
    '124043':
        {
            'compile': ['cd larkumEtAl2009_2', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr larkumEtAl2009_2']
        },
    '19591_1':
        {
            'variant': 'Figure 1A',
            'compile': ['cd granule', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig1a")'],
            'cleanup': ['cd ../', 'rm -fr granule']
        },
    '19591_2':
        {
            'variant': 'Figure 2A1',
            'compile': ['cd granule', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2a1")'],
            'cleanup': ['cd ../', 'rm -fr granule']
        },
    '19591_3':
        {
            'variant': 'Figure 2A2',
            'compile': ['cd granule', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2a2")'],
            'cleanup': ['cd ../', 'rm -fr granule']
        },
    '19591_4':
        {
            'variant': 'Figure 2A3',
            'compile': ['cd granule', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2a3")'],
            'cleanup': ['cd ../', 'rm -fr granule']
        },
    '19591_5':
        {
            'variant': 'Figure 2B1',
            'compile': ['cd granule', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2b1")'],
            'cleanup': ['cd ../', 'rm -fr granule']
        },
    '19591_6':
        {
            'variant': 'Figure 2B2',
            'compile': ['cd granule', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2b2")'],
            'cleanup': ['cd ../', 'rm -fr granule']
        },
    '19591_7':
        {
            'variant': 'Figure 2B3',
            'compile': ['cd granule', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2b3")'],
            'cleanup': ['cd ../', 'rm -fr granule']
        },
    '136095':
        {
            'variant': 'Run neocortical column simulation & display output',
            'compile': ['cd ncdemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.dorun()'],
            'cleanup': ['cd ../', 'rm -fr ncdemo']
        },
    '139657_1':
        {
            'variant': '50 hz',
            'compile': ['cd Kopp-Scheinpflug2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.NetStim[0].interval=20', 'h.myrun(h.NetStim[0].interval)'],
            'cleanup': ['cd ../', 'rm -fr Kopp-Scheinpflug2011']
        },
    '139657_2':
        {
            'variant': '100 hz',
            'compile': ['cd Kopp-Scheinpflug2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.NetStim[0].interval=10', 'h.myrun(h.NetStim[0].interval)'],
            'cleanup': ['cd ../', 'rm -fr Kopp-Scheinpflug2011']
        },
    '139657_3':
        {
            'variant': '200 hz',
            'compile': ['cd Kopp-Scheinpflug2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.NetStim[0].interval=5', 'h.myrun(h.NetStim[0].interval)'],
            'cleanup': ['cd ../', 'rm -fr Kopp-Scheinpflug2011']
        },
    '139657_4':
        {
            'variant': '300 hz',
            'compile': ['cd Kopp-Scheinpflug2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.NetStim[0].interval=3.3', 'h.myrun(h.NetStim[0].interval)'],
            'cleanup': ['cd ../', 'rm -fr Kopp-Scheinpflug2011']
        },
    '139657_5':
        {
            'variant': '400 hz',
            'compile': ['cd Kopp-Scheinpflug2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.NetStim[0].interval=2.5', 'h.myrun(h.NetStim[0].interval)'],
            'cleanup': ['cd ../', 'rm -fr Kopp-Scheinpflug2011']
        },
    '121253_1':
        {
            'variant': 'Short demo run',
            'compile': ['cd stnAxonDbsModel', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.short_run()'],
            'cleanup': ['cd ../', 'rm -fr stnAxonDbsModel']
        },
    '121253_2':
        {
            'variant': 'fig 2b (2 hour run)',
            'compile': ['cd stnAxonDbsModel', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig2b()'],
            'cleanup': ['cd ../', 'rm -fr stnAxonDbsModel']
        },
    '150621_1':
        {
            'variant': 'Figure 2A',
            'compile': ['cd MahonEtAl2000', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig2a()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr MahonEtAl2000']
        },
    '150621_2':
        {
            'variant': 'Figure 3A',
            'compile': ['cd MahonEtAl2000', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3a()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr MahonEtAl2000']
        },
    '64195_1':
        {
            'variant': 'fig6B simulation',
            'compile': ['cd Stochastic', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig6B")'],
            'cleanup': ['cd ../', 'rm -fr Stochastic']
        },
    '64195_2':
        {
            'variant': 'Short run simulation',
            'compile': ['cd Stochastic', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("shortRun")'],
            'cleanup': ['cd ../', 'rm -fr Stochastic']
        },
    '64259':
        {
            'compile': ['cd NCnote', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NCnote']
        },
    '144523':
        {
            'compile': ['cd LuthmanEtAl2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.DCNrun()'],
            'cleanup': ['cd ../', 'rm -fr LuthmanEtAl2011']
        },
    '50391':
        {
            'compile': ['cd stochastichh'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr stochastichh']
        },
    '39949':
        {
            'compile': ['cd spinycell', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr spinycell']
        },
    '116769':
        {
            'compile': ['cd SpineCaModel', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr SpineCaModel']
        },
    '18502_1':
        {
            'variant': 'branch near shaft',
            'compile': ['cd spinebranches', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("ltp_two")'],
            'cleanup': ['cd ../', 'rm -fr spinebranches']
        },
    '18502_2':
        {
            'variant': 'regular sized necks',
            'compile': ['cd spinebranches', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("ltp_spl")'],
            'cleanup': ['cd ../', 'rm -fr spinebranches']
        },
    '18502_3':
        {
            'variant': '0.25 nS AMPA (control)',
            'compile': ['cd spinebranches', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("ltp_ran")'],
            'cleanup': ['cd ../', 'rm -fr spinebranches']
        },
    '18502_4':
        {
            'variant': '0.35 nS AMPA (control)',
            'compile': ['cd spinebranches', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("ltp_ttt")'],
            'cleanup': ['cd ../', 'rm -fr spinebranches']
        },
    '3493':
        {
            'compile': ['cd motoneuron', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr motoneuron']
        },
    '3810':
        {
            'compile': ['cd MRGaxon', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr MRGaxon']
        },
    '143442':
        {
            'compile': ['cd FoustEtAl2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.node_inj()'],
            'cleanup': ['cd ../', 'rm -fr FoustEtAl2011']
        },
    '8210_1':
        {
            'variant': 'inject soma',
            'compile': ['cd spikeinit', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.soma_inj()'],
            'cleanup': ['cd ../', 'rm -fr spikeinit']
        },
    '8210_2':
        {
            'variant': 'inject dend',
            'compile': ['cd spikeinit', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.dend_inj()'],
            'cleanup': ['cd ../', 'rm -fr spikeinit']
        },
    '62284':
        {
            'compile': ['cd ba', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.steprun()'],
            'cleanup': ['cd ../', 'rm -fr ba']
        },
    '110560_1':
        {
            'variant': 'Potassium 1. L5 Pyramidal Neuron',
            'compile': ['cd SpaceClampDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("potassium.hoc")', 'h.fig1a()'],
            'cleanup': ['cd ../', 'rm -fr SpaceClampDemo']
        },
    '110560_2':
        {
            'variant': 'Potassium 2. L4 interneuron',
            'compile': ['cd SpaceClampDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("potassium.hoc")', 'h.fig1b()'],
            'cleanup': ['cd ../', 'rm -fr SpaceClampDemo']
        },
    '110560_3':
        {
            'variant': 'Potassium 3. L2/3 bipolar interneuron',
            'compile': ['cd SpaceClampDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("potassium.hoc")', 'h.fig1c()'],
            'cleanup': ['cd ../', 'rm -fr SpaceClampDemo']
        },
    '110560_4':
        {
            'variant': 'Potassium 4. L4 spiny stellate',
            'compile': ['cd SpaceClampDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("potassium.hoc")', 'h.fig1d()'],
            'cleanup': ['cd ../', 'rm -fr SpaceClampDemo']
        },
    '110560_5':
        {
            'variant': 'Calcium 1. L5 Pyramidal Neuron',
            'compile': ['cd SpaceClampDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("calcium.hoc")', 'h.fig1a()'],
            'cleanup': ['cd ../', 'rm -fr SpaceClampDemo']
        },
    '110560_6':
        {
            'variant': 'Calcium 2. L4 interneuron',
            'compile': ['cd SpaceClampDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("calcium.hoc")', 'h.fig1b()'],
            'cleanup': ['cd ../', 'rm -fr SpaceClampDemo']
        },
    '110560_7':
        {
            'variant': 'Calcium 3. L2/3 bipolar interneuron',
            'compile': ['cd SpaceClampDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("calcium.hoc")', 'h.fig1c()'],
            'cleanup': ['cd ../', 'rm -fr SpaceClampDemo']
        },
    '110560_8':
        {
            'variant': 'Calcium 4. L4 spiny stellate',
            'compile': ['cd SpaceClampDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("calcium.hoc")', 'h.fig1d()'],
            'cleanup': ['cd ../', 'rm -fr SpaceClampDemo']
        },
    '62673':
        {
            'compile': ['cd na2006', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr na2006']
        },
    '120692_1':
        {
            'variant': 'Figure 2-3',
            'compile': ['cd kootsey83', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load("fig2-3.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kootsey83']
        },
    '120692_2':
        {
            'variant': 'Figure 4-6',
            'compile': ['cd kootsey83', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load("fig4-6.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kootsey83']
        },
    '120692_3':
        {
            'variant': 'Figure 7',
            'compile': ['cd kootsey83', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load("fig7.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kootsey83']
        },
    '120692_4':
        {
            'variant': 'Figure 8-10',
            'compile': ['cd kootsey83', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load("fig8-10.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kootsey83']
        },
    '120692_5':
        {
            'variant': 'Figure 11-12',
            'compile': ['cd kootsey83', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load("fig11-12.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kootsey83']
        },
    '87585':
        {
            'compile': ['cd R859C', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr R859C']
        },
    '121259_1':
        {
            'variant': 'homogenous network run',
            'compile': ['cd bogaard2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("homrun.hoc")'],
            'cleanup': ['cd ../', 'rm -fr bogaard2009']
        },
    '121259_2':
        {
            'variant': 'heterogenous network run',
            'compile': ['cd bogaard2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("hetrun.hoc")'],
            'cleanup': ['cd ../', 'rm -fr bogaard2009']
        },
    '9852_1':
        {
            'variant': 'Figure 1A',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig1a()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_2':
        {
            'variant': 'Figure 1B',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig1b()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_3':
        {
            'variant': 'Figure 1C',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig1c()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_4':
        {
            'variant': 'Figure 1D',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig1d()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_5':
        {
            'variant': 'Figure 2A',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig2a()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_6':
        {
            'variant': 'Figure 2B',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig2b()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_7':
        {
            'variant': 'Figure 3A',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3a()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_8':
        {
            'variant': 'Figure 3B',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3b()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_9':
        {
            'variant': 'Figure 3C',
            'compile': ['cd moore83', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3c()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_10':
        {
            'variant': 'Figure 4A',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig4a()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_11':
        {
            'variant': 'Figure 4B',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig4b()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_12':
        {
            'variant': 'Figure 4C',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig4c()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_13':
        {
            'variant': 'Figure 5A',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5a()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_14':
        {
            'variant': 'Figure 5B',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5b()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_15':
        {
            'variant': 'Figure 5C',
            'compile': ['cd moore83'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5c()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '9852_16':
        {
            'variant': 'Figure 5D',
            'compile': ['cd moore83', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5d()'],
            'cleanup': ['cd ../', 'rm -fr moore83']
        },
    '150556':
        {
            'compile': ['cd BiddellJohnson2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr BiddellJohnson2013']
        },
    '29942':
        {
            'compile': ['cd lgnsigint', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr lgnsigint']
        },
#    '19746':
#        {
#            'compile': ['cd SNRCA1', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.steprun()'],
#            'cleanup': ['cd ../', 'rm -fr SNRCA1']
#        },
    '3264_1':
        {
            'variant': 'Fig. 3A using slow epsp',
            'compile': ['cd varela', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig3a()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr varela']
        },
    '3264_2':
        {
            'variant': 'Fig. 3C using slow epsp',
            'compile': ['cd varela', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig3c()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr varela']
        },
    '3264_3':
        {
            'variant': 'Fig. 3D using fast epsp',
            'compile': ['cd varela', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig3d()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr varela']
        },
#    '3264_4':
#        {
#            'variant': 'Fig. 3E',
#            'compile': ['cd varela', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig3e()', 'h.run()'],
#            'cleanup': ['cd ../', 'rm -fr varela']
#        },
#    '3264_5':
#        {
#            'variant': 'Artificial (integrate and fire) cell',
#            'compile': ['cd varela', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_art()', 'h.run()'],
#            'cleanup': ['cd ../', 'rm -fr varela']
#        },
    '3264_6':
        {
            'variant': '\'Biophysical\' cell with fast epsp',
            'compile': ['cd varela', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_cel()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr varela']
        },
    '3264_7':
        {
            'variant': '\'Biophysical\' cell with slow epsp',
            'compile': ['cd varela', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_cel2()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr varela']
        },
    '3264_8':
        {
            'variant': '\'Biophysical\' cell with multiple input streams',
            'compile': ['cd varela', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_test()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr varela']
        },
    '128446':
        {
            'variant': 'Init & Run',
            'compile': ['cd ShortTermPlasticityMFGRC_Nieus2006', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ShortTermPlasticityMFGRC_Nieus2006']
        },
    '140471':
        {
            'compile': ['cd Figure5', 'nrnivmodl mods'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr Figure5']
        },
    '150245_1':
        {
            'variant': 'trained network',
            'compile': ['cd a2dmodeldb', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.trainedrun()'],
            'cleanup': ['cd ../', 'rm -fr a2dmodeldb']
        },
    '150245_2':
        {
            'variant': 'naive network',
            'compile': ['cd a2dmodeldb', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.naiverun()'],
            'cleanup': ['cd ../', 'rm -fr a2dmodeldb']
        },
    '135898':
        {
            'compile': ['cd YuEtAlPNAS2007', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.soma_inj()'],
            'cleanup': ['cd ../', 'rm -fr YuEtAlPNAS2007']
        },
    '3673':
        {
            'compile': ['cd 5chan', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr 5chan']
        },
    '95870':
        {
            'compile': ['cd ROD', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ROD']
        },
    '144553_1':
        {
            'variant': 'Figure 9C-D ( dlPFC )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("main_fig9_pfcElec.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_2':
        {
            'variant': 'Figure 9C-D ( V1 )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("main_fig9_v1Elec.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_3':
        {
            'variant': 'Figure 10 ( dlPFC )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("main_fig10_pfc.hoc")'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_4':
        {
            'variant': 'Figure 10 ( baseline V1 )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("main_fig10_v1baseline.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_5':
        {
            'variant': 'Figure 10 ( tuned V1 )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("main_fig10_v1tuned.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_6':
        {
            'variant': 'Figure 11 ( PFC apical )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doApic = 1")', 'h.xopen("main_PFC-ApBas_fig11epsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_7':
        {
            'variant': 'Figure 11 ( PFC basal )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doApic = 0")', 'h.xopen("main_PFC-ApBas_fig11epsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_8':
        {
            'variant': 'Figure 11  V1, same gAMPA, apical )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doSynType = 0")', 'h.xopen("main_V1-ApBas_fig11epsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_9':
        {
            'variant': 'Figure 11 ( V1, same gAMPA, basal )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doSynType = 1")', 'h.xopen("main_V1-ApBas_fig11epsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_10':
        {
            'variant': 'Figure 11 ( V1, low gAMPA, apical )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doSynType = 2")', 'h.xopen("main_V1-ApBas_fig11epsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_11':
        {
            'variant': 'Figure 11 ( V1, low gAMPA, basal )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doSynType = 3")', 'h.xopen("main_V1-ApBas_fig11epsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_12':
        {
            'variant': 'Figure 12 ( PFC apical )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doApic = 1")', 'h.xopen("main_PFC-ApBas_fig12ipsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_13':
        {
            'variant': 'Figure 12 ( PFC basal )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doApic = 0")', 'h.xopen("main_PFC-ApBas_fig12ipsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_14':
        {
            'variant': 'Figure 12 ( V1, same gAMPA, apical )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doSynType = 0")', 'h.xopen("main_V1-ApBas_fig12ipsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_15':
        {
            'variant': 'Figure 12 ( V1, same gAMPA, basal )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doSynType = 1")', 'h.xopen("main_V1-ApBas_fig12ipsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_16':
        {
            'variant': 'Figure 12 ( V1, low gAMPA, apical )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doSynType = 2")', 'h.xopen("main_V1-ApBas_fig12ipsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '144553_17':
        {
            'variant': 'Figure 12 ( V1, low gAMPA, basal )',
            'compile': ['cd V1_PFC_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doSynType = 3")', 'h.xopen("main_V1-ApBas_fig12ipsc.hoc")'],#, 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr V1_PFC_ModelDB']
        },
    '3802':
        {
            'compile': ['cd kx_photo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kx_photo']
        },
    '3483':
        {
            'compile': ['cd na_rgc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr na_rgc']
        },
    '3491':
        {
            'compile': ['cd kdr_rgc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kdr_rgc']
        },
    '3457':
        {
            'compile': ['cd ca_rgc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ca_rgc']
        },
    '3488':
        {
            'compile': ['cd ka_rgc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ka_rgc']
        },
    '118631':
        {
            'compile': ['cd KoendgenEtAl2008', 'nrnivmodl mechanisms'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.graph_and_run()'],
            'cleanup': ['cd ../', 'rm -fr KoendgenEtAl2008']
        },
    '147539_1':
        {
            'variant': 'Membrane voltage sensitivity',
            'compile': ['cd Chirp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Chirp_Ih_V()'],
            'cleanup': ['cd ../', 'rm -fr Chirp']
        },
    '147539_2':
        {
            'variant': 'Rm sensitivity',
            'compile': ['cd Chirp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Chirp_Ih_Rm()'],
            'cleanup': ['cd ../', 'rm -fr Chirp']
        },
    '147539_3':
        {
            'variant': 'Cm sensitivity',
            'compile': ['cd Chirp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Chirp_Ih_Cm()'],
            'cleanup': ['cd ../', 'rm -fr Chirp']
        },
    '147539_4':
        {
            'variant': 'h conductance sensitivity',
            'compile': ['cd Chirp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Chirp_Gh()'],
            'cleanup': ['cd ../', 'rm -fr Chirp']
        },
    '147539_5':
        {
            'variant': 'h activation vhalf sensitivity',
            'compile': ['cd Chirp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Chirp_Ih_vhalf()'],
            'cleanup': ['cd ../', 'rm -fr Chirp']
        },
    '147539_6':
        {
            'variant': 'h activation time constant sensitivity',
            'compile': ['cd Chirp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Chirp_Ih_tau()'],
            'cleanup': ['cd ../', 'rm -fr Chirp']
        },
    '97860':
        {
            'compile': ['cd rejuvenation', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr rejuvenation']
        },
    '83547':
        {
            'compile': ['cd damodel', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr damodel']
        },
    '127507_1':
        {
            'variant': 'Fig. 2a2',
            'compile': ['cd KuznetsovaEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig2a2()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KuznetsovaEtAl2010']
        },
    '127507_2':
        {
            'variant': 'Fig. 2b2',
            'compile': ['cd KuznetsovaEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig2b2()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KuznetsovaEtAl2010']
        },
    '127507_3':
        {
            'variant': 'Fig. 2f2',
            'compile': ['cd KuznetsovaEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig2f2()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KuznetsovaEtAl2010']
        },
    '127507_4':
        {
            'variant': 'Fig. 6a solid',
            'compile': ['cd KuznetsovaEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig6asolid()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KuznetsovaEtAl2010']
        },
    '127507_5':
        {
            'variant': 'Fig. 6a dashed',
            'compile': ['cd KuznetsovaEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig6adashed()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KuznetsovaEtAl2010']
        },
    '3511':
        {
            'compile': ['cd mcn1', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr mcn1']
        },
    '151443':
        {
            'compile': ['cd BalbiEtAl2013', 'nrnivmodl channels'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr BalbiEtAl2013']
        },
    '84655':
        {
            'compile': ['cd oltedal', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("fig10a.hoc")'],
            'cleanup': ['cd ../', 'rm -fr oltedal']
        },
    '139883_1':
        {
            'variant': 'In vitro',
            'compile': ['cd ReConv', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Invitro()'],
            'cleanup': ['cd ../', 'rm -fr ReConv']
        },
    '139883_2':
        {
            'variant': 'In vivo',
            'compile': ['cd ReConv', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Invivo()'],
            'cleanup': ['cd ../', 'rm -fr ReConv']
        },
    '64216':
        {
            'variant': 'Init & Run',
            'compile': ['cd Kourennyi-etal2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.myrun()'],
            'cleanup': ['cd ../', 'rm -fr Kourennyi-etal2004']
        },
    '74298':
        {
            'compile': ['cd sth-model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file(1,"sample.hoc")'],
            'cleanup': ['cd ../', 'rm -fr sth-model']
        },
    '122442_1':
        {
            'variant': 'Double Cable Model (DCM)',
            'compile': ['cd Gow_Devaux_2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("DCM_0.6um_axon.ses")'],
            'cleanup': ['cd ../', 'rm -fr Gow_Devaux_2009']
        },
    '122442_2':
        {
            'variant': 'Tight Junction Model (TJM)',
            'compile': ['cd Gow_Devaux_2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("TJM_0.6um_axon.ses")'],
            'cleanup': ['cd ../', 'rm -fr Gow_Devaux_2009']
        },
    '62285':
        {
            'compile': ['cd b', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr b']
        },
    '53569':
        {
            'compile': ['cd lamina1', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr lamina1']
        },
    '20014_1':
        {
            'variant': 'Fig.2. A-D',
            'compile': ['cd kkt98', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(1)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kkt98']
        },
    '20014_2':
        {
            'variant': 'Fig.2. E-H',
            'compile': ['cd kkt98', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(2)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kkt98']
        },
    '20014_3':
        {
            'variant': 'Fig.3. A',
            'compile': ['cd kkt98', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(3)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kkt98']
        },
    '20014_4':
        {
            'variant': 'Fig.3.',
            'compile': ['cd kkt98', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(4)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kkt98']
        },
    '20014_5':
        {
            'variant': 'Fig.3. C',
            'compile': ['cd kkt98', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(5)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr kkt98']
        },
    '96444_1':
        {
            'variant': 'Ring (Serial)',
            'compile': ['cd HinesCarnevaleJNM2007', 'nrnivmodl random'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.launch("ring", "ringser.hoc")'],
            'cleanup': ['cd ../', 'rm -fr HinesCarnevaleJNM2007']
        },
    '96444_2':
        {
            'variant': 'Ring (Parallel)',
            'compile': ['cd HinesCarnevaleJNM2007', 'nrnivmodl random'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.launch("ring", "ringpar.hoc")'],
            'cleanup': ['cd ../', 'rm -fr HinesCarnevaleJNM2007']
        },
    '96444_3':
        {
            'variant': 'Random (Serial)',
            'compile': ['cd HinesCarnevaleJNM2007', 'nrnivmodl random'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.launch("random", "ran3ser.hoc")'],
            'cleanup': ['cd ../', 'rm -fr HinesCarnevaleJNM2007']
        },
    '96444_4':
        {
            'variant': 'Random (Parallel)',
            'compile': ['cd HinesCarnevaleJNM2007', 'nrnivmodl random'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.launch("random", "ran3par.hoc")'],
            'cleanup': ['cd ../', 'rm -fr HinesCarnevaleJNM2007']
        },
    '93325':
        {
            'compile': ['cd nfrost', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr nfrost']
        },
    '3682':
        {
            'compile': ['cd synmap', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr synmap']
        },
    '3812':
        {
            'compile': ['cd anderson', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr anderson']
        },
    '144482':
        {
            'variant': 'Run',
            'compile': ['cd Pyramidal_STDP_Gomez_Delgado_2010', 'nrnivmodl mechanism/mechanism_cell1/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Pyramidal_STDP_Gomez_Delgado_2010']
        },
    '3289':
        {
            'compile': ['cd db', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr db']
        },
    '149100':
        {
            'compile': ['cd HayEtAl2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr HayEtAl2013']
        },
    '143100':
        {
            'compile': ['cd GPeNeuronKitano', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr GPeNeuronKitano']
        },
    '87454':
        {
            'compile': ['cd BahmerLangner2007/NEURON_Chopper_Network_Simulation', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runhere()'],
            'cleanup': ['cd ../../', 'rm -fr BahmerLangner2007']
        },
    '43039_1':
        {
            'variant': 'control - no GJ (fig.6A)',
            'compile': ['cd gap-modeldb', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runc()'],
            'cleanup': ['cd ../', 'rm -fr gap-modeldb']
        },
    '43039_2':
        {
            'variant': 'with GJ (fig.6B)',
            'compile': ['cd gap-modeldb', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.rung()'],
            'cleanup': ['cd ../', 'rm -fr gap-modeldb']
        },
    '43039_3':
        {
            'variant': 'with GJ & Na+ block (fig.6C)',
            'compile': ['cd gap-modeldb', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.rungb()'],
            'cleanup': ['cd ../', 'rm -fr gap-modeldb']
        },
    '146030':
        {
            'compile': ['cd oconnoretal2012', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr oconnoretal2012']
        },
    '97263':
        {
            'compile': ['cd MT-GC', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr MT-GC']
        },
    '50210_1':
        {
            'variant': 'control',
            'compile': ['cd saghatelyan', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.control()'],
            'cleanup': ['cd ../', 'rm -fr saghatelyan']
        },
    '50210_2':
        {
            'variant': 'short dend',
            'compile': ['cd saghatelyan', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.rundend()'],
            'cleanup': ['cd ../', 'rm -fr saghatelyan']
        },
    '50210_3':
        {
            'variant': 'Na shift',
            'compile': ['cd saghatelyan', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runshift()'],
            'cleanup': ['cd ../', 'rm -fr saghatelyan']
        },
    '127995':
        {
            'compile': ['cd migliore2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr migliore2010']
        },
    '3665':
        {
            'compile': ['cd h_pg', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr h_pg']
        },
    '3648':
        {
            'compile': ['cd ka_kdr_mt', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ka_kdr_mt']
        },
    '3342':
        {
            'compile': ['cd mitral_1999', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr mitral_1999']
        },
    '2487_1':
        {
            'variant': 'Stimulate soma with 0.2 uA/cm2',
            'compile': ['cd mit4', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig6(0)'],
            'cleanup': ['cd ../', 'rm -fr mit4']
        },
    '2487_2':
        {
            'variant': 'Stimulate soma with 1.6 uA/cm2',
            'compile': ['cd mit4', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig6(1)'],
            'cleanup': ['cd ../', 'rm -fr mit4']
        },
    '2487_3':
        {
            'variant': 'Stimulate glomerulus with 0.2 uA/cm2',
            'compile': ['cd mit4', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig6(2)'],
            'cleanup': ['cd ../', 'rm -fr mit4']
        },
    '2487_4':
        {
            'variant': 'Stimulate glomerulus with 1.6 uA/cm2',
            'compile': ['cd mit4', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_fig6(3)'],
            'cleanup': ['cd ../', 'rm -fr mit4']
        },
    '2733':
        {
            'compile': ['cd bbmit', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr bbmit']
        },
    '149415':
        {
            'compile': ['cd MiglioreMcTavish2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ../', 'rm -fr MiglioreMcTavish2013']
        },
    '102288_1':
        {
            'variant': 'Create Fig 9 A1',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9A1()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '102288_2':
        {
            'variant': 'Create Fig 9 B1',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9B1()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '102288_3':
        {
            'variant': 'Create Fig 9 C1',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9C1()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '102288_4':
        {
            'variant': 'Create Fig 9 A2',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9A2()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '102288_5':
        {
            'variant': 'Create Fig 9 B2',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9B2()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '102288_6':
        {
            'variant': 'Create Fig 9 C2',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9C2()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '102288_7':
        {
            'variant': 'Create Fig 9 A3',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9A3()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '102288_8':
        {
            'variant': 'Create Fig 9 B3',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9B3()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '102288_9':
        {
            'variant': 'Create Fig 9 C3',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9C3()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '102288_10':
        {
            'variant': 'Create all of Fig 9',
            'compile': ['cd RichyandStarfish', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig9()'],
            'cleanup': ['cd ../', 'rm -fr RichyandStarfish']
        },
    '146565':
        {
            'compile': ['cd LavzinEtAl2012', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr LavzinEtAl2012']
        },
    '112359_1':
        {
            'variant': 'Control',
            'compile': ['cd modeldb-etoh', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.control()'],
            'cleanup': ['cd ../', 'rm -fr modeldb-etoh']
        },
    '112359_2':
        {
            'variant': '50mM',
            'compile': ['cd modeldb-etoh', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.etohh()'],
            'cleanup': ['cd ../', 'rm -fr modeldb-etoh']
        },
    '112359_3':
        {
            'variant': '100mM',
            'compile': ['cd modeldb-etoh', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.etoh()'],
            'cleanup': ['cd ../', 'rm -fr modeldb-etoh']
        },
    '145672_1':
        {
            'variant': 'Figure11C CSI',
            'compile': ['cd Fineberg_et_al_2012', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Figure11C CSI.hoc")', 'h.runu()'],
            'cleanup': ['cd ../', 'rm -fr Fineberg_et_al_2012']
        },
    '145672_2':
        {
            'variant': 'Figure11D',
            'compile': ['cd Fineberg_et_al_2012', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Fineberg_et_al_2012']
        },
    '145672_3':
        {
            'variant': 'Figure11E',
            'compile': ['cd Fineberg_et_al_2012', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Fineberg_et_al_2012']
        },
    '145672_4':
        {
            'variant': 'Figure11C CSI+OSI',
            'compile': ['cd Fineberg_et_al_2012', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Figure11C CSIOSI.hoc")', 'h.runu()'],
            'cleanup': ['cd ../', 'rm -fr Fineberg_et_al_2012']
        },
    '148644':
        {
            'compile': ['cd ParekhAscoli2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ../', 'rm -fr ParekhAscoli2013']
        },
    '83319_1':
        {
            'variant': 'CobaHH',
            'compile': ['cd destexhe_benchmarks/NEURON', 'nrnivmodl coba cuba cubadv'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.mosinvl = 10', 'h.launch("cobahh", h.intrin)'],
            'cleanup': ['cd ../../', 'rm -fr destexhe_benchmarks']
        },
    '83319_2':
        {
            'variant': 'Coba',
            'compile': ['cd destexhe_benchmarks/NEURON', 'nrnivmodl coba cuba cubadv'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.mosinvl = 10', 'h.launch("coba", h.intrin)'],
            'cleanup': ['cd ../../', 'rm -fr destexhe_benchmarks']
        },
#    '83319_3':
#        {
#            'variant': 'Cuba',
#            'compile': ['cd destexhe_benchmarks/NEURON', 'nrnivmodl coba cuba cubadv'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.launch("cuba", h.intrin)'],
#            'cleanup': ['cd ../../', 'rm -fr destexhe_benchmarks']
#        },
#    '83319_4':
#        {
#            'variant': 'CubaDV',
#            'compile': ['cd destexhe_benchmarks/NEURON', 'nrnivmodl coba cuba cubadv'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.launch("cubadv", h.intrin)'],
#            'cleanup': ['cd ../../', 'rm -fr destexhe_benchmarks']
#        },
    '10360':
        {
            'variant': 'Init & Run',
            'compile': ['cd lindgren89', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr lindgren89']
        },
    '82849':
        {
            'compile': ['cd pcell', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("fig2A.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr pcell']
        },
    '3660':
        {
            'compile': ['cd ka_kdr_neoLI', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ka_kdr_neoLI']
        },
    '114394':
        {
            'compile': ['cd NN_kole', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NN_kole']
        },
    '7988_1':
        {
            'variant': 'NR2A',
            'compile': ['cd murphy01', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.nrn2a_model()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr murphy01']
        },
    '7988_2':
        {
            'variant': 'NR2B',
            'compile': ['cd murphy01', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.nrn2b_model()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr murphy01']
        },
    '126640':
        {
            'compile': ['cd withdrawal', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr withdrawal']
        },
    '116835':
        {
            'compile': ['cd GrC', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr GrC']
        },
    '7659_1':
        {
            'variant': 'S1 and S2 prox (black)',
            'compile': ['cd window', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runp()'],
            'cleanup': ['cd ../', 'rm -fr window']
        },
    '7659_2':
        {
            'variant': 'S1 prox, S2 dist (red)',
            'compile': ['cd window', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ../', 'rm -fr window']
        },
    '7659_3':
        {
            'variant': 'S1 and S2 dist (blue)',
            'compile': ['cd window', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.rund()'],
            'cleanup': ['cd ../', 'rm -fr window']
        },
    '7659_4':
        {
            'variant': 'S1 prox, S2 dist, + Ih (green)',
            'compile': ['cd window', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.rundh()'],
            'cleanup': ['cd ../', 'rm -fr window']
        },

#    '144589':
#        {
#            'compile': ['cd BerzThetaGamm2013', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file(1,"netwOPb.hoc")', 'h.xfield()', 'h.run()'],
#            'cleanup': ['cd ../', 'rm -fr BerzThetaGamm2013']
#        },
    '85112':
        {
            'compile': ['cd baker05', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("fig8.hoc")'],
            'cleanup': ['cd ../', 'rm -fr baker05']
        },
    '119266':
        {
            'compile': ['cd CA1_Aged', 'nrnivmodl mechanism'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CA1_Aged']
        },
    '136310':
        {
            'variant': '=> 1. Calculate impedances',
            'compile': ['cd LFP', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.calc_filter()', 'h.draw_filter()', 'h.runfft()', 'h.draw_fft()', 'h.calc_extracellular()', 'h.draw_extracellular()'],
            'cleanup': ['cd ../', 'rm -fr LFP']
        },
    '122329_1':
        {
            'variant': 'with SK soma',
            'compile': ['cd GPSingleCompartment', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("withSKsoma.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr GPSingleCompartment']
        },
    '122329_2':
        {
            'variant': 'no SK soma',
            'compile': ['cd GPSingleCompartment', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("noSKsoma.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr GPSingleCompartment']
        },
    '6763':
        {
            'variant': 'Init & Run',
            'compile': ['cd canavier1999', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr canavier1999']
        },
    '120798_1':
        {
            'variant': 'Fig. 5B',
            'compile': ['cd PalmerStuart2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5b()'],
            'cleanup': ['cd ../', 'rm -fr PalmerStuart2009']
        },
    '120798_2':
        {
            'variant': 'Fig. 5',
            'compile': ['cd PalmerStuart2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5cd()'],
            'cleanup': ['cd ../', 'rm -fr PalmerStuart2009']
        },
    '120798_3':
        {
            'variant': 'Suppl. Fig. 2 c',
            'compile': ['cd PalmerStuart2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.suppl_fig2c()'],
            'cleanup': ['cd ../', 'rm -fr PalmerStuart2009']
        },
   '138321':
        {
            'compile': ['cd pashut2011', 'nrnivmodl OneDimension/Neuron'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr pashut2011']
        },
    '20756_1':
        {
            'variant': 'Figure 2 ( left )',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 21 )', 'h.setFig2()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_2':
        {
            'variant': 'Figure 2 ( right )',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 22 )', 'h.setFig2()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_3':
        {
            'variant': 'Figure 4 Injection 2.5 nA',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 41 )', 'h.setFig4()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_4':
        {
            'variant': 'Figure 4 Injection 1.5 nA',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 42 )', 'h.setFig4()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_5':
        {
            'variant': 'Figure 4 Injection 1.1 nA',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 43 )', 'h.setFig4()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_6':
        {
            'variant': 'Figure 4 Injection 0.6 nA',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 44 )', 'h.setFig4()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_7':
        {
            'variant': 'Figure 5 B1',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 51 )', 'h.setFig5()',  'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_8':
        {
            'variant': 'Figure 5 B2',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 52 )', 'h.setFig5()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_9':
        {
            'variant': 'Figure 6 B1',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 61 )', 'h.setFig6()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_10':
        {
            'variant': 'Figure 6 B2',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 62 )', 'h.setFig6()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_11':
        {
            'variant': 'Figure 7 g_NaP x 0.0',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 71 )', 'h.setFig7()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_12':
        {
            'variant': 'Figure 7 g_NaP x 0.7',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 72 )', 'h.setFig7()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '20756_13':
        {
            'variant': 'Figure 7 g_NaP x 1.0',
            'compile': ['cd Traub2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.pyr3_ = h.pyr3( 73 )', 'h.setFig7()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Traub2003']
        },
    '128559':
        {
            'compile': ['cd WDR-Model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr WDR-Model']
        },
    '93398_1':
        {
            'variant': 'Original GA settings',
            'compile': ['cd StiefelSejnowskiCode', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("GA")'],
            'cleanup': ['cd ../', 'rm -fr StiefelSejnowskiCode']
        },
    '93398_2':
        {
            'variant': 'Short run test',
            'compile': ['cd StiefelSejnowskiCode', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("shortRun")'],
            'cleanup': ['cd ../', 'rm -fr StiefelSejnowskiCode']
        },
    '97863':
        {
            'compile': ['cd beelerReuter', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr beelerReuter']
        },
    '3454_1':
        {
            'variant': '100 hz',
            'compile': ['cd kv31model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.NetStim[0].interval=10', 'h.run(10)'],
            'cleanup': ['cd ../', 'rm -fr kv31model']
        },
    '3454_2':
        {
            'variant': '200 hz',
            'compile': ['cd kv31model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.NetStim[0].interval=5', 'h.run(5)'],
            'cleanup': ['cd ../', 'rm -fr kv31model']
        },
    '3454_3':
        {
            'variant': '300 hz',
            'compile': ['cd kv31model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.NetStim[0].interval=3.3', 'h.run(3.3)'],
            'cleanup': ['cd ../', 'rm -fr kv31model']
        },
    '3454_4':
        {
            'variant': '400 hz',
            'compile': ['cd kv31model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.NetStim[0].interval=2.5', 'h.run(2.5)'],
            'cleanup': ['cd ../', 'rm -fr kv31model']
        },
    '113732_1':
        {
            'variant': 'Wiring configuration for the supra-threshold evoked response',
            'compile': ['cd SS-cortex', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.suprathresh()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr SS-cortex']
        },
    '113732_2':
        {
            'variant': 'Wiring configuration for the non-perceived evoked response',
            'compile': ['cd SS-cortex', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.nonperceived()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr SS-cortex']
        },
    '113732_3':
        {
            'variant': 'Wiring configuration for the perceived evoked response',
            'compile': ['cd SS-cortex', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.perceived()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr SS-cortex']
        },
    '150239':
        {
            'compile': ['cd grid', 'nrnivmodl nrn/mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr grid']
        },
    '279_1':
        {
            'variant': 'Burst behavior in single-compartment model',
            'compile': ['cd dendtc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("tc1_cc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendtc']
        },
    '279_2':
        {
            'variant': 'Burst behavior in 3-compartment model',
            'compile': ['cd dendtc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("tc3_cc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendtc']
        },
    '279_3':
        {
            'variant': 'Burst behavior in detailed cell model',
            'compile': ['cd dendtc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("tc200_cc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendtc']
        },
    '279_4':
        {
            'variant': 'Voltage-clamp in detailed cell model',
            'compile': ['cd dendtc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("tc200_vc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendtc']
        },
    '279_5':
        {
            'variant': 'Voltage-clamp in dissociated cell model',
            'compile': ['cd dendtc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("tcD_vc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr dendtc']
        },
    '3807':
        {
            'compile': ['cd baccus98', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig6()'],
            'cleanup': ['cd ../', 'rm -fr baccus98']
        },
    '64261':
        {
            'compile': ['cd bfstdp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr bfstdp']
        },
    '144089':
        {
            'compile': ['cd PFCcell', 'nrnivmodl mechanism'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_sim()'],
            'cleanup': ['cd ../', 'rm -fr PFCcell']
        },
    '139653_1':
        {
            'variant': 'Fig 4A. (BAC_firing.hoc)',
            'compile': ['cd L5bPCmodelsEH', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("BAC_firing")'],
            'cleanup': ['cd ../', 'rm -fr L5bPCmodelsEH']
        },
    '139653_2':
        {
            'variant': 'Fig 4B. Upper trace. (Step_current_firing.hoc)',
            'compile': ['cd L5bPCmodelsEH', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Step_current_firing")'],
            'cleanup': ['cd ../', 'rm -fr L5bPCmodelsEH']
        },
    '139653_3':
        {
            'variant': 'Fig 5A. (critical_frequency.hoc)',
            'compile': ['cd L5bPCmodelsEH', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("critical_frequency")'],
            'cleanup': ['cd ../', 'rm -fr L5bPCmodelsEH']
        },
    '150538':
        {
            'compile': ['cd XiEtal2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.circ_run()'],
            'cleanup': ['cd ../', 'rm -fr XiEtal2013']
        },
    '50207':
        {
            'compile': ['cd NMDA_Mg', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NMDA_Mg']
        },
    '106891':
        {
            'compile': ['cd b07dec27_20091025', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runeg()'],
            'cleanup': ['cd ../', 'rm -fr b07dec27_20091025']
        },
    '82784':
        {
            'compile': ['cd DynBasIrregSpNMDA', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("runThis.hoc")'],
            'cleanup': ['cd ../', 'rm -fr DynBasIrregSpNMDA']
        },
    '151825':
        {
            'compile': ['cd Demo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Demo']
        },
    '97756':
        {
            'compile': ['cd Ga_demo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("ga_run.hoc")'],
            'cleanup': ['cd ../', 'rm -fr Ga_demo']
        },
    '135787_1':
        {
            'variant': 'spike initialization',
            'compile': ['cd ShuEtAl20062007', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("best_full_axon_spike_init.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ShuEtAl20062007']
        },
    '135787_2':
        {
            'variant': 'axon potential decay',
            'compile': ['cd ShuEtAl20062007', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("best_full_axon_decay.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ShuEtAl20062007']
        },
    '83590':
        {
            'compile': ['cd Arsiero_et_al2007', 'nrnivmodl mechanisms'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr Arsiero_et_al2007']
        },
    '139150':
        {
            'compile': ['cd Poleg-PolskyDiamond2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.visrun()'],
            'cleanup': ['cd ../', 'rm -fr Poleg-PolskyDiamond2011']
        },
    '94321':
        {
            'compile': ['cd chain_1d', 'nrnivmodl mechanisms'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.execute_simulation()'],
            'cleanup': ['cd ../', 'rm -fr chain_1d']
        },
    '147867_1':
        {
            'variant': '0% Atrophy',
            'compile': ['cd CA3Atrophy', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.proc_load(1)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CA3Atrophy']
        },
    '147867_2':
        {
            'variant': '25% Atrophy',
            'compile': ['cd CA3Atrophy', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.proc_load(2)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CA3Atrophy']
        },
    '147867_3':
        {
            'variant': '35% Atrophy',
            'compile': ['cd CA3Atrophy', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.proc_load(3)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CA3Atrophy']
        },
    '147867_4':
        {
            'variant': '75% Atrophy',
            'compile': ['cd CA3Atrophy', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.proc_load(4)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CA3Atrophy']
        },
    '82364_1':
        {
            'variant': 'regular - 20 Hz',
            'compile': ['cd Welie-Wadman-JPhysiol-subiculum', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.reg_20()'],
            'cleanup': ['cd ../', 'rm -fr Welie-Wadman-JPhysiol-subiculum']
        },
    '82364_2':
        {
            'variant': 'regular - 50 Hz',
            'compile': ['cd Welie-Wadman-JPhysiol-subiculum', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.reg_50()'],
            'cleanup': ['cd ../', 'rm -fr Welie-Wadman-JPhysiol-subiculum']
        },
    '82364_3':
        {
            'variant': 'burster - 20 Hz',
            'compile': ['cd Welie-Wadman-JPhysiol-subiculum', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.burst_20()'],
            'cleanup': ['cd ../', 'rm -fr Welie-Wadman-JPhysiol-subiculum']
        },
    '82364_4':
        {
            'variant': 'burster - 50 Hz',
            'compile': ['cd Welie-Wadman-JPhysiol-subiculum', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.burst_50()'],
            'cleanup': ['cd ../', 'rm -fr Welie-Wadman-JPhysiol-subiculum']
        },
    '2798_1':
        {
            'variant': 'before training',
            'compile': ['cd HB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_u()'],
            'cleanup': ['cd ../', 'rm -fr HB']
        },
    '2798_2':
        {
            'variant': 'after training',
            'compile': ['cd HB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_c()'],
            'cleanup': ['cd ../', 'rm -fr HB']
        },
    '2798_3':
        {
            'variant': 'random activation',
            'compile': ['cd HB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_r()'],
            'cleanup': ['cd ../', 'rm -fr HB']
        },
    '114735':
        {
            'compile': ['cd HFO', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr HFO']
        },
    '115357_1':
        {
            'variant': '++',
            'compile': ['cd GeneralizedCarnevaleHinesScheme', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.makeplusplus()'],
            'cleanup': ['cd ../', 'rm -fr GeneralizedCarnevaleHinesScheme']
        },
    '115357_2':
        {
            'variant': '+-',
            'compile': ['cd GeneralizedCarnevaleHinesScheme', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.makeplusminus()'],
            'cleanup': ['cd ../', 'rm -fr GeneralizedCarnevaleHinesScheme']
        },
    '115357_3':
        {
            'variant': '-+',
            'compile': ['cd GeneralizedCarnevaleHinesScheme', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.makeminusplus()'],
            'cleanup': ['cd ../', 'rm -fr GeneralizedCarnevaleHinesScheme']
        },
    '115357_4':
        {
            'variant': '--',
            'compile': ['cd GeneralizedCarnevaleHinesScheme', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.makeminusminus()'],
            'cleanup': ['cd ../', 'rm -fr GeneralizedCarnevaleHinesScheme']
        },
    '26997_1':
        {
            'variant': 'Fig 1A',
            'compile': ['cd wang1996', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig1a()'],
            'cleanup': ['cd ../', 'rm -fr wang1996']
        },
    '26997_2':
        {
            'variant': 'Fig 3A',
            'compile': ['cd wang1996', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3a()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr wang1996']
        },
    '21329':
        {
            'compile': ['cd inhibnet', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr inhibnet']
        },
    '114685_1':
        {
            'variant': 'Short test run of the GPi neuron similar to Fig 1A',
            'compile': ['cd JohnsonMcIntyre2008', 'nrnivmodl GPi_model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.short_run()'],
            'cleanup': ['cd ../', 'rm -fr JohnsonMcIntyre2008']
        },
    '114685_2':
        {
            'variant': 'Sample run for the current injections that created Fig 2C',
            'compile': ['cd JohnsonMcIntyre2008', 'nrnivmodl GPi_model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig2c_point()'],
            'cleanup': ['cd ../', 'rm -fr JohnsonMcIntyre2008']
        },
    '146509':
        {
            'compile': ['cd Branch_Point_Tapering', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_simulation()'],
            'cleanup': ['cd ../', 'rm -fr Branch_Point_Tapering']
        },
    '139654_1':
        {
            'variant': 'Phasic model T8 step',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("stim_type = 1")', 'h("amp = 1")', 'h("cell_type = 1")', 'h("cell_nr = 8")',  'h.restart()', 'h.load_file(1, "control.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_2':
        {
            'variant': 'Phasic model T8 ZAP',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("stim_type = 2")', 'h("amp = 1")', 'h("cell_type = 1")', 'h("cell_nr = 8")',  'h.restart()', 'h.load_file(1, "control.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_3':
        {
            'variant': 'Tonic model T1 step',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("stim_type = 1")', 'h("amp = 0.6")', 'h("cell_type = 2")', 'h("cell_nr = 1")',  'h.restart()', 'h.load_file(1, "control.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_4':
        {
            'variant': 'Tonic model T1 ZAP',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("stim_type = 2")', 'h("amp = 0.5")', 'h("cell_type = 2")', 'h("cell_nr = 1")',  'h.restart()', 'h.load_file(1, "control.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_5':
        {
            'variant': 'Synaptic train stimulation, with inhibition',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("ton_inhib = 1")', 'h("cell_nr = 7")',  'h.restart()', 'h.load_file(1, "traincontrol.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_6':
        {
            'variant': 'Synaptic train stimulation, no inhibition',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("ton_inhib = 0")', 'h("cell_nr = 7")',  'h.restart()', 'h.load_file(1, "traincontrol.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '140299_1':
        {
            'variant': 'BE17BNoActive',
            'compile': ['cd KubotaEtAl2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadModel("BE17B_length_adjusted_NoActive.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KubotaEtAl2011']
        },
    '140299_2':
        {
            'variant': 'BE59DNoActive',
            'compile': ['cd KubotaEtAl2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadModel("BE59D_length_adjusted_NoActive.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KubotaEtAl2011']
        },
    '140299_3':
        {
            'variant': 'BE77CNoActive',
            'compile': ['cd KubotaEtAl2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadModel("BE77C_length_adjusted_NoActive.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KubotaEtAl2011']
        },
    '140299_4':
        {
            'variant': 'LV38ENoActive',
            'compile': ['cd KubotaEtAl2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadModel("LV38E_length_adjusted_NoActive.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KubotaEtAl2011']
        },
    '116956':
        {
            'compile': ['cd vs4_modelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig10e()'],
            'cleanup': ['cd ../', 'rm -fr vs4_modelDB']
        },
    '8115':
        {
            'compile': ['cd fluct', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr fluct']
        },
    '113435':
        {
            'compile': ['cd fs_internrn_neuron', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr fs_internrn_neuron']
        },
    '8284_1':
        {
            'variant': 'HT',
            'compile': ['cd ihmodel', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.HT()'],
            'cleanup': ['cd ../', 'rm -fr ihmodel']
        },
    '8284_2':
        {
            'variant': 'Control',
            'compile': ['cd ihmodel', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Control()'],
            'cleanup': ['cd ../', 'rm -fr ihmodel']
        },
    '19022':
        {
            'compile': ['cd geigerEtAl1997', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("fig8d.hoc")'],
            'cleanup': ['cd ../', 'rm -fr geigerEtAl1997']
        },
    '3167':
        {
            'compile': ['cd timing', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runu()'],
            'cleanup': ['cd ../', 'rm -fr timing']
        },
    '3676_1':
        {
            'variant': 'Fig 2',
            'compile': ['cd ephaptic', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("fig2.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ephaptic']
        },
    '3676_2':
        {
            'variant': 'Fig 3B',
            'compile': ['cd ephaptic', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("fig3.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ephaptic']
        },
    '123815':
        {
            'compile': ['cd Hipp_paper_code', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Hipp_paper_code']
        },
    '120910':
        {
            'compile': ['cd ElectricallycoupledRetziusneurons', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ElectricallycoupledRetziusneurons']
        },
    '116981_1':
        {
            'variant': 'Fig. 5--exc central vs. peripheral tree',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '116981_2':
        {
            'variant': 'Fig. 5 inset--brief excitation',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5inset()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '116981_3':
        {
            'variant': 'Fig. 6--effect of location of excitatory input',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig6()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '116981_4':
        {
            'variant': 'Fig. 7--effect of activation sequence',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig7()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '116981_5':
        {
            'variant': 'Fig. 8--effect of inh location',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig8()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '151126':
        {
            'compile': ['cd BianchiEtAl2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr BianchiEtAl2013']
        },
    '121060':
        {
            'compile': ['cd MSN2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Exec()'],
            'cleanup': ['cd ../', 'rm -fr MSN2009']
        },
    '148253':
        {
            'compile': ['cd Chloride_Model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Chloride_Model']
        },
    '123453':
        {
            'compile': ['cd AkemannEtAl2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run_model( prot )")'],
            'cleanup': ['cd ../', 'rm -fr AkemannEtAl2009']
        },
    '64296_1':
        {
            'variant': 'Figure 2A Top Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Atop()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_2':
        {
            'variant': 'Figure 2A Middle Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Amiddle()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_3':
        {
            'variant': 'Figure 2A Bottom Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Abottom()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_4':
        {
            'variant': 'Figure 2B Top Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Btop()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_5':
        {
            'variant': 'Figure 2B Second Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Bsecond()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_6':
        {
            'variant': 'Figure 2B Third Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Bthird()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_7':
        {
            'variant': 'Figure 2B Bottom Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Bbottom()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_8':
        {
            'variant': 'Figure 3A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig3A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_9':
        {
            'variant': 'Figure 3B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig3B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_10':
        {
            'variant': 'Figure 3C Top',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig3Ctop()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_11':
        {
            'variant': 'Figure 3C Bottom',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig3Cbottom()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_12':
        {
            'variant': 'Figure 4A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig4A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_13':
        {
            'variant': 'Figure 5B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig5B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_14':
        {
            'variant': 'Figure 6A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_15':
        {
            'variant': 'Figure 6B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_16':
        {
            'variant': 'Figure 6C',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6C()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_17':
        {
            'variant': 'Figure 6D',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6D()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_18':
        {
            'variant': 'Figure 6E',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6E()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_19':
        {
            'variant': 'Figure 7A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig7A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_20':
        {
            'variant': 'Figure 7B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig7B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_21':
        {
            'variant': 'Figure 8A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig8A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_22':
        {
            'variant': 'Figure 8B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig8B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_23':
        {
            'variant': 'Figure 8C',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig8C()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '118662_1':
        {
            'variant': 'Figure 4a cell 1',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4a_cell1\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_2':
        {
            'variant': 'Figure 4a cell 2',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4a_cell2\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_3':
        {
            'variant': 'Figure 4a cell 3',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4a_cell3\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_4':
        {
            'variant': 'Figure 4b dendrite 1',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4b_dendrite1\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_5':
        {
            'variant': 'Figure 4b dendrite 2',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4b_dendrite2\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_6':
        {
            'variant': 'Figure 4b dendrite 3',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4b_dendrite3\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '51022':
        {
            'compile': ['cd amirdevor03', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr amirdevor03']
        },
    '140789':
        {
            'compile': ['cd DG_BC/Figure_2', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr DG_BC']
        },
    '116740_1':
        {
            'variant': 'T-Ca',
            'compile': ['cd aradi1999', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("control()")'],
            'cleanup': ['cd ../', 'rm -fr aradi1999']
        },
    '116740_2':
        {
            'variant': 'T-Ca and BK',
            'compile': ['cd aradi1999', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("bk()")'],
            'cleanup': ['cd ../', 'rm -fr aradi1999']
        },
    '116740_3':
        {
            'variant': 'T-Ca and SK',
            'compile': ['cd aradi1999', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("sk()")'],
            'cleanup': ['cd ../', 'rm -fr aradi1999']
        },
    '124291':
        {
            'compile': ['cd FFI/MOPP_Fig_1B_left', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runa()")'],
            'cleanup': ['cd ../../', 'rm -fr FFI']
        },
    '3801_1':
        {
            'variant': 'All three synaptic terminals are active',
            'compile': ['cd dgbc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doit(3)")'],
            'cleanup': ['cd ../', 'rm -fr dgbc']
        },
    '3801_2':
        {
            'variant': 'synapse 0 only',
            'compile': ['cd dgbc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doit(0)")'],
            'cleanup': ['cd ../', 'rm -fr dgbc']
        },
    '3801_3':
        {
            'variant': 'synapse 1 only',
            'compile': ['cd dgbc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doit(1)")'],
            'cleanup': ['cd ../', 'rm -fr dgbc']
        },
    '3801_4':
        {
            'variant': 'synapse 2 only',
            'compile': ['cd dgbc', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doit(2)")'],
            'cleanup': ['cd ../', 'rm -fr dgbc']
        },
    '144385':
        {
            'compile': ['cd ShepherdBrayton1979', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr ShepherdBrayton1979']
        },
    '18738':
        {
            'compile': ['cd dendgeom', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr dendgeom']
        },
    '147218':
        {
            'compile': ['cd genet_PC', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr genet_PC']
        },
    '124394':
        {
            'compile': ['cd nevian', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr nevian']
        },
    '140828':
        {
            'compile': ['cd Branco_2010', 'nrnivmodl mod.files'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr Branco_2010']
        },
    '151949':
        {
            'compile': ['cd SousaEtAl2014', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr SousaEtAl2014']
        },
   '3344':
        {
            'compile': ['cd ka_dg', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr ka_dg']
        },
    '98005':
        {
            'compile': ['cd D2modulation', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr D2modulation']
        },
    '9853':
        {
            'compile': ['cd joyner80', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr joyner80']
        },
    '52034':
        {
            'compile': ['cd ctxnet', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run_fig6()")'],
            'cleanup': ['cd ../', 'rm -fr ctxnet']
        },
    '138382_1':
        {
            'variant': 'Detailed Calcium dynamics model',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runDM\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_2':
        {
            'variant': 'Calcium transients using different buffering models',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaTransients\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_3':
        {
            'variant': 'Calcium spikes using single pool model',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaSpikesSP\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_4':
        {
            'variant': 'Calcium spikes using double pool model',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaSpikesDP\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_5':
        {
            'variant': 'Calcium spikes using detailed model',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaSpikesDM\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_6':
        {
            'variant': 'Calcium spikes using DCM',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaSpikesDCM\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '114637':
        {
            'compile': ['cd SSC_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr SSC_model']
        },
    '9851':
        {
            'compile': ['cd moore78', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr moore78']
        },
    '19366_1':
        {
            'variant': 'Fig.1. A-C',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(1)")'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '19366_2':
        {
            'variant': 'Fig.2. A',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(2)")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '19366_3':
        {
            'variant': 'Fig.2. B',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(3)")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '19366_4':
        {
            'variant': 'Fig.3. A-D',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(4)")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '19366_5':
        {
            'variant': 'Fig.3. E-H',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(5)")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '119283_1':
        {
            'variant': '(1-4) Gray - Control',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runi()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '119283_2':
        {
            'variant': '(1) Black - Lamotrigine',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runii()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '119283_3':
        {
            'variant': '(2) Black - Diazepam',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiii()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '119283_4':
        {
            'variant': '(3) Black - Flindokalner',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiv()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '119283_5':
        {
            'variant': '(4) Black - Lamotrigine+Flindokalner',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runv()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '123927':
        {
            'compile': ['cd Wimmer-et-al2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run_sim_graph_coarse()")'],
            'cleanup': ['cd ../', 'rm -fr Wimmer-et-al2009']
        },
    '143604_1':
        {
            'variant': 'spine inhibiton with bAP (compartmentalized inhibition)',
            'compile': ['cd singleDendrite', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("spineinhib_bAP_demo()")'],
            'cleanup': ['cd ../', 'rm -fr singleDendrite']
        },
    '143604_2':
        {
            'variant': '10x dend inhib with bAP (widespread inhib with smaller change in amplitude)',
            'compile': ['cd singleDendrite', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("dend10x_bAP_demo()")'],
            'cleanup': ['cd ../', 'rm -fr singleDendrite']
        },
    '93326':
        {
            'compile': ['cd ngetting', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ngetting']
        },
    '3434':
        {
            'compile': ['cd cdlab', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr cdlab']
        },
    '64212':
        {
            'compile': ['cd VNO', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr VNO']
        },
    '147578_1':
        {
            'variant': 'Compute Input Resistances Along Trunk',
            'compile': ['cd MultiChirp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("RN_Trunk()")'],
            'cleanup': ['cd ../', 'rm -fr MultiChirp']
        },
    '147578_2':
        {
            'variant': 'Save Local Chirp Responses for Locations Along Trunk',
            'compile': ['cd MultiChirp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Chirp_Trunk()")'],
            'cleanup': ['cd ../', 'rm -fr MultiChirp']
        },
    '80769_1':
        {
            'variant': 'Off On Off original protocol',
            'compile': ['cd AkemannKnopfelPurkinje_cell_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"OFF_ON_OFF_protocol\\")")'],
            'cleanup': ['cd ../', 'rm -fr AkemannKnopfelPurkinje_cell_model']
        },
    '80769_2':
        {
            'variant': 'Short demo run simulation',
            'compile': ['cd AkemannKnopfelPurkinje_cell_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"shortRun\\")")'],
            'cleanup': ['cd ../', 'rm -fr AkemannKnopfelPurkinje_cell_model']
        },
    '17664':
        {
            'compile': ['cd prknj', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr prknj']
        },
    '48332':
        {
            'compile': ['cd purkinje', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr purkinje']
        },
    '112685':
        {
            'compile': ['cd Golgi_cell', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Golgi_cell']
        },
    '126467':
        {
            'compile': ['cd NegroniLascano', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr NegroniLascano']
        },
    '144520':
        {
            'compile': ['cd DiFrancescoNoble1985', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr DiFrancescoNoble1985']
        },
    '3800':
        {
            'compile': ['cd cardiac1998', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr cardiac1998']
        },
    '125745':
        {
            'compile': ['cd fink2000', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr fink2000']
        },
    '150551_1':
        {
            'variant': 'Figure 4F-G',
            'compile': ['cd AshhadNarayanan2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("{ load_file(\\"Fig4F-G.hoc\\") }")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr AshhadNarayanan2013']
        },
    '150551_2':
        {
            'variant': 'Figure 6C-F',
            'compile': ['cd AshhadNarayanan2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("{ load_file(\\"Fig6C-F.hoc\\") }")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr AshhadNarayanan2013']
        },
    '108458':
        {
            'compile': ['cd KampaStuart2006', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr KampaStuart2006']
        },
    '151458':
        {
            'compile': ['cd Nakano_FICN_model', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr Nakano_FICN_model']
        },
    '140462':
        {
            'compile': ['cd MasurkarChen2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig7c()'],
            'cleanup': ['cd ../', 'rm -fr MasurkarChen2011']
        },
    '118098':
        {
            'compile': ['cd ca3-summ', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runl()")'],
            'cleanup': ['cd ../', 'rm -fr ca3-summ']
        },
    '76879_1':
        {
            'variant': 'No drive (slow)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(1)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_2':
        {
            'variant': 'Driven (slow)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(2)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_3':
        {
            'variant': 'As set (slow)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(3)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_4':
        {
            'variant': 'No drive (fast)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(4)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_5':
        {
            'variant': 'Driven (fast)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(5)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_6':
        {
            'variant': 'As set (fast)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(6)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '3509_1':
        {
            'variant': 'rate',
            'compile': ['cd kca', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("prate()")'],
            'cleanup': ['cd ../', 'rm -fr kca']
        },
    '3509_2':
        {
            'variant': 'steady state current',
            'compile': ['cd kca', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("pcur2()")'],
            'cleanup': ['cd ../', 'rm -fr kca']
        },
    '3509_3':
        {
            'variant': 'voltage clamp',
            'compile': ['cd kca', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("pvc()")'],
            'cleanup': ['cd ../', 'rm -fr kca']
        },
    '3332':
        {
            'compile': ['cd h_cno', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr h_cno']
        },
    '101629_1':
        {
            'variant': 'Fig.9B',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig9b()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '101629_2':
        {
            'variant': 'Fig.9C',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig9c()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '101629_3':
        {
            'variant': 'Fig.9D',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig9d()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '101629_4':
        {
            'variant': 'Fig.9E',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig9e()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '126814':
        {
            'compile': ['cd develop', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr develop']
        },
    '20007':
        {
            'compile': ['cd ca3_2002', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ca3_2002']
        },
    '3263_1':
        {
            'variant': 'burst',
            'compile': ['cd ca3_db', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runb()")'],
            'cleanup': ['cd ../', 'rm -fr ca3_db']
        },
    '3263_2':
        {
            'variant': 'no-burst short',
            'compile': ['cd ca3_db', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runnbs()")'],
            'cleanup': ['cd ../', 'rm -fr ca3_db']
        },
    '3263_3':
        {
            'variant': 'no-burst long',
            'compile': ['cd ca3_db', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runnbl()")'],
            'cleanup': ['cd ../', 'rm -fr ca3_db']
        },
    '118986':
        {
            'compile': ['cd mutant', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr mutant']
        },
    '144392_1':
        {
            'variant': 'soma=0',
            'compile': ['cd modeldb', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runs()")'],
            'cleanup': ['cd ../', 'rm -fr modeldb']
        },
    '144392_2':
        {
            'variant': 'km in both',
            'compile': ['cd modeldb', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runii()")'],
            'cleanup': ['cd ../', 'rm -fr modeldb']
        },
    '144392_3':
        {
            'variant': 'axon=0',
            'compile': ['cd modeldb', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runa()")'],
            'cleanup': ['cd ../', 'rm -fr modeldb']
        },
    '144976_1':
        {
            'variant': 'control',
            'compile': ['cd alzheimer', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("control()")'],
            'cleanup': ['cd ../', 'rm -fr alzheimer']
        },
    '144976_2':
        {
            'variant': 'alzheimer',
            'compile': ['cd alzheimer', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("AD()")'],
            'cleanup': ['cd ../', 'rm -fr alzheimer']
        },
    '144976_3':
        {
            'variant': 'KA-treatment',
            'compile': ['cd alzheimer', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("AD_KA()")'],
            'cleanup': ['cd ../', 'rm -fr alzheimer']
        },
    '87535':
        {
            'compile': ['cd magical7', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ../', 'rm -fr magical7']
        },
    '55035':
        {
            'compile': ['cd obliques', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runm()")'],
            'cleanup': ['cd ../', 'rm -fr obliques']
        },
    '126776_1':
        {
            'variant': 'control',
            'compile': ['cd rebound', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runc()")'],
            'cleanup': ['cd ../', 'rm -fr rebound']
        },
    '126776_2':
        {
            'variant': '4-AP',
            'compile': ['cd rebound', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run4ap()")'],
            'cleanup': ['cd ../', 'rm -fr rebound']
        },
    '126776_3':
        {
            'variant': '4-AP+ZD',
            'compile': ['cd rebound', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run4apzd()")'],
            'cleanup': ['cd ../', 'rm -fr rebound']
        },
    '19696_1':
        {
            'variant': 'full model (black)',
            'compile': ['cd sc-pp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runf()")'],
            'cleanup': ['cd ../', 'rm -fr sc-pp']
        },
    '19696_2':
        {
            'variant': 'uniform KA (red)',
            'compile': ['cd sc-pp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runa()")'],
            'cleanup': ['cd ../', 'rm -fr sc-pp']
        },
    '19696_3':
        {
            'variant': 'uniform KA and I-h (blue)',
            'compile': ['cd sc-pp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runh()")'],
            'cleanup': ['cd ../', 'rm -fr sc-pp']
        },
    '112546_1':
        {
            'variant': 'fig.4(i)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runi()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '112546_2':
        {
            'variant': 'fig.4(ii)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runii()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '112546_3':
        {
            'variant': 'fig.4(iii)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiii()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '112546_4':
        {
            'variant': 'fig.4(iv)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiv()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '116983':
        {
            'compile': ['cd theta', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runm()")'],
            'cleanup': ['cd ../', 'rm -fr theta']
        },
    '148094':
        {
            'compile': ['cd kv72-R213QW-mutations', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr kv72-R213QW-mutations']
        },
    '9769_distal':
        {
            'variant': 'distal',
            'compile': ['cd lamotrigine', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("rund()")'],
            'cleanup': ['cd ../', 'rm -fr lamotrigine']
        },
    '9769_proximal':
        {
            'variant': 'proximal',
            'compile': ['cd lamotrigine', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runp()")'],
            'cleanup': ['cd ../', 'rm -fr lamotrigine']
        }

}

manually_curated_protocols = {
#    '168314':
#        {
#            'compile': ['cd HummosEtAl2014', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
#            'cleanup': ['cd ../', 'rm -fr HummosEtAl2014']
#        },
#    '156780':
#        {
#            'compile': ['cd models', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("microcircuit.hoc")'],
#            'cleanup': ['cd ../', 'rm -fr models']
#        },
#    '155705':
#        {
#            'compile': ['cd AvellaEtAl2014/Two_netsPaper/main', 'nrnivmodl ../mods/all_mods/'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("Control_execute_network_bgk.hoc")'],
#            'cleanup': ['cd ../', 'rm -fr AvellaEtAl2014']
#        },
#    155602 is probably fine... except it has way too many cells to deal with quickly
#    '155602_1':
#        {
#            'variant': 'Control -74',
#            'compile': ['cd YuEtAl2013', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("fixed rseed Control -74 spill_ tonic 10uS with mossy kill.hoc")', 'h.custom_init()', 'h.rrun()'],
#            'cleanup': ['cd ../', 'rm -fr YuEtAl2013']
#        },
#    '155602_2':
#        {
#            'variant': 'Pilo -54',
#            'compile': ['cd YuEtAl2013', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("fixed rseed Pilo -54 spill_ tonic 10uS with mossy kill.hoc")'],
#            'cleanup': ['cd ../', 'rm -fr YuEtAl2013']
#        },
    '152028_1':
        {
            'variant': 'Chans in All',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-in-all.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_2':
        {
            'variant': 'Chans Ext Axon 70 um',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-70um.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_3':
        {
            'variant': 'Chans Ext Axon 70 um tomasz',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-70um-tomasz.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_4':
        {
            'variant': 'Chans Ext Axon 70 um only Na',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-70um-onlyNa.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_5':
        {
            'variant': 'Chans Ext Axon 70 um mimic synapses',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-70um-mimic-synapses.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_6':
        {
            'variant': 'Chans Ext Axon 70 um mimic synapses v change',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-70um-mimic-synapses-v-change.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_7':
        {
            'variant': 'Chans Ext Axon 70 um mimic synapses sustained currents',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-70um-mimic-synapses-sustained-currents.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_8':
        {
            'variant': 'Chans Ext Axon 70 um 10x mimic sustained',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-70um-10x-mimic-sustained.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_9':
        {
            'variant': 'Chans Ext Axon 70 um 10x mimic sustained random',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-70um-10x-mimic-sustained-random.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_10':
        {
            'variant': 'Chans Ext Axon 70 um 10 alpha synapses',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-70um-10alphasynapses.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_11':
        {
            'variant': 'Chans Ext Axon 50 only Na',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-ext-axon-50um-onlyNa.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_12':
        {
            'variant': 'Chans Ext Axon botdend',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-botdend.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_13':
        {
            'variant': 'Chans Ext Axon',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-axon.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_14':
        {
            'variant': 'Chans Ext Axon Last',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2-chans-axon-last.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '152028_15':
        {
            'variant': 'Chans Ext Axon [base]',
            'compile': ['cd Gunay_etal_2014/neuron-model'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("exp-axon-tail2.ses")', 'h.run()'],
            'cellviews': [[[0, 0, 100, 100], [20, -20, 80, 40], [0, -50, 100, 50]]],
            'cleanup': ['cd ../../', 'rm -fr Gunay_etal_2014']
        },
    '151482_1':
        {
            'variant': 'Fig. 3B',
            'compile': ['cd SPN_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("hoc_code/Model_fit_code/I-V.hoc")'],
            'cleanup': ['cd ../', 'rm -fr SPN_ModelDB']
        },
    '151482_2':
        {
            'variant': 'Fig. 3Ab',
            'compile': ['cd SPN_ModelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("hoc_code/Model_fit_code/I-F.hoc")'],
            'cleanup': ['cd ../', 'rm -fr SPN_ModelDB']
        },
    '151731':
        {
            'variant': 'run sim',
            'compile': ['cd CavarrettaEtAl2014', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.sim()'],
            'cleanup': ['cd ../', 'rm -fr CavarrettaEtAl2014']
        },
    '151825':
        {
            'compile': ['cd Demo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Demo']
        },
    '151949':
        {
            'compile': ['cd SousaEtAl2014', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr SousaEtAl2014']
        },
# 153280 is probably fine, except it's a large network model and spends 112 seconds just creating the cells       
#    '153280':
#        {
#            'compile': ['cd superdeep', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'h.load_file("superdeep.hoc")'],
#            'cleanup': ['cd ../', 'rm -fr superdeep']
#        },
# 153196 works except that it doesn't... it's hardcoded to run in an ipython notebook, but all that has to be done is remove the %pylab directive
#    '153196':
#        {
#            'compile': ['cd FoutzEtAl2012', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'execfile("Optical Stimulation.py")'],
#            'cleanup': ['cd ../', 'rm -fr FoutzEtAl2012']
#        },
    '155796_1':
        {
            'variant': 'Fig 1',
            'compile': ['cd ChambersEtAl2013', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.hide_xpanel()', 'h.load_file("fig1.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ChambersEtAl2013']
        },
    '155796_2':
        {
            'variant': 'Fig 2',
            'compile': ['cd ChambersEtAl2013', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.hide_xpanel()', 'h.load_file("fig2.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ChambersEtAl2013']
        },
    '155796_3':
        {
            'variant': 'Fig 3',
            'compile': ['cd ChambersEtAl2013', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")',  'h.hide_xpanel()', 'h.load_file("fig3.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ChambersEtAl2013']
        },
    '156039':
        {
            'compile': ['cd AllkenEtAl2014', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'execfile("mosinit.py")'],
            'cleanup': ['cd ../', 'rm -fr AllkenEtAl2014']
        },
    '156120':
        {
            'compile': ['cd HAE_LAE_Netk', 'nrnivmodl mods/other_mods mods/synapse'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr HAE_LAE_Netk']
        },
    '168148':
        {
            'compile': ['cd stadler2014_layerV', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_simulation()'],
            'cleanup': ['cd ../', 'rm -fr stadler2014_layerV']
        },
    '168310':
        {
            'compile': ['cd KonstantoudakiEtAl2014', 'nrnivmodl experiment'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KonstantoudakiEtAl2014']
        },
    '168414_1':
        {
            'variant': 'WindUp',
            'compile': ['cd ZhangEtAl2014/WindUp', r'cp ../Critical\ Mod\ Files/*.mod .', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Shell_NoSurround.hoc")'],
            'cleanup': ['cd ../..', 'rm -fr ZhangEtAl2014']
        },
    '168414_2':
        {
            'variant': 'Fiber, No EP',
            'compile': [r'cd "ZhangEtAl2014/A Fiber Inhibition"', r'cp ../Critical\ Mod\ Files/*.mod .', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Shell_NoEP.hoc")'],
            'cleanup': ['cd ../..', 'rm -fr ZhangEtAl2014']
        },
    '168414_3':
        {
            'variant': 'Foreman SCS',
            'compile': [r'cd "ZhangEtAl2014/Foreman SCS"', r'cp ../Critical\ Mod\ Files/*.mod .', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Shell.hoc")'],
            'cleanup': ['cd ../..', 'rm -fr ZhangEtAl2014']
        },
    '168874_1':
        {
            'variant': 'Fig 11 AMPA 0',
            'compile': ['cd ca1dDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'import sys', 'sys.argv[0] = "AMPA0.cfg"', 'execfile("cawave.py")'],
            'cleanup': ['cd ..', 'rm -fr ca1dDemo']
        },
    '168874_2':
        {
            'variant': 'Fig 11 AMPA 150',
            'compile': ['cd ca1dDemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'import sys', 'sys.argv[0] = "AMPA150.cfg"', 'execfile("cawave.py")'],
            'cleanup': ['cd ..', 'rm -fr ca1dDemo']
        },
    '129067_1':
        {
            'variant': 'Fig 9A',
            'compile': ['cd Welday_et_al/Welday_et_al_Fig9AB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("RUNSIM_FIG9A.hoc")', 'h.run()'],
            'cleanup': ['cd ../..', 'rm -fr Welday_et_al']
        },
    '129067_2':
        {
            'variant': 'Fig 9B',
            'compile': ['cd Welday_et_al/Welday_et_al_Fig9AB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("RUNSIM_FIG9B.hoc")', 'h.run()'],
            'cleanup': ['cd ../..', 'rm -fr Welday_et_al']
        },
    '150446_1':
        {
            'variant': '16PC 1IN',
            'compile': ['cd VladimirovTuTraub2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_16PC_1IN.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr VladimirovTuTraub2013']
        },
    '150446_2':
        {
            'variant': '1PC 1IN',
            'compile': ['cd VladimirovTuTraub2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_1PC_1IN.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr VladimirovTuTraub2013']
        },
    '150446_3':
        {
            'variant': '1PC 1IN myelinated Ax',
            'compile': ['cd VladimirovTuTraub2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_1PC_1INmyelinatedAx.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr VladimirovTuTraub2013']
        },
    '150446_4':
        {
            'variant': '1PC 1IN silent2firing',
            'compile': ['cd VladimirovTuTraub2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_1PC_1INsilent2firing.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr VladimirovTuTraub2013']
        },
    '150446_5':
        {
            'variant': '81PC 9IN forward',
            'compile': ['cd VladimirovTuTraub2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_81PC_9INforward.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr VladimirovTuTraub2013']
        },
    '108459_1':
        {
            'variant': '3 AP burst',
            'compile': ['cd LetzkusEtAl2006', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.three_AP()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr LetzkusEtAl2006']
        },
    '108459_2':
        {
            'variant': 'no APs',
            'compile': ['cd LetzkusEtAl2006', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.no_AP()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr LetzkusEtAl2006']
        },
    '3805_1':
        {
            'variant': 'Fig 3 Soma voltage clamp',
            'compile': ['cd dodge73', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart(0)', 'h.load_file(1, "fig3.hoc")'],
            'cleanup': ['cd ../', 'rm -fr dodge73']
        },
    '3805_2':
        {
            'variant': 'Fig 5 IS conductance',
            'compile': ['cd dodge73', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart(1)', 'h.load_file(1, "fig5.hoc")'],
            'cleanup': ['cd ../', 'rm -fr dodge73']
        },
    '3805_3':
        {
            'variant': 'Fig 6 Threshold difference',
            'compile': ['cd dodge73', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart(1)', 'h.load_file(1, "fig6.hoc")'],
            'cleanup': ['cd ../', 'rm -fr dodge73']
        },
    '3805_4':
        {
            'variant': 'Fig 7 Soma hyperpolarization',
            'compile': ['cd dodge73', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart(1)', 'h.load_file(1, "fig7.hoc")'],
            'cleanup': ['cd ../', 'rm -fr dodge73']
        },
    '3805_5':
        {
            'variant': 'Fig 8 Antidromic spatial pattern',
            'compile': ['cd dodge73', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart(1)', 'h.load_file(1, "fig8.hoc")'],
            'cleanup': ['cd ../', 'rm -fr dodge73']
        },
    '53451_1':
        {
            'variant': 'Fig 1',
            'compile': ['cd hines2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig1")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr hines2001']
        },
    '53451_2':
        {
            'variant': 'Fig 3,4',
            'compile': ['cd hines2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig34")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr hines2001']
        },
    '53451_3':
        {
            'variant': 'Fig 5',
            'compile': ['cd hines2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig5")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr hines2001']
        },
    '53451_4':
        {
            'variant': 'Fig 7',
            'compile': ['cd hines2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig7")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr hines2001']
        },
    '53451_5':
        {
            'variant': 'Fig 8',
            'compile': ['cd hines2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig8")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr hines2001']
        },
    '53451_6':
        {
            'variant': 'Fig 9',
            'compile': ['cd hines2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig9")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr hines2001']
        },
    '64228_1':
        {
            'variant': 'Fig5_IVCompare',
            'compile': ['cd Liu-Kourennyi_2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig5_IVCompare.ses")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Liu-Kourennyi_2004']
        },
    '64228_2':
        {
            'variant': 'fig 8B. AP_BR',
            'compile': ['cd Liu-Kourennyi_2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("0222AP_BR.ses")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Liu-Kourennyi_2004']
        },
    '64228_3':
        {
            'variant': 'fig 8D. AP_DIM',
            'compile': ['cd Liu-Kourennyi_2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("0222AP_DIM.ses")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Liu-Kourennyi_2004']
        },
    '64228_4':
        {
            'variant': 'Kx_BR',
            'compile': ['cd Liu-Kourennyi_2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("0222Kx_BR.ses")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Liu-Kourennyi_2004']
        },
    '64228_5':
        {
            'variant': 'Kx_DIM',
            'compile': ['cd Liu-Kourennyi_2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("0222Kx_DIM.ses")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Liu-Kourennyi_2004']
        },
    '64228_6':
        {
            'variant': 'Fig9_AP_Patterns',
            'compile': ['cd Liu-Kourennyi_2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("Fig9_AP_Patterns.ses")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Liu-Kourennyi_2004']
        },
#    '152197':
#        {
#            'compile': ['cd colorModelDemo', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'execfile("runMe.py")'],
#            'cleanup': ['cd ../', 'rm -fr colorModelDemo']
#        },
    '50997_1':
        {
            'variant': 'Fig 7',
            'compile': ['cd Ribbon', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("makefig7")'],
            'cleanup': ['cd ../', 'rm -fr Ribbon']
        },
    '50997_2':
        {
            'variant': 'Fig 8a',
            'compile': ['cd Ribbon', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("makefig8a")'],
            'cleanup': ['cd ../', 'rm -fr Ribbon']
        },
    '50997_3':
        {
            'variant': 'Fig 8b',
            'compile': ['cd Ribbon', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("makefig8b")'],
            'cleanup': ['cd ../', 'rm -fr Ribbon']
        },
    '50997_4':
        {
            'variant': 'Fig 8c',
            'compile': ['cd Ribbon', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("makefig8c")'],
            'cleanup': ['cd ../', 'rm -fr Ribbon']
        },
    '50997_5':
        {
            'variant': 'Fig 8c_250',
            'compile': ['cd Ribbon', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("makefig8c_250ms")'],
            'cleanup': ['cd ../', 'rm -fr Ribbon']
        },
    '50997_6':
        {
            'variant': 'Fig 9',
            'compile': ['cd Ribbon', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig9-11")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Ribbon']
        },
    '144566':
        {
            'compile': ['cd modeldb_package', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'execfile("claudia_pairing.py")'],
            'cleanup': ['cd ../', 'rm -fr modeldb_package']
        },
    '3677_1':
        {
            'variant': 'Ri18',
            'compile': ['cd spru1998/Ri18', 'nrnivmodl ..'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("ri18run.hoc")'],
            'cleanup': ['cd ../..', 'rm -fr spru1998']
        },
    '3677_2':
        {
            'variant': 'Ri21',
            'compile': ['cd spru1998/Ri21', 'nrnivmodl ..'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("ri21run.hoc")'],
            'cleanup': ['cd ../..', 'rm -fr spru1998']
        },
    '3677_3':
        {
            'variant': 'Ri22',
            'compile': ['cd spru1998/Ri22', 'nrnivmodl ..'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("ri22run.hoc")'],
            'cleanup': ['cd ../..', 'rm -fr spru1998']
        },
    '2488_1':
        {
            'variant': '1a. L3 Aspiny',
            'compile': ['cd patdemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig_1()', 'h.fig1a()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr patdemo']
        },
    '2488_2':
        {
            'variant': '1b. L4 Stellate',
            'compile': ['cd patdemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig_1()', 'h.fig1b()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr patdemo']
        },
    '2488_3':
        {
            'variant': '1c. L3 Pyramid',
            'compile': ['cd patdemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig_1()', 'h.fig1c()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr patdemo']
        },
    '2488_4':
        {
            'variant': '1d. L5 Pyramid',
            'compile': ['cd patdemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig_1()', 'h.fig1d()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr patdemo']
        },
    '2488_5':
        {
            'variant': '2',
            'compile': ['cd patdemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig_2()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr patdemo']
        },
    '2730_1':
        {
            'variant': 'Fig 2 (Olfactory nerve shock)',
            'compile': ['cd bulbNet', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_experiment("ddi_baseline")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr bulbNet']
        },
    '2730_2':
        {
            'variant': 'Fig 8 (Odor stimulus)',
            'compile': ['cd bulbNet', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_experiment("odour_baseline")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr bulbNet']
        },
    '18742_1':
        {
            'variant': '6A',
            'compile': ['cd nainact', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig6A")'],
            'cleanup': ['cd ../', 'rm -fr nainact']
        },
    '18742_2':
        {
            'variant': '6B',
            'compile': ['cd nainact', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig6B")'],
            'cleanup': ['cd ../', 'rm -fr nainact']
        },
    '18742_3':
        {
            'variant': '7A',
            'compile': ['cd nainact', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig7A")'],
            'cleanup': ['cd ../', 'rm -fr nainact'],
            'stopmidsim': False
        },
    '105385_1':
        {
            'variant': 'Figure 9',
            'compile': ['cd gp', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadfig9()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr gp']
        },
    '105385_2':
        {
            'variant': 'Figure 10',
            'compile': ['cd gp', 'nrnivmodl mod'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadfig10()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr gp']
        },
    '116491':
        {
            'compile': ['cd nrnpython', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['execfile("ch6_model.py")'],
            'cleanup': ['cd ../', 'rm -fr nrnpython']
        },
    '9848_1':
        {
            'variant': 'Figure 1',
            'compile': ['cd brill77', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig1")'],
            'cleanup': ['cd ../', 'rm -fr brill77']
        },
    '9848_2':
        {
            'variant': 'Figure 2A',
            'compile': ['cd brill77', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2a")'],
            'cleanup': ['cd ../', 'rm -fr brill77']
        },
    '9848_3':
        {
            'variant': 'Figure 2B',
            'compile': ['cd brill77', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2b")'],
            'cleanup': ['cd ../', 'rm -fr brill77']
        },
#    '151282':
#        {
#            'compile': ['cd ca3ihdemo', 'nrnivmodl'],
#            'launch': ['python'],
#            'run': ['from neuron import h, gui', 'import sys', 'sys.argv = ["python", "sim.py", "8000"]', 'execfile("sim.py")'],
#            'cleanup': ['cd ../', 'rm -fr ca3ihdemo']
#        },
    '53876_1':
        {
            'variant': '2 A1 B1',
            'compile': ['cd mvns', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2a1b1")'],
            'cleanup': ['cd ../', 'rm -fr mvns']
        },
    '53876_2':
        {
            'variant': '2 A2 B2',
            'compile': ['cd mvns', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2a2b2")'],
            'cleanup': ['cd ../', 'rm -fr mvns']
        },
    '53876_3':
        {
            'variant': '2 C',
            'compile': ['cd mvns', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2c")'],
            'cleanup': ['cd ../', 'rm -fr mvns']
        },
    '53876_4':
        {
            'variant': '2 D',
            'compile': ['cd mvns', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig2d")'],
            'cleanup': ['cd ../', 'rm -fr mvns']
        },
    '53876_5':
        {
            'variant': '3',
            'compile': ['cd mvns', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig3")'],
            'cleanup': ['cd ../', 'rm -fr mvns']
        },
    '53876_6':
        {
            'variant': '4 A',
            'compile': ['cd mvns', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("fig4a")'],
            'cleanup': ['cd ../', 'rm -fr mvns']
        },
    '33975_1':
        {
            'variant': 'Fig 1',
            'compile': ['cd locstepperf', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig1()'],
            'cleanup': ['cd ../', 'rm -fr locstepperf']
        },
    '33975_2':
        {
            'variant': 'Fig 5 Ring Performance',
            'compile': ['cd locstepperf', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.ringperf()'],
            'cleanup': ['cd ../', 'rm -fr locstepperf']
        },
    '116094_1':
        {
            'variant': 'Long Dendrite - Fig1bde',
            'compile': ['cd DendroDendriticInhibition/LongDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig1")', 'h.run_fig1bde()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_2':
        {
            'variant': 'Long Dendrite - Fig1fg',
            'compile': ['cd DendroDendriticInhibition/LongDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig1")', 'h.run_fig1fg()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_3':
        {
            'variant': 'Long Dendrite - Fig2ace',
            'compile': ['cd DendroDendriticInhibition/LongDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig2ace")', 'h.run_fig2()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_4':
        {
            'variant': 'Short Dendrite - Fig1cde',
            'compile': ['cd DendroDendriticInhibition/ShortDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig1cde")', 'h.run_fig1cde()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_5':
        {
            'variant': 'Short Dendrite - Fig1fg',
            'compile': ['cd DendroDendriticInhibition/ShortDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig1fg")', 'h.run_fig1fg()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_6':
        {
            'variant': 'Short Dendrite - Fig2bf',
            'compile': ['cd DendroDendriticInhibition/ShortDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig2bdf")', 'h.run_fig2bdf()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_7':
        {
            'variant': 'Short Dendrite - Fig3',
            'compile': ['cd DendroDendriticInhibition/ShortDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig3")', 'h.run_fig3()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_8':
        {
            'variant': 'Short Dendrite - Fig4abcd',
            'compile': ['cd DendroDendriticInhibition/ShortDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig4")', 'h.run_fig4abcd()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_9':
        {
            'variant': 'Short Dendrite - Fig4ef',
            'compile': ['cd DendroDendriticInhibition/ShortDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig4")', 'h.run_fig4ef()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_10':
        {
            'variant': 'Short Dendrite - Fig5',
            'compile': ['cd DendroDendriticInhibition/ShortDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig5")', 'h.run_fig5()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '116094_11':
        {
            'variant': 'Short Dendrite - Fig6',
            'compile': ['cd DendroDendriticInhibition/ShortDendrite', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")', 'h.run_experiment("fig6")', 'h.run_fig6()'],
            'cleanup': ['cd ../../', 'rm -fr DendroDendriticInhibition']
        },
    '18500_1':
        {
            'variant': 'AMPA/Kainate glutamatergic receptors',
            'compile': ['cd Channels_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_ampa.oc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Channels_NEW']
        },
    '18500_2':
        {
            'variant': 'NMDA glutamatergic receptors',
            'compile': ['cd Channels_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_nmda.oc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Channels_NEW']
        },
    '18500_3':
        {
            'variant': 'GABA-A receptors',
            'compile': ['cd Channels_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_gabaa.oc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Channels_NEW']
        },
    '18500_4':
        {
            'variant': 'GABA-B receptors',
            'compile': ['cd Channels_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_gabab.oc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Channels_NEW']
        },
    '150024_1':
        {
            'variant': 'Fig 9A,B',
            'compile': ['cd CNModel_May2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("DCN_spontact_loop_main.hoc")'],
            'cleanup': ['cd ../', 'rm -fr CNModel_May2013']
        },
    '150024_2':
        {
            'variant': 'Fig 9C,D',
            'compile': ['cd CNModel_May2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("DCN_rebound_main.hoc")'],
            'cleanup': ['cd ../', 'rm -fr CNModel_May2013']
        },
    '150024_3':
        {
            'variant': 'Fig 9E',
            'compile': ['cd CNModel_May2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("DCN_cip_fi_main.hoc")'],
            'cleanup': ['cd ../', 'rm -fr CNModel_May2013']
        },
    '150024_4':
        {
            'variant': 'Fig 9F',
            'compile': ['cd CNModel_May2013', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("DCN_cip_axis_main.hoc")'],
            'cleanup': ['cd ../', 'rm -fr CNModel_May2013']
        },
    '144502':
        {
            'compile': ['cd package', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'execfile("cluster_hyp.py")'],
            'cleanup': ['cd ../', 'rm -fr package']
        },
    '123623_1':
        {
            'variant': 'Regular-spiking pyramidal cell',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '123623_2':
        {
            'variant': 'Bursting pyramidal cell',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_PY_IB")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '123623_3':
        {
            'variant': 'Repetitive bursting pyramidal cell',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_PY_IBR")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '123623_4':
        {
            'variant': 'LTS pyramidal cell',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_PY_LTS")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '123623_5':
        {
            'variant': 'Fast-spiking interneuron',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_IN_FS")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '7400':
        {
            'compile': ['cd lytton99', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr lytton99']
        },
    '114047':
        {
            'compile': ['cd Basketcell', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.tstop=1e4', 'h.xopen("fig6.hoc")'],
            'cleanup': ['cd ../', 'rm -fr Basketcell']
        },
    '19214_1':
        {
            'variant': 'Fig.1. A,C',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(1)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_2':
        {
            'variant': 'Fig.1. B,D',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(2)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_3':
        {
            'variant': 'Fig.2. A,C',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(3)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_4':
        {
            'variant': 'Fig.2. B,D',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(4)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_5':
        {
            'variant': 'Fig.3. A-C Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(5)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_6':
        {
            'variant': 'Fig.3. A-C Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(6)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_7':
        {
            'variant': 'Fig.3. D Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(7)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_8':
        {
            'variant': 'Fig.3. D Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(8)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_9':
        {
            'variant': 'Fig.3. E-G Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(9)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_10':
        {
            'variant': 'Fig.3. E-G Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(10)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_11':
        {
            'variant': 'Fig.4. A-C Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(11)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_12':
        {
            'variant': 'Fig.4. A-C Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(12)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_13':
        {
            'variant': 'Fig.4. D Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(13)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_14':
        {
            'variant': 'Fig.4. D Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(14)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_15':
        {
            'variant': 'Fig.4. E-G Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(15)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_16':
        {
            'variant': 'Fig.4. E-G Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(16)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_17':
        {
            'variant': 'Fig.5. A-C Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(17)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_18':
        {
            'variant': 'Fig.5. A-C Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(18)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_19':
        {
            'variant': 'Fig.5. D Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(19)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_20':
        {
            'variant': 'Fig.5. D Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(20)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_21':
        {
            'variant': 'Fig.5. E-G Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(21)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_22':
        {
            'variant': 'Fig.5. E-G Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(22)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '136026_1':
        {
            'variant': 'Passive tuft, control',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_spiketuft.hoc")', 'h.setparams(h.BOTHCONTROL)', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '136026_2':
        {
            'variant': 'Passive tuft, cm = 2*control',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_spiketuft.hoc")', 'h.setparams(h.CMx2)', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '136026_3':
        {
            'variant': 'Passive tuft, Ra = 2*control',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_spiketuft.hoc")', 'h.setparams(h.RAx2)', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '136026_4':
        {
            'variant': 'Passive tuft, both 2*control',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_spiketuft.hoc")', 'h.setparams(h.BOTHx2)', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '136026_5':
        {
            'variant': 'Active tuft',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_active.hoc")', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '7399':
        {
            'compile': ['cd lytton98', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.sim_panel()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr na8st']
        },
    '128079':
        {
            'compile': ['cd na8st', 'nrnivmodl mod/'],
            'launch': ['python'],
            'run': ['execfile("ap.py")'],
            'cleanup': ['cd ../', 'rm -fr na8st']
        },
    '113997_1':
        {
            'variant': 'HPGA non-saturating',
            'compile': ['cd HAGPA', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_HPGA_non-saturating.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr HAGPA']
        },
    '113997_2':
        {
            'variant': 'HPGA non-saturating (no Ih)',
            'compile': ['cd HAGPA', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_HPGA_non-saturating_noIh.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr HAGPA']
        },
    '113997_3':
        {
            'variant': 'HPGA saturating',
            'compile': ['cd HAGPA', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_HPGA_saturating.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr HAGPA']
        },
    '144376_1':
        {
            'variant': 'HPGA non-saturating',
            'compile': ['cd Skolnik_python_WinogradEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['execfile("demo_HPGA_non_saturating.py")'],
            'cleanup': ['cd ../', 'rm -fr Skolnik_python_WinogradEtAl2008']
        },
    '144376_2':
        {
            'variant': 'HPGA non-saturating (no Ih)',
            'compile': ['cd Skolnik_python_WinogradEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['execfile("demo_HPGA_non_saturating_noIh.py")'],
            'cleanup': ['cd ../', 'rm -fr Skolnik_python_WinogradEtAl2008']
        },
    '144376_3':
        {
            'variant': 'HPGA saturating',
            'compile': ['cd Skolnik_python_WinogradEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['execfile("demo_HPGA_saturating.py")'],
            'cleanup': ['cd ../', 'rm -fr Skolnik_python_WinogradEtAl2008']
        },
    '62266':
        {
            'compile': ['cd b1', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr b1']
        },
    '138379':
        {
            'compile': ['cd fdemo', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.mytstop=20e3', 'h.finish_run()'],
            'cleanup': ['cd ../', 'rm -fr fdemo']
        },
    '18197_1':
        {
            'variant': 'fig 1A (Glutamate)',
            'compile': ['cd Neural_Computation', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_glutamate_neuralcomputation")'],
            'cleanup': ['cd ../', 'rm -fr Neural_Computation']
        },
    '18197_2':
        {
            'variant': 'fig 1D (GABA)',
            'compile': ['cd Neural_Computation', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_gaba_neuralcomputation")'],
            'cleanup': ['cd ../', 'rm -fr Neural_Computation']
        },
    '143114_1':
        {
            'variant': 'Synaptic Input',
            'compile': ['cd ZhouColburn2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("LSO_synaptic_input.hoc")', 'h.rerun()'],
            'cleanup': ['cd ../', 'rm -fr ZhouColburn2010']
        },
    '143114_2':
        {
            'variant': 'Current Input',
            'compile': ['cd ZhouColburn2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("LSO_current_input.hoc")', 'h.rerun()'],
            'cleanup': ['cd ../', 'rm -fr ZhouColburn2010']
        },
    '3798_1':
        {
            'variant': 'A',
            'compile': ['cd shrager91', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.inter_fhdens(0.4e-3)', 'h.unmyl()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr shrager91']
        },
    '3798_2':
        {
            'variant': 'B',
            'compile': ['cd shrager91', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.inter_fhdens(0.5e-3)', 'h.unmyl()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr shrager91']
        },
    '3798_3':
        {
            'variant': 'C',
            'compile': ['cd shrager91', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.inter_fhdens(0.4e-3)', 'h.demyl1(1, 3)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr shrager91']
        },
    '3798_4':
        {
            'variant': 'D',
            'compile': ['cd shrager91', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.inter_fhdens(0.4e-3)', 'h.demyl1(1, 19)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr shrager91']
        },
    '19491':
        {
            'compile': ['cd EurJNeurosci2000', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr EurJNeurosci2000']
        },
    '113446':
        {
            'compile': ['cd NEURON-2008b', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NEURON-2008b']
        },
    '117459':
        {
            'compile': ['cd CruzEtAlS_cellModel', 'nrnivmodl plus5HT/3cell'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CruzEtAlS_cellModel']
        },
    '53435_1':
        {
            'variant': 'Real EPSP',
            'compile': ['cd anyas2005/model_bf_real_EPSP', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr anyas2005']
        },
    '53435_2':
        {
            'variant': 'HPP',
            'compile': ['cd anyas2005/model_bf_HPP', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr anyas2005']
        },
    '112086_1':
        {
            'variant': 'Metal electrode',
            'compile': ['cd giuglianoEtAl2007', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("metal()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr giuglianoEtAl2007']
        },
    '112086_2':
        {
            'variant': 'Metal electrode',
            'compile': ['cd giuglianoEtAl2007', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("cntel()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr giuglianoEtAl2007']
        },
    '112086_3':
        {
            'variant': 'Metal electrode',
            'compile': ['cd giuglianoEtAl2007', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("cntel2()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr giuglianoEtAl2007']
        },

    '37856_1':
        {
            'variant': 'Fig 2',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiv()")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_2':
        {
            'variant': 'Fig 3A',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,0,0,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_3':
        {
            'variant': 'Fig 3B',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,0,1,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_4':
        {
            'variant': 'Fig 4A',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,1,0,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_5':
        {
            'variant': 'Fig 4B',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,1,1,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_6':
        {
            'variant': 'Fig 10A',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,0,0,1)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_7':
        {
            'variant': 'Fig 10B',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,1,0,1)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37857_1':
        {
            'variant': 'Figure2A',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig2A()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_2':
        {
            'variant': 'Figure2B',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig2B()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_3':
        {
            'variant': 'Figure2C',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig2C()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_4':
        {
            'variant': 'Figure2D',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig2D()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_5':
        {
            'variant': 'Panel A',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig3A()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_6':
        {
            'variant': 'Panel B',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig3B()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_7':
        {
            'variant': 'Panel C',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig3C()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_8':
        {
            'variant': 'Panel D',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig3D()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_9':
        {
            'variant': 'Type I',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig4A()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_10':
        {
            'variant': 'Type I-II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig4B()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_11':
        {
            'variant': 'Type II-I',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig4C()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_12':
        {
            'variant': 'Type II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig4D()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_13':
        {
            'variant': 'Type I-c',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type1c()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_14':
        {
            'variant': 'Type I-t',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type1t()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_15':
        {
            'variant': 'Type I-II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type12()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_16':
        {
            'variant': 'Type II-I',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type21()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_17':
        {
            'variant': 'Type II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type2()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_18':
        {
            'variant': 'Type IIo (Octopus)',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type2o()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '35358':
        {
            'compile': ['cd b04feb12', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr b04feb12']
        },
    '136176':
        {
            'compile': ['cd Katona_et_al', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Katona_et_al']
        },
    '138205':
        {
            'compile': ['cd Schizophr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("display_cell()")'],
            'cleanup': ['cd ../', 'rm -fr Schizophr']
        },
    '144490':
        {
            'compile': ['cd bpap', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.gui_run_bpap()'],
            'cleanup': ['cd ../', 'rm -fr bpap']
        },
    '143719':
        {
            'compile': ['cd Ca1_Bianchi/experiment', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr Ca1_Bianchi']
        },

    '20212_1':
        {
            'variant': 'Disperse 6_2',
            'compile': ['cd CA1_multi/experiment/cluster-dispersion', 'nrnivmodl ../../mechanism', 'chmod +x newshiftsyn', 'export PATH=.:$PATH'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Disperse_6_2.hoc")'],
            'cleanup': ['cd ../../..', 'rm -fr CA1_multi']
        },
    '44050_1':
        {
            'variant': 'Control',
            'compile': ['cd gaspiriniEtAl2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runc()'],
            'cleanup': ['cd ..', 'rm -fr gaspiriniEtAl2004']
        },        
    '44050_2':
        {
            'variant': 'AMPA',
            'compile': ['cd gaspiriniEtAl2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runa()'],
            'cleanup': ['cd ..', 'rm -fr gaspiriniEtAl2004']
        },        
    '44050_3':
        {
            'variant': 'AMPA + NMDA',
            'compile': ['cd gaspiriniEtAl2004', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ..', 'rm -fr gaspiriniEtAl2004']
        },        
    '144541_1':
        {
            'variant': 'Control',
            'compile': ['cd Ih_current', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("fig-5a.hoc")', 'h.loop()'],
            'cleanup': ['cd ..', 'rm -fr Ih_current']
        },        
    '144541_2':
        {
            'variant': 'Control',
            'compile': ['cd Ih_current', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("fig-5a.hoc")', 'h.zd()'],
            'cleanup': ['cd ..', 'rm -fr Ih_current']
        },
    '151949':
        {
            'compile': ['cd SousaEtAl2014', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr SousaEtAl2014']
        },
    '7509':
        {
            'compile': ['cd magee2000'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr magee2000'],
            'stopmidsim': False       # need this because an xpanel is open until after the sim completes
        },
    '106551':
        {
            'compile': ['cd nc-mri', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ..', 'rm -fr nc-mri']
        },
    '3507':
        {
            'compile': ['cd fh', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr fh']
        },
    '7386':
        {
            'compile': ['cd boosting', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runc()'],
            'cleanup': ['cd ..', 'rm -fr boosting']
        },
    '125152':
        {
            'compile': ['cd Uebachs-et-al_2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_sim_graph()'],
            'cleanup': ['cd ..', 'rm -fr Uebachs-et-al_2010']
        },
    '2796_1':
        {
            'variant': 'Fig 1A',
            'compile': ['cd ca1', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("fig_1a.hoc")', 'h.runu()'],
            'cleanup': ['cd ..', 'rm -fr ca1']
        },        
    '2796_2':
        {
            'variant': 'Fig 1C',
            'compile': ['cd ca1', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("fig_1c.hoc")', 'h.runu()'],
            'cleanup': ['cd ..', 'rm -fr ca1']
        },        
    '144401':
        {
            'compile': ['cd VladimirovTuTraub2012', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr VladimirovTuTraub2012']
        },
    '87546':
        {
            'compile': ['cd olm-int', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr olm-int']
        },
    '20015':
        {
            'compile': ['cd k_interneurons', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("kinetics.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr k_interneurons']
        },
    '32992':
        {
            'compile': ['cd synchro-ca1', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr synchro-ca1']
        },
    '2937_1':
        {
            'variant': 'Fig 3',
            'compile': ['cd slowinact', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run3()'],
            'cleanup': ['cd ..', 'rm -fr slowinact']
        },        
    '2937_2':
        {
            'variant': 'Fig 4bc',
            'compile': ['cd slowinact', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run4bc()'],
            'cleanup': ['cd ..', 'rm -fr slowinact']
        },        
    '2937_3':
        {
            'variant': 'Fig 4bd',
            'compile': ['cd slowinact', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run4bd()'],
            'cleanup': ['cd ..', 'rm -fr slowinact']
        },        
    '139418_1':
        {
            'variant': 'Fig 11',
            'compile': ['cd fietkiewicz2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("figure11.hoc")'],
            'cleanup': ['cd ..', 'rm -fr fietkiewicz2011']
        },        
    '139418_2':
        {
            'variant': 'Fig 13',
            'compile': ['cd fietkiewicz2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("figure13.hoc")'],
            'cleanup': ['cd ..', 'rm -fr fietkiewicz2011']
        },        
    '46839':
        {
            'compile': ['cd GranuleCell', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr GranuleCell']
        },
    '116830':
        {
            'compile': ['cd b08dec23', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")'],
            'cleanup': ['cd ..', 'rm -fr b08dec23']
        },
    '125689':
        {
            'compile': ['cd CarvalhoBuonomano/Neuron2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.MULTI()'],
            'cleanup': ['cd ../..', 'rm -fr CarvalhoBuonomano']
        },
    '127388':
        {
            'compile': ['cd BGnet', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_sim()'],
            'cleanup': ['cd ../..', 'rm -fr BGnet']
        },
    '136803':
        {
            'compile': ['cd JonesEtAl2009', 'nrnivmodl mod_files'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../..', 'rm -fr JonesEtAl2009']
        },
    '116096_1':
        {
            'variant': 'Fig 2A',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = -100', 'h.set_axis_limits(0.0014, 0.007, 0.7, 0.014)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },        
    '116096_2':
        {
            'variant': 'Fig 2B',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = -10', 'h.set_axis_limits(0.0014, 0.007, 0.7, 0.35)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },        
    '116096_3':
        {
            'variant': 'Fig 2C',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = 10', 'h.set_axis_limits(0.0045, 0.5, 0.9, 0.014)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },
    '116096_4':
        {
            'variant': 'Fig 2D',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = 200', 'h.ampasyn.onset = 10', 'h.set_axis_limits(0.0016, 0.016, 0.7, 0.014)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },
    '147538_1':
        {
            'variant': 'Fig 2A',
            'compile': ['cd NarayananJohnston2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Fig2A()'],
            'cleanup': ['cd ..', 'rm -fr NarayananJohnston2010']
        },
    '147538_2':
        {
            'variant': 'Fig 2B',
            'compile': ['cd NarayananJohnston2010', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Fig2B()'],
            'cleanup': ['cd ..', 'rm -fr NarayananJohnston2010']
        },
    '112834':
        {
            'compile': ['cd nacb_msp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr nacb_msp']
        },
    '125378':
        {
            'compile': ['cd leeEtAl2003', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig8b()'],
            'cleanup': ['cd ..', 'rm -fr leeEtAl2003']
        },
    '115356':
        {
            'compile': ['cd RoyeckEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_sim_graph()'],
            'cleanup': ['cd ..', 'rm -fr RoyeckEtAl2008']
        },
    '127021':
        {
            'compile': ['cd Golgi_cell_NaKATPAse', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.recreate()'],
            'cleanup': ['cd ..', 'rm -fr Golgi_cell_NaKATPAse']
        },
    '147514':
        {
            'compile': ['cd dendritic_complexity', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr dendritic_complexity']
        },
    '135838':
        {
            'compile': ['cd Alle_et_al_2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Alle_et_al_2009']
        },
    '143635':
        {
            'compile': ['cd CasaleEtAl2011', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.measure()'],
            'cleanup': ['cd ..', 'rm -fr CasaleEtAl2011']
        },
    '87473':
        {
            'compile': ['cd weaver_SimAnn_ObjFcn', 'nrnivmodl model optmz'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr weaver_SimAnn_ObjFcn']
        },
    '135839':
        {
            'compile': ['cd McCormickEtAl2007YuEtAl2008', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.soma_inj()'],
            'cleanup': ['cd ..', 'rm -fr McCormickEtAl2007YuEtAl2008']
        },
    '127992':
        {
            'compile': ['cd HHcn', 'nrnivmodl mod-files/', 'cp python/* .'],
            'launch': ['python'],
            'run': ['execfile("HHneuron.py")'],
            'cleanup': ['cd ..', 'rm -fr HHcn']
        },
    '145836':
        {
            'compile': ['cd MoradiEtAl2012', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr MoradiEtAl2012']
        },
    '28316_1':
        {
            'variant': '8A Long',
            'compile': ['cd OLMmodel', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("initFig8Along")'],
            'cleanup': ['cd ..', 'rm -fr OLMmodel']
        },
    '3785_1':
        {
            'variant': 'Figure 3 1A in vitro',
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(1)', 'h.fig1A_vitro()'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_2':
        {
            'variant': 'Figure 4 2A in vitro',
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(1)', 'h("mcab[0] othervitro(10000)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_3':
        {
            'variant': "Figure 4 2A' in vitro",
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(1)', 'h("ecab[0] othervitro(10000)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_4':
        {
            'variant': "Figure 5 3A in vitro",
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(0)', 'h("mcab[0] othervitro(100)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_5':
        {
            'variant': "Figure 5 3A' in vitro",
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(0)', 'h("ecab[0] othervitro(100)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '87284_1':
        {
            'variant': 'Figure 1, 2',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig1and2()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_2':
        {
            'variant': 'Figure 3',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_3':
        {
            'variant': 'Figure 4',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig4()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_4':
        {
            'variant': 'Figure 5',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_5':
        {
            'variant': 'Figure 6',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig6()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '18198_1':
        {
            'variant': 'Synaptic Release',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("release")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_2':
        {
            'variant': 'AMPA - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("ampa")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_3':
        {
            'variant': 'AMPA - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("ampa5")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_4':
        {
            'variant': 'NMDA - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("nmda")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_5':
        {
            'variant': 'NMDA - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("nmda5")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_6':
        {
            'variant': 'GABA_A - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("gabaa")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_7':
        {
            'variant': 'GABA_A - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("gabaa5")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_8':
        {
            'variant': 'GABA_B - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("gabab")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_9':
        {
            'variant': 'GABA_B - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("gabab3")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '136715_1':
        {
            'variant': 'Fig 6B',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig6B.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '136715_2':
        {
            'variant': 'Fig 4B 10APs',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig4B 10APs ver7a.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '136715_3':
        {
            'variant': 'Fig 4B 100APs',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig4B 100APs ver7a.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '136715_4':
        {
            'variant': 'Fig 3A',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig3A.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '93321_1':
        {
            'variant': 'Fig 3A (top left)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3topleft()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_2':
        {
            'variant': 'Fig 3B (top right)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3topright()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_3':
        {
            'variant': 'Fig 3A middle (left)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3middleleft()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_4':
        {
            'variant': 'Fig 3B middle (right)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['python'],
            'stopmidsim': False,
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3middleright()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_5':
        {
            'variant': 'Fig 3 bottom',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3bottom()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '123897_1':
        {
            'variant': 'Pyramidal Cell',
            'compile': ['cd HuEtAl2009', 'nrnivmodl mechanism/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("experiment/Pyramidal_Main.hoc")', 'h.freePlay()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr HuEtAl2009']
        },
    '123897_2':
        {
            'variant': 'Uniform Axon',
            'compile': ['cd HuEtAl2009', 'nrnivmodl mechanism/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("experiment/UniformAxon_Main.hoc")'],
            'cleanup': ['cd ..', 'rm -fr HuEtAl2009']
        },
    '123897_3':
        {
            'variant': 'Single Compartment (activation)',
            'compile': ['cd HuEtAl2009', 'nrnivmodl mechanism/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("experiment/SingleComp_Main.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr HuEtAl2009']
        },
    '19176_1':
        {
            'variant': 'Current Steps',
            'compile': ['cd HCN2k', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.experiment1()'],
            'cleanup': ['cd ..', 'rm -fr HCN2k']
        },
    '19176_2':
        {
            'variant': 'cAMP pulse',
            'compile': ['cd HCN2k', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.experiment2()'],
            'cleanup': ['cd ..', 'rm -fr HCN2k']
        },
    '124063':
        {
            'compile': ['cd PublioEtAl2009', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.start()'],
            'cleanup': ['cd ..', 'rm -fr PublioEtAl2009']
        },
    '54903_1':
        {
            'variant': 'Fig 7C: hh-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-hh-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },
    '54903_1':
        {
            'variant': 'Fig 7C: hh-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-hh-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },
    '54903_2':
        {
            'variant': 'Fig 7C: hh-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-hh-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },
    '54903_3':
        {
            'variant': 'Fig 7C: NaCh-black_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-NaCh-black_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_4':
        {
            'variant': 'Fig 7C: NaCh-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-NaCh-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_5':
        {
            'variant': 'Fig 7C: NaCh-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-NaCh-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_6':
        {
            'variant': 'Fig 7C: naf-black_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naf-black_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_7':
        {
            'variant': 'Fig 7C: naf-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naf-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_8':
        {
            'variant': 'Fig 7C: naf-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naf-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_9':
        {
            'variant': 'Fig 7C: naxn-black',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naxn-black.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_10':
        {
            'variant': 'Fig 7C: naxn-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naxn-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_11':
        {
            'variant': 'Fig 7C: naxn-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naxn-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_12':
        {
            'variant': 'Fig 7D',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7D.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_13':
        {
            'variant': 'Fig 7E',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7E.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_14':
        {
            'variant': 'Fig 6B',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-B.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_15':
        {
            'variant': 'Fig 6C',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-C.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_16':
        {
            'variant': 'Fig 7B',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7B.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_17':
        {
            'variant': 'Fig 6D',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-D.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_18':
        {
            'variant': 'Fig 6E',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-D.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_19':
        {
            'variant': 'Fig 6F',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-F.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_20':
        {
            'variant': 'Fig 7A',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7A.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_21':
        {
            'variant': 'Fig 6B-inset',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-B-inset.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '126637_2c':
        {
            'variant': 'Fig 2C + 2E',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_spine and spine neck at spinydendrite133.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '126637_2d':
        {
            'variant': 'Fig 2D + 2F',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_reduced_PPR model.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '126637_cvode':
        {
            'variant': 'CVODE or other solvers',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_reduced_PPR model_cvode.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '146026_ex1':
        {
            'variant': 'Example 1',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("example1.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '146026_ex2':
        {
            'variant': 'Example 2',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("example2.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '146026_ex3':
        {
            'variant': 'Example 3',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("example3.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '137259':
        {
            'compile': ['cd ca3-synresp', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr ca3-synresp']
        },
    '53869':
        {
            'compile': ['cd MSO_Zhouetal_2005', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("MSO_Zhouetal_2005")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr MSO_Zhouetal_2005']
        },
    '125857_2frb':
        {
            'variant': '2FRB',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("2FRB")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '140249_a1':
        {
            'variant': 'Fig 4 A1',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runP1MP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_b1':
        {
            'variant': 'Fig 4 B1',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runP1HP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_a2':
        {
            'variant': 'Fig 4 A2',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runP2MP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_b2':
        {
            'variant': 'Fig 4 B2',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runP2HP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },        
    '125857_frb3':
        {
            'variant': 'FRB3',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("FRB3")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '125857_frb_12_19':
        {
            'variant': 'FRB_12_19',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("FRB_12_19")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '125857_frb_12_21':
        {
            'variant': 'FRB_12_21',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("FRB_12_21")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '150240':
        {
            'compile': ['cd TCconvergenceModel', 'nrnivmodl'],
            'launch': ['python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr TCconvergenceModel']
        }
}

protocol = dict(automatically_curated_protocols)
protocol.update(manually_curated_protocols)

if __name__ == '__main__':
    import json
    import sys
    import os
    multi = {}
    all_ids = {}
    for key in protocol:
        split = key.split('_')
        all_ids[split[0]] = 0
        if len(split) > 1:
            if split[0] not in multi:
                multi[split[0]] = []
            multi[split[0]].append([protocol[key]['variant'], key])
    for id in multi:
        multi[id] = sorted(multi[id], key=lambda row: row[0])
    if len(sys.argv) == 1:
        print(json.dumps(multi))
        print()
        print()
        print('models with multiple protocols:')
        for key in multi:
            print(key)
        print()
        print()
        print('all models with at least one protocol:')
        for key in all_ids:
            print(key)
        print()
        print()
        print('Protocols for %d models' % len(list(all_ids.keys())))
        print('Number of models with multiple protocols: %d' % len(list(multi.keys())))
        print('Total number of protocols: %d' % len(list(protocol.keys())))
    elif sys.argv[1] == 'savejson':
        with open(os.path.join('/home/morse/senselab/Web/ModelDB/jsondata', 'modelview_duplicates.txt'), 'w') as f:
            f.write(json.dumps(multi))
