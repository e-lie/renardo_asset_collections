sccode = """
SynthDef.new(\\Ringmod, {
	|bus, ringzfreq, ringz|
	var osc;
	osc = In.ar(bus, 2);
	osc = Ringz.ar(osc, freq: ringzfreq, decaytime: ringz, mul: 0.05);
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="ringz",
    fullname="Ringmod",
    description="Ringmod effect",
    code=sccode,
    arguments={
        "ringzfreq": 50,
        "ringz": 0.1
    },
    order=2,
)
