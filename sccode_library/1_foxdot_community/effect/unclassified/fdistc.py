sccode = """
SynthDef.new(\\fdistc,
{|bus, fdistc, fdistcfreq1, fdistcfreq2, fdistcfreq3, fdistcfreq4, fdistcm1, fdistcm2, fdistcm3, fdistcm4, fdistcq1, fdistcq2, fdistcq3, fdistcq4|
var osc;
osc = In.ar(bus, 2);
osc = RLPF.ar(osc, fdistcfreq1, fdistcq1);
osc = (osc * fdistcm1 * fdistc).tanh;
osc = RLPF.ar(osc, fdistcfreq2, fdistcq2);
osc = (osc * fdistcm2 * fdistc).tanh;
osc = RLPF.ar(osc, fdistcfreq3, fdistcq3);
osc = (osc * fdistcm3 * fdistc).tanh;
osc = RLPF.ar(osc, fdistcfreq4, fdistcq4);
osc = (osc * fdistcm4 * fdistc).tanh;
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="fdistc",
    fullname="fdistc",
    description="Fdistc effect",
    code=sccode,
    arguments={
        "fdistc": 0,
        "fdistcfreq1": 1600,
        "fdistcfreq2": 1600,
        "fdistcfreq3": 1600,
        "fdistcfreq4": 1600,
        "fdistcm1": 1.1,
        "fdistcm2": 1.1,
        "fdistcm3": 1.4,
        "fdistcm4": 2,
        "fdistcq1": 1,
        "fdistcq2": 1,
        "fdistcq3": 1,
        "fdistcq4": 1
    },
    order=2,
)
