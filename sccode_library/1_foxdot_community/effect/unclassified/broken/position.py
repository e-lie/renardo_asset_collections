sccode = """
SynthDef.new(\\position, {
	|bus, position, sus|
	var osc;
	osc = In.ar(bus, 2);
	osc = osc * EnvGen.ar(Env([0, 0, 1], curve='step', times=[sus * position, 0]));
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="position",
    fullname="position",
    description="Position effect",
    code=sccode,
    arguments={},
    order=2,
)
