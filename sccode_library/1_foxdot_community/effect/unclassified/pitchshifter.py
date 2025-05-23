sccode = """
SynthDef.new(\\pitchshifter, {
	|bus, shift, shiftsize|
	var osc;
	osc = In.ar(bus, 2);
	osc = PitchShift.ar(osc, shiftsize, shift, 0.02, 0.01);
	ReplaceOut.ar(bus, osc)
}).add;

"""

effect = SCEffect(
    shortname="pitchshifter",
    fullname="pitchshifter",
    description="Pitchshifter effect",
    code=sccode,
    arguments={},
    order=2,
)
