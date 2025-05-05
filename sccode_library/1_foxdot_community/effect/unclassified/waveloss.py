sccode = """
SynthDef.new(\\waveloss, {
	|bus, drop, dropof|
	var osc;
	osc = In.ar(bus, 2);
	osc = WaveLoss.ar(osc, drop, outof: dropof, mode: 2);
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="drop",
    fullname="waveloss",
    description="Waveloss effect",
    code=sccode,
    arguments={
        "drop": 0,
        "dropof": 100
    },
    order=2,
)
