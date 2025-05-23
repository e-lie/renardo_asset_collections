sccode = """
SynthDef.new(\\slideFrom,
{|bus, slidefrom, sus, slidedelay|
var osc;
osc = In.kr(bus, 1);
osc = osc * EnvGen.ar(Env([slidefrom + 1, slidefrom + 1, 1], [sus*slidedelay, sus*(1-slidedelay)]));
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="slidefrom",
    fullname="slideFrom",
    description="Slidefrom effect",
    code=sccode,
    arguments={
        "slidefrom": 0,
        "sus": 1,
        "slidedelay": 0
    },
    order=0,
)
