sccode = """
SynthDef.new(\\pitchShift,
{|bus, pshift|
var osc;
osc = In.kr(bus, 1);
osc = osc * (1.059463**pshift);
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="pshift",
    fullname="pitchShift",
    description="Pitchshift effect",
    code=sccode,
    arguments={
        "pshift": 0
    },
    order=0,
)
