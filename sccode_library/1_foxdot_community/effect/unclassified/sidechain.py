sccode = """
SynthDef.new(\\sidechain, {
	|bus, sidechain, sidechain_atk, sidechain_rel, thresh|
	var osc,schain;
	osc = In.ar(bus, 2);
	schain = In.ar(sidechain,1);
	osc = Compander.ar(osc, schain, thresh: thresh, slopeAbove: 0.1, slopeBelow: 1, clampTime: sidechain_atk, relaxTime: sidechain_rel, mul: 1);
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="sidechain",
    fullname="sidechain",
    description="Sidechain effect",
    code=sccode,
    arguments={
        "sidechain": 0,
        "sidechain_atk": 0.05,
        "sidechain_rel": 0.1,
        "thresh": 0.006
    },
    order=2,
)
