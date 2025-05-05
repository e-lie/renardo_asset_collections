sccode = """
SynthDef.new(\\spinPan,
{|bus, spin, sus|
var osc;
osc = In.ar(bus, 2);
osc = osc * [FSinOsc.ar(spin / 2, iphase: 1, mul: 0.5, add: 0.5), FSinOsc.ar(spin / 2, iphase: 3, mul: 0.5, add: 0.5)];
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="spin",
    fullname="spinPan",
    description="Spinpan effect",
    code=sccode,
    arguments={
        "spin": 0,
        "sus": 1
    },
    order=2,
)
