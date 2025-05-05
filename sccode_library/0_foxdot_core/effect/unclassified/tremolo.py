sccode = """
SynthDef.new(\\tremolo,
{|bus, tremolo, beat_dur|
var osc;
osc = In.ar(bus, 2);
osc = osc * SinOsc.ar( tremolo / beat_dur, mul:0.5, add:0.5);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="tremolo",
    fullname="tremolo",
    description="Tremolo effect",
    code=sccode,
    arguments={
        "tremolo": 0,
        "beat_dur": 1
    },
    order=2,
)
