sccode = """
SynthDef.new(\\bitcrush,
{|bus, bits, sus, amp, crush|
var osc;
osc = In.ar(bus, 2);
osc = Decimator.ar(osc, rate: 44100/crush, bits: bits);
osc = osc * Line.ar(amp * 0.85, 0.0001, sus * 2);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="crush",
    fullname="bitcrush",
    description="Bitcrush effect",
    code=sccode,
    arguments={
        "bits": 8,
        "sus": 1,
        "amp": 1,
        "crush": 0
    },
    order=1,
)
