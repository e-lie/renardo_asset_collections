sccode = """
SynthDef.new(\\coarse,
{|bus, coarse, sus|
var osc;
osc = In.kr(bus, 1);
osc = osc * LFPulse.ar(coarse / sus);
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="coarse",
    fullname="coarse",
    description="Coarse effect",
    code=sccode,
    arguments={
        "coarse": 0,
        "sus": 1
    },
    order=0,
)
