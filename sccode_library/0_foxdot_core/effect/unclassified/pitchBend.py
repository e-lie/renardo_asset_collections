sccode = """
SynthDef.new(\\pitchBend,
{|bus, bend, sus, benddelay|
var osc;
osc = In.kr(bus, 1);
osc = osc * EnvGen.ar(Env([1, 1, 1 + bend, 1], [sus * benddelay, (sus*(1-benddelay)/2), (sus*(1-benddelay)/2)]));
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="bend",
    fullname="pitchBend",
    description="Pitchbend effect",
    code=sccode,
    arguments={
        "bend": 0,
        "sus": 1,
        "benddelay": 0
    },
    order=0,
)
