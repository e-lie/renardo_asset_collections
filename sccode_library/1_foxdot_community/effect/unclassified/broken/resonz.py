sccode = """
SynthDef.new(\\resonz, {
	|bus, rfreq, resonz|
	var osc;
	osc = In.ar(bus, 2);
	osc = Resonz.ar(osc, freq: rfreq, bwr: resonz);
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="resonz",
    fullname="resonz",
    description="Resonz effect",
    code=sccode,
    arguments={
        "rfreq": 50,
        "resonz": 0.1
    },
    order=2,
)
