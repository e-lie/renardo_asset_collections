sccode = """
SynthDef.new(\\leg,
{|bus, leg, sus|
var osc;
osc = In.kr(bus, 1);
osc = osc * XLine.ar(Rand(0.5,1.5)*leg,1,0.05*sus);
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="leg",
    fullname="leg",
    description="Leg effect",
    code=sccode,
    arguments={
        "leg": 0,
        "sus": 1
    },
    order=0,
)
