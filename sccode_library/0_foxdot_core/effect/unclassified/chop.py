sccode = """
SynthDef.new(\\chop,
{|bus, chop, sus|
var osc;
osc = In.ar(bus, 2);
osc = osc * LFPulse.kr(chop / sus, add: 0.01);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="chop",
    fullname="chop",
    description="Chop effect",
    code=sccode,
    arguments={
        "chop": 0,
        "sus": 1,
        "chopmix": 1,
        "chopwave": 0,
        "chopi": 0
    },
    order=2,
)
