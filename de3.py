from neuron import h, gui
 
h.load_file("nrngui.hoc")
h.nao0_na_ion = 110
h.cao0_ca_ion = 1.8

soma = h.Section(name="soma")
soma.Ra = 200 
soma.L = 40 
soma.diam = 50 
soma.nseg = 2
soma.insert("pcell") 
soma.insert("na")
soma.insert("napump") 
soma.insert("gkca")
soma.insert("ca")
soma.insert("cach") 
soma.insert("capump") 

junction = h.Section(name="soma")
junction.Ra = 200
junction.L = 40
junction.diam = 10
junction.nseg = 2
junction.insert("pcell") 
junction.insert("na")
junction.insert("napump") 
junction.insert("gkca")
junction.insert("ca")
junction.insert("cach") 
junction.insert("capump") 

axthick = h.Section(name="axthick")
axthick.Ra = 200
axthick.L = 150
axthick.diam = 6
axthick.nseg = 10
axthick.insert("pcell") 
axthick.insert("na")
axthick.insert("napump") 
axthick.insert("gkca")
axthick.insert("ca")
axthick.insert("cach") 
axthick.insert("capump") 

axsiz = h.Section(name="axsiz")
axsiz.Ra = 200
axsiz.L = 10
axsiz.diam = 2
axsiz.nseg = 1
axsiz.insert("pcell") 
axsiz.insert("na")
axsiz.insert("napump") 
axsiz.insert("gkca")
axsiz.insert("ca")
axsiz.insert("cach") 
axsiz.insert("capump") 

axthin = h.Section(name="axthin")
axthin.Ra = 200
axthin.L = 500
axthin.diam = 2
axthin.nseg = 30
axthin.insert("pcell") 
axthin.insert("na")
axthin.insert("napump") 
axthin.insert("gkca")
axthin.insert("ca")
axthin.insert("cach") 
axthin.insert("capump") 

for sec in h.allsec():
  sec.ek = -68 

junction.connect(soma)
axthick.connect(junction)
axsiz.connect(axthick)
axthin.connect(axsiz)

# Model changes for spike height
soma.gnabar_pcell = 0
junction.gnabar_pcell = 0
axsiz.gnabar_pcell = .5

axthick.gnabar_pcell = 0.15


for sec in h.allsec():
  sec.kactrate_pcell = 2

soma.push()

h.celsius = 20
h.tstop = 300
h.xopen("de3_1.ses")

ic = h.IClamp(0.5, sec=axthick)
ic.delay = 100
ic.dur = 300
ic.amp = 1

h.init()
h.run()
