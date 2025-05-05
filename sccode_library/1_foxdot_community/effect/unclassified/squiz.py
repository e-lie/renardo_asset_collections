sccode = """
SynthDef.new(\\squiz,
{|bus, squiz|
var osc;
osc = In.ar(bus, 2);
osc = Squiz.ar(osc, squiz);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="squiz",
    fullname="squiz",
    description="Squiz effect",
    code=sccode,
    arguments={
        "squiz": 0
    },
    order=2,
)
