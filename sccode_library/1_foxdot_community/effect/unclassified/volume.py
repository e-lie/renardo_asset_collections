sccode = """
SynthDef.new(\\volume,
{|bus, vol|
var osc;
osc = In.ar(bus, 2);
osc = osc * vol;
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="vol",
    fullname="volume",
    description="Volume effect",
    code=sccode,
    arguments={
        "vol": 1
    },
    order=2,
)
