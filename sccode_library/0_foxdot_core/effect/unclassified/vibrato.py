sccode = """
SynthDef.new(\\vibrato,
{|bus, vib, vibdepth|
var osc;
osc = In.kr(bus, 1);
osc = Vibrato.ar(osc, vib, depth: vibdepth);
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="vib",
    fullname="vibrato",
    description="Vibrato effect",
    code=sccode,
    arguments={
        "vib": 0,
        "vibdepth": 0.02
    },
    order=0,
)
