sccode = """
SynthDef.new(\\reverb,
{|bus, room, mix|
var osc;
osc = In.ar(bus, 2);
osc = FreeVerb.ar(osc, mix, room);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="room",
    fullname="reverb",
    description="Reverb effect",
    code=sccode,
    arguments={
        "room": 0,
        "mix": 0.1
    },
    order=2,
)
